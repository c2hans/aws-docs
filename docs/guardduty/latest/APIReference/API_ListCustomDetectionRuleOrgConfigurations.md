---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCustomDetectionRuleOrgConfigurations.html
---

# ListCustomDetectionRuleOrgConfigurations
<a name="API_ListCustomDetectionRuleOrgConfigurations"></a>

Returns all organization-level configurations for custom detection rules. You can filter the results by status.

## Request Syntax
<a name="API_ListCustomDetectionRuleOrgConfigurations_RequestSyntax"></a>

```
GET /custom-detection-rule/org-configuration?maxResults={{MaxResults}}&nextToken={{NextToken}}&status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCustomDetectionRuleOrgConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListCustomDetectionRuleOrgConfigurations_RequestSyntax) **   <a name="guardduty-ListCustomDetectionRuleOrgConfigurations-request-uri-MaxResults"></a>
The maximum number of results to return in a single page. Minimum value of 1, maximum value of 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListCustomDetectionRuleOrgConfigurations_RequestSyntax) **   <a name="guardduty-ListCustomDetectionRuleOrgConfigurations-request-uri-NextToken"></a>
A pagination token from a previous response. Use this token to retrieve the next page of results.

 ** [Status](#API_ListCustomDetectionRuleOrgConfigurations_RequestSyntax) **   <a name="guardduty-ListCustomDetectionRuleOrgConfigurations-request-uri-Status"></a>
The configuration status to filter by.
Valid Values: `ACTIVE | PROCESSING | FAILED`

## Request Body
<a name="API_ListCustomDetectionRuleOrgConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCustomDetectionRuleOrgConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configurations": [
      {
         "createdAt": number,
         "expiresAt": number,
         "mode": "string",
         "ruleId": "string",
         "status": "string",
         "statusReason": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomDetectionRuleOrgConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configurations](#API_ListCustomDetectionRuleOrgConfigurations_ResponseSyntax) **   <a name="guardduty-ListCustomDetectionRuleOrgConfigurations-response-configurations"></a>
A list of organization configurations for custom detection rules.
Type: Array of [DetectionRuleOrgConfigurationSummary](API_DetectionRuleOrgConfigurationSummary.md) objects

 ** [nextToken](#API_ListCustomDetectionRuleOrgConfigurations_ResponseSyntax) **   <a name="guardduty-ListCustomDetectionRuleOrgConfigurations-response-nextToken"></a>
A pagination token to retrieve the next page of results. If this field is empty, there are no additional results.
Type: String

## Errors
<a name="API_ListCustomDetectionRuleOrgConfigurations_Errors"></a>

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
<a name="API_ListCustomDetectionRuleOrgConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/ListCustomDetectionRuleOrgConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/ListCustomDetectionRuleOrgConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ListCustomDetectionRuleOrgConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/ListCustomDetectionRuleOrgConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ListCustomDetectionRuleOrgConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/ListCustomDetectionRuleOrgConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/ListCustomDetectionRuleOrgConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/ListCustomDetectionRuleOrgConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/ListCustomDetectionRuleOrgConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ListCustomDetectionRuleOrgConfigurations)
