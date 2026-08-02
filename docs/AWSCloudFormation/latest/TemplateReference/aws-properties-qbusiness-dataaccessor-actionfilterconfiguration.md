---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-dataaccessor-actionfilterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataAccessor ActionFilterConfiguration
<a name="aws-properties-qbusiness-dataaccessor-actionfilterconfiguration"></a>

Specifies filters to apply to an allowed action.

## Syntax
<a name="aws-properties-qbusiness-dataaccessor-actionfilterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-dataaccessor-actionfilterconfiguration-syntax.json"></a>

```
{
  "[DocumentAttributeFilter](#cfn-qbusiness-dataaccessor-actionfilterconfiguration-documentattributefilter)" : {{AttributeFilter}}
}
```

### YAML
<a name="aws-properties-qbusiness-dataaccessor-actionfilterconfiguration-syntax.yaml"></a>

```
  [DocumentAttributeFilter](#cfn-qbusiness-dataaccessor-actionfilterconfiguration-documentattributefilter): {{
    AttributeFilter}}
```

## Properties
<a name="aws-properties-qbusiness-dataaccessor-actionfilterconfiguration-properties"></a>

`DocumentAttributeFilter`  <a name="cfn-qbusiness-dataaccessor-actionfilterconfiguration-documentattributefilter"></a>
Enables filtering of responses based on document attributes or metadata fields.
*Required*: Yes
*Type*: [AttributeFilter](aws-properties-qbusiness-dataaccessor-attributefilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
