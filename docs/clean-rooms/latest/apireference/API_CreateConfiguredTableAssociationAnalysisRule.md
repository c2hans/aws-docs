---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateConfiguredTableAssociationAnalysisRule.html
---

# CreateConfiguredTableAssociationAnalysisRule
<a name="API_CreateConfiguredTableAssociationAnalysisRule"></a>

 Creates a new analysis rule for an associated configured table.

## Request Syntax
<a name="API_CreateConfiguredTableAssociationAnalysisRule_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/configuredTableAssociations/{{configuredTableAssociationIdentifier}}/analysisRule HTTP/1.1
Content-type: application/json

{
   "analysisRulePolicy": { ... },
   "analysisRuleType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateConfiguredTableAssociationAnalysisRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [configuredTableAssociationIdentifier](#API_CreateConfiguredTableAssociationAnalysisRule_RequestSyntax) **   <a name="API-CreateConfiguredTableAssociationAnalysisRule-request-uri-configuredTableAssociationIdentifier"></a>
 The unique ID for the configured table association. Currently accepts the configured table association ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [membershipIdentifier](#API_CreateConfiguredTableAssociationAnalysisRule_RequestSyntax) **   <a name="API-CreateConfiguredTableAssociationAnalysisRule-request-uri-membershipIdentifier"></a>
 A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_CreateConfiguredTableAssociationAnalysisRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [analysisRulePolicy](#API_CreateConfiguredTableAssociationAnalysisRule_RequestSyntax) **   <a name="API-CreateConfiguredTableAssociationAnalysisRule-request-analysisRulePolicy"></a>
The analysis rule policy that was created for the configured table association.
Type: [ConfiguredTableAssociationAnalysisRulePolicy](API_ConfiguredTableAssociationAnalysisRulePolicy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [analysisRuleType](#API_CreateConfiguredTableAssociationAnalysisRule_RequestSyntax) **   <a name="API-CreateConfiguredTableAssociationAnalysisRule-request-analysisRuleType"></a>
 The type of analysis rule.
Type: String
Valid Values: `AGGREGATION | LIST | CUSTOM`
Required: Yes

## Response Syntax
<a name="API_CreateConfiguredTableAssociationAnalysisRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "analysisRule": {
      "configuredTableAssociationArn": "string",
      "configuredTableAssociationId": "string",
      "createTime": number,
      "membershipIdentifier": "string",
      "policy": { ... },
      "type": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_CreateConfiguredTableAssociationAnalysisRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analysisRule](#API_CreateConfiguredTableAssociationAnalysisRule_ResponseSyntax) **   <a name="API-CreateConfiguredTableAssociationAnalysisRule-response-analysisRule"></a>
The analysis rule for the conﬁgured table association. In the console, the `ConfiguredTableAssociationAnalysisRule` is referred to as the *collaboration analysis rule*.
Type: [ConfiguredTableAssociationAnalysisRule](API_ConfiguredTableAssociationAnalysisRule.md) object

## Errors
<a name="API_CreateConfiguredTableAssociationAnalysisRule_Errors"></a>

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
<a name="API_CreateConfiguredTableAssociationAnalysisRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/CreateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/CreateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CreateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/CreateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CreateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/CreateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/CreateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/CreateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/CreateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CreateConfiguredTableAssociationAnalysisRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
