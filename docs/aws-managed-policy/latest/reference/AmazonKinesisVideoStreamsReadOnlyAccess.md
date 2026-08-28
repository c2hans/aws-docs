---
source_url: https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonKinesisVideoStreamsReadOnlyAccess.html
---

# AmazonKinesisVideoStreamsReadOnlyAccess
<a name="AmazonKinesisVideoStreamsReadOnlyAccess"></a>

**Description**: Provides read only access to AWS Kinesis Video Streams via the AWS Management Console.

`AmazonKinesisVideoStreamsReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonKinesisVideoStreamsReadOnlyAccess-how-to-use"></a>

You can attach `AmazonKinesisVideoStreamsReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonKinesisVideoStreamsReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy
+ **Creation time**: December 01, 2017, 23:14 UTC
+ **Edited time:** December 01, 2017, 23:14 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonKinesisVideoStreamsReadOnlyAccess`

## Policy version
<a name="AmazonKinesisVideoStreamsReadOnlyAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request.

## JSON policy document
<a name="AmazonKinesisVideoStreamsReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "kinesisvideo:Describe*",
        "kinesisvideo:Get*",
        "kinesisvideo:List*"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonKinesisVideoStreamsReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html)
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html)
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Policy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-managed-policy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
