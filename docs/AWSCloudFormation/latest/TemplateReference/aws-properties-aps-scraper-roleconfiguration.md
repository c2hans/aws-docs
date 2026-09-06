---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-scraper-roleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Scraper RoleConfiguration
<a name="aws-properties-aps-scraper-roleconfiguration"></a>

The role configuration in an Amazon Managed Service for Prometheus scraper.

## Syntax
<a name="aws-properties-aps-scraper-roleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-scraper-roleconfiguration-syntax.json"></a>

```
{
  "[SourceRoleArn](#cfn-aps-scraper-roleconfiguration-sourcerolearn)" : {{String}},
  "[TargetRoleArn](#cfn-aps-scraper-roleconfiguration-targetrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-aps-scraper-roleconfiguration-syntax.yaml"></a>

```
  [SourceRoleArn](#cfn-aps-scraper-roleconfiguration-sourcerolearn): {{String}}
  [TargetRoleArn](#cfn-aps-scraper-roleconfiguration-targetrolearn): {{String}}
```

## Properties
<a name="aws-properties-aps-scraper-roleconfiguration-properties"></a>

`SourceRoleArn`  <a name="cfn-aps-scraper-roleconfiguration-sourcerolearn"></a>
The ARN of the source role.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetRoleArn`  <a name="cfn-aps-scraper-roleconfiguration-targetrolearn"></a>
The ARN of the target role.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
