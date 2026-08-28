---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/jython-language-support.html
---

# Jython
<a name="jython-language-support"></a>

You can add support for the CodeGuru Profiler agent into your Jython application by adding the following lines into your startup or `main` function.

```
import sys
sys.path.append("/path/to/codeguru-profiler-java-agent-1.2.6.jar")
from software.amazon.codeguruprofilerjavaagent import Profiler

Profiler.builder()
    .profilingGroupName("MyProfilingGroup")
    .build()
    .start()
...
```

You need to [add a dependency](enabling-the-agent-with-code.md) to the agent .jar file.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
