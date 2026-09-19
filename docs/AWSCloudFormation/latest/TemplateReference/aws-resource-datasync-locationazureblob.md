---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datasync-locationazureblob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationAzureBlob
<a name="aws-resource-datasync-locationazureblob"></a>

Creates a transfer *location* for a Microsoft Azure Blob Storage container. AWS DataSync can use this location as a transfer source or destination. You can make transfers with or without a [DataSync agent](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-creating-agent) that connects to your container.

Before you begin, make sure you know [how DataSync accesses Azure Blob Storage](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access) and works with [access tiers](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access-tiers) and [blob types](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#blob-types).

## Syntax
<a name="aws-resource-datasync-locationazureblob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datasync-locationazureblob-syntax.json"></a>

```
{
  "Type" : "AWS::DataSync::LocationAzureBlob",
  "Properties" : {
      "[AgentArns](#cfn-datasync-locationazureblob-agentarns)" : {{[ String, ... ]}},
      "[AzureAccessTier](#cfn-datasync-locationazureblob-azureaccesstier)" : {{String}},
      "[AzureBlobAuthenticationType](#cfn-datasync-locationazureblob-azureblobauthenticationtype)" : {{String}},
      "[AzureBlobContainerUrl](#cfn-datasync-locationazureblob-azureblobcontainerurl)" : {{String}},
      "[AzureBlobSasConfiguration](#cfn-datasync-locationazureblob-azureblobsasconfiguration)" : {{AzureBlobSasConfiguration}},
      "[AzureBlobType](#cfn-datasync-locationazureblob-azureblobtype)" : {{String}},
      "[CmkSecretConfig](#cfn-datasync-locationazureblob-cmksecretconfig)" : {{CmkSecretConfig}},
      "[CustomSecretConfig](#cfn-datasync-locationazureblob-customsecretconfig)" : {{CustomSecretConfig}},
      "[FederatedIdentity](#cfn-datasync-locationazureblob-federatedidentity)" : {{AzureFederatedIdentityConfig}},
      "[Subdirectory](#cfn-datasync-locationazureblob-subdirectory)" : {{String}},
      "[Tags](#cfn-datasync-locationazureblob-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-datasync-locationazureblob-syntax.yaml"></a>

```
Type: AWS::DataSync::LocationAzureBlob
Properties:
  [AgentArns](#cfn-datasync-locationazureblob-agentarns): {{
    - String}}
  [AzureAccessTier](#cfn-datasync-locationazureblob-azureaccesstier): {{String}}
  [AzureBlobAuthenticationType](#cfn-datasync-locationazureblob-azureblobauthenticationtype): {{String}}
  [AzureBlobContainerUrl](#cfn-datasync-locationazureblob-azureblobcontainerurl): {{String}}
  [AzureBlobSasConfiguration](#cfn-datasync-locationazureblob-azureblobsasconfiguration): {{
    AzureBlobSasConfiguration}}
  [AzureBlobType](#cfn-datasync-locationazureblob-azureblobtype): {{String}}
  [CmkSecretConfig](#cfn-datasync-locationazureblob-cmksecretconfig): {{
    CmkSecretConfig}}
  [CustomSecretConfig](#cfn-datasync-locationazureblob-customsecretconfig): {{
    CustomSecretConfig}}
  [FederatedIdentity](#cfn-datasync-locationazureblob-federatedidentity): {{
    AzureFederatedIdentityConfig}}
  [Subdirectory](#cfn-datasync-locationazureblob-subdirectory): {{String}}
  [Tags](#cfn-datasync-locationazureblob-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-datasync-locationazureblob-properties"></a>

`AgentArns`  <a name="cfn-datasync-locationazureblob-agentarns"></a>
(Optional) Specifies the Amazon Resource Name (ARN) of the DataSync agent that can connect with your Azure Blob Storage container. If you are setting up an agentless cross-cloud transfer, you do not need to specify a value for this parameter.
You can specify more than one agent. For more information, see [Using multiple agents for your transfer](https://docs.aws.amazon.com/datasync/latest/userguide/multiple-agents.html).
Make sure you configure this parameter correctly when you first create your storage location. You cannot add or remove agents from a storage location after you create it.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128 | 8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AzureAccessTier`  <a name="cfn-datasync-locationazureblob-azureaccesstier"></a>
Specifies the access tier that you want your objects or files transferred into. This only applies when using the location as a transfer destination. For more information, see [Access tiers](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access-tiers).
*Required*: No
*Type*: String
*Allowed values*: `HOT | COOL | ARCHIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AzureBlobAuthenticationType`  <a name="cfn-datasync-locationazureblob-azureblobauthenticationtype"></a>
Specifies the authentication method DataSync uses to access your Azure Blob Storage. DataSync can access blob storage using a shared access signature (SAS).
*Required*: Yes
*Type*: String
*Allowed values*: `SAS | NONE | OIDC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AzureBlobContainerUrl`  <a name="cfn-datasync-locationazureblob-azureblobcontainerurl"></a>
Specifies the URL of the Azure Blob Storage container involved in your transfer.
*Required*: No
*Type*: String
*Pattern*: `^https://[A-Za-z0-9]((.|-+)?[A-Za-z0-9]){0,252}/[a-z0-9](-?[a-z0-9]){2,62}$`
*Maximum*: `325`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AzureBlobSasConfiguration`  <a name="cfn-datasync-locationazureblob-azureblobsasconfiguration"></a>
Specifies the SAS configuration that allows DataSync to access your Azure Blob Storage.
If you provide an authentication token using `SasConfiguration`, but do not provide secret configuration details using `CmkSecretConfig` or `CustomSecretConfig`, then DataSync stores the token using your AWS account's secrets manager secret.
*Required*: No
*Type*: [AzureBlobSasConfiguration](aws-properties-datasync-locationazureblob-azureblobsasconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AzureBlobType`  <a name="cfn-datasync-locationazureblob-azureblobtype"></a>
Specifies the type of blob that you want your objects or files to be when transferring them into Azure Blob Storage. Currently, DataSync only supports moving data into Azure Blob Storage as block blobs. For more information on blob types, see the [Azure Blob Storage documentation](https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs).
*Required*: No
*Type*: String
*Allowed values*: `BLOCK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CmkSecretConfig`  <a name="cfn-datasync-locationazureblob-cmksecretconfig"></a>
Specifies configuration information for a DataSync-managed secret, such as an authentication token, secret key, password, or Kerberos keytab that DataSync uses to access a specific storage location, with a customer-managed AWS KMS key.
You can use either `CmkSecretConfig` or `CustomSecretConfig` to provide credentials for a `CreateLocation` request. Do not provide both parameters for the same request.
*Required*: No
*Type*: [CmkSecretConfig](aws-properties-datasync-locationazureblob-cmksecretconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomSecretConfig`  <a name="cfn-datasync-locationazureblob-customsecretconfig"></a>
Specifies configuration information for a customer-managed Secrets Manager secret where a storage location credentials is stored in Secrets Manager as plain text (for authentication token, secret key, or password) or as binary (for Kerberos keytab). This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret.
You can use either `CmkSecretConfig` or `CustomSecretConfig` to provide credentials for a `CreateLocation` request. Do not provide both parameters for the same request.
*Required*: No
*Type*: [CustomSecretConfig](aws-properties-datasync-locationazureblob-customsecretconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FederatedIdentity`  <a name="cfn-datasync-locationazureblob-federatedidentity"></a>
Property description not available.
*Required*: No
*Type*: [AzureFederatedIdentityConfig](aws-properties-datasync-locationazureblob-azurefederatedidentityconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subdirectory`  <a name="cfn-datasync-locationazureblob-subdirectory"></a>
Specifies path segments if you want to limit your transfer to a virtual directory in your container (for example, `/my/images`).
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}\p{C}]*$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-datasync-locationazureblob-tags"></a>
Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your transfer location.
*Required*: No
*Type*: Array of [Tag](aws-properties-datasync-locationazureblob-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datasync-locationazureblob-return-values"></a>

### Ref
<a name="aws-resource-datasync-locationazureblob-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the location resource ARN. For example:

 `arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50s3`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datasync-locationazureblob-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datasync-locationazureblob-return-values-fn--getatt-fn--getatt"></a>

`CmkSecretConfig.SecretArn`  <a name="CmkSecretConfig.SecretArn-fn::getatt"></a>
Property description not available.

`LocationArn`  <a name="LocationArn-fn::getatt"></a>
The ARN of the Azure Blob Storage transfer location that you created.

`LocationUri`  <a name="LocationUri-fn::getatt"></a>
The URI of the Azure Blob Storage transfer location that you created.
