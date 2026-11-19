---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/clojure-language-support.html
---

# Clojure

You can add support for the CodeGuru Profiler agent into your Clojure application by adding the following lines into your startup or `main` function.

```
(-> (software.amazon.codeguruprofilerjavaagent.Profiler/builder)
    (.profilingGroupName "MyProfilingGroup")
    (.awsCredentialsProvider myAwsCredentialsProvider) ; optional
    (.build)
    (.start))
...
```

You need to [add a dependency](enabling-the-agent-with-code.md) to the agent .jar file.
