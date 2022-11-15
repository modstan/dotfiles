#!/usr/bin/python
import i3ipc
import argparse

i3 = i3ipc.Connection()

workspaces = i3.get_workspaces()
outputs = i3.get_outputs()

def get_focused_workspace():
    for w in workspaces:
        if w.focused:
            return w.name, w.num

def get_focused_screen():
    for o in outputs:
        print(o.name)
        if o.current_workspace and o.current_workspace == get_focused_workspace()[0]:
            return o.name

def change_screen():
    for o in outputs:
        if o['current_workspace'] and o['current_workspace'] != get_focused_workspace()[0]:
            i3.workspace(o['current_workspace'])
            break

def workspace_change(num):
    num = int(num)
    if get_focused_screen() == "HDMI1":
        num = num + 5
    i3.command("workspace %s" % num)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''switch for i3''')
    parser.add_argument('-s', '--change_screen', action='store_true')
    parser.add_argument('-w', '--workspace_screen')

    args = parser.parse_args()

    if args.change_screen: change_screen()
    if args.workspace_screen: workspace_change(args.workspace_screen)
