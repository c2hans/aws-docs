---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/least-privilege-cloudformation/limiting-and-requiring-stack-policies.html
---

# Limiting and requiring stack policies
<a name="limiting-and-requiring-stack-policies"></a>

As a best practice for least-privilege permissions, consider requiring IAM principals to assign stack policies and limiting which stack policies IAM principals can assign. Many IAM principals should not have permissions to create and assign custom stack policies to their own stacks.

After you create your stack policies, we recommend that you upload them to an S3 bucket. You can then reference these stack policies by using the `cloudformation:StackPolicyUrl` condition key and providing the URL of the stack policy in the S3 bucket.

## Granting permissions to attach stack policies
<a name="granting-permissions-to-attach-stack-policies"></a>

As a best practice for least-privilege permissions, consider limiting which stack policies IAM principals can attach to CloudFormation stacks. In the identity-based policy for the IAM principal, you can specify which stack policies the IAM principal has permissions to assign. This prevents the IAM principal from attaching any stack policy, which can reduce the risk of misconfiguration.

For example, an organization might have different teams with different requirements. Accordingly, each team builds stack policies for their team-specific CloudFormation stacks. In a shared environment, if all teams store their stack policies in the same S3 bucket, a team member might attach a stack policy that is available but not intended for their team's CloudFormation stacks. To avoid this scenario, you can define a policy statement that allows IAM principals to attach only specific stack policies.

The following sample policy allows the IAM principal to attach stack policies that are stored in a team-specific folder in an S3 bucket. You can store approved stack policies in this bucket.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:SetStackPolicy"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "cloudformation:StackPolicyUrl": "<Bucket URL>/<Team folder>/*"
                }
            }
        }
    ]
}
```

This policy statement doesn't require an IAM principal to assign a stack policy to every stack. Even if the IAM principal has permissions to create stacks with a specific stack policy, they could choose to create a stack that doesn't have a stack policy.

## Requiring stack policies
<a name="requiring-stack-policies"></a>

To ensure all IAM principals assign stack policies to their stacks, you can define a service control policy (SCP) or permissions boundary as a preventive guardrail.

The following sample policy shows how you can configure an SCP that requires IAM principals to assign a stack policy when creating a stack. If the IAM principal doesn't attach a stack policy, they can't create the stack. Additionally, this policy prevents IAM principals with stack update permissions from removing the stack policy during an update. the policy restricts the `cloudformation:UpdateStack` action by using the `cloudformation:StackPolicyUrl` condition key.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
   "cloudformation:CreateStack",
   "cloudformation:UpdateStack"
],
      "Resource": "*",
      "Condition": {
        "Null": {
          "cloudformation:StackPolicyUrl": "true"
        }
      }
    }
  ]
}
```

By including this policy statement in an SCP instead of a permissions boundary, you can apply your guardrail to all accounts in the organization. This can do the following:

1. Reduce the effort to attach the policy individually to multiple IAM principals in an AWS account. Permissions boundaries can be directly attached only to an IAM principal.

1. Reduce the effort to create and manage multiple copies of the permissions boundary for different AWS accounts. This reduces the risk of configuration error in multiple identical permissions boundaries.

|
|
| Note: SCPs and permissions boundaries are permissions guardrails that define the maximum available permissions for IAM principals in an account or organization. These policies do not grant permissions to the IAM principals. If you want to standardize the requirement that all IAM principals in your account or organization assign stack policies, you need to use both permission guardrails and the identity-based policies. |
| --- |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
