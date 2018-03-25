# わかりにくい点

## extendsテンプレの変数定義と参照

以下のテンプレートはエラーになる。

MyClass.py
```
class {% block Name %}MyClass{% endblock %}:
    def __init__(self):
	    print('init')


{% include "py/main.py" %}
    c = {% block Name %}MyClass{% endblock %}()
```

以下のエラーとなる。

```sh
jinja2.exceptions.TemplateAssertionError: block 'Name' defined twice
```

以下のようにすべき。[参考](https://stackoverflow.com/questions/20929241/how-to-repeat-a-block-in-a-jinja2-template?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)

```sh
class {% block Name %}MyClass{% endblock %}:
    def __init__(self):
	    print('init')


{% include "py/main.py" %}
    c = {{ self.Name() }}()
```

渡された変数を2箇所以上で使おうとするときにハマる。

### 複数の構文を併用せねばならない

* テンプレ変数
    * 宣言: `{% block Name %}{% endblock %}`
    * 参照: `{{ self.Name() }}`

テンプレの字面をみたとき、上記2つが同じものだと思うだろうか？　いや、思えない。

`block *`はスペース区切りの構文なのに、`self.*()`はpython構文。複数の構文を併用せねばならない。見難く、理解しにくく、書きにくい。

### プロパティでなく関数

`self.`と`()`が冗長。

テンプレ変数の参照は、なぜか関数。`self.Name()` でなく `self.Name` にすべきだと思うのだが。

あと、`self.`は省略できるようにすべき。継承があるときだけ`super().Name`とすることで区別できるようにしてほしい。

# こうなったらわかりやすい？

もし、こんなふうに書けたら。

```sh
class {{ Name:MyClass }}:
    def __init__(self):
	    print('init')


{% include "py/main.py" %}
    c = {{ Name }}()
```

extendsしないときのテンプレ同様、`{{}}`で変数名を定義し、参照する。`:`以降でデフォルト値を設定する。

複数行のときはブロック構文にして、インデント対応させるのがいいか。

```sh
class {{ Name:MyClass }}:
    def __init__(self):
	    {% block InitCode %}
        print('called __init__.')
        {% endblock}


{% include "py/main.py" %}
    c = {{ Name }}()
```

テンプレートからテキストを作成する。デフォルト値があるため省略可。
```python
jinja2.Template.render()
```
テンプレ変数を指定すれば、デフォルト値でなく指定値になる。
```python
jinja2.Template.render(Name='Cls1', InitCode='pass')
```

デフォルト値とテンプレートを分離したら、もっとスッキリ書けそう。

MyClass.py
```sh
class {{ Name:MyClass }}:
    def __init__(self):
	    {% block InitCode default="MyClass_InitCode_Default.py" %}


{% include "py/main.py" %}
    c = {{ Name }}()
```

デフォルト値にパスも設定できたら、さらに簡単になる。

MyClass.py
```sh
class {{ Name:MyClass }}:
    def __init__(self):
	    {{ InitCode:MyClass_InitCode_Default.py }}


{% include "py/main.py" %}
    c = {{ Name }}()
```

MyClass_InitCode_Default.py
```sh
print('called __init__.')
```

ただ、以下の問題がある。

* デフォルト値の定義で変数を参照できない
* 外部テンプレをデフォルト値に使うとき、変数を渡せない

jinja2の書式なら解決できる？

# macroで解決できる？

class.py
```python
{% macro define(Name='MyClass') -%}
class {{ Name }}:
{%- endmacro %}
```

MyClasses.py
```python
{% import 'class.py' as class %}
{{ class.define() }} pass
{{ class.define('AAA') }} pass
{{ class.define(Name) }} pass
```

変数`Name`のつもり。これができるかは未確認。

```python
t.render(Name='ZZZ')
```

出力結果。
```python
class MyClass: pass
class AAA: pass
class ZZZ: pass
```

こっちのほうが見やすい？　ただ、実際のテキストがテンプレから見えない。はたしてこれをテンプレと呼べるのか。

以下のようなひとつのテンプレを用意したほうが、はるかに見やすく早い。

```python
class MyClass: pass
class AAA: pass
class {{ Name }}: pass
```

`class *:`が何度も使われるからといって、子テンプレにする価値があるのか。どれくらいの量なら子テンプレにすべきか。判断できないので、結局は最小単位を`macro`化することになる。そして`macro`だらけのテンプレとなる。

# 結論

`extends`はテンプレートが見づらくなるので使わないほうがいい？

* 必ず配置する部分は`include`でまかなう
* デフォルト値か値があるときは上書きしたいなら`macro`を使う


