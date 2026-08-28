---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/clojure-language-support.html
---

# Clojure
<a name="clojure-language-support"></a>

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
