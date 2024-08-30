# pytest-testdata

![Languate - Python](https://img.shields.io/badge/language-python-blue.svg)
![PyPI - License](https://img.shields.io/pypi/l/pytest-testdata)
![PyPI](https://img.shields.io/pypi/v/pytest-testdata)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pytest-testdata)

Pytest测试项目数据目录配置及数据文件加载

---

### 如何使用

1. 安装 `pytest-testdata`

使用pip安装

```sh
pip install pytest-testdata
```

2. 配置测试目录
> 默认测试目录为 项目跟目录 (rootdir) / data

也可以通过命令行参数或pytest.ini配置修改
```sh
pytest . --testdata-dr=testdata
```

或在pytest.ini中配置
```ini
[pytest]
testdata_dir=testdata
```

3. 测试中使用测试目录或测试数据
- Fixture函数testdata_dir: 当前项目测试数据目录路径
- Fixture函数testdata: 测试数据加载对象

例如，测试项目中数据如下
```
project
  data/
    1.txt
    2.png
    3.json
```

```python
import json

def test_use_testdata_01(testdata_dir):
    data1 = (testdata_dir / '1.txt').read()
    data2 = (testdata_dir / '2.png').read_bytes()
    with open(testdata_dir / '3.json') as f:
        data3 = json.load(f)
    
def test_use_testdata_02(testdata):
    data1 = testdata.read('1.txt')
    data2 = testdata.read_bytes('2.png')
    data3 = testdata.load('3.json')
```