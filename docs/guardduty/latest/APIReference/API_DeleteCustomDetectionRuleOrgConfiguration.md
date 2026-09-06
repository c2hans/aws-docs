---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteCustomDetectionRuleOrgConfiguration.html
---

# DeleteCustomDetectionRuleOrgConfiguration
<a name="API_DeleteCustomDetectionRuleOrgConfiguration"></a>

Deletes the organization-level configuration for a custom detection rule. This operation is available only to the delegated administrator account.

## Request Syntax
<a name="API_DeleteCustomDetectionRuleOrgConfiguration_RequestSyntax"></a>

```
DELETE /custom-detection-rule/org-configuration/{{RuleId}}?mode={{Mode}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCustomDetectionRuleOrgConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Mode](#API_DeleteCustomDetectionRuleOrgConfiguration_RequestSyntax) **   <a name="guardduty-DeleteCustomDetectionRuleOrgConfiguration-request-uri-Mode"></a>
The execution mode of the organization configuration to delete. Valid values: `LIVE` \| `DRY_RUN`.
Valid Values: `LIVE | DRY_RUN`
Required: Yes

 ** [RuleId](#API_DeleteCustomDetectionRuleOrgConfiguration_RequestSyntax) **   <a name="guardduty-DeleteCustomDetectionRuleOrgConfiguration-request-uri-RuleId"></a>
The unique identifier for the custom detection rule.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: Yes

## Request Body
<a name="API_DeleteCustomDetectionRuleOrgConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCustomDetectionRuleOrgConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteCustomDetectionRuleOrgConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCustomDetectionRuleOrgConfiguration_Errors"></a>

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
<a name="API_DeleteCustomDetectionRuleOrgConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/DeleteCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/DeleteCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DeleteCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/DeleteCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DeleteCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/DeleteCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/DeleteCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/DeleteCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/DeleteCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DeleteCustomDetectionRuleOrgConfiguration)
