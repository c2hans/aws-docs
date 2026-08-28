---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteHubContent.html
---

# DeleteHubContent
<a name="API_DeleteHubContent"></a>

Delete the contents of a hub.

## Request Syntax
<a name="API_DeleteHubContent_RequestSyntax"></a>

```
{
   "HubContentName": "{{string}}",
   "HubContentType": "{{string}}",
   "HubContentVersion": "{{string}}",
   "HubName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteHubContent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HubContentName](#API_DeleteHubContent_RequestSyntax) **   <a name="sagemaker-DeleteHubContent-request-HubContentName"></a>
The name of the content that you want to delete from a hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [HubContentType](#API_DeleteHubContent_RequestSyntax) **   <a name="sagemaker-DeleteHubContent-request-HubContentType"></a>
The type of content that you want to delete from a hub.
Type: String
Valid Values: `Model | Notebook | ModelReference | DataSet | JsonDoc`
Required: Yes

 ** [HubContentVersion](#API_DeleteHubContent_RequestSyntax) **   <a name="sagemaker-DeleteHubContent-request-HubContentVersion"></a>
The version of the content that you want to delete from a hub.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: Yes

 ** [HubName](#API_DeleteHubContent_RequestSyntax) **   <a name="sagemaker-DeleteHubContent-request-HubName"></a>
The name of the hub that you want to delete content in.
Type: String
Pattern: `(arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:(\d{12}|aws):hub\/)?[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Elements
<a name="API_DeleteHubContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteHubContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteHubContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteHubContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteHubContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteHubContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteHubContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteHubContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteHubContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteHubContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteHubContent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteHubContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteHubContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
