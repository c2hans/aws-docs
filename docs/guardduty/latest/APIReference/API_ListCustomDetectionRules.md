---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCustomDetectionRules.html
---

# ListCustomDetectionRules
<a name="API_ListCustomDetectionRules"></a>

Returns all available custom detection rules in GuardDuty. You can filter the results by data source, severity, tactic, technique, and service.

## Request Syntax
<a name="API_ListCustomDetectionRules_RequestSyntax"></a>

```
POST /custom-detection-rule/rule HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "condition": "{{string}}",
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCustomDetectionRules_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListCustomDetectionRules_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListCustomDetectionRules_RequestSyntax) **   <a name="guardduty-ListCustomDetectionRules-request-filters"></a>
A list of filter criteria to apply when listing custom detection rules.
Type: Array of [DetectionRuleFilter](API_DetectionRuleFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [maxResults](#API_ListCustomDetectionRules_RequestSyntax) **   <a name="guardduty-ListCustomDetectionRules-request-maxResults"></a>
The maximum number of results to return in a single page. Minimum value of 1, maximum value of 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListCustomDetectionRules_RequestSyntax) **   <a name="guardduty-ListCustomDetectionRules-request-nextToken"></a>
A pagination token from a previous response. Use this token to retrieve the next page of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListCustomDetectionRules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "rules": [
      {
         "arn": "string",
         "createdAt": number,
         "dataSource": "string",
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
   ]
}
```

## Response Elements
<a name="API_ListCustomDetectionRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListCustomDetectionRules_ResponseSyntax) **   <a name="guardduty-ListCustomDetectionRules-response-nextToken"></a>
A pagination token to retrieve the next page of results. If this field is empty, there are no additional results.
Type: String

 ** [rules](#API_ListCustomDetectionRules_ResponseSyntax) **   <a name="guardduty-ListCustomDetectionRules-response-rules"></a>
A list of custom detection rule summaries.
Type: Array of [RuleSummary](API_RuleSummary.md) objects

## Errors
<a name="API_ListCustomDetectionRules_Errors"></a>

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

## See Also
<a name="API_ListCustomDetectionRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/ListCustomDetectionRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/ListCustomDetectionRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ListCustomDetectionRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/ListCustomDetectionRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ListCustomDetectionRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/ListCustomDetectionRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/ListCustomDetectionRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/ListCustomDetectionRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/ListCustomDetectionRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ListCustomDetectionRules)
