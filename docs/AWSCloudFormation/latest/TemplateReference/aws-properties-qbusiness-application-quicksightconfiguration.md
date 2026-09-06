---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-application-quicksightconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Application QuickSightConfiguration
<a name="aws-properties-qbusiness-application-quicksightconfiguration"></a>

The Amazon Quick configuration for an Amazon Q Business application that uses Quick as the identity provider. For more information, see [Creating an Amazon Quick integrated application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-quicksight-integrated-application.html).

## Syntax
<a name="aws-properties-qbusiness-application-quicksightconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-application-quicksightconfiguration-syntax.json"></a>

```
{
  "[ClientNamespace](#cfn-qbusiness-application-quicksightconfiguration-clientnamespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-application-quicksightconfiguration-syntax.yaml"></a>

```
  [ClientNamespace](#cfn-qbusiness-application-quicksightconfiguration-clientnamespace): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-application-quicksightconfiguration-properties"></a>

`ClientNamespace`  <a name="cfn-qbusiness-application-quicksightconfiguration-clientnamespace"></a>
The Amazon Quick namespace that is used as the identity provider. For more information about Quick namespaces, see [Namespace operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/namespace-operations.html).
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
