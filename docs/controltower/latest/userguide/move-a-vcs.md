---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/move-a-vcs.html
---

# Move AFT from AWS CodeCommit to another VCS provider
<a name="move-a-vcs"></a>

This section provides an overview of how you can move AWS Control Tower Account Factory for Terraform (AFT) from AWS CodeCommit as your version control system (VCS) to another VCS provider.

**Step 1.** Set up new repositories in the VCS of your choice.

**Step 2.** Add these repositories as new remotes in `git`.

**Step 3.** Execute `git push` to the new VCS provider.

**Note**
The repository structure that you create should be the same as in AWS CodeCommit. Changing the structure impedes the ability of AFT to execute the desired code.
aft-account-request
 aft-account-customizations
 aft-global-customizations
aft-account-provisioning-customizations

**Step 4.** In your AWS Control Tower management account, update the Terraform module (bootstrap) to point to your VCS provider, as shown in the following example:

**Example: ** [GitLab with Terraform OSS](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/blob/main/examples/gitlab%2Btf_oss/main.tf)

– Perform `terraform plan` to preview changes, then `terraform apply`.

**Step 5.** Complete the steps to finish setting up the CodeConnection (formerly known as CodeStar):

1. Sign in to your AFT management account

1. Locate and complete the pending AWS CodeConnections for the new VCS provider, as described in [Update a pending connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-update.html), or in the AWS console, [`https://us-east-1.console.aws.amazon.com/codesuite/settings/connections`].

1. Reference: [Post-deployment steps](https://docs.aws.amazon.com/controltower/latest/userguide/aft-post-deployment.html)

**Note**
Account pipelines retain the previous source until `aft-invoke-customizations` *Step Functions* is invoked. This invocation can be done as part of the upgrade or as part of the next customizations invocations.

For more information, see this blog: [How to migrate your AWS CodeCommit repository to another Git provider](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
