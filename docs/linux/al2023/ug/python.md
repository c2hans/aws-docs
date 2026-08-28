---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/python.html
---

# Python in AL2023
<a name="python"></a>

AL2023 removed Python 2.7 and any components requiring Python are now written to work with Python 3.

AL2023 makes Python 3 available as `/usr/bin/python3` to retain compatibility with customer code, as well as Python code shipped with AL2023, this will remain as Python 3.9 for the life of AL2023.

The version of python that `/usr/bin/python3` points to is considered the *system Python* and for AL2023 this is Python 3.9.

AL2023 currently provides newer versions of Python, including versions 3.11, 3.12, 3.13, and 3.14. Each version is supported for the same period of time as upstream Python. For more information, see [Package support statements](https://docs.aws.amazon.com/linux/al2023/release-notes/all-packages-AL2023.12.html).

Multiple versions of Python can be installed simultaneously on AL2023. Although `/usr/bin/python3` will always be Python 3.9, each version of Python is namespaced and can be found by its version number. For example, if `python3.11` is installed, then `/usr/bin/python3.11` will exist alongside `/usr/bin/python3.9` and the `/usr/bin/python3` symlink to `/usr/bin/python3.9`.

**Note**
Do not change what the `/usr/bin/python3` symlink points to because this might break the core functionality of AL2023.

## Migrating to newer Python versions
<a name="python-migration"></a>

**The upstream Python community provides migration documentation for moving:**
+ [ to Python 3.14](https://docs.python.org/3/whatsnew/3.14.html)
+ [ to Python 3.13](https://docs.python.org/3/whatsnew/3.13.html)
+ [ to Python 3.12](https://docs.python.org/3/whatsnew/3.12.html)
+ [ to Python 3.11](https://docs.python.org/3/whatsnew/3.11.html)

## Python modules in AL2023
<a name="python-modules"></a>

Various Python modules are packaged as RPMs in AL2023. Typically, RPMs for Python modules will be built targeting only the system version of Python.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
