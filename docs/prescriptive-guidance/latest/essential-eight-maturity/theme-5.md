---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/theme-5.html
---

# Theme 5: Establish a data perimeter
<a name="theme-5"></a>

**Essential Eight strategy covered**: Restrict administrative privileges

A *data perimeter* is a set of preventive guardrails in your AWS environment that help make sure that only trusted identities are accessing trusted resources from expected networks. These guardrails serve as always-on boundaries that help protect your data across a broad set of AWS accounts and resources. These organisation-wide guardrails do not replace your existing fine-grained access controls. Instead, they help improve your security strategy by making sure that all AWS Identity and Access Management (IAM) users, roles, and resources adhere to a set of defined security standards.

You can establish a data perimeter by using policies that prevent access from outside of an organisation boundary, typically created in AWS Organizations. The three primary perimeter authorization conditions used to establish a data perimeter are:
+ **Trusted identities** – Principals (IAM roles or users) within your AWS accounts, or AWS services acting on your behalf.
+ **Trusted resources** – Resources that are in your AWS accounts or are managed by AWS services acting on your behalf.
+ **Expected networks – **Your on-premises data centres and virtual private clouds (VPCs), or the networks of AWS services acting on your behalf.

Consider implementing data perimeters between environments of different data classifications, such as `OFFICIAL:SENSITIVE` or `PROTECTED`, or different risk levels, such as development, test, or production. For more information, see [Building a data perimeter on AWS](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) (AWS whitepaper) and [Establishing a data perimeter on AWS: Overview](https://aws.amazon.com/blogs/security/establishing-a-data-perimeter-on-aws/) (AWS blog post).

## Related best practices in the AWS Well-Architected Framework
<a name="theme-5-best-practices"></a>
+ [SEC03-BP05 Define permission guardrails for your organization](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define_guardrails.html)
+ [SEC07-BP02 Define data protection controls based on sensitivity](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_define_protection.html)

## Implementing this theme
<a name="theme-5-implementation"></a>

### Implement identity controls
<a name="implement-identity-controls.9766078b-24e6-5636-bd98-d284c471b1dc"></a>
+ **Allow only trusted identities to access your resources** – Use [resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_resource-based) with the condition keys `aws:PrincipalOrgID` and `aws:PrincipalIsAWSService`. This allows only principals from your AWS organization and from AWS to access your resources.
+ **Allow trusted identities only from your network – **Use [VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) with the condition keys `aws:PrincipalOrgID` and `aws:PrincipalIsAWSService`. This allows only principals from your AWS organization and from AWS to access services through VPC endpoints.

### Implement resource controls
<a name="implement-resource-controls.b20c1109-c360-5b68-9b98-c33ae37ed5fb"></a>
+ **Allow your identities to access only trusted resources – **Use [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) with the condition key `aws:ResourceOrgID`. This allows your identities to access only resources in your AWS organization.
+ **Allow access to trusted resources only from your network** – Use VPC endpoint policies with the condition key `aws:ResourceOrgID`. This allows your identities to access services only through VPC endpoints that are part of your AWS organization.

### Implement network controls
<a name="implement-network-controls.49e7aac9-c3e4-5d82-94ab-837cd6ed5b52"></a>
+ **Allow identities to access resources only from expected networks – **Use SCPs with the condition keys `aws:SourceIp`, `aws:SourceVpc`, `aws:SourceVpce`, and `aws:ViaAWSService`. This allows your identities to access resources only from expected IP addresses, VPCs, and VPC endpoints, and through AWS services.
+ **Allow access to your resources only from expected networks – **Use resource-based policies with the condition keys `aws:SourceIp`, `aws:SourceVpc`, `aws:SourceVpce`, `aws:ViaAWSService`, and `aws:PrincipalIsAWSService`. This allows access to your resources only from expected IPs, from expected VPCs, from expected VPC endpoints, through AWS services, or when the calling identity is an AWS service.

## Monitoring this theme
<a name="theme-5-monitoring"></a>

### Monitor policies
<a name="monitor-policies.f4873b5d-0aca-50c0-901b-50894cc8f208"></a>
+ Implement mechanisms to review SCPs, IAM policies, and VPC endpoint policies

### Implement the following AWS Config rule
<a name="implement-the-following-9999999999999999cc--rule.a1389bfa-9f83-55ab-aa6a-6d69c5a2a21d"></a>
+ `SERVICE_VPC_ENDPOINT_ENABLED`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
