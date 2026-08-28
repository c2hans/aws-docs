---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-macro.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::Macro
<a name="aws-resource-cloudformation-macro"></a>

The `AWS::CloudFormation::Macro` resource is a CloudFormation resource type that creates a CloudFormation macro to perform custom processing on CloudFormation templates.

For more information, see [Perform custom processing on CloudFormation templates with template macros](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html) in the *CloudFormation User Guide*.

## Syntax
<a name="aws-resource-cloudformation-macro-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-macro-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::Macro",
  "Properties" : {
      "[Description](#cfn-cloudformation-macro-description)" : {{String}},
      "[FunctionName](#cfn-cloudformation-macro-functionname)" : {{String}},
      "[LogGroupName](#cfn-cloudformation-macro-loggroupname)" : {{String}},
      "[LogRoleARN](#cfn-cloudformation-macro-logrolearn)" : {{String}},
      "[Name](#cfn-cloudformation-macro-name)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-macro-syntax.yaml"></a>

```
Type: AWS::CloudFormation::Macro
Properties:
  [Description](#cfn-cloudformation-macro-description): {{String}}
  [FunctionName](#cfn-cloudformation-macro-functionname): {{String}}
  [LogGroupName](#cfn-cloudformation-macro-loggroupname): {{String}}
  [LogRoleARN](#cfn-cloudformation-macro-logrolearn): {{String}}
  [Name](#cfn-cloudformation-macro-name): {{String}}
```

## Properties
<a name="aws-resource-cloudformation-macro-properties"></a>

`Description`  <a name="cfn-cloudformation-macro-description"></a>
A description of the macro.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionName`  <a name="cfn-cloudformation-macro-functionname"></a>
The Amazon Resource Name (ARN) of the underlying Lambda function that you want CloudFormation to invoke when the macro is run.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupName`  <a name="cfn-cloudformation-macro-loggroupname"></a>
The CloudWatch Logs group to which CloudFormation sends error logging information when invoking the macro's underlying Lambda function.
This will be an existing CloudWatch Logs LogGroup. Neither CloudFormation or Lambda will create the group.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogRoleARN`  <a name="cfn-cloudformation-macro-logrolearn"></a>
The ARN of the role CloudFormation should assume when sending log entries to CloudWatch Logs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudformation-macro-name"></a>
The name of the macro. The name of the macro must be unique across all macros in the account.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cloudformation-macro-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-macro-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example:

 `{ "Ref": "myMacro" }`

For the macro `myMacro`, `Ref` returns the name of the macro.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudformation-macro-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudformation-macro-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
Returns a unique identifier for the resource.

## See also
<a name="aws-resource-cloudformation-macro--seealso"></a>
+ [Perform custom processing on CloudFormation templates with template macros](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html) in the *CloudFormation User Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
