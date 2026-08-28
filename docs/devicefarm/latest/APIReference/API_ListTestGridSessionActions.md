---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTestGridSessionActions.html
---

# ListTestGridSessionActions
<a name="API_ListTestGridSessionActions"></a>

Returns a list of the actions taken in a [TestGridSession](API_TestGridSession.md).

## Request Syntax
<a name="API_ListTestGridSessionActions_RequestSyntax"></a>

```
{
   "maxResult": {{number}},
   "nextToken": "{{string}}",
   "sessionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTestGridSessionActions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResult](#API_ListTestGridSessionActions_RequestSyntax) **   <a name="devicefarm-ListTestGridSessionActions-request-maxResult"></a>
The maximum number of sessions to return per response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListTestGridSessionActions_RequestSyntax) **   <a name="devicefarm-ListTestGridSessionActions-request-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

 ** [sessionArn](#API_ListTestGridSessionActions_RequestSyntax) **   <a name="devicefarm-ListTestGridSessionActions-request-sessionArn"></a>
The ARN of the session to retrieve.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

## Response Syntax
<a name="API_ListTestGridSessionActions_ResponseSyntax"></a>

```
{
   "actions": [
      {
         "action": "string",
         "duration": number,
         "requestMethod": "string",
         "started": number,
         "statusCode": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListTestGridSessionActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actions](#API_ListTestGridSessionActions_ResponseSyntax) **   <a name="devicefarm-ListTestGridSessionActions-response-actions"></a>
The action taken by the session.
Type: Array of [TestGridSessionAction](API_TestGridSessionAction.md) objects

 ** [nextToken](#API_ListTestGridSessionActions_ResponseSyntax) **   <a name="devicefarm-ListTestGridSessionActions-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

## Errors
<a name="API_ListTestGridSessionActions_Errors"></a>

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
<a name="API_ListTestGridSessionActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListTestGridSessionActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListTestGridSessionActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListTestGridSessionActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListTestGridSessionActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListTestGridSessionActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListTestGridSessionActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListTestGridSessionActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListTestGridSessionActions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListTestGridSessionActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListTestGridSessionActions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
