---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-directoryservice-microsoftad-vpcsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DirectoryService::MicrosoftAD VpcSettings
<a name="aws-properties-directoryservice-microsoftad-vpcsettings"></a>

Contains VPC information for the [CreateDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html) or [CreateMicrosoftAD](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateMicrosoftAD.html) operation.

## Syntax
<a name="aws-properties-directoryservice-microsoftad-vpcsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-directoryservice-microsoftad-vpcsettings-syntax.json"></a>

```
{
  "[SubnetIds](#cfn-directoryservice-microsoftad-vpcsettings-subnetids)" : {{[ String, ... ]}},
  "[VpcId](#cfn-directoryservice-microsoftad-vpcsettings-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-directoryservice-microsoftad-vpcsettings-syntax.yaml"></a>

```
  [SubnetIds](#cfn-directoryservice-microsoftad-vpcsettings-subnetids): {{
    - String}}
  [VpcId](#cfn-directoryservice-microsoftad-vpcsettings-vpcid): {{String}}
```

## Properties
<a name="aws-properties-directoryservice-microsoftad-vpcsettings-properties"></a>

`SubnetIds`  <a name="cfn-directoryservice-microsoftad-vpcsettings-subnetids"></a>
The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. Directory Service specifies a directory server and a DNS server in each of these subnets.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-directoryservice-microsoftad-vpcsettings-vpcid"></a>
The identifier of the VPC in which to create the directory.
*Required*: Yes
*Type*: String
*Pattern*: `^(vpc-[0-9a-f]{8}|vpc-[0-9a-f]{17})$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
