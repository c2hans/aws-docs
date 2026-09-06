---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateTestGridUrl.html
---

# CreateTestGridUrl
<a name="API_CreateTestGridUrl"></a>

Creates a signed, short-term URL that can be passed to a Selenium `RemoteWebDriver` constructor.

## Request Syntax
<a name="API_CreateTestGridUrl_RequestSyntax"></a>

```
{
   "expiresInSeconds": {{number}},
   "projectArn": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateTestGridUrl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [expiresInSeconds](#API_CreateTestGridUrl_RequestSyntax) **   <a name="devicefarm-CreateTestGridUrl-request-expiresInSeconds"></a>
Lifetime, in seconds, of the URL.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 86400.
Required: Yes

 ** [projectArn](#API_CreateTestGridUrl_RequestSyntax) **   <a name="devicefarm-CreateTestGridUrl-request-projectArn"></a>
ARN (from [CreateTestGridProject](API_CreateTestGridProject.md) or [ListTestGridProjects](API_ListTestGridProjects.md)) to associate with the short-term URL.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

## Response Syntax
<a name="API_CreateTestGridUrl_ResponseSyntax"></a>

```
{
   "expires": number,
   "url": "string"
}
```

## Response Elements
<a name="API_CreateTestGridUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [expires](#API_CreateTestGridUrl_ResponseSyntax) **   <a name="devicefarm-CreateTestGridUrl-response-expires"></a>
The number of seconds the URL from [CreateTestGridUrl:url](#devicefarm-CreateTestGridUrl-response-url) stays active.
Type: Timestamp

 ** [url](#API_CreateTestGridUrl_ResponseSyntax) **   <a name="devicefarm-CreateTestGridUrl-response-url"></a>
A signed URL, expiring in [CreateTestGridUrl:expiresInSeconds](#devicefarm-CreateTestGridUrl-request-expiresInSeconds) seconds, to be passed to a `RemoteWebDriver`.
Type: String

## Errors
<a name="API_CreateTestGridUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** InternalServiceException **
An internal exception was raised in the service. Contact [aws-devicefarm-support@amazon.com](mailto:aws-devicefarm-support@amazon.com) if you see this error.
HTTP Status Code: 500

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateTestGridUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/CreateTestGridUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/CreateTestGridUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/CreateTestGridUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/CreateTestGridUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/CreateTestGridUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/CreateTestGridUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/CreateTestGridUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/CreateTestGridUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/CreateTestGridUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/CreateTestGridUrl)
