---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListSessions.html
---

# ListSessions
<a name="API_ListSessions"></a>

Retrieve a list of sessions.

## Request Syntax
<a name="API_ListSessions_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RequestOrigin": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ListSessions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListSessions_RequestSyntax) **   <a name="Glue-ListSessions-request-MaxResults"></a>
The maximum number of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListSessions_RequestSyntax) **   <a name="Glue-ListSessions-request-NextToken"></a>
The token for the next set of results, or null if there are no more result.
Type: String
Length Constraints: Maximum length of 400000.
Required: No

 ** [RequestOrigin](#API_ListSessions_RequestSyntax) **   <a name="Glue-ListSessions-request-RequestOrigin"></a>
The origin of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** [Tags](#API_ListSessions_RequestSyntax) **   <a name="Glue-ListSessions-request-Tags"></a>
Tags belonging to the session.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_ListSessions_ResponseSyntax"></a>

```
{
   "Ids": [ "string" ],
   "NextToken": "string",
   "Sessions": [
      {
         "Command": {
            "Name": "string",
            "PythonVersion": "string"
         },
         "CompletedOn": number,
         "Connections": {
            "Connections": [ "string" ]
         },
         "CreatedOn": number,
         "DefaultArguments": {
            "string" : "string"
         },
         "Description": "string",
         "DPUSeconds": number,
         "ErrorMessage": "string",
         "ExecutionTime": number,
         "GlueVersion": "string",
         "Id": "string",
         "IdleTimeout": number,
         "MaxCapacity": number,
         "NumberOfWorkers": number,
         "ProfileName": "string",
         "Progress": number,
         "Role": "string",
         "SecurityConfiguration": "string",
         "Status": "string",
         "WorkerType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Ids](#API_ListSessions_ResponseSyntax) **   <a name="Glue-ListSessions-response-Ids"></a>
Returns the ID of the session.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [NextToken](#API_ListSessions_ResponseSyntax) **   <a name="Glue-ListSessions-response-NextToken"></a>
The token for the next set of results, or null if there are no more result.
Type: String
Length Constraints: Maximum length of 400000.

 ** [Sessions](#API_ListSessions_ResponseSyntax) **   <a name="Glue-ListSessions-response-Sessions"></a>
Returns the session object.
Type: Array of [Session](API_Session.md) objects

## Errors
<a name="API_ListSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListSessions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListSessions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
