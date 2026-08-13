---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-accessgrantsinstance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::AccessGrantsInstance
<a name="aws-resource-s3-accessgrantsinstance"></a>

The `AWS::S3::AccessGrantInstance` resource creates an S3 Access Grants instance, which serves as a logical grouping for access grants. You can create one S3 Access Grants instance per Region per account.

Permissions
You must have the `s3:CreateAccessGrantsInstance` permission to use this resource.

Additional Permissions
To associate an IAM Identity Center instance with your S3 Access Grants instance, you must also have the `sso:DescribeInstance`, `sso:CreateApplication`, `sso:PutApplicationGrant`, and `sso:PutApplicationAuthenticationMethod` permissions.

## Syntax
<a name="aws-resource-s3-accessgrantsinstance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3-accessgrantsinstance-syntax.json"></a>

```
{
  "Type" : "AWS::S3::AccessGrantsInstance",
  "Properties" : {
      "[IdentityCenterArn](#cfn-s3-accessgrantsinstance-identitycenterarn)" : {{String}},
      "[Tags](#cfn-s3-accessgrantsinstance-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-s3-accessgrantsinstance-syntax.yaml"></a>

```
Type: AWS::S3::AccessGrantsInstance
Properties:
  [IdentityCenterArn](#cfn-s3-accessgrantsinstance-identitycenterarn): {{String}}
  [Tags](#cfn-s3-accessgrantsinstance-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-s3-accessgrantsinstance-properties"></a>

`IdentityCenterArn`  <a name="cfn-s3-accessgrantsinstance-identitycenterarn"></a>
If you would like to associate your S3 Access Grants instance with an AWSIAM Identity Center instance, use this field to pass the Amazon Resource Name (ARN) of the AWSIAM Identity Center instance that you are associating with your S3 Access Grants instance. An IAM Identity Center instance is your corporate identity directory that you added to the IAM Identity Center.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-s3-accessgrantsinstance-tags"></a>
The AWS resource tags that you are adding to the S3 Access Grants instance. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources.
*Required*: No
*Type*: Array of [Tag](aws-properties-s3-accessgrantsinstance-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-s3-accessgrantsinstance-return-values"></a>

### Ref
<a name="aws-resource-s3-accessgrantsinstance-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns some information about your S3 Access Grants instance.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-s3-accessgrantsinstance-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-s3-accessgrantsinstance-return-values-fn--getatt-fn--getatt"></a>

`AccessGrantsInstanceArn`  <a name="AccessGrantsInstanceArn-fn::getatt"></a>
The ARN of the S3 Access Grants instance.

`AccessGrantsInstanceId`  <a name="AccessGrantsInstanceId-fn::getatt"></a>
The ID of the S3 Access Grants instance. The ID is `default`. You can have one S3 Access Grants instance per Region per account.
