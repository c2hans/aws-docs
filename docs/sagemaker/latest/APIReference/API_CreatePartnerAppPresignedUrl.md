---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePartnerAppPresignedUrl.html
---

# CreatePartnerAppPresignedUrl
<a name="API_CreatePartnerAppPresignedUrl"></a>

Creates a presigned URL to access an Amazon SageMaker Partner AI App.

## Request Syntax
<a name="API_CreatePartnerAppPresignedUrl_RequestSyntax"></a>

```
{
   "Arn": "{{string}}",
   "ExpiresInSeconds": {{number}},
   "SessionExpirationDurationInSeconds": {{number}}
}
```

## Request Parameters
<a name="API_CreatePartnerAppPresignedUrl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Arn](#API_CreatePartnerAppPresignedUrl_RequestSyntax) **   <a name="sagemaker-CreatePartnerAppPresignedUrl-request-Arn"></a>
The ARN of the SageMaker Partner AI App to create the presigned URL for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:partner-app\/app-[A-Z0-9]{12}`
Required: Yes

 ** [ExpiresInSeconds](#API_CreatePartnerAppPresignedUrl_RequestSyntax) **   <a name="sagemaker-CreatePartnerAppPresignedUrl-request-ExpiresInSeconds"></a>
The time that will pass before the presigned URL expires.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 300.
Required: No

 ** [SessionExpirationDurationInSeconds](#API_CreatePartnerAppPresignedUrl_RequestSyntax) **   <a name="sagemaker-CreatePartnerAppPresignedUrl-request-SessionExpirationDurationInSeconds"></a>
Indicates how long the Amazon SageMaker Partner AI App session can be accessed for after logging in.
Type: Integer
Valid Range: Minimum value of 1800. Maximum value of 43200.
Required: No

## Response Syntax
<a name="API_CreatePartnerAppPresignedUrl_ResponseSyntax"></a>

```
{
   "Url": "string"
}
```

## Response Elements
<a name="API_CreatePartnerAppPresignedUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Url](#API_CreatePartnerAppPresignedUrl_ResponseSyntax) **   <a name="sagemaker-CreatePartnerAppPresignedUrl-response-Url"></a>
The presigned URL that you can use to access the SageMaker Partner AI App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_CreatePartnerAppPresignedUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreatePartnerAppPresignedUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreatePartnerAppPresignedUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreatePartnerAppPresignedUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreatePartnerAppPresignedUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreatePartnerAppPresignedUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreatePartnerAppPresignedUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreatePartnerAppPresignedUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreatePartnerAppPresignedUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreatePartnerAppPresignedUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreatePartnerAppPresignedUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreatePartnerAppPresignedUrl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
