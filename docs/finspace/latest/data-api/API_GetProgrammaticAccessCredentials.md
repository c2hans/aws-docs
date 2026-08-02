---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_GetProgrammaticAccessCredentials.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# GetProgrammaticAccessCredentials
<a name="API_GetProgrammaticAccessCredentials"></a>

Request programmatic credentials to use with FinSpace SDK. For more information, see [Step 2. Access credentials programmatically using IAM access key id and secret access key](https://docs.aws.amazon.com/finspace/latest/data-api/fs-using-the-finspace-api.html#accessing-credentials).

## Request Syntax
<a name="API_GetProgrammaticAccessCredentials_RequestSyntax"></a>

```
GET /credentials/programmatic?durationInMinutes={{durationInMinutes}}&environmentId={{environmentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetProgrammaticAccessCredentials_RequestParameters"></a>

The request uses the following URI parameters.

 ** [durationInMinutes](#API_GetProgrammaticAccessCredentials_RequestSyntax) **   <a name="finspace-GetProgrammaticAccessCredentials-request-uri-durationInMinutes"></a>
The time duration in which the credentials remain valid.
Valid Range: Minimum value of 1. Maximum value of 60.

 ** [environmentId](#API_GetProgrammaticAccessCredentials_RequestSyntax) **   <a name="finspace-GetProgrammaticAccessCredentials-request-uri-environmentId"></a>
The FinSpace environment identifier.
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: Yes

## Request Body
<a name="API_GetProgrammaticAccessCredentials_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetProgrammaticAccessCredentials_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "credentials": {
      "accessKeyId": "string",
      "secretAccessKey": "string",
      "sessionToken": "string"
   },
   "durationInMinutes": number
}
```

## Response Elements
<a name="API_GetProgrammaticAccessCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [credentials](#API_GetProgrammaticAccessCredentials_ResponseSyntax) **   <a name="finspace-GetProgrammaticAccessCredentials-response-credentials"></a>
Returns the programmatic credentials.
Type: [Credentials](API_Credentials.md) object

 ** [durationInMinutes](#API_GetProgrammaticAccessCredentials_ResponseSyntax) **   <a name="finspace-GetProgrammaticAccessCredentials-response-durationInMinutes"></a>
Returns the duration in which the credentials will remain valid.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 60.

## Errors
<a name="API_GetProgrammaticAccessCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetProgrammaticAccessCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/GetProgrammaticAccessCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/GetProgrammaticAccessCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/GetProgrammaticAccessCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/GetProgrammaticAccessCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/GetProgrammaticAccessCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/GetProgrammaticAccessCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/GetProgrammaticAccessCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/GetProgrammaticAccessCredentials)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/GetProgrammaticAccessCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/GetProgrammaticAccessCredentials)
