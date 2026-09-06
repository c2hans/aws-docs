---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateCustomDetectionRuleOrgConfiguration.html
---

# UpdateCustomDetectionRuleOrgConfiguration
<a name="API_UpdateCustomDetectionRuleOrgConfiguration"></a>

Updates the organization-level configuration for a custom detection rule, including the mode and include/exclude account lists.

## Request Syntax
<a name="API_UpdateCustomDetectionRuleOrgConfiguration_RequestSyntax"></a>

```
PUT /custom-detection-rule/org-configuration/{{RuleId}} HTTP/1.1
Content-type: application/json

{
   "excludeAccountIds": [ "{{string}}" ],
   "includeAccountIds": [ "{{string}}" ],
   "mode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCustomDetectionRuleOrgConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [RuleId](#API_UpdateCustomDetectionRuleOrgConfiguration_RequestSyntax) **   <a name="guardduty-UpdateCustomDetectionRuleOrgConfiguration-request-uri-RuleId"></a>
The unique identifier for the custom detection rule.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: Yes

## Request Body
<a name="API_UpdateCustomDetectionRuleOrgConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [excludeAccountIds](#API_UpdateCustomDetectionRuleOrgConfiguration_RequestSyntax) **   <a name="guardduty-UpdateCustomDetectionRuleOrgConfiguration-request-excludeAccountIds"></a>
The account IDs to exclude from the organization configuration. Mutually exclusive with `IncludeAccountIds`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50000 items.
Length Constraints: Fixed length of 12.
Required: No

 ** [includeAccountIds](#API_UpdateCustomDetectionRuleOrgConfiguration_RequestSyntax) **   <a name="guardduty-UpdateCustomDetectionRuleOrgConfiguration-request-includeAccountIds"></a>
The account IDs to include in the organization configuration. Mutually exclusive with `ExcludeAccountIds`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50000 items.
Length Constraints: Fixed length of 12.
Required: No

 ** [mode](#API_UpdateCustomDetectionRuleOrgConfiguration_RequestSyntax) **   <a name="guardduty-UpdateCustomDetectionRuleOrgConfiguration-request-mode"></a>
The execution mode of the organization configuration. Valid values: `LIVE` \| `DRY_RUN`.
Type: String
Valid Values: `LIVE | DRY_RUN`
Required: Yes

## Response Syntax
<a name="API_UpdateCustomDetectionRuleOrgConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateCustomDetectionRuleOrgConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateCustomDetectionRuleOrgConfiguration_Errors"></a>

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
<a name="API_UpdateCustomDetectionRuleOrgConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/UpdateCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/UpdateCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UpdateCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/UpdateCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UpdateCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/UpdateCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/UpdateCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/UpdateCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/UpdateCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UpdateCustomDetectionRuleOrgConfiguration)
