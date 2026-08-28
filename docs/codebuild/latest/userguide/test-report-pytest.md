---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-pytest.html
---

# Set up test reporting with pytest
<a name="test-report-pytest"></a>

The following procedure demonstrates how to set up test reporting in AWS CodeBuild with the [pytest testing framework](https://docs.pytest.org/).

The procedure requires the following prerequisites:
+ You have an existing CodeBuild project.
+ Your project is a Python project that is set up to use the pytest testing framework.

Add the following entry to either the `build` or `post_build` phase of your `buildspec.yml` file. This code automatically discovers tests in the current directory and exports the test reports to the file specified by {{<test report directory>}}/{{<report filename>}}. The report uses the `JunitXml` format.

```
      - python -m pytest --junitxml={{<test report directory>}}/{{<report filename>}}
```

In your `buildspec.yml` file, add/update the following sections.

```
version: 0.2

phases:
  install:
    runtime-versions:
      python: 3.7
    commands:
      - pip3 install pytest
  build:
    commands:
      - python -m pytest --junitxml={{<test report directory>}}/{{<report filename>}}

reports:
  pytest_reports:
    files:
      - {{<report filename>}}
    base-directory: {{<test report directory>}}
    file-format: JUNITXML
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
