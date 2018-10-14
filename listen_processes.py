from typing import List, Set, Tuple
from os import popen, sep
import re
import time


class ProcessInfo:
    endings = ['.app']
    stop_headers = ['S', 'D', 'T']
    sleep_headers = ['S', 'D']
    root_users = ['root']

    def __init__(self, owner, pid, stat, cmd):
        self.owner = owner
        self.pid = pid
        self.stat = stat
        self.cmd = cmd
        self.app_name, self.is_app = self._app_name_from_command(self.cmd)
        # print(self)

    @classmethod
    def _app_name_from_command(cls, cmd: str) -> Tuple[str, bool]:
        for fn in cmd.split(sep):
            if True in [fn.endswith(e) for e in cls.endings]:
                return fn, True
        return '', False

    def __eq__(self, other):
        try:
            return self.app_name == other.app_name and self.pid == other.pid
        except AttributeError:
            return False

    @classmethod
    def from_str(cls, s: str):
        raw_info = re.split('[ \t][ \t]*', s)
        attributes = {'cmd': ''}
        for i in range(0, len(raw_info)):
            if i == 0:
                attributes['owner'] = raw_info[i]
            elif i == 1:
                attributes['pid'] = raw_info[i]
            elif i == 6:
                attributes['stat'] = raw_info[i]
            elif i > 8:
                attributes['cmd'] += ' ' + raw_info[i]

        return cls(**attributes)

    def __str__(self):
        return '\t'.join([self.owner.strip(), self.pid.strip(), self.stat.strip(), self.app_name.strip()])

    @property
    def not_working(self) -> bool:
        return self.stat[0] in self.stop_headers

    @property
    def sleeping(self) -> bool:
        return self.stat[0] in self.sleep_headers

    @property
    def is_root(self) -> bool:
        return self.owner in self.root_users

    def __hash__(self):
        return hash(''.join([self.app_name, self.pid]))


#                             working app, sleeping app
def listen_process() -> Tuple[List[ProcessInfo], List[ProcessInfo]]:
    cmd = 'ps -ej'
    output = popen(cmd)
    ps_info = []
    for l in output.readlines():
        # l: str
        if l.startswith('USER'):
            continue
        ps_info.append(ProcessInfo.from_str(l))
    wp = list(filter(lambda i: i is not None and i.is_app and not i.is_root,
                     [info if not info.not_working else None for info in ps_info]))
    slp = list(filter(lambda i: i is not None and i.is_app and not i.is_root,
                      [info if info.sleeping else None for info in ps_info]))
    return wp, slp


def get_apps(lst_ps_info: List[ProcessInfo]) -> Set[ProcessInfo]:
    return set([i for i in lst_ps_info])


def _print_lst(l: list):
    print('[\n\t' + '\n\t'.join([str(li) for li in l]) + '\n]')


def running_process_during_interval(secs: float, get_sleeps=False):
    s = time.time()
    ws = set()
    ss = set()
    while time.time() - s <= secs:
        wps, slps = listen_process()
        ws.update(get_apps(wps))
        ss.update(get_apps(slps))
    if not get_sleeps:
        return ws
    else:
        return {*ws, *ss}


if __name__ == '__main__':
    # _print_lst(wps)
    # _print_lst(slps)
    # s = time.time()
    #
    # ws = set()
    # ss = set()
    # while time.time() - s <= 5:
    #     wps, slps = listen_process()
    #
    #     ws.update(get_apps(wps))
    #     ss.update(get_apps(slps))
    #     # print(get_apps(wps))
    #     # print(get_apps(slps))
    # print(ws)
    # print(ss)
    print(running_process_during_interval(5))
