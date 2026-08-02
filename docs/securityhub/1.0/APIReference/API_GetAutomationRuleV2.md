---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetAutomationRuleV2.html
---

# GetAutomationRuleV2
<a name="API_GetAutomationRuleV2"></a>

Returns an automation rule for the V2 service.

## Request Syntax
<a name="API_GetAutomationRuleV2_RequestSyntax"></a>

```
GET /automationrulesv2/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAutomationRuleV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetAutomationRuleV2_RequestSyntax) **   <a name="securityhub-GetAutomationRuleV2-request-uri-Identifier"></a>
The ARN of the V2 automation rule.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_GetAutomationRuleV2_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAutomationRuleV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Actions": [
      {
         "ExternalIntegrationConfiguration": {
            "ConnectorArn": "string"
         },
         "FindingFieldsUpdate": {
            "Comment": "string",
            "SeverityId": number,
            "StatusId": number
         },
         "Type": "string"
      }
   ],
   "CreatedAt": "string",
   "Criteria": { ... },
   "Description": "string",
   "RuleArn": "string",
   "RuleId": "string",
   "RuleName": "string",
   "RuleOrder": number,
   "RuleStatus": "string",
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_GetAutomationRuleV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Actions](#API_GetAutomationRuleV2_ResponseSyntax) **   <a name="securityhub-GetAutomationRuleV2-response-Actions"></a>
A list of actions performed when the rule criteria is met.
Type: Array of [AutomationRulesActionV2](API_AutomationRulesActionV2.md) objects
Array Members: Fixed number of 1 item.

 ** [CreatedAt](#API_GetAutomationRuleV2_ResponseSyntax) **   <a name="securityhub-GetAutomationRuleV2-response-CreatedAt"></a>
The timestamp when the V2 automation rule was created.
Type: Timestamp

 ** [Criteria](#API_GetAutomationRuleV2_ResponseSyntax) **   <a name="securityhub-GetAutomationRuleV2-response-Criteria"></a>
The filtering type and configuration of the V2 automation rule.
Type: [Criteria](API_Criteria.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [Description](#API_GetAutomationRuleV2_ResponseSyntax) **   <a name="securityhub-GetAutomationRuleV2-response-Description"></a>
A description of the automation rule.
Type: String
Pattern: `.*\S.*`

 ** [RuleArn](#API_GetAutomationRuleV2_ResponseSyntax) **   <a name="securityhub-GetAutomationRuleV2-response-RuleArn"></a>
The ARN of the V2 automation rule.
Type: String
Pattern: `.*\S.*`

 ** [RuleId](#API_GetAutomationRuleV2_ResponseSyntax) **   <a name="securityhub-GetAutomationRuleV2-response-RuleId"></a>
The ID of the V2 automation rule.
Type: String
Pattern: `.*\S.*`

 ** [RuleName](#API_GetAutomationRuleV2_ResponseSyntax) **   <a name="securityhub-GetAutomationRuleV2-response-RuleName"></a>
The name of the V2 automation rule.
Type: String
Pattern: `.*\S.*`

 ** [RuleOrder](#API_GetAutomationRuleV2_ResponseSyntax) **   <a name="securityhub-GetAutomationRuleV2-response-RuleOrder"></a>
The value for the rule priority.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 1000.0.

 ** [RuleStatus](#API_GetAutomationRuleV2_ResponseSyntax) **   <a name="securityhub-GetAutomationRuleV2-response-RuleStatus"></a>
The status of the V2 automation automation rule.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [UpdatedAt](#API_GetAutomationRuleV2_ResponseSyntax) **   <a name="securityhub-GetAutomationRuleV2-response-UpdatedAt"></a>
The timestamp when the V2 automation rule was updated.
Type: Timestamp

## Errors
<a name="API_GetAutomationRuleV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** ConflictException **
The request causes conflict with the current state of the service resource.
HTTP Status Code: 409

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_GetAutomationRuleV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetAutomationRuleV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetAutomationRuleV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetAutomationRuleV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetAutomationRuleV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetAutomationRuleV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetAutomationRuleV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetAutomationRuleV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetAutomationRuleV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetAutomationRuleV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetAutomationRuleV2)
