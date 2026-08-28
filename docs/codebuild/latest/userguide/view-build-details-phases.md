---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/view-build-details-phases.html
---

# Build phase transitions
<a name="view-build-details-phases"></a>

Builds in AWS CodeBuild proceed in phases:

![The CodeBuild phases.](http://docs.aws.amazon.com/codebuild/latest/userguide/images/build-phases.png)

**Important**
The `UPLOAD_ARTIFACTS` phase is always attempted, even if the `BUILD` phase fails.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
