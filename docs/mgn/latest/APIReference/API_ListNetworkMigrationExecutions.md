---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationExecutions.html
---

# ListNetworkMigrationExecutions
<a name="API_ListNetworkMigrationExecutions"></a>

Lists network migration execution instances for a given definition, showing the status and progress of each execution.

## Request Syntax
<a name="API_ListNetworkMigrationExecutions_RequestSyntax"></a>

```
POST /network-migration/ListNetworkMigrationExecutions HTTP/1.1
Content-type: application/json

{
   "filters": {
      "networkMigrationExecutionIDs": [ "{{string}}" ],
      "networkMigrationExecutionStatuses": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "networkMigrationDefinitionID": "{{string}}",
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListNetworkMigrationExecutions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListNetworkMigrationExecutions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListNetworkMigrationExecutions_RequestSyntax) **   <a name="mgn-ListNetworkMigrationExecutions-request-filters"></a>
Filters to apply when listing executions, such as status or execution ID.
Type: [ListNetworkMigrationExecutionRequestFilters](API_ListNetworkMigrationExecutionRequestFilters.md) object
Required: No

 ** [maxResults](#API_ListNetworkMigrationExecutions_RequestSyntax) **   <a name="mgn-ListNetworkMigrationExecutions-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [networkMigrationDefinitionID](#API_ListNetworkMigrationExecutions_RequestSyntax) **   <a name="mgn-ListNetworkMigrationExecutions-request-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition to list executions for.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: Yes

 ** [nextToken](#API_ListNetworkMigrationExecutions_RequestSyntax) **   <a name="mgn-ListNetworkMigrationExecutions-request-nextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListNetworkMigrationExecutions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "activity": "string",
         "createdAt": number,
         "networkMigrationDefinitionID": "string",
         "networkMigrationExecutionID": "string",
         "stage": "string",
         "status": "string",
         "tags": {
            "string" : "string"
         },
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListNetworkMigrationExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListNetworkMigrationExecutions_ResponseSyntax) **   <a name="mgn-ListNetworkMigrationExecutions-response-items"></a>
A list of network migration execution details.
Type: Array of [NetworkMigrationExecution](API_NetworkMigrationExecution.md) objects

 ** [nextToken](#API_ListNetworkMigrationExecutions_ResponseSyntax) **   <a name="mgn-ListNetworkMigrationExecutions-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListNetworkMigrationExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Operation denied due to a file permission or access check error.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

## See Also
<a name="API_ListNetworkMigrationExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/ListNetworkMigrationExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/ListNetworkMigrationExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListNetworkMigrationExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/ListNetworkMigrationExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListNetworkMigrationExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/ListNetworkMigrationExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/ListNetworkMigrationExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/ListNetworkMigrationExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/ListNetworkMigrationExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListNetworkMigrationExecutions)
