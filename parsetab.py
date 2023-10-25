
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIRECTORY LS OPTIONstatement : ls option directoryls : LSoption : option options\n                | emptydirectory : directories directory\n                   | emptyempty :options : OPTIONdirectories : DIRECTORY'
    
_lr_action_items = {'LS':([0,],[3,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,],[0,-7,-2,-7,-4,-1,-3,-7,-6,-8,-9,-5,]),'OPTION':([2,3,4,5,7,10,],[-7,-2,10,-4,-3,-8,]),'DIRECTORY':([2,3,4,5,7,8,10,11,],[-7,-2,11,-4,-3,11,-8,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'ls':([0,],[2,]),'option':([2,],[4,]),'empty':([2,4,8,],[5,9,9,]),'directory':([4,8,],[6,12,]),'options':([4,],[7,]),'directories':([4,8,],[8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> ls option directory','statement',3,'p_statement','lsparse.py',5),
  ('ls -> LS','ls',1,'p_ls','lsparse.py',9),
  ('option -> option options','option',2,'p_option','lsparse.py',13),
  ('option -> empty','option',1,'p_option','lsparse.py',14),
  ('directory -> directories directory','directory',2,'p_directory','lsparse.py',18),
  ('directory -> empty','directory',1,'p_directory','lsparse.py',19),
  ('empty -> <empty>','empty',0,'p_empty','lsparse.py',23),
  ('options -> OPTION','options',1,'p_options','lsparse.py',27),
  ('directories -> DIRECTORY','directories',1,'p_directories','lsparse.py',31),
]
