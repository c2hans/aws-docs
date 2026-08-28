---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/aws-codecommit.html
---

# AWS CodeCommit
<a name="aws-codecommit"></a>

[AWS CodeCommit](https://aws.amazon.com/codecommit/) is a secure, highly scalable, managed source control service that hosts private git repositories. CodeCommit reduces the need for you to operate your own source control system and there is no hardware to provision and scale or software to install, configure, and operate. You can use CodeCommit to store anything from code to binaries, and it supports the standard functionality of GitHub, allowing it to work seamlessly with your existing Git-based tools. Your team can also use CodeCommit’s online code tools to browse, edit, and collaborate on projects. AWS CodeCommit has several benefits:
+ **Collaboration** — AWS CodeCommit is designed for collaborative software development. You can easily commit, branch, and merge your code, which helps you easily maintain control of your team’s projects. CodeCommit also supports pull requests, which provide a mechanism to request code reviews and discuss code with collaborators.
+ **Encryption** — You can transfer your files to and from AWS CodeCommit using HTTPS or SSH, as you prefer. Your repositories are also automatically encrypted at rest through [AWS Key Management Service](https://aws.amazon.com/kms) (AWS KMS) using customer-specific keys.
+ **Access control** — AWS CodeCommit uses [AWS Identity and Access Management](https://aws.amazon.com/iam) (IAM) to control and monitor who can access your data in addition to how, when, and where they can access it. CodeCommit also helps you monitor your repositories through [AWS CloudTrail](https://aws.amazon.com/cloudtrail) and [Amazon CloudWatch](https://aws.amazon.com/cloudwatch).

  **High availability and durability** — AWS CodeCommit stores your repositories in [Amazon Simple Storage Service](https://aws.amazon.com/s3) (Amazon S3) and [Amazon DynamoDB](https://aws.amazon.com/dynamodb). Your encrypted data is redundantly stored across multiple facilities. This architecture increases the availability and durability of your repository data.
+ **Notifications and custom scripts** — You can now receive notifications for events impacting your repositories. Notifications will come as [Amazon Simple Notification Service](https://aws.amazon.com/sns) (Amazon SNS) notifications. Each notification will include a status message as well as a link to the resources whose event generated that notification. Additionally, using AWS CodeCommit repository cues, you can send notifications and create HTTP webhooks with Amazon SNS or invoke [AWS Lambda](https://aws.amazon.com/lambda) functions in response to the repository events you choose.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
