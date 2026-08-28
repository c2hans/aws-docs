---
source_url: https://docs.aws.amazon.com/billingconductor/latest/userguide/security_iam_resource-based-policy-examples.html
---

# AWS Billing Conductor resource-based policy examples
<a name="security_iam_resource-based-policy-examples"></a>

**Topics**
+ [Restricting Amazon S3 bucket access to specific IP addresses](#security_iam_resource-based-policy-examples-restrict-bucket-by-ip)

## Restricting Amazon S3 bucket access to specific IP addresses
<a name="security_iam_resource-based-policy-examples-restrict-bucket-by-ip"></a>

The following example grants permissions to any user to perform any Amazon S3 operations on objects in the specified bucket. However, the request must originate from the range of IP addresses specified in the condition.

The condition in this statement identifies the 54.240.143.\* range of allowed Internet Protocol version 4 (IPv4) IP addresses, with one exception: 54.240.143.188.

The `Condition` block uses the `IpAddress` and `NotIpAddress` conditions and the `aws:SourceIp` condition key, which is an AWS wide condition key. For more information about these condition keys, see [Specifying Conditions in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html). The`aws:sourceIp` IPv4 values use the standard CIDR notation. For more information, see [IP Address Condition Operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_IPAddress) in the *IAM User Guide*.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Id": "S3PolicyId1",
  "Statement": [
    {
      "Sid": "IPAllow",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::amzn-s3-demo-bucket1/*",
      "Condition": {
         "IpAddress": {"aws:SourceIp": "54.240.143.0/24"},
         "NotIpAddress": {"aws:SourceIp": "54.240.143.188/32"}
      }
    }
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
