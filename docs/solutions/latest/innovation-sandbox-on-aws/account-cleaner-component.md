---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-cleaner-component.html
---

# Account Cleaner components
<a name="account-cleaner-component"></a>

![account cleaner.drawio](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/account-cleaner.drawio.png)

**ISB Account Cleaner components**
The **Account Cleaner** is used to clean sandbox accounts either during onboarding to Innovation Sandbox, or after a lease has expired and the account needs to be recycled for reuse. It is composed of an AWS StepFunction with these steps:

1. The account cleaner invokes the **initialize cleanup** Lambda which performs pre-cleanup actions.

1. An [AWS CodeBuild](https://aws.amazon.com/codebuild/) project is initiated that assumes into the sandbox account and runs [AWS Nuke](https://github.com/ekristen/aws-nuke) on the account to delete all supported resources (Innovation Sandbox configures AWS Nuke to ignore protected solution assets). The CodeBuild project uses a public ECR image with the AWS Nuke binary installed and is managed by the development team.

1. The workflow enters a loop where it attempts clean-up multiple times. This is so that any deletion failures due to resource dependencies eventually resolve themselves and that any resources that are created during clean-up (db snapshots, logs, custom resources OnDelete) are deleted. By default, the solution performs three successful passes of the clean-up loop, but customers can configure this value using AWS AppConfig.

**Note**
If the clean-up fails, the Step Function (state machine) exits and sends a clean-up failure event to the event bus which moves the account to **Quarantine** OU. If the clean-up is successful, a success event is sent to the event bus which will move the account to **Available** OU so that it can be reused.
