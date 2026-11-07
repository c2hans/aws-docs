---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationazureblob-azurefederatedidentityconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationAzureBlob AzureFederatedIdentityConfig
<a name="aws-properties-datasync-locationazureblob-azurefederatedidentityconfig"></a>

Specifies federated identity parameters that allow AWS DataSync to obtain an OpenID Connect token for access to customer Azure Blob Storage. The token allows for temporary, short-term access to the storage. DataSync automatically refreshes the token to assure uninterrupted access to the storage.

**Note**
Federated identity parameters are an alternative to the `SasConfiguration` credentials that are expected to be valid long-term (e.g. at least for the duration of DataSync task execution). Do not specify federated identity and the SAS configuration for the same Azure Blob location.

## Syntax
<a name="aws-properties-datasync-locationazureblob-azurefederatedidentityconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationazureblob-azurefederatedidentityconfig-syntax.json"></a>

```
{
  "[AwsIamRole](#cfn-datasync-locationazureblob-azurefederatedidentityconfig-awsiamrole)" : {{String}},
  "[AzureOidc](#cfn-datasync-locationazureblob-azurefederatedidentityconfig-azureoidc)" : {{AzureOidcConfig}}
}
```

### YAML
<a name="aws-properties-datasync-locationazureblob-azurefederatedidentityconfig-syntax.yaml"></a>

```
  [AwsIamRole](#cfn-datasync-locationazureblob-azurefederatedidentityconfig-awsiamrole): {{String}}
  [AzureOidc](#cfn-datasync-locationazureblob-azurefederatedidentityconfig-azureoidc): {{
    AzureOidcConfig}}
```

## Properties
<a name="aws-properties-datasync-locationazureblob-azurefederatedidentityconfig-properties"></a>

`AwsIamRole`  <a name="cfn-datasync-locationazureblob-azurefederatedidentityconfig-awsiamrole"></a>
Specifies the ARN for an AWS role that allows DataSync to invoke STS GetWebIdentityToken API on behalf of the customer account and to obtain AWS STS JWT (web token).
*Required*: No
*Type*: String
*Pattern*: `^(arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*|)$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AzureOidc`  <a name="cfn-datasync-locationazureblob-azurefederatedidentityconfig-azureoidc"></a>
External identity parameters for Azure Blob Storage.
*Required*: No
*Type*: [AzureOidcConfig](aws-properties-datasync-locationazureblob-azureoidcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
