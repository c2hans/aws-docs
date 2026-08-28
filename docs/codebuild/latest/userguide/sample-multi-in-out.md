---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/sample-multi-in-out.html
---

# Multiple input sources and output artifacts sample
<a name="sample-multi-in-out"></a>

You can create an AWS CodeBuild build project with more than one input source and more than one set of output artifacts. This sample shows you how to set up a build project that:
+ Uses multiple sources and repositories of varying types.
+ Publishes build artifacts to multiple S3 buckets in a single build.

 In the following sample, you create a build project and use it to run a build. The sample uses the build project's buildspec file to show you how to incorporate more than one source and create more than one set of artifacts.

To learn how to create a pipeline that uses multiple source inputs to CodeBuild to create multiple output artifacts, see [Sample of a CodePipeline/CodeBuild integration with multiple input sources and output artifacts](sample-codepipeline.md#sample-pipeline-multi-input-output).

**Topics**
+ [Create a build project with multiple inputs and outputs](sample-multi-in-out-create.md)
+ [Create a build project without a source](no-source.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
