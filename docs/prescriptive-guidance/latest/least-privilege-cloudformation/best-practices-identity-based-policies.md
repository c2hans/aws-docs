---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/least-privilege-cloudformation/best-practices-identity-based-policies.html
---

# Best practices for configuring identity-based policies for least-privilege CloudFormation access
<a name="best-practices-identity-based-policies"></a>
+ For IAM principals who require permissions to access CloudFormation, you must balance the need for permissions to operate CloudFormation with the principle of least privilege. To help you adhere to the principle of least privilege, we recommend that you define the IAM principal's identity-based with specific actions that allow the principal to do the following:
  + Create, update, and delete a CloudFormation stack.
  + Pass one or more service roles that have the permissions required to deploy the resources defined in the CloudFormation templates. This allows CloudFormation to assume the service role and provision the resources in the stack on behalf of the IAM principal.
+ *Privilege escalation* refers to the ability of a user with access, to elevate their permission levels and compromise security. Least-privilege is an important best practice that can help prevent privilege escalation. Because CloudFormation supports provisioning of [IAM resource types](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IAM.html), such as policies and roles, an IAM principal could escalate their privileges through CloudFormation by:
  + **Using a CloudFormation stack to provision an IAM principal with highly privileged permissions, policies, or credentials** – To help prevent this, we recommend using permission guardrails to constrain the level of access for IAM principals. *Permission guardrails* set the maximum permissions that an identity-based policy can grant to an IAM principal. This helps prevent intentional and unintentional privilege escalation. You can use the following types of policies as permissions guardrails:
    + Permissions boundaries define the maximum permissions that an identity-based policy can grant to an IAM principal. For more information, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html).
    + In AWS Organizations, you can use [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCPs) to define the maximum available permissions at an organizational level. SCPs affect only IAM roles and users that are managed by accounts in the organization. You can attach SCPs to accounts, organizational units, or to the organizational root. For more information, see [SCP effects on permissions](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html#scp-effects-on-permissions).
  + **Creating a CloudFormation service role that offers extensive permissions** – To help prevent this, we recommend that you add the following fine-grained permissions to the identity-based policies for IAM principals who will be using CloudFormation:
    + Use the `cloudformation:RoleARN` condition key to control which CloudFormation service roles the IAM principal can use.
    + Allow the `iam:PassRole` action only for the specific CloudFormation service roles that the IAM principal needs to pass.

  For more information, see [Granting an IAM principal permissions to use service roles for CloudFormation](service-roles-for-cloudformation.md#permissions-use-cloudformation-service-role) in this guide.
+ Restrict permissions by using permissions guardrails, such as permissions boundaries and SCPs, and grant permissions by using an identity-based or resource-based policy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
