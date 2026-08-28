---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-conda-aftereffects.html
---

# Build an Adobe After Effects conda package for Deadline Cloud
<a name="examples-conda-aftereffects"></a>

The samples repository includes the following After Effects conda recipes:
+ [aftereffects-25.1](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/aftereffects-25.1): Adobe After Effects 25.1.
+ [aftereffects-plugin-bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/aftereffects-plugin-bundle): A bundle of After Effects plugins.
+ [aftereffects-saber](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/aftereffects-saber): The Saber plugin for After Effects.

Submit the build:

```
./submit-package-job aftereffects-25.1
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
