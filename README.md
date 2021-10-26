> All Available Data
+------------------------+------------------+
|          dept          |     courses      |
+------------------------+------------------+
|      Data Science      |   [325K,462k]    |
|    Game Development    | [319K,464K,360C] |
| Web/Mobile Development |   [303K,303L]    |
+------------------------+------------------+
+-----+----------+-------------------+----------------------------------------+
|  id | course # | max # of students |              instructors               |
+-----+----------+-------------------+----------------------------------------+
| SEM |   325K   |         25        |       Нурлан Иманмаликович, Адик       |
| SoL |   319K   |         35        | Нурлан Иманмаликович, Адик, Измуханова |
| LLO |   462k   |         25        |       Нурлан Иманмаликович, Адик       |
| SoL |   464K   |         35        |           Измуханова, Кирилл           |
| SoM |   360C   |         35        |                 Кирилл                 |
| SSE |   303K   |         45        |    Нурлан Иманмаликович, Измуханова    |
| MMK |   303L   |         45        |              Адик, Кирилл              |
+-----+----------+-------------------+----------------------------------------+
+--------+----------------------+
| room # | max seating capacity |
+--------+----------------------+
|  401a  |          25          |
|  324   |          45          |
|  325   |          35          |
+--------+----------------------+
+----+----------------------+
| id |     instructors      |
+----+----------------------+
| I1 | Нурлан Иманмаликович |
| I2 |         Адик         |
| I3 |      Измуханова      |
| I4 |        Кирилл        |
+----+----------------------+
+-----+-------------------+
|  id |    Meeting Time   |
+-----+-------------------+
| MT1 | MWF 09:00 - 10:00 |
| MT2 | MWF 10:00 - 11:00 |
| MT3 | TTH 09:00 - 10:30 |
| MT4 | TTH 10:30 - 12:00 |
+-----+-------------------+

> Generation # 0
+------------+---------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| schedule # | fitness | # of conflicts |                                                                                                                                   classes                                                                                                                                   |
+------------+---------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|     0      |   0.5   |       1        |   ['Data Science,325K,325,I3, MT2', 'Data Science,462k,324,I1, MT4', 'Game Development,319K,325,I3, MT3', 'Game Development,464K,324,I1, MT3', 'Game Development,360C,324,I4, MT3', 'Web/Mobile Development,303K,324,I2, MT1', 'Web/Mobile Development,303L,324,I1, MT2']   |
|     1      |  0.333  |       2        |  ['Data Science,325K,325,I2, MT2', 'Data Science,462k,401a,I3, MT2', 'Game Development,319K,324,I4, MT4', 'Game Development,464K,325,I2, MT1', 'Game Development,360C,324,I1, MT4', 'Web/Mobile Development,303K,324,I1, MT2', 'Web/Mobile Development,303L,401a,I3, MT1']  |
|     2      |  0.333  |       2        |  ['Data Science,325K,401a,I1, MT1', 'Data Science,462k,401a,I1, MT4', 'Game Development,319K,325,I2, MT1', 'Game Development,464K,325,I1, MT2', 'Game Development,360C,325,I4, MT3', 'Web/Mobile Development,303K,401a,I1, MT2', 'Web/Mobile Development,303L,324,I3, MT1'] |
|     3      |   0.2   |       4        |  ['Data Science,325K,324,I2, MT4', 'Data Science,462k,325,I2, MT1', 'Game Development,319K,401a,I3, MT1', 'Game Development,464K,324,I2, MT1', 'Game Development,360C,325,I2, MT3', 'Web/Mobile Development,303K,325,I4, MT2', 'Web/Mobile Development,303L,401a,I2, MT2']  |
|     4      |   0.2   |       4        |   ['Data Science,325K,324,I1, MT4', 'Data Science,462k,325,I2, MT1', 'Game Development,319K,325,I4, MT3', 'Game Development,464K,324,I3, MT3', 'Game Development,360C,324,I4, MT4', 'Web/Mobile Development,303K,325,I2, MT2', 'Web/Mobile Development,303L,325,I4, MT2']   |
|     5      |  0.167  |       5        |  ['Data Science,325K,401a,I1, MT1', 'Data Science,462k,325,I2, MT4', 'Game Development,319K,324,I3, MT4', 'Game Development,464K,324,I1, MT2', 'Game Development,360C,401a,I4, MT3', 'Web/Mobile Development,303K,325,I2, MT4', 'Web/Mobile Development,303L,324,I2, MT2']  |
|     6      |  0.167  |       5        |  ['Data Science,325K,324,I3, MT2', 'Data Science,462k,324,I3, MT3', 'Game Development,319K,325,I2, MT3', 'Game Development,464K,324,I4, MT4', 'Game Development,360C,324,I4, MT2', 'Web/Mobile Development,303K,401a,I1, MT2', 'Web/Mobile Development,303L,401a,I1, MT2']  |
|     7      |  0.143  |       6        |  ['Data Science,325K,324,I3, MT1', 'Data Science,462k,324,I3, MT2', 'Game Development,319K,401a,I4, MT2', 'Game Development,464K,401a,I1, MT3', 'Game Development,360C,324,I2, MT2', 'Web/Mobile Development,303K,324,I4, MT2', 'Web/Mobile Development,303L,324,I2, MT4']  |
|     8      |  0.111  |       8        | ['Data Science,325K,401a,I3, MT2', 'Data Science,462k,401a,I4, MT2', 'Game Development,319K,324,I4, MT2', 'Game Development,464K,401a,I3, MT2', 'Game Development,360C,401a,I1, MT4', 'Web/Mobile Development,303K,324,I1, MT1', 'Web/Mobile Development,303L,324,I3, MT1'] |
+------------+---------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+---------+------------------------+----------------+-----------+---------------------------+-------------------------+
| Class # |          Dept          |     Course     |    Room   |         Instructor        |       Meeting Time      |
+---------+------------------------+----------------+-----------+---------------------------+-------------------------+
|    0    |      Data Science      | 325K (SEM, 25) | 325, (35) |      Измуханова (I3)      | MWF 10:00 - 11:00 (MT2) |
|    1    |      Data Science      | 462k (LLO, 25) | 324, (45) | Нурлан Иманмаликович (I1) | TTH 10:30 - 12:00 (MT4) |
|    2    |    Game Development    | 319K (SoL, 35) | 325, (35) |      Измуханова (I3)      | TTH 09:00 - 10:30 (MT3) |
|    3    |    Game Development    | 464K (SoL, 35) | 324, (45) | Нурлан Иманмаликович (I1) | TTH 09:00 - 10:30 (MT3) |
|    4    |    Game Development    | 360C (SoM, 35) | 324, (45) |        Кирилл (I4)        | TTH 09:00 - 10:30 (MT3) |
|    5    | Web/Mobile Development | 303K (SSE, 45) | 324, (45) |         Адик (I2)         | MWF 09:00 - 10:00 (MT1) |
|    6    | Web/Mobile Development | 303L (MMK, 45) | 324, (45) | Нурлан Иманмаликович (I1) | MWF 10:00 - 11:00 (MT2) |
+---------+------------------------+----------------+-----------+---------------------------+-------------------------+
=