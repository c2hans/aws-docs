---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ipamresourcediscovery-ipamresourcediscoveryorganizationalunitexclusion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::IPAMResourceDiscovery IpamResourceDiscoveryOrganizationalUnitExclusion
<a name="aws-properties-ec2-ipamresourcediscovery-ipamresourcediscoveryorganizationalunitexclusion"></a>

If your IPAM is integrated with AWS Organizations, you can exclude an [organizational unit (OU)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#organizationalunit) from being managed by IPAM. When you exclude an OU, IPAM will not manage the IP addresses in accounts in that OU. For more information, see [Exclude organizational units from IPAM ](https://docs.aws.amazon.com/vpc/latest/ipam/exclude-ous.html) in the *Amazon Virtual Private Cloud IP Address Manager User Guide*.

## Syntax
<a name="aws-properties-ec2-ipamresourcediscovery-ipamresourcediscoveryorganizationalunitexclusion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ipamresourcediscovery-ipamresourcediscoveryorganizationalunitexclusion-syntax.json"></a>

```
{
  "[OrganizationsEntityPath](#cfn-ec2-ipamresourcediscovery-ipamresourcediscoveryorganizationalunitexclusion-organizationsentitypath)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-ipamresourcediscovery-ipamresourcediscoveryorganizationalunitexclusion-syntax.yaml"></a>

```
  [OrganizationsEntityPath](#cfn-ec2-ipamresourcediscovery-ipamresourcediscoveryorganizationalunitexclusion-organizationsentitypath): {{String}}
```

## Properties
<a name="aws-properties-ec2-ipamresourcediscovery-ipamresourcediscoveryorganizationalunitexclusion-properties"></a>

`OrganizationsEntityPath`  <a name="cfn-ec2-ipamresourcediscovery-ipamresourcediscoveryorganizationalunitexclusion-organizationsentitypath"></a>
An AWS Organizations entity path. For more information on the entity path, see [Understand the AWS Organizations entity path](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html#access_policies_access-advisor-viewing-orgs-entity-path) in the *AWS Identity and Access Management User Guide*.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
