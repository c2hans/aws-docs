---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetTestGridSession.html
---

# GetTestGridSession
<a name="API_GetTestGridSession"></a>

A session is an instance of a browser created through a `RemoteWebDriver` with the URL from [CreateTestGridUrl:url](API_CreateTestGridUrl.md#devicefarm-CreateTestGridUrl-response-url). You can use the following to look up sessions:
+ The session ARN ([GetTestGridSession:sessionArn](#devicefarm-GetTestGridSession-request-sessionArn)).
+ The project ARN and a session ID ([GetTestGridSession:projectArn](#devicefarm-GetTestGridSession-request-projectArn) and [GetTestGridSession:sessionId](#devicefarm-GetTestGridSession-request-sessionId)).

## Request Syntax
<a name="API_GetTestGridSession_RequestSyntax"></a>

```
{
   "projectArn": "{{string}}",
   "sessionArn": "{{string}}",
   "sessionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTestGridSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [projectArn](#API_GetTestGridSession_RequestSyntax) **   <a name="devicefarm-GetTestGridSession-request-projectArn"></a>
The ARN for the project that this session belongs to. See [CreateTestGridProject](API_CreateTestGridProject.md) and [ListTestGridProjects](API_ListTestGridProjects.md).
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** [sessionArn](#API_GetTestGridSession_RequestSyntax) **   <a name="devicefarm-GetTestGridSession-request-sessionArn"></a>
An ARN that uniquely identifies a [TestGridSession](API_TestGridSession.md).
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** [sessionId](#API_GetTestGridSession_RequestSyntax) **   <a name="devicefarm-GetTestGridSession-request-sessionId"></a>
An ID associated with this session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_GetTestGridSession_ResponseSyntax"></a>

```
{
   "testGridSession": {
      "arn": "string",
      "billingMinutes": number,
      "created": number,
      "ended": number,
      "seleniumProperties": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_GetTestGridSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [testGridSession](#API_GetTestGridSession_ResponseSyntax) **   <a name="devicefarm-GetTestGridSession-response-testGridSession"></a>
The [TestGridSession](API_TestGridSession.md) that was requested.
Type: [TestGridSession](API_TestGridSession.md) object

## Errors
<a name="API_GetTestGridSession_Errors"></a>

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
<a name="API_GetTestGridSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/GetTestGridSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/GetTestGridSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/GetTestGridSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/GetTestGridSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/GetTestGridSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/GetTestGridSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/GetTestGridSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/GetTestGridSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/GetTestGridSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/GetTestGridSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
