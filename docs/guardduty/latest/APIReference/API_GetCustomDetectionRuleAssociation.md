---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCustomDetectionRuleAssociation.html
---

# GetCustomDetectionRuleAssociation
<a name="API_GetCustomDetectionRuleAssociation"></a>

Returns details for a custom detection rule association.

## Request Syntax
<a name="API_GetCustomDetectionRuleAssociation_RequestSyntax"></a>

```
GET /custom-detection-rule/rule/{{RuleId}}/association/{{AssociationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCustomDetectionRuleAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssociationId](#API_GetCustomDetectionRuleAssociation_RequestSyntax) **   <a name="guardduty-GetCustomDetectionRuleAssociation-request-uri-AssociationId"></a>
The unique identifier for the association.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]{1,64}`
Required: Yes

 ** [RuleId](#API_GetCustomDetectionRuleAssociation_RequestSyntax) **   <a name="guardduty-GetCustomDetectionRuleAssociation-request-uri-RuleId"></a>
The unique identifier for the custom detection rule.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: Yes

## Request Body
<a name="API_GetCustomDetectionRuleAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCustomDetectionRuleAssociation_ResponseSyntax"></a>

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
   },
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetCustomDetectionRuleAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ruleAssociation](#API_GetCustomDetectionRuleAssociation_ResponseSyntax) **   <a name="guardduty-GetCustomDetectionRuleAssociation-response-ruleAssociation"></a>
The details of the custom detection rule association.
Type: [AssociationDetail](API_AssociationDetail.md) object

 ** [tags](#API_GetCustomDetectionRuleAssociation_ResponseSyntax) **   <a name="guardduty-GetCustomDetectionRuleAssociation-response-tags"></a>
The tags associated with the custom detection rule association resource.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetCustomDetectionRuleAssociation_Errors"></a>

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
<a name="API_GetCustomDetectionRuleAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetCustomDetectionRuleAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetCustomDetectionRuleAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetCustomDetectionRuleAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetCustomDetectionRuleAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetCustomDetectionRuleAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetCustomDetectionRuleAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetCustomDetectionRuleAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetCustomDetectionRuleAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetCustomDetectionRuleAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetCustomDetectionRuleAssociation)
