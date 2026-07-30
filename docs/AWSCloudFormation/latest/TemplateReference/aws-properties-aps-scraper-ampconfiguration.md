---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-scraper-ampconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Scraper AmpConfiguration
<a name="aws-properties-aps-scraper-ampconfiguration"></a>

The `AmpConfiguration` structure defines the Amazon Managed Service for Prometheus instance a scraper should send metrics to.

## Syntax
<a name="aws-properties-aps-scraper-ampconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-scraper-ampconfiguration-syntax.json"></a>

```
{
  "[WorkspaceArn](#cfn-aps-scraper-ampconfiguration-workspacearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-aps-scraper-ampconfiguration-syntax.yaml"></a>

```
  [WorkspaceArn](#cfn-aps-scraper-ampconfiguration-workspacearn): {{String}}
```

## Properties
<a name="aws-properties-aps-scraper-ampconfiguration-properties"></a>

`WorkspaceArn`  <a name="cfn-aps-scraper-ampconfiguration-workspacearn"></a>
ARN of the Amazon Managed Service for Prometheus workspace.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z]*:aps:[-a-z0-9]+:[0-9]{12}:workspace/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
