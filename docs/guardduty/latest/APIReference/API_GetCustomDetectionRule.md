---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCustomDetectionRule.html
---

# GetCustomDetectionRule
<a name="API_GetCustomDetectionRule"></a>

Returns details for a custom detection rule in GuardDuty, including its detection logic.

## Request Syntax
<a name="API_GetCustomDetectionRule_RequestSyntax"></a>

```
GET /custom-detection-rule/rule/{{RuleId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCustomDetectionRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [RuleId](#API_GetCustomDetectionRule_RequestSyntax) **   <a name="guardduty-GetCustomDetectionRule-request-uri-RuleId"></a>
The unique identifier for the custom detection rule.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: Yes

## Request Body
<a name="API_GetCustomDetectionRule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCustomDetectionRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "rule": {
      "arn": "string",
      "createdAt": number,
      "dataSource": "string",
      "definition": {
         "expression": "string"
      },
      "description": "string",
      "language": "string",
      "name": "string",
      "ruleId": "string",
      "schema": "string",
      "service": "string",
      "severity": "string",
      "tactic": "string",
      "technique": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_GetCustomDetectionRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [rule](#API_GetCustomDetectionRule_ResponseSyntax) **   <a name="guardduty-GetCustomDetectionRule-response-rule"></a>
The details of the custom detection rule.
Type: [RuleDetail](API_RuleDetail.md) object

## Errors
<a name="API_GetCustomDetectionRule_Errors"></a>

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
<a name="API_GetCustomDetectionRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetCustomDetectionRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetCustomDetectionRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetCustomDetectionRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetCustomDetectionRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetCustomDetectionRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetCustomDetectionRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetCustomDetectionRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetCustomDetectionRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetCustomDetectionRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetCustomDetectionRule)
