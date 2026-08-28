---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-02.html
---

# WKLD.02 Restrict credential usage scope with resource-based policies
<a name="wkld-02"></a>

*Policies* define permissions or specify access conditions for AWS resources. There are two primary types of policies:
+ *Identity-based policies* are attached to principals and define what the principal's permissions are in the AWS environment.
+ *Resource-based policies* are attached to a resource, such as an Amazon Simple Storage Service (Amazon S3) bucket, or virtual private cloud (VPC) endpoint. These policies specify which principals are allowed access, supported actions, and any other conditions that must be met.

For a principal to access a resource, the principal must have permission in its identity-based policy and meet the conditions of the resource-based policy. For more information, see [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) in the IAM documentation.

The following conditions help restrict access to trusted sources and reduce the risk of unintended access:
+ Restrict access to principals in a specified organization (defined in AWS Organizations) by using the `aws:PrincipalOrgID` condition.
+ Restrict access to traffic that originates from a specific VPC or VPC endpoint by using the `aws:SourceVpc` or `aws:SourceVpce` condition, respectively.
+ Allow or deny traffic based on the source IP address by using an `aws:SourceIp` condition.

The following example shows a resource-based policy that uses the `aws:PrincipalOrgID` condition to allow only principals in your organization to access an Amazon S3 bucket.

Replace `o-xxxxxxxxxxx` with your organization ID and `bucket-name` with your bucket name:

```
{
    "Version": "2012-10-17",
    "Statement":[
      {
        "Sid":"AllowFromOrganization",
        "Effect":"Allow",
        "Principal":"*",
        "Action":"s3:*",
        "Resource":"arn:aws:s3:::bucket-name/*",
        "Condition": {
          "StringEquals": {"aws:PrincipalOrgID":"<o-xxxxxxxxxxx>"}
        }
      }
    ]
 }
```

Note: This example uses `s3:*` for illustration purposes. In practice, replace `s3:*` with only the specific actions your workload requires, such as `s3:GetObject` and `s3:PutObject`. Granting the minimum set of actions follows the principle of least privilege.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
