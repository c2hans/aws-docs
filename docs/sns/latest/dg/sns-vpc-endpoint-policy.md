---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-vpc-endpoint-policy.html
---

# Creating an Amazon VPC endpoint policy for Amazon SNS
<a name="sns-vpc-endpoint-policy"></a>

You can create a policy for Amazon VPC endpoints for Amazon SNS in which you specify the following:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling Access to Services with VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

The following example VPC endpoint policy specifies that the IAM user `MyUser` is allowed to publish to the Amazon SNS topic `MyTopic`.

```
{
  "Statement": [{
    "Action": ["sns:Publish"],
    "Effect": "Allow",
    "Resource": "arn:aws:sns:us-east-2:123456789012:MyTopic",
    "Principal": {
      "AWS": "arn:aws:iam:123456789012:user/MyUser"
    }
  }]
}
```

The following are denied:
+ Other Amazon SNS API actions, such as `sns:Subscribe` and `sns:Unsubscribe`.
+ Other IAM users and rules which attempt to use this VPC endpoint.
+ `MyUser` publishing to a different Amazon SNS topic.

**Note**
The IAM user can still use other Amazon SNS API actions from *outside* the VPC.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
