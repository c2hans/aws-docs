---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationazureblob-azurefederatedidentityconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationAzureBlob AzureFederatedIdentityConfig
<a name="aws-properties-datasync-locationazureblob-azurefederatedidentityconfig"></a>

<a name="aws-properties-datasync-locationazureblob-azurefederatedidentityconfig-description"></a>The `AzureFederatedIdentityConfig` property type specifies Property description not available. for an [AWS::DataSync::LocationAzureBlob](aws-resource-datasync-locationazureblob.md).

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
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^(arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*|)$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AzureOidc`  <a name="cfn-datasync-locationazureblob-azurefederatedidentityconfig-azureoidc"></a>
Property description not available.
*Required*: No
*Type*: [AzureOidcConfig](aws-properties-datasync-locationazureblob-azureoidcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
