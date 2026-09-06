---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/multi-factor-authentication.html
---

# Multi-Factor-Authentication
<a name="multi-factor-authentication"></a>

For extra security, customers can add two-factor authentication to their AWS account and to IAM users. With multi-factor authentication (MFA) enabled, when customers sign into the [AWS Management Console](https://aws.amazon.com/console/), they are prompted for their credentials (the first factor), as well as an authentication response from their AWS MFA device (the second factor). Customers can enable MFA for their AWS account and for individual IAM users they have created in their account. Customers can also use MFA to control access to AWS service APIs.

For example, customers can define a policy that allows full access to all AWS API operations in [Amazon EC2](https://aws.amazon.com/ec2/), but explicitly denies access to specific API operations – such as StopInstances and TerminateInstances – if the user is not authenticated with MFA.

```
{
“Version”: “2012-10-17”,
“Statement”: [
{
“Sid”: “AllowAllActionsForEC2”,
“Effect”: “Allow”,
“Action”: “ec2:*”,
“Resource”: “*”
},
{
“Sid”: “DenyStopAndTerminateWhenMFAIsNotPResent”,
“Effect”: “Deny”,
“Action”: [
“ec2:StopInstances”,
“ec2:TerminateInstances”
],
“Resource”: “*”,
“Conditions”: {
“BoolIfExists”: {“aws:MultiFactorAuthPresent”:false}
}
}
}
}
```

To add an extra layer of security to Amazon S3 buckets, customers can configure [MFA Delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html), which requires additional authentication to change the versioning state of a bucket and permanently delete an object version. MFA Delete provides added security in the event that your security credentials are compromised.

To use [MFA Delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html), customers can use either a hardware or virtual MFA device to generate an authentication code. See the [Multi-Factor Authentication page](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) for a list of supported hardware or virtual MFA devices.
