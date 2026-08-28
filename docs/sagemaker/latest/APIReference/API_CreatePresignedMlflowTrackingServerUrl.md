---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedMlflowTrackingServerUrl.html
---

# CreatePresignedMlflowTrackingServerUrl
<a name="API_CreatePresignedMlflowTrackingServerUrl"></a>

Returns a presigned URL that you can use to connect to the MLflow UI attached to your tracking server. For more information, see [Launch the MLflow UI using a presigned URL](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-launch-ui.html).

## Request Syntax
<a name="API_CreatePresignedMlflowTrackingServerUrl_RequestSyntax"></a>

```
{
   "ExpiresInSeconds": {{number}},
   "SessionExpirationDurationInSeconds": {{number}},
   "TrackingServerName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreatePresignedMlflowTrackingServerUrl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExpiresInSeconds](#API_CreatePresignedMlflowTrackingServerUrl_RequestSyntax) **   <a name="sagemaker-CreatePresignedMlflowTrackingServerUrl-request-ExpiresInSeconds"></a>
The duration in seconds that your presigned URL is valid. The presigned URL can be used only once.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 300.
Required: No

 ** [SessionExpirationDurationInSeconds](#API_CreatePresignedMlflowTrackingServerUrl_RequestSyntax) **   <a name="sagemaker-CreatePresignedMlflowTrackingServerUrl-request-SessionExpirationDurationInSeconds"></a>
The duration in seconds that your MLflow UI session is valid.
Type: Integer
Valid Range: Minimum value of 1800. Maximum value of 43200.
Required: No

 ** [TrackingServerName](#API_CreatePresignedMlflowTrackingServerUrl_RequestSyntax) **   <a name="sagemaker-CreatePresignedMlflowTrackingServerUrl-request-TrackingServerName"></a>
The name of the tracking server to connect to your MLflow UI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: Yes

## Response Syntax
<a name="API_CreatePresignedMlflowTrackingServerUrl_ResponseSyntax"></a>

```
{
   "AuthorizedUrl": "string"
}
```

## Response Elements
<a name="API_CreatePresignedMlflowTrackingServerUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthorizedUrl](#API_CreatePresignedMlflowTrackingServerUrl_ResponseSyntax) **   <a name="sagemaker-CreatePresignedMlflowTrackingServerUrl-response-AuthorizedUrl"></a>
A presigned URL with an authorization token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_CreatePresignedMlflowTrackingServerUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreatePresignedMlflowTrackingServerUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreatePresignedMlflowTrackingServerUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreatePresignedMlflowTrackingServerUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreatePresignedMlflowTrackingServerUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreatePresignedMlflowTrackingServerUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreatePresignedMlflowTrackingServerUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreatePresignedMlflowTrackingServerUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreatePresignedMlflowTrackingServerUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreatePresignedMlflowTrackingServerUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreatePresignedMlflowTrackingServerUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreatePresignedMlflowTrackingServerUrl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
