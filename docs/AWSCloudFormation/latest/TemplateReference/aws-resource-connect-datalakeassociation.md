---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-datalakeassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::DataLakeAssociation
<a name="aws-resource-connect-datalakeassociation"></a>

Associates the specified dataset for a Amazon Connect Customer instance with the target account. You can associate only one dataset in a single resource.

## Syntax
<a name="aws-resource-connect-datalakeassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-datalakeassociation-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::DataLakeAssociation",
  "Properties" : {
      "[DataSetId](#cfn-connect-datalakeassociation-datasetid)" : {{String}},
      "[InstanceId](#cfn-connect-datalakeassociation-instanceid)" : {{String}},
      "[TargetAccountId](#cfn-connect-datalakeassociation-targetaccountid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-datalakeassociation-syntax.yaml"></a>

```
Type: AWS::Connect::DataLakeAssociation
Properties:
  [DataSetId](#cfn-connect-datalakeassociation-datasetid): {{String}}
  [InstanceId](#cfn-connect-datalakeassociation-instanceid): {{String}}
  [TargetAccountId](#cfn-connect-datalakeassociation-targetaccountid): {{String}}
```

## Properties
<a name="aws-resource-connect-datalakeassociation-properties"></a>

`DataSetId`  <a name="cfn-connect-datalakeassociation-datasetid"></a>
The identifier of the dataset to associate with the target account.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceId`  <a name="cfn-connect-datalakeassociation-instanceid"></a>
The identifier of the Amazon Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^[-a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetAccountId`  <a name="cfn-connect-datalakeassociation-targetaccountid"></a>
The identifier of the target account. Use to associate a dataset to a different account than the one containing the Amazon Connect Customer instance. If not specified, by default this value is the AWS account that has the Amazon Connect Customer instance.
*Required*: No
*Type*: String
*Pattern*: `^\d+$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-connect-datalakeassociation-return-values"></a>

### Ref
<a name="aws-resource-connect-datalakeassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the composite identifier of the data lake association in the format `InstanceId|DataSetId|TargetAccountId`. For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-datalakeassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

####
<a name="aws-resource-connect-datalakeassociation-return-values-fn--getatt-fn--getatt"></a>

`ResourceShareArn`  <a name="ResourceShareArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the AWS Resource Access Manager share.

`ResourceShareId`  <a name="ResourceShareId-fn::getatt"></a>
The AWS Resource Access Manager share ID that is generated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
