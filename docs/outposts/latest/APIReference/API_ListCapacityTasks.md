---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListCapacityTasks.html
---

# ListCapacityTasks
<a name="API_ListCapacityTasks"></a>

Lists the capacity tasks for your AWS account.

Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.

## Request Syntax
<a name="API_ListCapacityTasks_RequestSyntax"></a>

```
GET /capacity/tasks?CapacityTaskStatusFilter={{CapacityTaskStatusFilter}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&OutpostIdentifierFilter={{OutpostIdentifierFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCapacityTasks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CapacityTaskStatusFilter](#API_ListCapacityTasks_RequestSyntax) **   <a name="outposts-ListCapacityTasks-request-uri-CapacityTaskStatusFilter"></a>
A list of statuses. For example, `REQUESTED` or `WAITING_FOR_EVACUATION`.
Valid Values: `REQUESTED | IN_PROGRESS | FAILED | COMPLETED | WAITING_FOR_EVACUATION | CANCELLATION_IN_PROGRESS | CANCELLED`

 ** [MaxResults](#API_ListCapacityTasks_RequestSyntax) **   <a name="outposts-ListCapacityTasks-request-uri-MaxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListCapacityTasks_RequestSyntax) **   <a name="outposts-ListCapacityTasks-request-uri-NextToken"></a>
The pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [OutpostIdentifierFilter](#API_ListCapacityTasks_RequestSyntax) **   <a name="outposts-ListCapacityTasks-request-uri-OutpostIdentifierFilter"></a>
Filters the results by an Outpost ID or an Outpost ARN.
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`

## Request Body
<a name="API_ListCapacityTasks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCapacityTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CapacityTasks": [
      {
         "AssetId": "string",
         "CapacityTaskId": "string",
         "CapacityTaskStatus": "string",
         "CompletionDate": number,
         "CreationDate": number,
         "LastModifiedDate": number,
         "OrderId": "string",
         "OutpostId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCapacityTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CapacityTasks](#API_ListCapacityTasks_ResponseSyntax) **   <a name="outposts-ListCapacityTasks-response-CapacityTasks"></a>
Lists all the capacity tasks.
Type: Array of [CapacityTaskSummary](API_CapacityTaskSummary.md) objects

 ** [NextToken](#API_ListCapacityTasks_ResponseSyntax) **   <a name="outposts-ListCapacityTasks-response-NextToken"></a>
The pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

## Errors
<a name="API_ListCapacityTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListCapacityTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/ListCapacityTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/ListCapacityTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/ListCapacityTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/ListCapacityTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/ListCapacityTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/ListCapacityTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/ListCapacityTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/ListCapacityTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/ListCapacityTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/ListCapacityTasks)
