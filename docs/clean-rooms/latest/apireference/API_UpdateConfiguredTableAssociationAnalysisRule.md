---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateConfiguredTableAssociationAnalysisRule.html
---

# UpdateConfiguredTableAssociationAnalysisRule
<a name="API_UpdateConfiguredTableAssociationAnalysisRule"></a>

 Updates the analysis rule for a configured table association.

## Request Syntax
<a name="API_UpdateConfiguredTableAssociationAnalysisRule_RequestSyntax"></a>

```
PATCH /memberships/{{membershipIdentifier}}/configuredTableAssociations/{{configuredTableAssociationIdentifier}}/analysisRule/{{analysisRuleType}} HTTP/1.1
Content-type: application/json

{
   "analysisRulePolicy": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateConfiguredTableAssociationAnalysisRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [analysisRuleType](#API_UpdateConfiguredTableAssociationAnalysisRule_RequestSyntax) **   <a name="API-UpdateConfiguredTableAssociationAnalysisRule-request-uri-analysisRuleType"></a>
 The analysis rule type that you want to update.
Valid Values: `AGGREGATION | LIST | CUSTOM`
Required: Yes

 ** [configuredTableAssociationIdentifier](#API_UpdateConfiguredTableAssociationAnalysisRule_RequestSyntax) **   <a name="API-UpdateConfiguredTableAssociationAnalysisRule-request-uri-configuredTableAssociationIdentifier"></a>
 The identifier for the configured table association to update.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [membershipIdentifier](#API_UpdateConfiguredTableAssociationAnalysisRule_RequestSyntax) **   <a name="API-UpdateConfiguredTableAssociationAnalysisRule-request-uri-membershipIdentifier"></a>
 A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_UpdateConfiguredTableAssociationAnalysisRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [analysisRulePolicy](#API_UpdateConfiguredTableAssociationAnalysisRule_RequestSyntax) **   <a name="API-UpdateConfiguredTableAssociationAnalysisRule-request-analysisRulePolicy"></a>
 The updated analysis rule policy for the conﬁgured table association.
Type: [ConfiguredTableAssociationAnalysisRulePolicy](API_ConfiguredTableAssociationAnalysisRulePolicy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_UpdateConfiguredTableAssociationAnalysisRule_ResponseSyntax"></a>

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
<a name="API_UpdateConfiguredTableAssociationAnalysisRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analysisRule](#API_UpdateConfiguredTableAssociationAnalysisRule_ResponseSyntax) **   <a name="API-UpdateConfiguredTableAssociationAnalysisRule-response-analysisRule"></a>
 The updated analysis rule for the conﬁgured table association. In the console, the `ConfiguredTableAssociationAnalysisRule` is referred to as the *collaboration analysis rule*.
Type: [ConfiguredTableAssociationAnalysisRule](API_ConfiguredTableAssociationAnalysisRule.md) object

## Errors
<a name="API_UpdateConfiguredTableAssociationAnalysisRule_Errors"></a>

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
<a name="API_UpdateConfiguredTableAssociationAnalysisRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/UpdateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/UpdateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/UpdateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/UpdateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/UpdateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/UpdateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/UpdateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/UpdateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/UpdateConfiguredTableAssociationAnalysisRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/UpdateConfiguredTableAssociationAnalysisRule)
