---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateConfiguredTableAnalysisRule.html
---

# CreateConfiguredTableAnalysisRule
<a name="API_CreateConfiguredTableAnalysisRule"></a>

Creates a new analysis rule for a configured table. Currently, only one analysis rule can be created for a given configured table.

## Request Syntax
<a name="API_CreateConfiguredTableAnalysisRule_RequestSyntax"></a>

```
POST /configuredTables/{{configuredTableIdentifier}}/analysisRule HTTP/1.1
Content-type: application/json

{
   "analysisRulePolicy": { ... },
   "analysisRuleType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateConfiguredTableAnalysisRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [configuredTableIdentifier](#API_CreateConfiguredTableAnalysisRule_RequestSyntax) **   <a name="API-CreateConfiguredTableAnalysisRule-request-uri-configuredTableIdentifier"></a>
The identifier for the configured table to create the analysis rule for. Currently accepts the configured table ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_CreateConfiguredTableAnalysisRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [analysisRulePolicy](#API_CreateConfiguredTableAnalysisRule_RequestSyntax) **   <a name="API-CreateConfiguredTableAnalysisRule-request-analysisRulePolicy"></a>
The analysis rule policy that was created for the configured table.
Type: [ConfiguredTableAnalysisRulePolicy](API_ConfiguredTableAnalysisRulePolicy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [analysisRuleType](#API_CreateConfiguredTableAnalysisRule_RequestSyntax) **   <a name="API-CreateConfiguredTableAnalysisRule-request-analysisRuleType"></a>
The type of analysis rule.
Type: String
Valid Values: `AGGREGATION | LIST | CUSTOM`
Required: Yes

## Response Syntax
<a name="API_CreateConfiguredTableAnalysisRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "analysisRule": {
      "configuredTableArn": "string",
      "configuredTableId": "string",
      "createTime": number,
      "policy": { ... },
      "type": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_CreateConfiguredTableAnalysisRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analysisRule](#API_CreateConfiguredTableAnalysisRule_ResponseSyntax) **   <a name="API-CreateConfiguredTableAnalysisRule-response-analysisRule"></a>
The analysis rule that was created for the configured table.
Type: [ConfiguredTableAnalysisRule](API_ConfiguredTableAnalysisRule.md) object

## Errors
<a name="API_CreateConfiguredTableAnalysisRule_Errors"></a>

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
<a name="API_CreateConfiguredTableAnalysisRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/CreateConfiguredTableAnalysisRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/CreateConfiguredTableAnalysisRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CreateConfiguredTableAnalysisRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/CreateConfiguredTableAnalysisRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CreateConfiguredTableAnalysisRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/CreateConfiguredTableAnalysisRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/CreateConfiguredTableAnalysisRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/CreateConfiguredTableAnalysisRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/CreateConfiguredTableAnalysisRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CreateConfiguredTableAnalysisRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
