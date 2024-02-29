# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tabulate import tabulate


def truth_table(p, q):
  """
  輸出P和Q的真質表

  Args:
    p: 布林值
    q: 布林值

  Returns:
    真質表
  """

  # 建立真值表
  table = [
    ["P", "Q", "P & Q", "P or Q", "P -> Q", "Q -> P", "P <=> Q"],
  ]

  # 迴圈所有可能的P和Q值
  for p_value in [True, False]:
    for q_value in [True, False]:
      # 計算P和Q的真值
      p = p_value
      q = q_value
      not_p = not p
      not_q = not q
      p_and_q = p and q
      p_or_q = p or q
      p_implies_q = not p or q
      q_implies_p = not q or p
      p_iff_q = p_implies_q and q_implies_p

      # 將真值加入真值表
      table.append([p, q, p_and_q, p_or_q, p_implies_q, q_implies_p, p_iff_q])

  # 輸出真值表
  return tabulate(table, tablefmt="pipe", headers="firstrow")


# 輸出真值表
print(truth_table(True, True))
print()
print(truth_table(True, False))
print()
print(truth_table(False, True))
print()
print(truth_table(False, False))