---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_CreateLocationAzureBlob.html
---

# CreateLocationAzureBlob
<a name="API_CreateLocationAzureBlob"></a>

Creates a transfer *location* for a Microsoft Azure Blob Storage container. AWS DataSync can use this location as a transfer source or destination. You can make transfers with or without a [DataSync agent](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-creating-agent) that connects to your container.

Before you begin, make sure you know [how DataSync accesses Azure Blob Storage](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access) and works with [access tiers](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access-tiers) and [blob types](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#blob-types).

## Request Syntax
<a name="API_CreateLocationAzureBlob_RequestSyntax"></a>

```
{
   "AccessTier": "{{string}}",
   "AgentArns": [ "{{string}}" ],
   "AuthenticationType": "{{string}}",
   "BlobType": "{{string}}",
   "CmkSecretConfig": {
      "KmsKeyArn": "{{string}}",
      "SecretArn": "{{string}}"
   },
   "ContainerUrl": "{{string}}",
   "CustomSecretConfig": {
      "SecretAccessRoleArn": "{{string}}",
      "SecretArn": "{{string}}"
   },
   "SasConfiguration": {
      "Token": "{{string}}"
   },
   "Subdirectory": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateLocationAzureBlob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessTier](#API_CreateLocationAzureBlob_RequestSyntax) **   <a name="DataSync-CreateLocationAzureBlob-request-AccessTier"></a>
Specifies the access tier that you want your objects or files transferred into. This only applies when using the location as a transfer destination. For more information, see [Access tiers](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access-tiers).
Type: String
Valid Values: `HOT | COOL | ARCHIVE`
Required: No

 ** [AgentArns](#API_CreateLocationAzureBlob_RequestSyntax) **   <a name="DataSync-CreateLocationAzureBlob-request-AgentArns"></a>
(Optional) Specifies the Amazon Resource Name (ARN) of the DataSync agent that can connect with your Azure Blob Storage container. If you are setting up an agentless cross-cloud transfer, you do not need to specify a value for this parameter.
You can specify more than one agent. For more information, see [Using multiple agents for your transfer](https://docs.aws.amazon.com/datasync/latest/userguide/multiple-agents.html).
Make sure you configure this parameter correctly when you first create your storage location. You cannot add or remove agents from a storage location after you create it.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`
Required: No

 ** [AuthenticationType](#API_CreateLocationAzureBlob_RequestSyntax) **   <a name="DataSync-CreateLocationAzureBlob-request-AuthenticationType"></a>
Specifies the authentication method DataSync uses to access your Azure Blob Storage. DataSync can access blob storage using a shared access signature (SAS).
Type: String
Valid Values: `SAS | NONE`
Required: Yes

 ** [BlobType](#API_CreateLocationAzureBlob_RequestSyntax) **   <a name="DataSync-CreateLocationAzureBlob-request-BlobType"></a>
Specifies the type of blob that you want your objects or files to be when transferring them into Azure Blob Storage. Currently, DataSync only supports moving data into Azure Blob Storage as block blobs. For more information on blob types, see the [Azure Blob Storage documentation](https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs).
Type: String
Valid Values: `BLOCK`
Required: No

 ** [CmkSecretConfig](#API_CreateLocationAzureBlob_RequestSyntax) **   <a name="DataSync-CreateLocationAzureBlob-request-CmkSecretConfig"></a>
Specifies configuration information for a DataSync-managed secret, which includes the authentication token that DataSync uses to access a specific AzureBlob storage location, with a customer-managed AWS KMS key.
When you include this parameter as part of a `CreateLocationAzureBlob` request, you provide only the KMS key ARN. DataSync uses this KMS key together with the authentication token you specify for `SasConfiguration` to create a DataSync-managed secret to store the location access credentials.
Make sure that DataSync has permission to access the KMS key that you specify. For more information, see [ Using a service-managed secret encrypted with a custom AWS KMS key](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#service-secret-custom-key).
You can use either `CmkSecretConfig` (with `SasConfiguration`) or `CustomSecretConfig` (without `SasConfiguration`) to provide credentials for a `CreateLocationAzureBlob` request. Do not provide both parameters for the same request.
Type: [CmkSecretConfig](API_CmkSecretConfig.md) object
Required: No

 ** [ContainerUrl](#API_CreateLocationAzureBlob_RequestSyntax) **   <a name="DataSync-CreateLocationAzureBlob-request-ContainerUrl"></a>
Specifies the URL of the Azure Blob Storage container involved in your transfer.
Type: String
Length Constraints: Maximum length of 325.
Pattern: `^https:\/\/[A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252}\/[a-z0-9](-?[a-z0-9]){2,62}$`
Required: Yes

 ** [CustomSecretConfig](#API_CreateLocationAzureBlob_RequestSyntax) **   <a name="DataSync-CreateLocationAzureBlob-request-CustomSecretConfig"></a>
Specifies configuration information for a customer-managed Secrets Manager secret where the authentication token for an AzureBlob storage location is stored in plain text, in Secrets Manager. This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret. For more information, see [ Using a secret that you manage](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#custom-secret-custom-key).
You can use either `CmkSecretConfig` (with `SasConfiguration`) or `CustomSecretConfig` (without `SasConfiguration`) to provide credentials for a `CreateLocationAzureBlob` request. Do not provide both parameters for the same request.
Type: [CustomSecretConfig](API_CustomSecretConfig.md) object
Required: No

 ** [SasConfiguration](#API_CreateLocationAzureBlob_RequestSyntax) **   <a name="DataSync-CreateLocationAzureBlob-request-SasConfiguration"></a>
Specifies the SAS configuration that allows DataSync to access your Azure Blob Storage.
If you provide an authentication token using `SasConfiguration`, but do not provide secret configuration details using `CmkSecretConfig` or `CustomSecretConfig`, then DataSync stores the token using your AWS account's secrets manager secret.
Type: [AzureBlobSasConfiguration](API_AzureBlobSasConfiguration.md) object
Required: No

 ** [Subdirectory](#API_CreateLocationAzureBlob_RequestSyntax) **   <a name="DataSync-CreateLocationAzureBlob-request-Subdirectory"></a>
Specifies path segments if you want to limit your transfer to a virtual directory in your container (for example, `/my/images`).
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}\p{C}]*$`
Required: No

 ** [Tags](#API_CreateLocationAzureBlob_RequestSyntax) **   <a name="DataSync-CreateLocationAzureBlob-request-Tags"></a>
Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your transfer location.
Type: Array of [TagListEntry](API_TagListEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateLocationAzureBlob_ResponseSyntax"></a>

```
{
   "LocationArn": "string"
}
```

## Response Elements
<a name="API_CreateLocationAzureBlob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LocationArn](#API_CreateLocationAzureBlob_ResponseSyntax) **   <a name="DataSync-CreateLocationAzureBlob-response-LocationArn"></a>
The ARN of the Azure Blob Storage transfer location that you created.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

## Errors
<a name="API_CreateLocationAzureBlob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_CreateLocationAzureBlob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/CreateLocationAzureBlob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationAzureBlob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/CreateLocationAzureBlob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/CreateLocationAzureBlob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationAzureBlob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationAzureBlob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/CreateLocationAzureBlob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationAzureBlob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/CreateLocationAzureBlob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationAzureBlob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
