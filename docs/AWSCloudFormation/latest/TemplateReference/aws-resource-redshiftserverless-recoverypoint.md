---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshiftserverless-recoverypoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RedshiftServerless::RecoveryPoint
<a name="aws-resource-redshiftserverless-recoverypoint"></a>

The automatically created recovery point of a namespace. Recovery points are created every 30 minutes and kept for 24 hours.

## Syntax
<a name="aws-resource-redshiftserverless-recoverypoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-redshiftserverless-recoverypoint-syntax.json"></a>

```
{
  "Type" : "AWS::RedshiftServerless::RecoveryPoint",
  "Properties" : {
      "[NamespaceName](#cfn-redshiftserverless-recoverypoint-namespacename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-redshiftserverless-recoverypoint-syntax.yaml"></a>

```
Type: AWS::RedshiftServerless::RecoveryPoint
Properties:
  [NamespaceName](#cfn-redshiftserverless-recoverypoint-namespacename): {{String}}
```

## Properties
<a name="aws-resource-redshiftserverless-recoverypoint-properties"></a>

`NamespaceName`  <a name="cfn-redshiftserverless-recoverypoint-namespacename"></a>
The name of the namespace the recovery point is associated with.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9-]+$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-redshiftserverless-recoverypoint-return-values"></a>

### Ref
<a name="aws-resource-redshiftserverless-recoverypoint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-redshiftserverless-recoverypoint-return-values-fn--getatt"></a>

####
<a name="aws-resource-redshiftserverless-recoverypoint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`NamespaceArn`  <a name="NamespaceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the namespace the recovery point is associated with.

`RecoveryPointCreateTime`  <a name="RecoveryPointCreateTime-fn::getatt"></a>
The time the recovery point is created.

`RecoveryPointId`  <a name="RecoveryPointId-fn::getatt"></a>
The unique identifier of the recovery point.

`Tags`  <a name="Tags-fn::getatt"></a>
Property description not available.

`TotalSizeInMegaBytes`  <a name="TotalSizeInMegaBytes-fn::getatt"></a>
The total size of the data in the recovery point in megabytes.
