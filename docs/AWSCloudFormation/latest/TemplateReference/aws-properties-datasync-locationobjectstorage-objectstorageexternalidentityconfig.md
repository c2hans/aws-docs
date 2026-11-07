---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationobjectstorage-objectstorageexternalidentityconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationObjectStorage ObjectStorageExternalIdentityConfig
<a name="aws-properties-datasync-locationobjectstorage-objectstorageexternalidentityconfig"></a>

Specifies cloud-provider-specific external identity parameters used when exchanging the AWS web token for an OpenID Connect token at the object storage provider.

## Syntax
<a name="aws-properties-datasync-locationobjectstorage-objectstorageexternalidentityconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationobjectstorage-objectstorageexternalidentityconfig-syntax.json"></a>

```
{
  "[GoogleOidc](#cfn-datasync-locationobjectstorage-objectstorageexternalidentityconfig-googleoidc)" : {{GoogleOidcConfig}}
}
```

### YAML
<a name="aws-properties-datasync-locationobjectstorage-objectstorageexternalidentityconfig-syntax.yaml"></a>

```
  [GoogleOidc](#cfn-datasync-locationobjectstorage-objectstorageexternalidentityconfig-googleoidc): {{
    GoogleOidcConfig}}
```

## Properties
<a name="aws-properties-datasync-locationobjectstorage-objectstorageexternalidentityconfig-properties"></a>

`GoogleOidc`  <a name="cfn-datasync-locationobjectstorage-objectstorageexternalidentityconfig-googleoidc"></a>
External identity parameters for Google Cloud Storage.
*Required*: No
*Type*: [GoogleOidcConfig](aws-properties-datasync-locationobjectstorage-googleoidcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
