---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/step-4-call-the-blueprint.html
---

# Step 4. Call your blueprint to create a customized account
<a name="step-4-call-the-blueprint"></a>

When you follow the **Create account** workflow in the AWS Control Tower console, you'll see an optional section where you can enter information about the blueprint you'd like to use for customizing accounts.

**Prerequisites**
You must set up your customization hub account and add at least one blueprint (Service Catalog product) before you can enter that information into the AWS Control Tower console and begin to provision customized accounts.

**Create or update a customized account in the AWS Control Tower console.**

1. Enter the account ID for the account that contains your blueprints.

1. From that account, select an existing Service Catalog product (existing blueprint).

1. Select the proper version of the blueprint (Service Catalog product), if you have more than one version.

1. (Optional) You can add or change a blueprint provisioning policy at this point in the process. The blueprint provisioning policy is written in JSON and attached to an IAM role, so it can provision the resources that are specified in the blueprint template. AWS Control Tower creates this role in the member account so that Service Catalog can deploy resources using CloudFormation stack sets. The role is named `AWSControlTower-BlueprintExecution-bp-{{xxxx}}`. The `AdministratorAccess` policy is applied here by default.

1. Choose the AWS Region or Regions in which you wish to deploy accounts based on this blueprint.

1. If your blueprint contains parameters, you can enter the values for the parameters into additional fields in the AWS Control Tower workflow. The additional values may include: a GitHub repository name, a GitHub branch, an Amazon ECS cluster name, and a GitHub identity for the repository owner.

1. You can customize accounts at a later time by following the **Account update** process, if your hub account or blueprints are not yet ready.

For more details, see [Create a customized account from a blueprint](create-afc-customized-account.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
