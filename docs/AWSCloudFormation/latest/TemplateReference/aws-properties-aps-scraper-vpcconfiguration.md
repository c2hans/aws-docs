---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-scraper-vpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Scraper VpcConfiguration
<a name="aws-properties-aps-scraper-vpcconfiguration"></a>

<a name="aws-properties-aps-scraper-vpcconfiguration-description"></a>The `VpcConfiguration` property type specifies Property description not available. for an [AWS::APS::Scraper](aws-resource-aps-scraper.md).

## Syntax
<a name="aws-properties-aps-scraper-vpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-scraper-vpcconfiguration-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-aps-scraper-vpcconfiguration-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-aps-scraper-vpcconfiguration-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-aps-scraper-vpcconfiguration-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-aps-scraper-vpcconfiguration-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-aps-scraper-vpcconfiguration-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-aps-scraper-vpcconfiguration-properties"></a>

`SecurityGroupIds`  <a name="cfn-aps-scraper-vpcconfiguration-securitygroupids"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-aps-scraper-vpcconfiguration-subnetids"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
