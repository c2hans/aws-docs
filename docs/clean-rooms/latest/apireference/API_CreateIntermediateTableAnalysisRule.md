---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateIntermediateTableAnalysisRule.html
---

# CreateIntermediateTableAnalysisRule
<a name="API_CreateIntermediateTableAnalysisRule"></a>

Creates an analysis rule for an intermediate table. Only the CUSTOM analysis rule type is supported. Only the intermediate table owner can call this operation.

## Request Syntax
<a name="API_CreateIntermediateTableAnalysisRule_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/intermediateTables/{{intermediateTableIdentifier}}/analysisRule HTTP/1.1
Content-type: application/json

{
   "analysisRulePolicy": { ... },
   "analysisRuleType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateIntermediateTableAnalysisRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [intermediateTableIdentifier](#API_CreateIntermediateTableAnalysisRule_RequestSyntax) **   <a name="API-CreateIntermediateTableAnalysisRule-request-uri-intermediateTableIdentifier"></a>
The unique identifier of the intermediate table for which to create the analysis rule.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [membershipIdentifier](#API_CreateIntermediateTableAnalysisRule_RequestSyntax) **   <a name="API-CreateIntermediateTableAnalysisRule-request-uri-membershipIdentifier"></a>
The unique identifier of the membership that contains the intermediate table.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_CreateIntermediateTableAnalysisRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [analysisRulePolicy](#API_CreateIntermediateTableAnalysisRule_RequestSyntax) **   <a name="API-CreateIntermediateTableAnalysisRule-request-analysisRulePolicy"></a>
The analysis rule policy to apply to the intermediate table.
Type: [IntermediateTableAnalysisRulePolicy](API_IntermediateTableAnalysisRulePolicy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [analysisRuleType](#API_CreateIntermediateTableAnalysisRule_RequestSyntax) **   <a name="API-CreateIntermediateTableAnalysisRule-request-analysisRuleType"></a>
The type of analysis rule to create. Currently, only `CUSTOM` is supported.
Type: String
Valid Values: `CUSTOM`
Required: Yes

## Response Syntax
<a name="API_CreateIntermediateTableAnalysisRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "analysisRule": {
      "analysisRulePolicy": { ... },
      "analysisRuleType": "string",
      "createTime": number,
      "intermediateTableArn": "string",
      "intermediateTableIdentifier": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_CreateIntermediateTableAnalysisRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analysisRule](#API_CreateIntermediateTableAnalysisRule_ResponseSyntax) **   <a name="API-CreateIntermediateTableAnalysisRule-response-analysisRule"></a>
The analysis rule that was created for the intermediate table.
Type: [IntermediateTableAnalysisRule](API_IntermediateTableAnalysisRule.md) object

## Errors
<a name="API_CreateIntermediateTableAnalysisRule_Errors"></a>

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
<a name="API_CreateIntermediateTableAnalysisRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/CreateIntermediateTableAnalysisRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/CreateIntermediateTableAnalysisRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CreateIntermediateTableAnalysisRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/CreateIntermediateTableAnalysisRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CreateIntermediateTableAnalysisRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/CreateIntermediateTableAnalysisRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/CreateIntermediateTableAnalysisRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/CreateIntermediateTableAnalysisRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/CreateIntermediateTableAnalysisRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CreateIntermediateTableAnalysisRule)
