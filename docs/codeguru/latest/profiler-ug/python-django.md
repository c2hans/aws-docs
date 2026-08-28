---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-django.html
---

# Django
<a name="python-django"></a>

Start the profiler in your settings file. This is usually the file that you’re setting for `DJANGO_SETTINGS_MODULE`. Then, start your application as usual.

The following is an example that you can add to `settings.py`

```
from codeguru_profiler_agent import Profiler
Profiler(profiling_group_name='MyProfilingGroup').start()
```

Set the following in your `wsgi.py` file. This example is for a module named `mysite`. Your files may be in a different location.

```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
```

Set the following in your `settings.py` file.

```
Profiler(profiling_group_name='MyProfilingGroup').start()
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
