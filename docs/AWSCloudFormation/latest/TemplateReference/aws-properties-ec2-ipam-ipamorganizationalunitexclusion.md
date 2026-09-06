---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ipam-ipamorganizationalunitexclusion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::IPAM IpamOrganizationalUnitExclusion
<a name="aws-properties-ec2-ipam-ipamorganizationalunitexclusion"></a>

If your IPAM is integrated with AWS Organizations, you can exclude an [organizational unit (OU)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#organizationalunit) from being managed by IPAM. When you exclude an OU, IPAM will not manage the IP addresses in accounts in that OU. For more information, see [Exclude organizational units from IPAM ](https://docs.aws.amazon.com/vpc/latest/ipam/exclude-ous.html) in the *Amazon Virtual Private Cloud IP Address Manager User Guide*.

## Syntax
<a name="aws-properties-ec2-ipam-ipamorganizationalunitexclusion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ipam-ipamorganizationalunitexclusion-syntax.json"></a>

```
{
  "[OrganizationsEntityPath](#cfn-ec2-ipam-ipamorganizationalunitexclusion-organizationsentitypath)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-ipam-ipamorganizationalunitexclusion-syntax.yaml"></a>

```
  [OrganizationsEntityPath](#cfn-ec2-ipam-ipamorganizationalunitexclusion-organizationsentitypath): {{String}}
```

## Properties
<a name="aws-properties-ec2-ipam-ipamorganizationalunitexclusion-properties"></a>

`OrganizationsEntityPath`  <a name="cfn-ec2-ipam-ipamorganizationalunitexclusion-organizationsentitypath"></a>
An AWS Organizations entity path. For more information on the entity path, see [Understand the AWS Organizations entity path](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html#access_policies_access-advisor-viewing-orgs-entity-path) in the *AWS Identity and Access Management User Guide*.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
