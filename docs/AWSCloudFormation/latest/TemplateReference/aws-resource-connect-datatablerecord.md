---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-datatablerecord.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::DataTableRecord
<a name="aws-resource-connect-datatablerecord"></a>

<a name="aws-resource-connect-datatablerecord-description"></a>The `AWS::Connect::DataTableRecord` resource Property description not available. for Connect.

## Syntax
<a name="aws-resource-connect-datatablerecord-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-datatablerecord-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::DataTableRecord",
  "Properties" : {
      "[DataTableArn](#cfn-connect-datatablerecord-datatablearn)" : {{String}},
      "[DataTableRecord](#cfn-connect-datatablerecord-datatablerecord)" : {{DataTableRecord}},
      "[InstanceArn](#cfn-connect-datatablerecord-instancearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-datatablerecord-syntax.yaml"></a>

```
Type: AWS::Connect::DataTableRecord
Properties:
  [DataTableArn](#cfn-connect-datatablerecord-datatablearn): {{String}}
  [DataTableRecord](#cfn-connect-datatablerecord-datatablerecord): {{
    DataTableRecord}}
  [InstanceArn](#cfn-connect-datatablerecord-instancearn): {{String}}
```

## Properties
<a name="aws-resource-connect-datatablerecord-properties"></a>

`DataTableArn`  <a name="cfn-connect-datatablerecord-datatablearn"></a>
The Amazon Resource Name (ARN) for the data table. Does not include version aliases.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataTableRecord`  <a name="cfn-connect-datatablerecord-datatablerecord"></a>
Property description not available.
*Required*: Yes
*Type*: [DataTableRecord](aws-properties-connect-datatablerecord-datatablerecord.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-datatablerecord-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-connect-datatablerecord-return-values"></a>

### Ref
<a name="aws-resource-connect-datatablerecord-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-connect-datatablerecord-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-datatablerecord-return-values-fn--getatt-fn--getatt"></a>

`RecordId`  <a name="RecordId-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
