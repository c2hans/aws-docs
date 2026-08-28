---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/report-group-test-case-commands.html
---

# Specify test commands
<a name="report-group-test-case-commands"></a>

 You specify the commands that run your test cases in the `commands` section of your buildspec file. These commands run the test cases specified for your report groups in the `reports` section of your buildspec file. The following is a sample `commands` section that includes commands to run the tests in test files:

```
commands:
    - echo Running tests for surefire junit
    - mvn test -f surefire/pom.xml -fn
    - echo
    - echo Running tests for cucumber with json plugin
    - mvn test -Dcucumber.options="--plugin json:target/cucumber-json-report.json" -f cucumber-json/pom.xml -fn
```

For more information, see [Buildspec syntax](build-spec-ref.md#build-spec-ref-syntax).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
