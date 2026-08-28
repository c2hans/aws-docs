---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/setting-up-cli.html
---

# Interact with CodeBuild using the AWS CLI
<a name="setting-up-cli"></a>

If you follow the steps in [Getting started using the console](getting-started-overview.md#getting-started) to access AWS CodeBuild for the first time, you most likely do not need the information in this topic. However, as you continue using CodeBuild, you might want to do things such as allow users to use the AWS CLI to interact with CodeBuild instead of (or in addition to) the CodeBuild console, the CodePipeline console, or the AWS SDKs.

To install and configure the AWS CLI, see [Getting Set Up with the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html) in the *AWS Command Line Interface User Guide*.

After installing the AWS CLI, complete the following tasks:

1. Run the following command to confirm whether your installation of the AWS CLI supports CodeBuild:

   ```
   aws codebuild list-builds
   ```

   If successful, information similar to the following will appear in the output:

   ```
   {
     "ids": []
   }
   ```

   The empty square brackets indicate that you have not yet run any builds.

1. If an error is output, you must uninstall your current version of the AWS CLI and then install the latest version. For more information, see [Uninstalling the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-uninstall.html) and [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) in the *AWS Command Line Interface User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
