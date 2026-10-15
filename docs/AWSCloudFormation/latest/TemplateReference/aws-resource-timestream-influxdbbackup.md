---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-timestream-influxdbbackup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::InfluxDBBackup
<a name="aws-resource-timestream-influxdbbackup"></a>

<a name="aws-resource-timestream-influxdbbackup-description"></a>The `AWS::Timestream::InfluxDBBackup` resource Property description not available. for Timestream.

## Syntax
<a name="aws-resource-timestream-influxdbbackup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-timestream-influxdbbackup-syntax.json"></a>

```
{
  "Type" : "AWS::Timestream::InfluxDBBackup",
  "Properties" : {
      "[DbResourceId](#cfn-timestream-influxdbbackup-dbresourceid)" : {{String}},
      "[Name](#cfn-timestream-influxdbbackup-name)" : {{String}},
      "[RetentionDays](#cfn-timestream-influxdbbackup-retentiondays)" : {{Integer}},
      "[Tags](#cfn-timestream-influxdbbackup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-timestream-influxdbbackup-syntax.yaml"></a>

```
Type: AWS::Timestream::InfluxDBBackup
Properties:
  [DbResourceId](#cfn-timestream-influxdbbackup-dbresourceid): {{String}}
  [Name](#cfn-timestream-influxdbbackup-name): {{String}}
  [RetentionDays](#cfn-timestream-influxdbbackup-retentiondays): {{Integer}}
  [Tags](#cfn-timestream-influxdbbackup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-timestream-influxdbbackup-properties"></a>

`DbResourceId`  <a name="cfn-timestream-influxdbbackup-dbresourceid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-timestream-influxdbbackup-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*$`
*Minimum*: `3`
*Maximum*: `40`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RetentionDays`  <a name="cfn-timestream-influxdbbackup-retentiondays"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `3650`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-timestream-influxdbbackup-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-timestream-influxdbbackup-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-timestream-influxdbbackup-return-values"></a>

### Ref
<a name="aws-resource-timestream-influxdbbackup-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-timestream-influxdbbackup-return-values-fn--getatt"></a>

####
<a name="aws-resource-timestream-influxdbbackup-return-values-fn--getatt-fn--getatt"></a>

`AllocatedStorage`  <a name="AllocatedStorage-fn::getatt"></a>
Property description not available.

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`DbInstanceType`  <a name="DbInstanceType-fn::getatt"></a>
Property description not available.

`DbParameterGroupId`  <a name="DbParameterGroupId-fn::getatt"></a>
Property description not available.

`DbStorageType`  <a name="DbStorageType-fn::getatt"></a>
Property description not available.

`DeploymentType`  <a name="DeploymentType-fn::getatt"></a>
Property description not available.

`EngineType`  <a name="EngineType-fn::getatt"></a>
Property description not available.

`ExpiresAfter`  <a name="ExpiresAfter-fn::getatt"></a>
Property description not available.

`FailoverMode`  <a name="FailoverMode-fn::getatt"></a>
Property description not available.

`InfluxAuthParametersSecretArn`  <a name="InfluxAuthParametersSecretArn-fn::getatt"></a>
Property description not available.

`KmsKeyId`  <a name="KmsKeyId-fn::getatt"></a>
Property description not available.

`NetworkType`  <a name="NetworkType-fn::getatt"></a>
Property description not available.

`Port`  <a name="Port-fn::getatt"></a>
Property description not available.

`PubliclyAccessible`  <a name="PubliclyAccessible-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

`Type`  <a name="Type-fn::getatt"></a>
Property description not available.

`VpcSecurityGroupIds`  <a name="VpcSecurityGroupIds-fn::getatt"></a>
Property description not available.

`VpcSubnetIds`  <a name="VpcSubnetIds-fn::getatt"></a>
Property description not available.
