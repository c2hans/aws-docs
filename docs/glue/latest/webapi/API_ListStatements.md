---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListStatements.html
---

# ListStatements
<a name="API_ListStatements"></a>

Lists statements for the session.

## Request Syntax
<a name="API_ListStatements_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}",
   "RequestOrigin": "{{string}}",
   "SessionId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListStatements_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NextToken](#API_ListStatements_RequestSyntax) **   <a name="Glue-ListStatements-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Length Constraints: Maximum length of 400000.
Required: No

 ** [RequestOrigin](#API_ListStatements_RequestSyntax) **   <a name="Glue-ListStatements-request-RequestOrigin"></a>
The origin of the request to list statements.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** [SessionId](#API_ListStatements_RequestSyntax) **   <a name="Glue-ListStatements-request-SessionId"></a>
The Session ID of the statements.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_ListStatements_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Statements": [
      {
         "Code": "string",
         "CompletedOn": number,
         "Id": number,
         "Output": {
            "Data": {
               "TextPlain": "string"
            },
            "ErrorName": "string",
            "ErrorValue": "string",
            "ExecutionCount": number,
            "Status": "string",
            "Traceback": [ "string" ]
         },
         "Progress": number,
         "StartedOn": number,
         "State": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStatements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListStatements_ResponseSyntax) **   <a name="Glue-ListStatements-response-NextToken"></a>
A continuation token, if not all statements have yet been returned.
Type: String
Length Constraints: Maximum length of 400000.

 ** [Statements](#API_ListStatements_ResponseSyntax) **   <a name="Glue-ListStatements-response-Statements"></a>
Returns the list of statements.
Type: Array of [Statement](API_Statement.md) objects

## Errors
<a name="API_ListStatements_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** IllegalSessionStateException **
The session is in an invalid state to perform a requested operation.
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
<a name="API_ListStatements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListStatements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListStatements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListStatements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListStatements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListStatements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListStatements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListStatements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListStatements)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListStatements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListStatements)
