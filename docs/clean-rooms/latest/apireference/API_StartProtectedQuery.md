---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_StartProtectedQuery.html
---

# StartProtectedQuery
<a name="API_StartProtectedQuery"></a>

Creates a protected query that is started by AWS Clean Rooms.

## Request Syntax
<a name="API_StartProtectedQuery_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/protectedQueries HTTP/1.1
Content-type: application/json

{
   "computeConfiguration": { ... },
   "queryComputePayerAccountId": "{{string}}",
   "resultConfiguration": {
      "outputConfiguration": { ... }
   },
   "sqlParameters": {
      "analysisTemplateArn": "{{string}}",
      "parameters": {
         "{{string}}" : "{{string}}"
      },
      "queryString": "{{string}}"
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartProtectedQuery_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_StartProtectedQuery_RequestSyntax) **   <a name="API-StartProtectedQuery-request-uri-membershipIdentifier"></a>
A unique identifier for the membership to run this query against. Currently accepts a membership ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_StartProtectedQuery_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [computeConfiguration](#API_StartProtectedQuery_RequestSyntax) **   <a name="API-StartProtectedQuery-request-computeConfiguration"></a>
 The compute configuration for the protected query.
Type: [ComputeConfiguration](API_ComputeConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [queryComputePayerAccountId](#API_StartProtectedQuery_RequestSyntax) **   <a name="API-StartProtectedQuery-request-queryComputePayerAccountId"></a>
The account ID of the member that pays for the query compute costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** [resultConfiguration](#API_StartProtectedQuery_RequestSyntax) **   <a name="API-StartProtectedQuery-request-resultConfiguration"></a>
The details needed to write the query results.
Type: [ProtectedQueryResultConfiguration](API_ProtectedQueryResultConfiguration.md) object
Required: No

 ** [sqlParameters](#API_StartProtectedQuery_RequestSyntax) **   <a name="API-StartProtectedQuery-request-sqlParameters"></a>
The protected SQL query parameters.
Type: [ProtectedQuerySQLParameters](API_ProtectedQuerySQLParameters.md) object
Required: Yes

 ** [type](#API_StartProtectedQuery_RequestSyntax) **   <a name="API-StartProtectedQuery-request-type"></a>
The type of the protected query to be started.
Type: String
Valid Values: `SQL`
Required: Yes

## Response Syntax
<a name="API_StartProtectedQuery_ResponseSyntax"></a>

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
<a name="API_StartProtectedQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [protectedQuery](#API_StartProtectedQuery_ResponseSyntax) **   <a name="API-StartProtectedQuery-response-protectedQuery"></a>
The protected query.
Type: [ProtectedQuery](API_ProtectedQuery.md) object

## Errors
<a name="API_StartProtectedQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

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
<a name="API_StartProtectedQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/StartProtectedQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/StartProtectedQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/StartProtectedQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/StartProtectedQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/StartProtectedQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/StartProtectedQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/StartProtectedQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/StartProtectedQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/StartProtectedQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/StartProtectedQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
