
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\xa0\xb3\xbe\xbf\x14{\xeb\x93x\xf9\xb0\xea\xa4\xb1\xc54'
    
_lr_action_items = {'FOR':([0,],[2,]),'$end':([1,13,],[0,-1,]),'VAR':([2,],[3,]),'IN':([3,],[4,]),'VALUE':([4,5,6,7,9,],[7,7,-3,-4,-2,]),'DO':([5,6,7,9,],[8,-3,-4,-2,]),'COMMAND':([8,10,11,12,14,],[12,12,-5,-7,-6,]),'DONE':([10,11,12,14,],[13,-5,-7,-6,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'for_loop':([0,],[1,]),'values':([4,],[5,]),'value':([4,5,],[6,9,]),'commands':([8,],[10,]),'command':([8,10,],[11,14,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> for_loop","S'",1,None,None,None),
  ('for_loop -> FOR VAR IN values DO commands DONE','for_loop',7,'p_for_loop','c:\\Users\\anju5\\Desktop\\forloopeeee.py',6),
  ('values -> values value','values',2,'p_values','c:\\Users\\anju5\\Desktop\\forloopeeee.py',11),
  ('values -> value','values',1,'p_values','c:\\Users\\anju5\\Desktop\\forloopeeee.py',12),
  ('value -> VALUE','value',1,'p_value','c:\\Users\\anju5\\Desktop\\forloopeeee.py',17),
  ('commands -> command','commands',1,'p_commands','c:\\Users\\anju5\\Desktop\\forloopeeee.py',22),
  ('commands -> commands command','commands',2,'p_commands','c:\\Users\\anju5\\Desktop\\forloopeeee.py',23),
  ('command -> COMMAND','command',1,'p_command','c:\\Users\\anju5\\Desktop\\forloopeeee.py',28),
]
