---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_GetRules.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# GetRules
<a name="API_GetRules"></a>

Get all rules for a detector (paginated) if `ruleId` and `ruleVersion` are not specified. Gets all rules for the detector and the `ruleId` if present (paginated). Gets a specific rule if both the `ruleId` and the `ruleVersion` are specified.

This is a paginated API. Providing null maxResults results in retrieving maximum of 100 records per page. If you provide maxResults the value must be between 50 and 100. To get the next page result, a provide a pagination token from GetRulesResult as part of your request. Null pagination token fetches the records from the beginning.

## Request Syntax
<a name="API_GetRules_RequestSyntax"></a>

```
{
   "detectorId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "ruleId": "{{string}}",
   "ruleVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [detectorId](#API_GetRules_RequestSyntax) **   <a name="FraudDetector-GetRules-request-detectorId"></a>
The detector ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [maxResults](#API_GetRules_RequestSyntax) **   <a name="FraudDetector-GetRules-request-maxResults"></a>
The maximum number of rules to return for the request.
Type: Integer
Valid Range: Minimum value of 50. Maximum value of 100.
Required: No

 ** [nextToken](#API_GetRules_RequestSyntax) **   <a name="FraudDetector-GetRules-request-nextToken"></a>
The next page token.
Type: String
Required: No

 ** [ruleId](#API_GetRules_RequestSyntax) **   <a name="FraudDetector-GetRules-request-ruleId"></a>
The rule ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** [ruleVersion](#API_GetRules_RequestSyntax) **   <a name="FraudDetector-GetRules-request-ruleVersion"></a>
The rule version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^([1-9][0-9]*)$`
Required: No

## Response Syntax
<a name="API_GetRules_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "ruleDetails": [
      {
         "arn": "string",
         "createdTime": "string",
         "description": "string",
         "detectorId": "string",
         "expression": "string",
         "language": "string",
         "lastUpdatedTime": "string",
         "outcomes": [ "string" ],
         "ruleId": "string",
         "ruleVersion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetRules_ResponseSyntax) **   <a name="FraudDetector-GetRules-response-nextToken"></a>
The next page token to be used in subsequent requests.
Type: String

 ** [ruleDetails](#API_GetRules_ResponseSyntax) **   <a name="FraudDetector-GetRules-response-ruleDetails"></a>
The details of the requested rule.
Type: Array of [RuleDetail](API_RuleDetail.md) objects

## Errors
<a name="API_GetRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as `PutExternalModel`, that specifies a role that is not in your account.
HTTP Status Code: 400

 ** InternalServerException **
An exception indicating an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception indicating the specified resource was not found.
HTTP Status Code: 400

 ** ThrottlingException **
An exception indicating a throttling error.
HTTP Status Code: 400

 ** ValidationException **
An exception indicating a specified value is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_GetRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/GetRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/GetRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/GetRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/GetRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/GetRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/GetRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/GetRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/GetRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/GetRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/GetRules)
