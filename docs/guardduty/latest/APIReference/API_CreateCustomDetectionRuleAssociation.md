---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateCustomDetectionRuleAssociation.html
---

# CreateCustomDetectionRuleAssociation
<a name="API_CreateCustomDetectionRuleAssociation"></a>

Enables a custom detection rule for your account by creating an association. You specify the rule and the mode in which it operates.

## Request Syntax
<a name="API_CreateCustomDetectionRuleAssociation_RequestSyntax"></a>

```
POST /custom-detection-rule/association HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "mode": "{{string}}",
   "ruleId": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateCustomDetectionRuleAssociation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCustomDetectionRuleAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateCustomDetectionRuleAssociation_RequestSyntax) **   <a name="guardduty-CreateCustomDetectionRuleAssociation-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. Maximum 64 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [mode](#API_CreateCustomDetectionRuleAssociation_RequestSyntax) **   <a name="guardduty-CreateCustomDetectionRuleAssociation-request-mode"></a>
The rule execution mode. Valid values: `LIVE` \| `DRY_RUN`.
Type: String
Valid Values: `LIVE | DRY_RUN`
Required: Yes

 ** [ruleId](#API_CreateCustomDetectionRuleAssociation_RequestSyntax) **   <a name="guardduty-CreateCustomDetectionRuleAssociation-request-ruleId"></a>
The unique identifier for the custom detection rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: Yes

 ** [tags](#API_CreateCustomDetectionRuleAssociation_RequestSyntax) **   <a name="guardduty-CreateCustomDetectionRuleAssociation-request-tags"></a>
The tags to be added to the new custom detection rule association resource.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateCustomDetectionRuleAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ruleAssociation": {
      "accountId": "string",
      "arn": "string",
      "associationId": "string",
      "createdAt": number,
      "expiresAt": number,
      "mode": "string",
      "ruleId": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_CreateCustomDetectionRuleAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ruleAssociation](#API_CreateCustomDetectionRuleAssociation_ResponseSyntax) **   <a name="guardduty-CreateCustomDetectionRuleAssociation-response-ruleAssociation"></a>
The details of the newly created custom detection rule association.
Type: [AssociationDetail](API_AssociationDetail.md) object

## Errors
<a name="API_CreateCustomDetectionRuleAssociation_Errors"></a>

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
<a name="API_CreateCustomDetectionRuleAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/CreateCustomDetectionRuleAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/CreateCustomDetectionRuleAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CreateCustomDetectionRuleAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/CreateCustomDetectionRuleAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CreateCustomDetectionRuleAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/CreateCustomDetectionRuleAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/CreateCustomDetectionRuleAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/CreateCustomDetectionRuleAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/CreateCustomDetectionRuleAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CreateCustomDetectionRuleAssociation)
