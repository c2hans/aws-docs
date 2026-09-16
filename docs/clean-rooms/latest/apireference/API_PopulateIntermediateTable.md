---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PopulateIntermediateTable.html
---

# PopulateIntermediateTable
<a name="API_PopulateIntermediateTable"></a>

Runs the stored query of an intermediate table and makes the results available for querying. Each call creates a new version. Use `GetProtectedQuery` with the returned analysis ID to track progress. Only the intermediate table owner can call this operation.

## Request Syntax
<a name="API_PopulateIntermediateTable_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/intermediateTables/{{intermediateTableIdentifier}}/populate HTTP/1.1
Content-type: application/json

{
   "analysisPayerAccountId": "{{string}}",
   "computeConfiguration": { ... },
   "parameters": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_PopulateIntermediateTable_RequestParameters"></a>

The request uses the following URI parameters.

 ** [intermediateTableIdentifier](#API_PopulateIntermediateTable_RequestSyntax) **   <a name="API-PopulateIntermediateTable-request-uri-intermediateTableIdentifier"></a>
The unique identifier of the intermediate table to populate.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [membershipIdentifier](#API_PopulateIntermediateTable_RequestSyntax) **   <a name="API-PopulateIntermediateTable-request-uri-membershipIdentifier"></a>
The unique identifier of the membership that contains the intermediate table.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_PopulateIntermediateTable_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [analysisPayerAccountId](#API_PopulateIntermediateTable_RequestSyntax) **   <a name="API-PopulateIntermediateTable-request-analysisPayerAccountId"></a>
The account ID of the member that pays for the analysis compute costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** [computeConfiguration](#API_PopulateIntermediateTable_RequestSyntax) **   <a name="API-PopulateIntermediateTable-request-computeConfiguration"></a>
The compute configuration for the population query execution.
Type: [IntermediateTableComputeConfiguration](API_IntermediateTableComputeConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [parameters](#API_PopulateIntermediateTable_RequestSyntax) **   <a name="API-PopulateIntermediateTable-request-parameters"></a>
The runtime parameter values that override the defaults in the stored query.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[0-9a-zA-Z_]+`
Value Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## Response Syntax
<a name="API_PopulateIntermediateTable_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "analysisId": "string",
   "analysisType": "string",
   "versionId": "string"
}
```

## Response Elements
<a name="API_PopulateIntermediateTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analysisId](#API_PopulateIntermediateTable_ResponseSyntax) **   <a name="API-PopulateIntermediateTable-response-analysisId"></a>
The identifier for the protected query execution that populated the intermediate table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [analysisType](#API_PopulateIntermediateTable_ResponseSyntax) **   <a name="API-PopulateIntermediateTable-response-analysisType"></a>
The type of analysis performed to populate the intermediate table.
Type: String
Valid Values: `QUERY`

 ** [versionId](#API_PopulateIntermediateTable_ResponseSyntax) **   <a name="API-PopulateIntermediateTable-response-versionId"></a>
The unique identifier of the version created by this population operation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_PopulateIntermediateTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** reason **
A reason code for the exception.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request denied because service quota has been exceeded.
 ** quotaName **
The name of the quota.
 ** quotaValue **
The value of the quota.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_PopulateIntermediateTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/PopulateIntermediateTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/PopulateIntermediateTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PopulateIntermediateTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/PopulateIntermediateTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PopulateIntermediateTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/PopulateIntermediateTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/PopulateIntermediateTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/PopulateIntermediateTable)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/PopulateIntermediateTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PopulateIntermediateTable)
