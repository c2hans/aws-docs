---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dlpsetting-microsoftpurviewcredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DLPSetting MicrosoftPurviewCredentials
<a name="aws-properties-quicksight-dlpsetting-microsoftpurviewcredentials"></a>

<a name="aws-properties-quicksight-dlpsetting-microsoftpurviewcredentials-description"></a>The `MicrosoftPurviewCredentials` property type specifies Property description not available. for an [AWS::QuickSight::DLPSetting](aws-resource-quicksight-dlpsetting.md).

## Syntax
<a name="aws-properties-quicksight-dlpsetting-microsoftpurviewcredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dlpsetting-microsoftpurviewcredentials-syntax.json"></a>

```
{
  "[SecretArn](#cfn-quicksight-dlpsetting-microsoftpurviewcredentials-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dlpsetting-microsoftpurviewcredentials-syntax.yaml"></a>

```
  [SecretArn](#cfn-quicksight-dlpsetting-microsoftpurviewcredentials-secretarn): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dlpsetting-microsoftpurviewcredentials-properties"></a>

`SecretArn`  <a name="cfn-quicksight-dlpsetting-microsoftpurviewcredentials-secretarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[\w]+)*:secretsmanager:[a-z0-9\-]+:\d{12}:secret:.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
