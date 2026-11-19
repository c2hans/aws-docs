---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/theme-5.html
---

# Theme 5: Establish a data perimeter

**Essential Eight strategy covered**: Restrict administrative privileges

A *data perimeter* is a set of preventive guardrails in your AWS environment that help ensure that only trusted identities access trusted resources from expected networks. These guardrails serve as persistent boundaries that help protect your data across a broad set of AWS accounts and resources. These organization-wide guardrails don't replace your existing fine-grained access controls. Instead, they help improve your security strategy by helping to enforce a set of defined security standards for [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) (IAM) users, roles, and resources.

You can establish a data perimeter by using policies that prevent access from outside an organization boundary, which you typically create in [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html). The three primary perimeter authorization conditions that you use to establish a data perimeter are:
+ **Trusted identities** – Principals (IAM roles or users) within your AWS accounts, or AWS services acting on your behalf.
+ **Trusted resources** – Resources that are in your AWS accounts or are managed by AWS services acting on your behalf.
+ **Expected networks – **Your on-premises data centers and virtual private clouds (VPCs), or the networks of AWS services acting on your behalf.

Consider implementing data perimeters between environments of different data classifications, such as `OFFICIAL:SENSITIVE` or `PROTECTED`, or different risk levels, such as development, test, or production. For more information, see [Building a data perimeter on AWS](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) (AWS whitepaper) and [Establishing a data perimeter on AWS: Overview](https://aws.amazon.com/blogs/security/establishing-a-data-perimeter-on-aws/) (AWS blog post).

## Related best practices in the AWS Well-Architected Framework
<a name="theme-5-best-practices"></a>
+ [SEC03-BP05 Define permission guardrails for your organization](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define_guardrails.html)
+ [SEC07-BP02 Apply data protection controls based on data sensitivity](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_define_protection.html)

## Implementing this theme
<a name="theme-5-implementation"></a>

### Implement identity controls
<a name="implement-identity-controls.572d8d4c-6de9-5487-94b5-d483da10ae18"></a>
+ **Allow only trusted identities to access your resources** – Use [resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_resource-based) with the condition keys `aws:PrincipalOrgID` and `aws:PrincipalIsAWSService`. This allows only principals from your AWS organization and from AWS to access your resources.
+ **Allow trusted identities only from your network – **Use [virtual private cloud (VPC) endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) with the condition keys `aws:PrincipalOrgID` and `aws:PrincipalIsAWSService`. This allows only principals from your AWS organization and from AWS to access services through VPC endpoints.

### Implement resource controls
<a name="implement-resource-controls.b20c1109-c360-5b68-9b98-c33ae37ed5fb"></a>
+ **Allow your identities to access only trusted resources – **Use [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) with the condition key `aws:ResourceOrgID`. This allows your identities to access only resources in your AWS organization.
+ **Allow access to trusted resources only from your network** – Use VPC endpoint policies with the condition key `aws:ResourceOrgID`. This allows your identities to access services only through VPC endpoints that are part of your AWS organization.

### Implement network controls
<a name="implement-network-controls.a42d0693-2061-5134-a37a-fe1a6afd0655"></a>
+ **Allow identities to access resources only from expected networks – **Use SCPs with the condition keys `aws:SourceIp`, `aws:SourceVpc`, `aws:SourceVpce`, and `aws:ViaAWSService`. This allows your identities to access resources only from expected IP addresses, VPCs, and VPC endpoints, and through AWS services.
+ **Allow access to your resources only from expected networks – **Use resource-based policies with the condition keys `aws:SourceIp`, `aws:SourceVpc`, `aws:SourceVpce`, `aws:ViaAWSService`, and `aws:PrincipalIsAWSService`. This allows access to your resources only from expected IP addresses, from expected VPCs, from expected VPC endpoints, through AWS services, or when the calling identity is an AWS service.

## Monitoring this theme
<a name="theme-5-monitoring"></a>

### Monitor policies
<a name="monitor-policies.5b833a81-637f-503a-ac8a-f9ba96acc454"></a>
+ Implement mechanisms to review service control policies (SCPs), IAM policies, and Amazon VPC endpoint policies.

### Implement the following AWS Config rule
<a name="implement-the-following-9999999999999999cc--rule.a1389bfa-9f83-55ab-aa6a-6d69c5a2a21d"></a>
+ `SERVICE_VPC_ENDPOINT_ENABLED`
