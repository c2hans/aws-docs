---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html
---

# CreateSink
<a name="API_CreateSink"></a>

Use this to create a *sink* in the current account, so that it can be used as a monitoring account in CloudWatch cross-account observability. A sink is a resource that represents an attachment point in a monitoring account. Source accounts can link to the sink to send observability data.

After you create a sink, you must create a sink policy that allows source accounts to attach to it. For more information, see [PutSinkPolicy](https://docs.aws.amazon.com/OAM/latest/APIReference/API_PutSinkPolicy.html).

Each account can contain one sink per Region. If you delete a sink, you can then create a new one in that Region.

## Request Syntax
<a name="API_CreateSink_RequestSyntax"></a>

```
POST /CreateSink HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSink_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSink_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_CreateSink_RequestSyntax) **   <a name="OAM-CreateSink-request-Name"></a>
A name for the sink.
Type: String
Pattern: `[a-zA-Z0-9_\.\-]{1,255}`
Required: Yes

 ** [Tags](#API_CreateSink_RequestSyntax) **   <a name="OAM-CreateSink-request-Tags"></a>
Assigns one or more tags (key-value pairs) to the link.
Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.
For more information about using tags to control access, see [Controlling access to Amazon Web Services resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html).
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateSink_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Id": "string",
   "Name": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateSink_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateSink_ResponseSyntax) **   <a name="OAM-CreateSink-response-Arn"></a>
The ARN of the sink that is newly created.
Type: String

 ** [Id](#API_CreateSink_ResponseSyntax) **   <a name="OAM-CreateSink-response-Id"></a>
The random ID string that AWS generated as part of the sink ARN.
Type: String

 ** [Name](#API_CreateSink_ResponseSyntax) **   <a name="OAM-CreateSink-response-Name"></a>
The name of the sink.
Type: String

 ** [Tags](#API_CreateSink_ResponseSyntax) **   <a name="OAM-CreateSink-response-Tags"></a>
The tags assigned to the sink.
Type: String to string map

## Errors
<a name="API_CreateSink_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
A resource was in an inconsistent state during an update or a deletion.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 409

 ** InternalServiceFault **
Unexpected error while processing the request. Retry the request.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 500

 ** InvalidParameterException **
A parameter is specified incorrectly.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 400

 ** MissingRequiredParameterException **
A required parameter is missing from the request.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 429

## See Also
<a name="API_CreateSink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/oam-2022-06-10/CreateSink)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/oam-2022-06-10/CreateSink)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/CreateSink)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/oam-2022-06-10/CreateSink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/CreateSink)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/oam-2022-06-10/CreateSink)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/oam-2022-06-10/CreateSink)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/oam-2022-06-10/CreateSink)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/oam-2022-06-10/CreateSink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/CreateSink)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Observability Access Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query OAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
