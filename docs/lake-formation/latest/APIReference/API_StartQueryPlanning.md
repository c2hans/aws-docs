---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_StartQueryPlanning.html
---

# StartQueryPlanning
<a name="API_StartQueryPlanning"></a>

Submits a request to process a query statement.

This operation generates work units that can be retrieved with the `GetWorkUnits` operation as soon as the query state is WORKUNITS\_AVAILABLE or FINISHED.

## Request Syntax
<a name="API_StartQueryPlanning_RequestSyntax"></a>

```
POST /StartQueryPlanning HTTP/1.1
Content-type: application/json

{
   "QueryPlanningContext": {
      "CatalogId": "{{string}}",
      "DatabaseName": "{{string}}",
      "QueryAsOfTime": {{number}},
      "QueryParameters": {
         "{{string}}" : "{{string}}"
      },
      "TransactionId": "{{string}}"
   },
   "QueryString": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartQueryPlanning_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartQueryPlanning_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [QueryPlanningContext](#API_StartQueryPlanning_RequestSyntax) **   <a name="lakeformation-StartQueryPlanning-request-QueryPlanningContext"></a>
A structure containing information about the query plan.
Type: [QueryPlanningContext](API_QueryPlanningContext.md) object
Required: Yes

 ** [QueryString](#API_StartQueryPlanning_RequestSyntax) **   <a name="lakeformation-StartQueryPlanning-request-QueryString"></a>
A PartiQL query statement used as an input to the planner service.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## Response Syntax
<a name="API_StartQueryPlanning_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "QueryId": "string"
}
```

## Response Elements
<a name="API_StartQueryPlanning_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QueryId](#API_StartQueryPlanning_ResponseSyntax) **   <a name="lakeformation-StartQueryPlanning-response-QueryId"></a>
The ID of the plan query operation can be used to fetch the actual work unit descriptors that are produced as the result of the operation. The ID is also used to get the query state and as an input to the `Execute` operation.
Type: String

## Errors
<a name="API_StartQueryPlanning_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ThrottledException **
Contains details about an error where the query request was throttled.
 ** Message **
A message describing the error.
HTTP Status Code: 429

## See Also
<a name="API_StartQueryPlanning_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/StartQueryPlanning)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/StartQueryPlanning)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/StartQueryPlanning)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/StartQueryPlanning)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/StartQueryPlanning)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/StartQueryPlanning)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/StartQueryPlanning)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/StartQueryPlanning)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/StartQueryPlanning)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/StartQueryPlanning)
