---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-onb-roles.html
---

# The template to create AMS roles
<a name="acc-onb-roles"></a>

The following AMS role grants permissions to your AMS cloud architect (CA). The following zip file contains Terraform code and CloudFormation template that simplifies creating the IAM role, permissions policy, and trust policy. For more information, consult with your CA.

| Role Name | Required by | Sample Templates |
| --- |--- |--- |
| `aws_managedservices_onboarding_role` | AMS personnel during onboarding only | [onboarding\_role\_minimal.zip](samples/onboarding_role_minimal.zip) |

**Note**
After you select and download a sample template (one per role), you will upload these as definitions of CloudFormation stacks in [Create `aws_managedservices_onboarding_role` with CloudFormation for Accelerate](acc-onb-create-roles-with-cf.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
