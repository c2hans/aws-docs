---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-tasktemplate-contacthooks.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::TaskTemplate ContactHooks

<a name="aws-properties-connect-tasktemplate-contacthooks-description"></a>The `ContactHooks` property type specifies Property description not available. for an [AWS::Connect::TaskTemplate](aws-resource-connect-tasktemplate.md).

## Syntax
<a name="aws-properties-connect-tasktemplate-contacthooks-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-tasktemplate-contacthooks-syntax.json"></a>

```json
{
  "[WrapUpFlowArn](#cfn-connect-tasktemplate-contacthooks-wrapupflowarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-tasktemplate-contacthooks-syntax.yaml"></a>

```yaml
  [WrapUpFlowArn](#cfn-connect-tasktemplate-contacthooks-wrapupflowarn): {{String}}
```

## Properties
<a name="aws-properties-connect-tasktemplate-contacthooks-properties"></a>

`WrapUpFlowArn`  <a name="cfn-connect-tasktemplate-contacthooks-wrapupflowarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/flow-module/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
