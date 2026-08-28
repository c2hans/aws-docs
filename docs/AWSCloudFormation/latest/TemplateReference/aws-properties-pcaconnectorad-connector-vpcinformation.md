---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcaconnectorad-connector-vpcinformation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCAConnectorAD::Connector VpcInformation
<a name="aws-properties-pcaconnectorad-connector-vpcinformation"></a>

Information about your VPC and security groups used with the connector.

## Syntax
<a name="aws-properties-pcaconnectorad-connector-vpcinformation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcaconnectorad-connector-vpcinformation-syntax.json"></a>

```
{
  "[IpAddressType](#cfn-pcaconnectorad-connector-vpcinformation-ipaddresstype)" : {{String}},
  "[SecurityGroupIds](#cfn-pcaconnectorad-connector-vpcinformation-securitygroupids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-pcaconnectorad-connector-vpcinformation-syntax.yaml"></a>

```
  [IpAddressType](#cfn-pcaconnectorad-connector-vpcinformation-ipaddresstype): {{String}}
  [SecurityGroupIds](#cfn-pcaconnectorad-connector-vpcinformation-securitygroupids): {{
    - String}}
```

## Properties
<a name="aws-properties-pcaconnectorad-connector-vpcinformation-properties"></a>

`IpAddressType`  <a name="cfn-pcaconnectorad-connector-vpcinformation-ipaddresstype"></a>
The VPC IP address type.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | DUALSTACK`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIds`  <a name="cfn-pcaconnectorad-connector-vpcinformation-securitygroupids"></a>
The security groups used with the connector. You can use a maximum of 4 security groups with a connector.
*Required*: Yes
*Type*: Array of String
*Minimum*: `11 | 1`
*Maximum*: `20 | 5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
