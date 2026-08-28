---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-odbnetwork-stsaccess.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::OdbNetwork StsAccess
<a name="aws-properties-odb-odbnetwork-stsaccess"></a>

Configuration for AWS Security Token Service (STS) access from the ODB network.

## Syntax
<a name="aws-properties-odb-odbnetwork-stsaccess-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-odbnetwork-stsaccess-syntax.json"></a>

```
{
  "[DomainName](#cfn-odb-odbnetwork-stsaccess-domainname)" : {{String}},
  "[Ipv4Addresses](#cfn-odb-odbnetwork-stsaccess-ipv4addresses)" : {{[ String, ... ]}},
  "[Status](#cfn-odb-odbnetwork-stsaccess-status)" : {{String}},
  "[StsPolicyDocument](#cfn-odb-odbnetwork-stsaccess-stspolicydocument)" : {{String}}
}
```

### YAML
<a name="aws-properties-odb-odbnetwork-stsaccess-syntax.yaml"></a>

```
  [DomainName](#cfn-odb-odbnetwork-stsaccess-domainname): {{String}}
  [Ipv4Addresses](#cfn-odb-odbnetwork-stsaccess-ipv4addresses): {{
    - String}}
  [Status](#cfn-odb-odbnetwork-stsaccess-status): {{String}}
  [StsPolicyDocument](#cfn-odb-odbnetwork-stsaccess-stspolicydocument): {{String}}
```

## Properties
<a name="aws-properties-odb-odbnetwork-stsaccess-properties"></a>

`DomainName`  <a name="cfn-odb-odbnetwork-stsaccess-domainname"></a>
The domain name for AWS Security Token Service (STS) access configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv4Addresses`  <a name="cfn-odb-odbnetwork-stsaccess-ipv4addresses"></a>
The IPv4 addresses allowed for AWS Security Token Service (STS) access.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-odb-odbnetwork-stsaccess-status"></a>
The current status of the AWS Security Token Service (STS) access configuration.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | ENABLING | DISABLED | DISABLING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StsPolicyDocument`  <a name="cfn-odb-odbnetwork-stsaccess-stspolicydocument"></a>
The AWS Security Token Service (STS) policy document that defines permissions for token service usage.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
