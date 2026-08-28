---
source_url: https://docs.aws.amazon.com/aws-managed-policy/latest/reference/DynamoDBCloudWatchContributorInsightsServiceRolePolicy.html
---

# DynamoDBCloudWatchContributorInsightsServiceRolePolicy
<a name="DynamoDBCloudWatchContributorInsightsServiceRolePolicy"></a>

**Description**: Permissions required to support Amazon CloudWatch Contributor Insights for Amazon DynamoDB.

`DynamoDBCloudWatchContributorInsightsServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="DynamoDBCloudWatchContributorInsightsServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="DynamoDBCloudWatchContributorInsightsServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy
+ **Creation time**: November 15, 2019, 21:13 UTC
+ **Edited time:** November 15, 2019, 21:13 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/DynamoDBCloudWatchContributorInsightsServiceRolePolicy`

## Policy version
<a name="DynamoDBCloudWatchContributorInsightsServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request.

## JSON policy document
<a name="DynamoDBCloudWatchContributorInsightsServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "cloudwatch:DeleteInsightRules",
        "cloudwatch:PutInsightRule"
      ],
      "Effect" : "Allow",
      "Resource" : "arn:aws:cloudwatch:*:*:insight-rule/DynamoDBContributorInsights*"
    },
    {
      "Action" : [
        "cloudwatch:DescribeInsightRules"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="DynamoDBCloudWatchContributorInsightsServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Policy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-managed-policy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
