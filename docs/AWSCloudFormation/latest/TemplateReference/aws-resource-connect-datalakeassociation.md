---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-datalakeassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::DataLakeAssociation
<a name="aws-resource-connect-datalakeassociation"></a>

<a name="aws-resource-connect-datalakeassociation-description"></a>The `AWS::Connect::DataLakeAssociation` resource Property description not available. for Connect.

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
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceId`  <a name="cfn-connect-datalakeassociation-instanceid"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^[-a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetAccountId`  <a name="cfn-connect-datalakeassociation-targetaccountid"></a>
Property description not available.
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

### Fn::GetAtt
<a name="aws-resource-connect-datalakeassociation-return-values-fn--getatt"></a>

####
<a name="aws-resource-connect-datalakeassociation-return-values-fn--getatt-fn--getatt"></a>

`ResourceShareArn`  <a name="ResourceShareArn-fn::getatt"></a>
Property description not available.

`ResourceShareId`  <a name="ResourceShareId-fn::getatt"></a>
Property description not available.
