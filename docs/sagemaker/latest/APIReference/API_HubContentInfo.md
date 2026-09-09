---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HubContentInfo.html
---

# HubContentInfo
<a name="API_HubContentInfo"></a>

Information about hub content.

## Contents
<a name="API_HubContentInfo_Contents"></a>

 ** DocumentSchemaVersion **   <a name="sagemaker-Type-HubContentInfo-DocumentSchemaVersion"></a>
The version of the hub content document schema.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: Yes

 ** HubContentArn **   <a name="sagemaker-Type-HubContentInfo-HubContentArn"></a>
The Amazon Resource Name (ARN) of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: Yes

 ** HubContentName **   <a name="sagemaker-Type-HubContentInfo-HubContentName"></a>
The name of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** HubContentStatus **   <a name="sagemaker-Type-HubContentInfo-HubContentStatus"></a>
The status of the hub content.
Type: String
Valid Values: `Available | Importing | Deleting | ImportFailed | DeleteFailed | PendingImport | PendingDelete`
Required: Yes

 ** HubContentType **   <a name="sagemaker-Type-HubContentInfo-HubContentType"></a>
The type of hub content.
Type: String
Valid Values: `Model | Notebook | ModelReference | DataSet | JsonDoc`
Required: Yes

 ** HubContentVersion **   <a name="sagemaker-Type-HubContentInfo-HubContentVersion"></a>
The version of the hub content.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: Yes

 ** HubContentDescription **   <a name="sagemaker-Type-HubContentInfo-HubContentDescription"></a>
A description of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Pattern: `.*`
Required: No

 ** HubContentDisplayName **   <a name="sagemaker-Type-HubContentInfo-HubContentDisplayName"></a>
The display name of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** HubContentSearchKeywords **   <a name="sagemaker-Type-HubContentInfo-HubContentSearchKeywords"></a>
The searchable keywords for the hub content.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** SageMakerPublicHubContentArn **   <a name="sagemaker-Type-HubContentInfo-SageMakerPublicHubContentArn"></a>
The ARN of the public hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:aws:hub-content\/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}\/Model\/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
Required: No

 ** SupportStatus **   <a name="sagemaker-Type-HubContentInfo-SupportStatus"></a>
The support status of the hub content.
Type: String
Valid Values: `Supported | Deprecated | Restricted`
Required: No

## See Also
<a name="API_HubContentInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HubContentInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HubContentInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HubContentInfo)
