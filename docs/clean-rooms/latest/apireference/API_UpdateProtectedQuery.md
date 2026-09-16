---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateProtectedQuery.html
---

# UpdateProtectedQuery
<a name="API_UpdateProtectedQuery"></a>

Updates the processing of a currently running query.

## Request Syntax
<a name="API_UpdateProtectedQuery_RequestSyntax"></a>

```
PATCH /memberships/{{membershipIdentifier}}/protectedQueries/{{protectedQueryIdentifier}} HTTP/1.1
Content-type: application/json

{
   "targetStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateProtectedQuery_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_UpdateProtectedQuery_RequestSyntax) **   <a name="API-UpdateProtectedQuery-request-uri-membershipIdentifier"></a>
The identifier for a member of a protected query instance.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [protectedQueryIdentifier](#API_UpdateProtectedQuery_RequestSyntax) **   <a name="API-UpdateProtectedQuery-request-uri-protectedQueryIdentifier"></a>
The identifier for a protected query instance.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_UpdateProtectedQuery_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [targetStatus](#API_UpdateProtectedQuery_RequestSyntax) **   <a name="API-UpdateProtectedQuery-request-targetStatus"></a>
The target status of a query. Used to update the execution status of a currently running query.
Type: String
Valid Values: `CANCELLED`
Required: Yes

## Response Syntax
<a name="API_UpdateProtectedQuery_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "protectedQuery": {
      "computeConfiguration": { ... },
      "createTime": number,
      "differentialPrivacy": {
         "sensitivityParameters": [
            {
               "aggregationExpression": "string",
               "aggregationType": "string",
               "maxColumnValue": number,
               "minColumnValue": number,
               "userContributionLimit": number
            }
         ]
      },
      "error": {
         "code": "string",
         "message": "string"
      },
      "id": "string",
      "membershipArn": "string",
      "membershipId": "string",
      "queryComputePayerAccountId": "string",
      "result": {
         "output": { ... }
      },
      "resultConfiguration": {
         "outputConfiguration": { ... }
      },
      "sqlParameters": {
         "analysisTemplateArn": "string",
         "parameters": {
            "string" : "string"
         },
         "queryString": "string"
      },
      "statistics": {
         "billedResourceUtilization": {
            "units": number
         },
         "totalDurationInMillis": number
      },
      "status": "string"
   }
}
```

## Response Elements
<a name="API_UpdateProtectedQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [protectedQuery](#API_UpdateProtectedQuery_ResponseSyntax) **   <a name="API-UpdateProtectedQuery-response-protectedQuery"></a>
The protected query output.
Type: [ProtectedQuery](API_ProtectedQuery.md) object

## Errors
<a name="API_UpdateProtectedQuery_Errors"></a>

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
<a name="API_UpdateProtectedQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/UpdateProtectedQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/UpdateProtectedQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/UpdateProtectedQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/UpdateProtectedQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/UpdateProtectedQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/UpdateProtectedQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/UpdateProtectedQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/UpdateProtectedQuery)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/UpdateProtectedQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/UpdateProtectedQuery)
