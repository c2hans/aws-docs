---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteCustomDetectionRuleAssociation.html
---

# DeleteCustomDetectionRuleAssociation
<a name="API_DeleteCustomDetectionRuleAssociation"></a>

Disables a custom detection rule by deleting its association. This operation is idempotent.

## Request Syntax
<a name="API_DeleteCustomDetectionRuleAssociation_RequestSyntax"></a>

```
DELETE /custom-detection-rule/rule/{{RuleId}}/association/{{AssociationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCustomDetectionRuleAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssociationId](#API_DeleteCustomDetectionRuleAssociation_RequestSyntax) **   <a name="guardduty-DeleteCustomDetectionRuleAssociation-request-uri-AssociationId"></a>
The unique identifier for the association to delete.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]{1,64}`
Required: Yes

 ** [RuleId](#API_DeleteCustomDetectionRuleAssociation_RequestSyntax) **   <a name="guardduty-DeleteCustomDetectionRuleAssociation-request-uri-RuleId"></a>
The unique identifier for the custom detection rule.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: Yes

## Request Body
<a name="API_DeleteCustomDetectionRuleAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCustomDetectionRuleAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteCustomDetectionRuleAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCustomDetectionRuleAssociation_Errors"></a>

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
<a name="API_DeleteCustomDetectionRuleAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/DeleteCustomDetectionRuleAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/DeleteCustomDetectionRuleAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DeleteCustomDetectionRuleAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/DeleteCustomDetectionRuleAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DeleteCustomDetectionRuleAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/DeleteCustomDetectionRuleAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/DeleteCustomDetectionRuleAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/DeleteCustomDetectionRuleAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/DeleteCustomDetectionRuleAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DeleteCustomDetectionRuleAssociation)
