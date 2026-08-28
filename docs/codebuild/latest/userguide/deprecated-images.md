---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/deprecated-images.html
---

# Deprecated CodeBuild images
<a name="deprecated-images"></a>

A *deprecated image* is an image that is no longer cached or updated by CodeBuild. A deprecated image no longer receives minor version updates or patch version updates, and because they are no longer updated, using them may not be secure. If your CodeBuild project is configured to use an older image version, the provisioning process will download this docker image and use it to create the containerized runtime environment, which can increase the provisioning duration and overall build duration.

CodeBuild has deprecated the following Docker images. You can still use these images, but they won't be cached on the build host and will result in higher provisioning times.

| Platform | Image identifier | Definition | Deprecation date |
| --- | --- | --- | --- |
| Amazon Linux 2 | aws/codebuild/amazonlinux2-x86\_64-standard:3.0 | al2/standard/3.0 | May 9, 2023 |
| Ubuntu 18.04 | aws/codebuild/standard:4.0 | ubuntu/standard/4.0 | March 31, 2023 |
| Amazon Linux 2 | aws/codebuild/amazonlinux2-aarch64-standard:1.0 | al2/aarch64/standard/1.0 | March 31, 2023 |
| Ubuntu 18.04 | aws/codebuild/standard:3.0 | ubuntu/standard/3.0 | June 30, 2022 |
| Amazon Linux 2 | aws/codebuild/amazonlinux2-x86\_64-standard:2.0 | al2/standard/2.0 | June 30, 2022 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
