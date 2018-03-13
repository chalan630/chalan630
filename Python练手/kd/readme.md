# 快递查询

---

## 预期目标
- [x] 查询快递信息
- [ ] 交互

## 知识点
### PrettyTable 学习
PrettyTable 是python中的一个第三方库，可用来生成美观的ASCII格式的表格，十分实用。  

```python
from prettytable import PrettyTable

x = PrettyTable()
x._set_field_names(["City name", "Area", "Population", "Annual Rainfall"])
x.add_row(["Adelaide",1295, 1158259, 600.5])
x.add_row(["Brisbane",5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])

print(x)
```
输出结果：
```
+-----------+------+------------+-----------------+
| City name | Area | Population | Annual Rainfall |
+-----------+------+------------+-----------------+
|  Adelaide | 1295 |  1158259   |      600.5      |
|  Brisbane | 5905 |  1857594   |      1146.4     |
|   Darwin  | 112  |   120900   |      1714.7     |
|   Hobart  | 1357 |   205556   |      619.5      |
|   Sydney  | 2058 |  4336374   |      1214.8     |
| Melbourne | 1566 |  3806092   |      646.9      |
|   Perth   | 5386 |  1554769   |      869.4      |
+-----------+------+------------+-----------------+
```

## 参考资料
[PrettyTable库文档](https://github.com/dprince/python-prettytable)