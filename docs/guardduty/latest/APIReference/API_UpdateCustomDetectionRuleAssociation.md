---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateCustomDetectionRuleAssociation.html
---

# UpdateCustomDetectionRuleAssociation
<a name="API_UpdateCustomDetectionRuleAssociation"></a>

Updates the mode of an existing custom detection rule association.

## Request Syntax
<a name="API_UpdateCustomDetectionRuleAssociation_RequestSyntax"></a>

```
PUT /custom-detection-rule/rule/{{RuleId}}/association/{{AssociationId}} HTTP/1.1
Content-type: application/json

{
   "mode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCustomDetectionRuleAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssociationId](#API_UpdateCustomDetectionRuleAssociation_RequestSyntax) **   <a name="guardduty-UpdateCustomDetectionRuleAssociation-request-uri-AssociationId"></a>
The unique identifier for the association to update.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]{1,64}`
Required: Yes

 ** [RuleId](#API_UpdateCustomDetectionRuleAssociation_RequestSyntax) **   <a name="guardduty-UpdateCustomDetectionRuleAssociation-request-uri-RuleId"></a>
The unique identifier for the custom detection rule.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: Yes

## Request Body
<a name="API_UpdateCustomDetectionRuleAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [mode](#API_UpdateCustomDetectionRuleAssociation_RequestSyntax) **   <a name="guardduty-UpdateCustomDetectionRuleAssociation-request-mode"></a>
The rule execution mode. Valid values: `LIVE` \| `DRY_RUN`.
Type: String
Valid Values: `LIVE | DRY_RUN`
Required: Yes

## Response Syntax
<a name="API_UpdateCustomDetectionRuleAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateCustomDetectionRuleAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateCustomDetectionRuleAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An access denied exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 403

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** ConflictException **
A request conflict exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 409

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 404

## See Also
<a name="API_UpdateCustomDetectionRuleAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/UpdateCustomDetectionRuleAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/UpdateCustomDetectionRuleAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UpdateCustomDetectionRuleAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/UpdateCustomDetectionRuleAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UpdateCustomDetectionRuleAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/UpdateCustomDetectionRuleAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/UpdateCustomDetectionRuleAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/UpdateCustomDetectionRuleAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/UpdateCustomDetectionRuleAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UpdateCustomDetectionRuleAssociation)
