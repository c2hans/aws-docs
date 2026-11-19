---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-02.html
---

# WKLD.02 Restrict credential usage scope with resource-based policies

*Policies* define permissions or specify access conditions for AWS resources. There are two primary types of policies:
+ *Identity-based policies* are attached to principals and define what the principal's permissions are in the AWS environment.
+ *Resource-based policies* are attached to a resource, such as an Amazon Simple Storage Service (Amazon S3) bucket, or virtual private cloud (VPC) endpoint. These policies specify which principals are allowed access, supported actions, and any other conditions that must be met.

Identity-based and resource-based policies are evaluated together. An explicit Deny in either policy type overrides any Allow. Within a single account, an Allow in either an identity-based or a resource-based policy is enough. For cross-account requests, the requester's identity-based policy and the resource's resource-based policy must both allow the operation. For more information, see [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) in the IAM documentation.

The following conditions help restrict access to trusted sources and reduce the risk of unintended access:
+ Restrict access to principals in a specified organization (defined in AWS Organizations) by using the `aws:PrincipalOrgID` condition.
+ Restrict access to traffic that originates from a specific VPC or VPC endpoint by using the `aws:SourceVpc` or `aws:SourceVpce` condition, respectively.
+ Allow or deny traffic based on the source IP address by using an `aws:SourceIp` condition.

The following example shows a resource-based policy that uses the `aws:PrincipalOrgID` condition to deny access to an Amazon S3 bucket from principals outside your organization. The policy exempts AWS service principals.

Replace `o-xxxxxxxxxxx` with your organization ID and `bucket-name` with your bucket name:

```
{
    "Version": "2012-10-17",
    "Statement":[
      {
        "Sid":"DenyOutsideOrganization",
        "Effect":"Deny",
        "Principal":"*",
        "Action":"s3:*",
        "Resource": [
          "arn:aws:s3:::bucket-name",
          "arn:aws:s3:::bucket-name/*"
        ],
        "Condition": {
          "StringNotEqualsIfExists": {
            "aws:PrincipalOrgID":"o-xxxxxxxxxxx"
          },
          "BoolIfExists": {
            "aws:PrincipalIsAWSService":"false"
          }
        }
      }
    ]
 }
```

Note: A Deny doesn't grant any access. Pair this policy with an `Allow` statement that names only the actions your workload requires, such as `s3:GetObject` and `s3:PutObject`. Granting the minimum set of actions follows the principle of least privilege.

A Deny can block legitimate access that you didn't know about, such as third-party partner accounts. You can use AWS Identity and Access Management Access Analyzer to review external access findings and see which external entities your bucket policies currently allow. Then test the policy in a non-production environment.
