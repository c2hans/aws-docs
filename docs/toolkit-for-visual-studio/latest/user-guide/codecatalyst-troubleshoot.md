---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/codecatalyst-troubleshoot.html
---

# Troubleshooting
<a name="codecatalyst-troubleshoot"></a>

The following are troubleshooting topics for addressing known issues when working with Amazon CodeCatalyst from the AWS Toolkit for Visual Studio with Amazon Q.

**Topics**
+ [Credentials](#codecatalyst-troubleshoot-credentials)

## Credentials
<a name="codecatalyst-troubleshoot-credentials"></a>

If you encounter a dialog asking for credentials when attempting to clone a git-based repository from CodeCatalyst, your **AWS CodeCommit Credential helper** may be configured globally, causing interference with CodeCatalyst. For additional information about the AWS CodeCommit credential helper, see the [Set up steps for HTTPS connections to AWS CodeCommit repositories on Windows with the AWS CLI credential helper](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-https-windows.html) section of the *AWS CodeCommit* User Guide.

To limit the **AWS CodeCommit Credential helper** to handling only CodeCommit URLs, complete the following steps.

1. open the global git config file in: `%userprofile%\.gitconfig`

1. Locate the following section in your file:

   ```
                           [credential]
                               helper = !aws codecommit credential-helper $@
                               UseHttpPath = true
   ```

1. Change that section to the following:

   ```
                           [credential "https://git-codecommit.*.amazonaws.com"]
                               helper = !aws codecommit credential-helper $@
                               UseHttpPath = true
   ```

1. Save your changes, then complete the steps to clone your repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-visual-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
