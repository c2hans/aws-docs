---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_GetSignedBluinsightsUrl.html
---

# GetSignedBluinsightsUrl
<a name="API_GetSignedBluinsightsUrl"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Gets a single sign-on URL that can be used to connect to AWS Blu Insights.

## Request Syntax
<a name="API_GetSignedBluinsightsUrl_RequestSyntax"></a>

```
GET /signed-bi-url HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSignedBluinsightsUrl_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetSignedBluinsightsUrl_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSignedBluinsightsUrl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "signedBiUrl": "string"
}
```

## Response Elements
<a name="API_GetSignedBluinsightsUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [signedBiUrl](#API_GetSignedBluinsightsUrl_ResponseSyntax) **   <a name="m2-GetSignedBluinsightsUrl-response-signedBiUrl"></a>
Single sign-on AWS Blu Insights URL.
Type: String

## Errors
<a name="API_GetSignedBluinsightsUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The number of requests made exceeds the limit.
 ** quotaCode **
The identifier of the throttled request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The identifier of the service that the throttled request was made to.
HTTP Status Code: 429

## See Also
<a name="API_GetSignedBluinsightsUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/GetSignedBluinsightsUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/GetSignedBluinsightsUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/GetSignedBluinsightsUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/GetSignedBluinsightsUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/GetSignedBluinsightsUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/GetSignedBluinsightsUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/GetSignedBluinsightsUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/GetSignedBluinsightsUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/GetSignedBluinsightsUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/GetSignedBluinsightsUrl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
