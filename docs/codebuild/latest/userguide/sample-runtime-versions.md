---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runtime-versions.html
---

# Runtime versions in buildspec file sample for CodeBuild
<a name="sample-runtime-versions"></a>

If you use the Amazon Linux 2 (AL2) standard image version 1.0 or later, or the Ubuntu standard image version 2.0 or later, you can specify one or more runtimes in the `runtime-versions` section of your buildspec file. The following samples show how you can change your project runtime, specify more than one runtime, and specify a runtime that is dependent on another runtime. For information about supported runtimes, see [Docker images provided by CodeBuild](build-env-ref-available.md).

**Note**
If you use Docker in your build container, your build must run in privileged mode. For more information, see [Run AWS CodeBuild builds manually](run-build.md) and [Create a build project in AWS CodeBuild](create-project.md).

**Topics**
+ [Update the runtime version in the buildspec file](sample-runtime-update-version.md)
+ [Specify two runtimes](sample-runtime-two-major-version-runtimes.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
