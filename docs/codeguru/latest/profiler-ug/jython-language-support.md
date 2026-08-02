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
