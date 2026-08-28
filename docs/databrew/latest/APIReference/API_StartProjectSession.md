---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_StartProjectSession.html
---

# StartProjectSession
<a name="API_StartProjectSession"></a>

Creates an interactive session, enabling you to manipulate data in a DataBrew project.

## Request Syntax
<a name="API_StartProjectSession_RequestSyntax"></a>

```
PUT /projects/{{name}}/startProjectSession HTTP/1.1
Content-type: application/json

{
   "AssumeControl": {{boolean}}
}
```

## URI Request Parameters
<a name="API_StartProjectSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_StartProjectSession_RequestSyntax) **   <a name="databrew-StartProjectSession-request-uri-Name"></a>
The name of the project to act upon.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_StartProjectSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AssumeControl](#API_StartProjectSession_RequestSyntax) **   <a name="databrew-StartProjectSession-request-AssumeControl"></a>
A value that, if true, enables you to take control of a session, even if a different client is currently accessing the project.
Type: Boolean
Required: No

## Response Syntax
<a name="API_StartProjectSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ClientSessionId": "string",
   "Name": "string"
}
```

## Response Elements
<a name="API_StartProjectSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_StartProjectSession_ResponseSyntax) **   <a name="databrew-StartProjectSession-response-Name"></a>
The name of the project to be acted upon.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [ClientSessionId](#API_StartProjectSession_ResponseSyntax) **   <a name="databrew-StartProjectSession-response-ClientSessionId"></a>
A system-generated identifier for the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-]*$`

## Errors
<a name="API_StartProjectSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
A service quota is exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_StartProjectSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/StartProjectSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/StartProjectSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/StartProjectSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/StartProjectSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/StartProjectSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/StartProjectSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/StartProjectSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/StartProjectSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/StartProjectSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/StartProjectSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
