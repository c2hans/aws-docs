---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-accessgrant-grantee.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::AccessGrant Grantee
<a name="aws-properties-s3-accessgrant-grantee"></a>

The user, group, or role to which you are granting access. You can grant access to an IAM user or role. If you have added your corporate directory to AWSIAM Identity Center and associated your Identity Center instance with your S3 Access Grants instance, the grantee can also be a corporate directory user or group.

## Syntax
<a name="aws-properties-s3-accessgrant-grantee-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-accessgrant-grantee-syntax.json"></a>

```
{
  "[GranteeIdentifier](#cfn-s3-accessgrant-grantee-granteeidentifier)" : {{String}},
  "[GranteeType](#cfn-s3-accessgrant-grantee-granteetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-accessgrant-grantee-syntax.yaml"></a>

```
  [GranteeIdentifier](#cfn-s3-accessgrant-grantee-granteeidentifier): {{String}}
  [GranteeType](#cfn-s3-accessgrant-grantee-granteetype): {{String}}
```

## Properties
<a name="aws-properties-s3-accessgrant-grantee-properties"></a>

`GranteeIdentifier`  <a name="cfn-s3-accessgrant-grantee-granteeidentifier"></a>
The unique identifier of the `Grantee`. If the grantee type is `IAM`, the identifier is the IAM Amazon Resource Name (ARN) of the user or role. If the grantee type is a directory user or group, the identifier is 128-bit universally unique identifier (UUID) in the format `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`. You can obtain this UUID from your AWSIAM Identity Center instance.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GranteeType`  <a name="cfn-s3-accessgrant-grantee-granteetype"></a>
The type of the grantee to which access has been granted. It can be one of the following values:
+ `IAM` - An IAM user or role.
+ `DIRECTORY_USER` - Your corporate directory user. You can use this option if you have added your corporate identity directory to IAM Identity Center and associated the IAM Identity Center instance with your S3 Access Grants instance.
+ `DIRECTORY_GROUP` - Your corporate directory group. You can use this option if you have added your corporate identity directory to IAM Identity Center and associated the IAM Identity Center instance with your S3 Access Grants instance.
*Required*: Yes
*Type*: String
*Allowed values*: `IAM | DIRECTORY_USER | DIRECTORY_GROUP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
