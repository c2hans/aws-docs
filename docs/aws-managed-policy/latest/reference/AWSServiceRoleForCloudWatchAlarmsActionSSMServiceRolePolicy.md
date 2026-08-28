---
source_url: https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSServiceRoleForCloudWatchAlarmsActionSSMServiceRolePolicy.html
---

# AWSServiceRoleForCloudWatchAlarmsActionSSMServiceRolePolicy
<a name="AWSServiceRoleForCloudWatchAlarmsActionSSMServiceRolePolicy"></a>

**Description**: Provides access to Systems Manager resources used by CloudWatch Alarms

`AWSServiceRoleForCloudWatchAlarmsActionSSMServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSServiceRoleForCloudWatchAlarmsActionSSMServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSServiceRoleForCloudWatchAlarmsActionSSMServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy
+ **Creation time**: October 01, 2020, 09:49 UTC
+ **Edited time:** October 01, 2020, 09:49 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSServiceRoleForCloudWatchAlarmsActionSSMServiceRolePolicy`

## Policy version
<a name="AWSServiceRoleForCloudWatchAlarmsActionSSMServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request.

## JSON policy document
<a name="AWSServiceRoleForCloudWatchAlarmsActionSSMServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "ssm:CreateOpsItem"
      ],
      "Resource" : "*",
      "Effect" : "Allow"
    }
  ]
}
```

## Learn more
<a name="AWSServiceRoleForCloudWatchAlarmsActionSSMServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Policy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-managed-policy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
