---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HubContent.html
---

# HubContent
<a name="API_HubContent"></a>

Contains information about a hub content resource, including its name, version, type, associated documents, dependencies, and status, as returned by a search result.

## Contents
<a name="API_HubContent_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-HubContent-CreationTime"></a>
The date and time that hub content was created.
Type: Timestamp
Required: Yes

 ** DocumentSchemaVersion **   <a name="sagemaker-Type-HubContent-DocumentSchemaVersion"></a>
The document schema version for the hub content.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: Yes

 ** HubArn **   <a name="sagemaker-Type-HubContent-HubArn"></a>
The Amazon Resource Name (ARN) of the hub that contains the content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: Yes

 ** HubContentArn **   <a name="sagemaker-Type-HubContent-HubContentArn"></a>
The Amazon Resource Name (ARN) of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: Yes

 ** HubContentName **   <a name="sagemaker-Type-HubContent-HubContentName"></a>
The name of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** HubContentStatus **   <a name="sagemaker-Type-HubContent-HubContentStatus"></a>
The status of the hub content.
Type: String
Valid Values: `Available | Importing | Deleting | ImportFailed | DeleteFailed | PendingImport | PendingDelete`
Required: Yes

 ** HubContentType **   <a name="sagemaker-Type-HubContent-HubContentType"></a>
The type of hub content.
Type: String
Valid Values: `Model | Notebook | ModelReference | DataSet | JsonDoc`
Required: Yes

 ** HubContentVersion **   <a name="sagemaker-Type-HubContent-HubContentVersion"></a>
The version of the hub content.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: Yes

 ** HubName **   <a name="sagemaker-Type-HubContent-HubName"></a>
The name of the hub that contains the content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** FailureReason **   <a name="sagemaker-Type-HubContent-FailureReason"></a>
The failure reason if importing hub content failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** HubContentDependencies **   <a name="sagemaker-Type-HubContent-HubContentDependencies"></a>
The location of any dependencies that the hub content has, such as scripts, model artifacts, datasets, or notebooks.
Type: Array of [HubContentDependency](API_HubContentDependency.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** HubContentDescription **   <a name="sagemaker-Type-HubContent-HubContentDescription"></a>
A description of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Pattern: `.*`
Required: No

 ** HubContentDisplayName **   <a name="sagemaker-Type-HubContent-HubContentDisplayName"></a>
The display name of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** HubContentDocument **   <a name="sagemaker-Type-HubContent-HubContentDocument"></a>
The hub content document that describes information about the hub content such as type, associated containers, scripts, and more.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 327680.
Pattern: `.*`
Required: No

 ** HubContentMarkdown **   <a name="sagemaker-Type-HubContent-HubContentMarkdown"></a>
A string that provides a description of the hub content. This string can include links, tables, and standard markdown formatting.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 170391.
Required: No

 ** HubContentSearchKeywords **   <a name="sagemaker-Type-HubContent-HubContentSearchKeywords"></a>
The searchable keywords for the hub content.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-HubContent-LastModifiedTime"></a>
The last modified time of the hub content.
Type: Timestamp
Required: No

 ** ReferenceMinVersion **   <a name="sagemaker-Type-HubContent-ReferenceMinVersion"></a>
The minimum version of the hub content.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: No

 ** SageMakerPublicHubContentArn **   <a name="sagemaker-Type-HubContent-SageMakerPublicHubContentArn"></a>
The Amazon Resource Name (ARN) of the public hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:aws:hub-content\/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}\/Model\/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
Required: No

 ** SupportStatus **   <a name="sagemaker-Type-HubContent-SupportStatus"></a>
The support status of the hub content.
Type: String
Valid Values: `Supported | Deprecated | Restricted`
Required: No

 ** Tags **   <a name="sagemaker-Type-HubContent-Tags"></a>
Any tags associated with the hub content.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_HubContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HubContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HubContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HubContent)
