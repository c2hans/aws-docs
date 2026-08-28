---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListControlOperations.html
---

# ListControlOperations
<a name="API_ListControlOperations"></a>

Provides a list of operations in progress or queued. For usage examples, see [ListControlOperation examples](https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html#list-control-operations-api-examples).

## Request Syntax
<a name="API_ListControlOperations_RequestSyntax"></a>

```
POST /list-control-operations HTTP/1.1
Content-type: application/json

{
   "filter": {
      "controlIdentifiers": [ "{{string}}" ],
      "controlOperationTypes": [ "{{string}}" ],
      "enabledControlIdentifiers": [ "{{string}}" ],
      "statuses": [ "{{string}}" ],
      "targetIdentifiers": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListControlOperations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListControlOperations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListControlOperations_RequestSyntax) **   <a name="controltower-ListControlOperations-request-filter"></a>
An input filter for the `ListControlOperations` API that lets you select the types of control operations to view.
Type: [ControlOperationFilter](API_ControlOperationFilter.md) object
Required: No

 ** [maxResults](#API_ListControlOperations_RequestSyntax) **   <a name="controltower-ListControlOperations-request-maxResults"></a>
The maximum number of results to be shown.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListControlOperations_RequestSyntax) **   <a name="controltower-ListControlOperations-request-nextToken"></a>
A pagination token.
Type: String
Pattern: `.*\S+.*`
Required: No

## Response Syntax
<a name="API_ListControlOperations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "controlOperations": [
      {
         "controlIdentifier": "string",
         "enabledControlIdentifier": "string",
         "endTime": "string",
         "operationIdentifier": "string",
         "operationType": "string",
         "startTime": "string",
         "status": "string",
         "statusMessage": "string",
         "targetIdentifier": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListControlOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [controlOperations](#API_ListControlOperations_ResponseSyntax) **   <a name="controltower-ListControlOperations-response-controlOperations"></a>
Returns a list of output from control operations.
Type: Array of [ControlOperationSummary](API_ControlOperationSummary.md) objects

 ** [nextToken](#API_ListControlOperations_ResponseSyntax) **   <a name="controltower-ListControlOperations-response-nextToken"></a>
A pagination token.
Type: String
Pattern: `.*\S+.*`

## Errors
<a name="API_ListControlOperations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during processing of a request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListControlOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/ListControlOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/ListControlOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/ListControlOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/ListControlOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/ListControlOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/ListControlOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/ListControlOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/ListControlOperations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListControlOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/ListControlOperations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
