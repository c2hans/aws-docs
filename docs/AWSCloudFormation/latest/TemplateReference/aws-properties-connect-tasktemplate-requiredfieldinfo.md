---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-tasktemplate-requiredfieldinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::TaskTemplate RequiredFieldInfo
<a name="aws-properties-connect-tasktemplate-requiredfieldinfo"></a>

Information about a required field.

## Syntax
<a name="aws-properties-connect-tasktemplate-requiredfieldinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-tasktemplate-requiredfieldinfo-syntax.json"></a>

```
{
  "[Id](#cfn-connect-tasktemplate-requiredfieldinfo-id)" : {{FieldIdentifier}}
}
```

### YAML
<a name="aws-properties-connect-tasktemplate-requiredfieldinfo-syntax.yaml"></a>

```
  [Id](#cfn-connect-tasktemplate-requiredfieldinfo-id): {{
    FieldIdentifier}}
```

## Properties
<a name="aws-properties-connect-tasktemplate-requiredfieldinfo-properties"></a>

`Id`  <a name="cfn-connect-tasktemplate-requiredfieldinfo-id"></a>
The unique identifier for the field.
*Required*: Yes
*Type*: [FieldIdentifier](aws-properties-connect-tasktemplate-fieldidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
