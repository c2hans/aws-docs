---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-accessgrant.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::AccessGrant
<a name="aws-resource-s3-accessgrant"></a>

The `AWS::S3::AccessGrant` resource creates an access grant that gives a grantee access to your S3 data. The grantee can be an IAM user or role or a directory user, or group. Before you can create a grant, you must have an S3 Access Grants instance in the same Region as the S3 data. You can create an S3 Access Grants instance using the [AWS::S3::AccessGrantsInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accessgrantsinstance.html). You must also have registered at least one S3 data location in your S3 Access Grants instance using [AWS::S3::AccessGrantsLocation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accessgrantslocation.html).

Permissions
You must have the `s3:CreateAccessGrant` permission to use this resource.

Additional Permissions
For any directory identity - `sso:DescribeInstance` and `sso:DescribeApplication`
For directory users - `identitystore:DescribeUser`
For directory groups - `identitystore:DescribeGroup`

## Syntax
<a name="aws-resource-s3-accessgrant-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3-accessgrant-syntax.json"></a>

```
{
  "Type" : "AWS::S3::AccessGrant",
  "Properties" : {
      "[AccessGrantsLocationConfiguration](#cfn-s3-accessgrant-accessgrantslocationconfiguration)" : {{AccessGrantsLocationConfiguration}},
      "[AccessGrantsLocationId](#cfn-s3-accessgrant-accessgrantslocationid)" : {{String}},
      "[ApplicationArn](#cfn-s3-accessgrant-applicationarn)" : {{String}},
      "[Grantee](#cfn-s3-accessgrant-grantee)" : {{Grantee}},
      "[Permission](#cfn-s3-accessgrant-permission)" : {{String}},
      "[S3PrefixType](#cfn-s3-accessgrant-s3prefixtype)" : {{String}},
      "[Tags](#cfn-s3-accessgrant-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-s3-accessgrant-syntax.yaml"></a>

```
Type: AWS::S3::AccessGrant
Properties:
  [AccessGrantsLocationConfiguration](#cfn-s3-accessgrant-accessgrantslocationconfiguration): {{
    AccessGrantsLocationConfiguration}}
  [AccessGrantsLocationId](#cfn-s3-accessgrant-accessgrantslocationid): {{String}}
  [ApplicationArn](#cfn-s3-accessgrant-applicationarn): {{String}}
  [Grantee](#cfn-s3-accessgrant-grantee): {{
    Grantee}}
  [Permission](#cfn-s3-accessgrant-permission): {{String}}
  [S3PrefixType](#cfn-s3-accessgrant-s3prefixtype): {{String}}
  [Tags](#cfn-s3-accessgrant-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-s3-accessgrant-properties"></a>

`AccessGrantsLocationConfiguration`  <a name="cfn-s3-accessgrant-accessgrantslocationconfiguration"></a>
The configuration options of the grant location. The grant location is the S3 path to the data to which you are granting access. It contains the `S3SubPrefix` field. The grant scope is the result of appending the subprefix to the location scope of the registered location.
*Required*: No
*Type*: [AccessGrantsLocationConfiguration](aws-properties-s3-accessgrant-accessgrantslocationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AccessGrantsLocationId`  <a name="cfn-s3-accessgrant-accessgrantslocationid"></a>
The ID of the registered location to which you are granting access. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID `default` to the default location `s3://` and assigns an auto-generated ID to other locations that you register.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationArn`  <a name="cfn-s3-accessgrant-applicationarn"></a>
The Amazon Resource Name (ARN) of an AWSIAM Identity Center application associated with your Identity Center instance. If the grant includes an application ARN, the grantee can only access the S3 data through this application.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Grantee`  <a name="cfn-s3-accessgrant-grantee"></a>
The user, group, or role to which you are granting access. You can grant access to an IAM user or role. If you have added your corporate directory to AWSIAM Identity Center and associated your Identity Center instance with your S3 Access Grants instance, the grantee can also be a corporate directory user or group.
*Required*: Yes
*Type*: [Grantee](aws-properties-s3-accessgrant-grantee.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permission`  <a name="cfn-s3-accessgrant-permission"></a>
The type of access that you are granting to your S3 data, which can be set to one of the following values:
+ `READ` – Grant read-only access to the S3 data.
+ `WRITE` – Grant write-only access to the S3 data.
+ `READWRITE` – Grant both read and write access to the S3 data.
*Required*: Yes
*Type*: String
*Allowed values*: `READ | WRITE | READWRITE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3PrefixType`  <a name="cfn-s3-accessgrant-s3prefixtype"></a>
The type of `S3SubPrefix`. The only possible value is `Object`. Pass this value if the access grant scope is an object. Do not pass this value if the access grant scope is a bucket or a bucket and a prefix.
*Required*: No
*Type*: String
*Allowed values*: `Object`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-s3-accessgrant-tags"></a>
The AWS resource tags that you are adding to the access grant. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources.
*Required*: No
*Type*: Array of [Tag](aws-properties-s3-accessgrant-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-s3-accessgrant-return-values"></a>

### Ref
<a name="aws-resource-s3-accessgrant-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns some information about your access grant.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-s3-accessgrant-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-s3-accessgrant-return-values-fn--getatt-fn--getatt"></a>

`AccessGrantArn`  <a name="AccessGrantArn-fn::getatt"></a>
The ARN of the access grant.

`AccessGrantId`  <a name="AccessGrantId-fn::getatt"></a>
The ID of the access grant. S3 Access Grants auto-generates this ID when you create the access grant.

`GrantScope`  <a name="GrantScope-fn::getatt"></a>
The S3 path of the data to which you are granting access. It is the result of appending the `Subprefix` to the location scope.
