---
source_url: https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonAPIGatewayPushToCloudWatchLogs.html
---

# AmazonAPIGatewayPushToCloudWatchLogs
<a name="AmazonAPIGatewayPushToCloudWatchLogs"></a>

**Description**: Allows API Gateway to push logs to user's account.

`AmazonAPIGatewayPushToCloudWatchLogs` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonAPIGatewayPushToCloudWatchLogs-how-to-use"></a>

You can attach `AmazonAPIGatewayPushToCloudWatchLogs` to your users, groups, and roles.

## Policy details
<a name="AmazonAPIGatewayPushToCloudWatchLogs-details"></a>
+ **Type**: Service role policy
+ **Creation time**: November 11, 2015, 23:41 UTC
+ **Edited time:** November 11, 2015, 23:41 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs`

## Policy version
<a name="AmazonAPIGatewayPushToCloudWatchLogs-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request.

## JSON policy document
<a name="AmazonAPIGatewayPushToCloudWatchLogs-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams",
        "logs:PutLogEvents",
        "logs:GetLogEvents",
        "logs:FilterLogEvents"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonAPIGatewayPushToCloudWatchLogs-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html)
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html)
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Policy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-managed-policy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
