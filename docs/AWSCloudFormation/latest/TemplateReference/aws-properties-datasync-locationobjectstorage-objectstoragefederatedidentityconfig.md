---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationobjectstorage-objectstoragefederatedidentityconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationObjectStorage ObjectStorageFederatedIdentityConfig
<a name="aws-properties-datasync-locationobjectstorage-objectstoragefederatedidentityconfig"></a>

Specifies federated identity parameters that allow AWS DataSync to obtain OpenID Connect token for access to customer object storage. The token allows for temporary, short-term access to the storage. DataSync automatically refreshes the token to assure uninterrupted access to the storage.

**Note**
Federated identity parameters are an alternative to the `AccessKey`/`SecretKey` credentials that are expected to be valid long-term (e.g. at least for the duration of DataSync task execution). Do not specify federated identity and the key parameters for the same object storage location.

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
Specifies the ARN for an AWS role that allows DataSync to invoke STS GetWebIdentityToken API on behalf of the customer account and to obtain AWS STS JWT (web token).
*Required*: No
*Type*: String
*Pattern*: `^(arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*|)$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalIdentity`  <a name="cfn-datasync-locationobjectstorage-objectstoragefederatedidentityconfig-externalidentity"></a>
Specifies cloud-provider-specific external identity parameters used when exchanging the AWS web token for an OpenID Connect token at the object storage provider.
*Required*: No
*Type*: [ObjectStorageExternalIdentityConfig](aws-properties-datasync-locationobjectstorage-objectstorageexternalidentityconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
