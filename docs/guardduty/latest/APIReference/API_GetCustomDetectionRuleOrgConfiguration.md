---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCustomDetectionRuleOrgConfiguration.html
---

# GetCustomDetectionRuleOrgConfiguration
<a name="API_GetCustomDetectionRuleOrgConfiguration"></a>

Returns the organization-level configuration for a custom detection rule.

## Request Syntax
<a name="API_GetCustomDetectionRuleOrgConfiguration_RequestSyntax"></a>

```
GET /custom-detection-rule/org-configuration/{{RuleId}}?mode={{Mode}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCustomDetectionRuleOrgConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Mode](#API_GetCustomDetectionRuleOrgConfiguration_RequestSyntax) **   <a name="guardduty-GetCustomDetectionRuleOrgConfiguration-request-uri-Mode"></a>
The execution mode of the organization configuration to retrieve. Valid values: `LIVE` \| `DRY_RUN`.
Valid Values: `LIVE | DRY_RUN`
Required: Yes

 ** [RuleId](#API_GetCustomDetectionRuleOrgConfiguration_RequestSyntax) **   <a name="guardduty-GetCustomDetectionRuleOrgConfiguration-request-uri-RuleId"></a>
The unique identifier for the custom detection rule.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: Yes

## Request Body
<a name="API_GetCustomDetectionRuleOrgConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCustomDetectionRuleOrgConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuration": {
      "createdAt": number,
      "excludeAccountIds": [ "string" ],
      "expiresAt": number,
      "includeAccountIds": [ "string" ],
      "mode": "string",
      "ruleId": "string",
      "status": "string",
      "statusReason": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_GetCustomDetectionRuleOrgConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_GetCustomDetectionRuleOrgConfiguration_ResponseSyntax) **   <a name="guardduty-GetCustomDetectionRuleOrgConfiguration-response-configuration"></a>
The details of the organization configuration.
Type: [DetectionRuleOrgConfiguration](API_DetectionRuleOrgConfiguration.md) object

## Errors
<a name="API_GetCustomDetectionRuleOrgConfiguration_Errors"></a>

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
<a name="API_GetCustomDetectionRuleOrgConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetCustomDetectionRuleOrgConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetCustomDetectionRuleOrgConfiguration)
