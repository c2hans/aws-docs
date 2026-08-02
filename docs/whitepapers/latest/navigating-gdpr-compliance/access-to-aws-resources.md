---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/access-to-aws-resources.html
---

# Access to AWS Resources
<a name="access-to-aws-resources"></a>

To implement granular access to your AWS resources, customers can grant different levels of permissions to different people for different resources. For example, customers can allow only some users complete access to [Amazon EC2](https://aws.amazon.com/ec2/), [Amazon S3](https://aws.amazon.com/s3/), [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), [Amazon Redshift](https://aws.amazon.com/redshift/), and other AWS Services.

For other users, you can allow read-only access to only some Amazon S3 buckets; permission to administer only some Amazon EC2 instances, or access to only your billing information.

The following policy is an example of one method you can use to allow all actions on a specific Amazon S3 bucket and explicitly deny access to every AWS service that is not Amazon S3.

```
{
“Version”: “2012-10-17”,
“Statement”: [
{
“Effect”: “Allow”,
“Action”: “s3:*”,
“Resource”: [
“arn:aws:s3:::bucket-name”,
“arn:aws:s3:::bucket-name/*”
],
},
{
“Effect”: “Deny”,
“NotAction”: “s3:*”,
“NotResource”: [
“arn:aws:s3:::bucket-name”,
“arn:aws:s3:::bucket-name/*”
]
}
]
}
```

You can attach a policy to a user or to a role. For other examples of IAM policies, see [Example IAM Identity-Based Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html).
