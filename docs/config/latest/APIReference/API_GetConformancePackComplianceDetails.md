---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GetConformancePackComplianceDetails.html
---

# GetConformancePackComplianceDetails
<a name="API_GetConformancePackComplianceDetails"></a>

Returns compliance details of a conformance pack for all AWS resources that are monitered by conformance pack.

## Request Syntax
<a name="API_GetConformancePackComplianceDetails_RequestSyntax"></a>

```
{
   "ConformancePackName": "{{string}}",
   "Filters": {
      "ComplianceType": "{{string}}",
      "ConfigRuleNames": [ "{{string}}" ],
      "ResourceIds": [ "{{string}}" ],
      "ResourceType": "{{string}}"
   },
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetConformancePackComplianceDetails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConformancePackName](#API_GetConformancePackComplianceDetails_RequestSyntax) **   <a name="config-GetConformancePackComplianceDetails-request-ConformancePackName"></a>
Name of the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: Yes

 ** [Filters](#API_GetConformancePackComplianceDetails_RequestSyntax) **   <a name="config-GetConformancePackComplianceDetails-request-Filters"></a>
A `ConformancePackEvaluationFilters` object.
Type: [ConformancePackEvaluationFilters](API_ConformancePackEvaluationFilters.md) object
Required: No

 ** [Limit](#API_GetConformancePackComplianceDetails_RequestSyntax) **   <a name="config-GetConformancePackComplianceDetails-request-Limit"></a>
The maximum number of evaluation results returned on each page. If you do no specify a number, AWS Config uses the default. The default is 100.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetConformancePackComplianceDetails_RequestSyntax) **   <a name="config-GetConformancePackComplianceDetails-request-NextToken"></a>
The `nextToken` string returned in a previous request that you use to request the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_GetConformancePackComplianceDetails_ResponseSyntax"></a>

```
{
   "ConformancePackName": "string",
   "ConformancePackRuleEvaluationResults": [
      {
         "Annotation": "string",
         "ComplianceType": "string",
         "ConfigRuleInvokedTime": number,
         "EvaluationResultIdentifier": {
            "EvaluationResultQualifier": {
               "ConfigRuleName": "string",
               "EvaluationMode": "string",
               "ResourceId": "string",
               "ResourceType": "string"
            },
            "OrderingTimestamp": number,
            "ResourceEvaluationId": "string"
         },
         "ResultRecordedTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetConformancePackComplianceDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConformancePackName](#API_GetConformancePackComplianceDetails_ResponseSyntax) **   <a name="config-GetConformancePackComplianceDetails-response-ConformancePackName"></a>
Name of the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`

 ** [ConformancePackRuleEvaluationResults](#API_GetConformancePackComplianceDetails_ResponseSyntax) **   <a name="config-GetConformancePackComplianceDetails-response-ConformancePackRuleEvaluationResults"></a>
Returns a list of `ConformancePackEvaluationResult` objects.
Type: Array of [ConformancePackEvaluationResult](API_ConformancePackEvaluationResult.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [NextToken](#API_GetConformancePackComplianceDetails_ResponseSyntax) **   <a name="config-GetConformancePackComplianceDetails-response-NextToken"></a>
The `nextToken` string returned in a previous request that you use to request the next page of results in a paginated response.
Type: String

## Errors
<a name="API_GetConformancePackComplianceDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidLimitException **
The specified limit is outside the allowable range.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** NoSuchConfigRuleInConformancePackException **
 AWS Config rule that you passed in the filter does not exist.
HTTP Status Code: 400

 ** NoSuchConformancePackException **
You specified one or more conformance packs that do not exist.
HTTP Status Code: 400

## See Also
<a name="API_GetConformancePackComplianceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/GetConformancePackComplianceDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/GetConformancePackComplianceDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GetConformancePackComplianceDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/GetConformancePackComplianceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GetConformancePackComplianceDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/GetConformancePackComplianceDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/GetConformancePackComplianceDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/GetConformancePackComplianceDetails)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/GetConformancePackComplianceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GetConformancePackComplianceDetails)
