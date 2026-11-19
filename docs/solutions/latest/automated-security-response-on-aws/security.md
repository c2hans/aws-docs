---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/security.html
---

# Security

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit the [AWS Cloud Security](https://aws.amazon.com/security/).

## API Gateway Security Policy
<a name="api-gateway-security-policy"></a>

If you choose to enable the solution’s Web User Interface, an API Gateway REST API is deployed alongside the Admin CloudFormation stack which serves as the backend for all operations in the Web UI. The REST API deployed by the solution uses the default TLS security policy for API Gateway, which is `TLS-1-2` for regional APIs.

However, after deploying the Admin CloudFormation stack you may choose to customize the solution’s REST API by adding a more restrictive TLS security policy. For example, you can choose the `TLS_1_2 security policy` to restrict for traffic using TLSv1.2 or TLSv1.3. You can find the solution’s REST API in the API Gateway console under the name **AutomatedSecurityResponseApi**.

In order to choose a security policy for the solution’s REST API, you must first configure a custom domain name. For more information, see [Custom domain name for public REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).

For more information on adding a security policy to your REST API, see [Choose a security policy for your REST API custom domain in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html) in the API Gateway guide.

## Protect Action Log entries in member accounts
<a name="action-log-entry-protection"></a>

This section explains how to use a service control policy (SCP) to stop principals in a member account from writing false Action Log entries for that account.

If you enable the Action Log with the **EnableCloudTrailForASRActionLog** parameter, an EventProcessor AWS Lambda function in each member account writes entries to the Action Log. The Action Log is in the Admin account. The Admin account accepts entries only from an AWS Identity and Access Management (IAM) role named `SO0111-ASR-EventProcessor-` followed by the AWS Region code, for example `SO0111-ASR-EventProcessor-aa-example-1`. Each member account can write only to Amazon CloudWatch Logs log streams named for its own account ID.

If you grant broad IAM, Lambda, or Amazon S3 permissions to a principal in a member account, that principal can still write entries under the account’s own ID. For example, the principal can do the following:
+ Edit the code or configuration of the EventProcessor function.
+ Edit the trust policy or permissions policies of the EventProcessor role.
+ Create a role named for a Region where you didn’t deploy the member stack.
+ Invoke the function directly, or upload objects to the Amazon S3 bucket that triggers it.

To prevent this, attach an SCP to the organizational units (OUs) in AWS Organizations that contain your member accounts. You must enable all features in your organization to use SCPs.

The SCP must allow the IAM role that deploys the member stack, so that you can still update the stack. If you deploy the member stack with AWS CloudFormation StackSets with self-managed permissions, use the StackSets execution role in each member account. For example, `AWSCloudFormationStackSetExecutionRole`. If you deploy the member stack as a single stack, use the role that you deploy it with. If you pass a CloudFormation service role, use that role.

The following example SCP denies these changes to all principals except the deployment role:

 **Example – Service control policy (SCP) that protects Action Log entries**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ProtectAsrEventProcessorRole",
      "Effect": "Deny",
      "Action": [
        "iam:CreateRole",
        "iam:DeleteRole",
        "iam:UpdateAssumeRolePolicy",
        "iam:PutRolePolicy",
        "iam:DeleteRolePolicy",
        "iam:AttachRolePolicy",
        "iam:DetachRolePolicy",
        "iam:PutRolePermissionsBoundary",
        "iam:DeleteRolePermissionsBoundary",
        "iam:PassRole"
      ],
      "Resource": "arn:*:iam::*:role/SO0111-ASR-EventProcessor-*",
      "Condition": {
        "ArnNotLike": {
          "aws:PrincipalArn": "arn:*:iam::*:role/<member-stack-deployment-role>"
        }
      }
    },
    {
      "Sid": "ProtectAsrEventProcessorFunction",
      "Effect": "Deny",
      "Action": [
        "lambda:InvokeFunction",
        "lambda:UpdateFunctionCode",
        "lambda:UpdateFunctionConfiguration",
        "lambda:AddPermission",
        "lambda:RemovePermission",
        "lambda:DeleteFunction"
      ],
      "Resource": [
        "arn:*:lambda:*:*:function:SO0111-ASR-EventProcessor",
        "arn:*:lambda:*:*:function:SO0111-ASR-EventProcessor:*"
      ],
      "Condition": {
        "ArnNotLike": {
          "aws:PrincipalArn": "arn:*:iam::*:role/<member-stack-deployment-role>"
        }
      }
    },
    {
      "Sid": "ProtectAsrManagementEventsBucket",
      "Effect": "Deny",
      "Action": [
        "s3:PutObject",
        "s3:ReplicateObject"
      ],
      "Resource": "arn:*:s3:::so0111-asr-*-management-events-*/*"
    }
  ]
}
```

The example SCP contains the following elements:
+  {{<member-stack-deployment-role>}}: Replace this with the name of the role that deploys the member stack. If the role has a path, include the path. For example, roles for AWS IAM Identity Center permission sets have a path that starts with `aws-reserved/sso.amazonaws.com/`.
+  `ProtectAsrEventProcessorRole`: Denies changes to the EventProcessor role, and denies passing the role to another function.
+  `ProtectAsrEventProcessorFunction`: Denies changes to the EventProcessor function and its permissions, and denies invoking it directly.
+  `ProtectAsrManagementEventsBucket`: Denies uploads and replicated objects to the bucket that triggers the function.

SCPs don’t apply to AWS service principals. AWS CloudTrail can still deliver log files to the bucket, and Amazon S3 can still invoke the function.

Also protect the deployment role. Any principal that can assume that role, or change its trust policy, bypasses this SCP.

Test the SCP on an OU with a single test account before you attach it to other OUs. Then confirm that you can update the member stack.

SCPs don’t apply to the management account. If you deploy the member stack in the management account, this SCP doesn’t protect its EventProcessor. Restrict IAM, Lambda, and Amazon S3 permissions in that account directly. For more information, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide*.

Before v4.1.2, any principal in a member account could write Action Log entries for any account. If you can’t upgrade to v4.1.2 right away, do the following:
+ Attach an SCP to your member account OUs that denies `sts:AssumeRole` on `CrossAccountLogWriterRole` in the Admin account to all principals except the EventProcessor role. In versions before v4.1.2, CloudFormation generates the EventProcessor role name, so find it in each member account. In the Lambda console, open the EventProcessor function and view its execution role.
+ In the Admin account, alert on AWS CloudTrail `AssumeRole` events for `CrossAccountLogWriterRole` from any other principal. Don’t filter on the role session name, because the caller chooses it.

Entries in log streams named only with a date were written before v4.1.2. The Admin account didn’t verify which account wrote them. Before you rely on these entries, compare them to AWS CloudTrail in the member account.

## IAM.21 findings for the solution’s permissions boundaries
<a name="iam21-permissions-boundary-findings"></a>

This section explains why AWS Security Hub Cloud Security Posture Management (CSPM) reports IAM.21 findings for the solution’s permissions boundary policies, and how to suppress them.

Security Hub CSPM control IAM.21 (*IAM customer managed policies that you create should not allow wildcard actions for services*, Low severity) can report a `FAILED` finding in v4.1.2 and later for the customer managed policies in the following table.

| Policy | Account | Created by | When |
| --- | --- | --- | --- |
|  `SO0111-ASR-Remediation-Boundary`  | Each member account | Member roles stack | Always |
|  `SO0111-ASR-Custom-Runbook-Test-Boundary`  | Admin account | Admin stack | Only when you set **EnableMcpServer** to `yes`  |

For more information about this control, see [Security Hub CSPM controls for AWS Identity and Access Management](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-21) in the *AWS Security Hub User Guide*.

These policies are permissions boundaries. They limit the maximum permissions of the remediation roles that the solution creates for registered Custom Runbooks (see [Custom remediation runbooks](custom-remediation-runbooks.md)). A *permissions boundary* grants no permissions on its own. Each policy allows all actions except those in the AWS Identity and Access Management (IAM), AWS Security Token Service (AWS STS), and AWS Organizations namespaces. It does this with an `Allow` statement that uses `NotAction` with `iam:*`, `sts:*`, and `organizations:*`. Each policy also explicitly denies all actions in those three namespaces. IAM.21 fails any `Allow` statement whose `NotAction` element names all actions of a service, such as `iam:*`.

The boundary must allow any action that a Custom Runbook might call, so it can’t list individual actions. A policy that allows `"Action": "" ` instead fails control IAM.1 (High severity). In versions earlier than v4.1.2, the boundary used `"Action": "`, and IAM.1 reported a `FAILED` finding for it. Starting in v4.1.2, the solution uses the `NotAction` form so that the boundary passes IAM.1. Update to v4.1.2 or later to replace the High severity IAM.1 finding with this Low severity IAM.21 finding.

IAM.21 doesn’t evaluate a policy that is in use as a permissions boundary. The finding therefore remains until a Custom Runbook remediation role uses the boundary. When you deploy a Custom Runbook to a member account, the solution creates the runbook’s remediation role with `SO0111-ASR-Remediation-Boundary` as its permissions boundary. Each member account has its own copy of the policy. The finding remains in member accounts where you haven’t deployed a Custom Runbook.

The finding isn’t removed immediately. AWS Config doesn’t re-evaluate the policy when a role starts using it as a permissions boundary. Security Hub CSPM archives the finding after AWS Config next evaluates the policy, which can take several days.

In the admin account, only the temporary roles that test a Custom Runbook use `SO0111-ASR-Custom-Runbook-Test-Boundary`. The solution deletes those roles after the test, so this finding usually remains. To clear it, suppress it as described in the following steps.

 **Impact:** None. The policies grant no access on their own.

To suppress the finding, create an automation rule in the Security Hub CSPM administrator account with the following settings. Create the rule in the Region where AWS Config records global resources, such as IAM policies. Security Hub CSPM reports the finding in that Region, and an automation rule applies only in the Region where you create it.
+ Criteria: `ComplianceSecurityControlId` **EQUALS** `IAM.21`, and `ResourceId` **CONTAINS** `:policy/SO0111-ASR-Remediation-Boundary` or **CONTAINS** `:policy/SO0111-ASR-Custom-Runbook-Test-Boundary`.
+ Action: Set the workflow status to `SUPPRESSED`, with a note such as `ASR permissions boundary; grants no permissions.`

Security Hub CSPM doesn’t count suppressed findings when it calculates a control’s status. For more information about automation rules, see [Understanding automation rules in Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *AWS Security Hub User Guide*.
