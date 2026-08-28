---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeHubContent.html
---

# DescribeHubContent
<a name="API_DescribeHubContent"></a>

Describe the content of a hub.

## Request Syntax
<a name="API_DescribeHubContent_RequestSyntax"></a>

```
{
   "HubContentName": "{{string}}",
   "HubContentType": "{{string}}",
   "HubContentVersion": "{{string}}",
   "HubName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeHubContent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HubContentName](#API_DescribeHubContent_RequestSyntax) **   <a name="sagemaker-DescribeHubContent-request-HubContentName"></a>
The name of the content to describe.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [HubContentType](#API_DescribeHubContent_RequestSyntax) **   <a name="sagemaker-DescribeHubContent-request-HubContentType"></a>
The type of content in the hub.
Type: String
Valid Values: `Model | Notebook | ModelReference | DataSet | JsonDoc`
Required: Yes

 ** [HubContentVersion](#API_DescribeHubContent_RequestSyntax) **   <a name="sagemaker-DescribeHubContent-request-HubContentVersion"></a>
The version of the content to describe.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: No

 ** [HubName](#API_DescribeHubContent_RequestSyntax) **   <a name="sagemaker-DescribeHubContent-request-HubName"></a>
The name of the hub that contains the content to describe.
Type: String
Pattern: `(arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:(\d{12}|aws):hub\/)?[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeHubContent_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "DocumentSchemaVersion": "string",
   "FailureReason": "string",
   "HubArn": "string",
   "HubContentArn": "string",
   "HubContentDependencies": [
      {
         "DependencyCopyPath": "string",
         "DependencyOriginPath": "string"
      }
   ],
   "HubContentDescription": "string",
   "HubContentDisplayName": "string",
   "HubContentDocument": "string",
   "HubContentMarkdown": "string",
   "HubContentName": "string",
   "HubContentSearchKeywords": [ "string" ],
   "HubContentStatus": "string",
   "HubContentType": "string",
   "HubContentVersion": "string",
   "HubName": "string",
   "LastModifiedTime": number,
   "ReferenceMinVersion": "string",
   "SageMakerPublicHubContentArn": "string",
   "SupportStatus": "string"
}
```

## Response Elements
<a name="API_DescribeHubContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-CreationTime"></a>
The date and time that hub content was created.
Type: Timestamp

 ** [DocumentSchemaVersion](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-DocumentSchemaVersion"></a>
The document schema version for the hub content.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`

 ** [FailureReason](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-FailureReason"></a>
The failure reason if importing hub content failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [HubArn](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-HubArn"></a>
The Amazon Resource Name (ARN) of the hub that contains the content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [HubContentArn](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-HubContentArn"></a>
The Amazon Resource Name (ARN) of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [HubContentDependencies](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-HubContentDependencies"></a>
The location of any dependencies that the hub content has, such as scripts, model artifacts, datasets, or notebooks.
Type: Array of [HubContentDependency](API_HubContentDependency.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [HubContentDescription](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-HubContentDescription"></a>
A description of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Pattern: `.*`

 ** [HubContentDisplayName](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-HubContentDisplayName"></a>
The display name of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [HubContentDocument](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-HubContentDocument"></a>
The hub content document that describes information about the hub content such as type, associated containers, scripts, and more.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 327680.
Pattern: `.*`

 ** [HubContentMarkdown](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-HubContentMarkdown"></a>
A string that provides a description of the hub content. This string can include links, tables, and standard markdown formating.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 170391.

 ** [HubContentName](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-HubContentName"></a>
The name of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [HubContentSearchKeywords](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-HubContentSearchKeywords"></a>
The searchable keywords for the hub content.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [HubContentStatus](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-HubContentStatus"></a>
The status of the hub content.
Type: String
Valid Values: `Available | Importing | Deleting | ImportFailed | DeleteFailed | PendingImport | PendingDelete`

 ** [HubContentType](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-HubContentType"></a>
The type of hub content.
Type: String
Valid Values: `Model | Notebook | ModelReference | DataSet | JsonDoc`

 ** [HubContentVersion](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-HubContentVersion"></a>
The version of the hub content.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`

 ** [HubName](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-HubName"></a>
The name of the hub that contains the content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [LastModifiedTime](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-LastModifiedTime"></a>
The last modified time of the hub content.
Type: Timestamp

 ** [ReferenceMinVersion](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-ReferenceMinVersion"></a>
The minimum version of the hub content.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`

 ** [SageMakerPublicHubContentArn](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-SageMakerPublicHubContentArn"></a>
The ARN of the public hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:aws:hub-content\/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}\/Model\/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`

 ** [SupportStatus](#API_DescribeHubContent_ResponseSyntax) **   <a name="sagemaker-DescribeHubContent-response-SupportStatus"></a>
The support status of the hub content.
Type: String
Valid Values: `Supported | Deprecated | Restricted`

## Errors
<a name="API_DescribeHubContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeHubContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeHubContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeHubContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeHubContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeHubContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeHubContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeHubContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeHubContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeHubContent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeHubContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeHubContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
