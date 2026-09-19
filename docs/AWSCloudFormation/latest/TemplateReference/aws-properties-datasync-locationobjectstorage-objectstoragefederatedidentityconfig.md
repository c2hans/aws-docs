---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationobjectstorage-objectstoragefederatedidentityconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationObjectStorage ObjectStorageFederatedIdentityConfig
<a name="aws-properties-datasync-locationobjectstorage-objectstoragefederatedidentityconfig"></a>

<a name="aws-properties-datasync-locationobjectstorage-objectstoragefederatedidentityconfig-description"></a>The `ObjectStorageFederatedIdentityConfig` property type specifies Property description not available. for an [AWS::DataSync::LocationObjectStorage](aws-resource-datasync-locationobjectstorage.md).

## Syntax
<a name="aws-properties-datasync-locationobjectstorage-objectstoragefederatedidentityconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationobjectstorage-objectstoragefederatedidentityconfig-syntax.json"></a>

```
{
  "[AwsIamRole](#cfn-datasync-locationobjectstorage-objectstoragefederatedidentityconfig-awsiamrole)" : {{String}},
  "[ExternalIdentity](#cfn-datasync-locationobjectstorage-objectstoragefederatedidentityconfig-externalidentity)" : {{ObjectStorageExternalIdentityConfig}}
}
```

### YAML
<a name="aws-properties-datasync-locationobjectstorage-objectstoragefederatedidentityconfig-syntax.yaml"></a>

```
  [AwsIamRole](#cfn-datasync-locationobjectstorage-objectstoragefederatedidentityconfig-awsiamrole): {{String}}
  [ExternalIdentity](#cfn-datasync-locationobjectstorage-objectstoragefederatedidentityconfig-externalidentity): {{
    ObjectStorageExternalIdentityConfig}}
```

## Properties
<a name="aws-properties-datasync-locationobjectstorage-objectstoragefederatedidentityconfig-properties"></a>

`AwsIamRole`  <a name="cfn-datasync-locationobjectstorage-objectstoragefederatedidentityconfig-awsiamrole"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^(arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*|)$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalIdentity`  <a name="cfn-datasync-locationobjectstorage-objectstoragefederatedidentityconfig-externalidentity"></a>
Property description not available.
*Required*: No
*Type*: [ObjectStorageExternalIdentityConfig](aws-properties-datasync-locationobjectstorage-objectstorageexternalidentityconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
