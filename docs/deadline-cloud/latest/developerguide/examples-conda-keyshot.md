---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-conda-keyshot.html
---

# Build a KeyShot conda package for Deadline Cloud
<a name="examples-conda-keyshot"></a>

The [keyshot-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/keyshot-2025) conda recipe builds a KeyShot 2025 conda package.

Submit the build:

```
./submit-package-job keyshot-2025
```

For a job bundle that uses this package, see [Render KeyShot scenes on Deadline Cloud](examples-jb-keyshot.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
