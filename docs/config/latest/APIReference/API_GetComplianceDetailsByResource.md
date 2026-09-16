---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceDetailsByResource.html
---

# GetComplianceDetailsByResource
<a name="API_GetComplianceDetailsByResource"></a>

Returns the evaluation results for the specified AWS resource. The results indicate which AWS Config rules were used to evaluate the resource, when each rule was last invoked, and whether the resource complies with each rule.

## Request Syntax
<a name="API_GetComplianceDetailsByResource_RequestSyntax"></a>

```
{
   "ComplianceTypes": [ "{{string}}" ],
   "NextToken": "{{string}}",
   "ResourceEvaluationId": "{{string}}",
   "ResourceId": "{{string}}",
   "ResourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetComplianceDetailsByResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComplianceTypes](#API_GetComplianceDetailsByResource_RequestSyntax) **   <a name="config-GetComplianceDetailsByResource-request-ComplianceTypes"></a>
Filters the results by compliance.
 `INSUFFICIENT_DATA` is a valid `ComplianceType` that is returned when an AWS Config rule cannot be evaluated. However, `INSUFFICIENT_DATA` cannot be used as a `ComplianceType` for filtering results.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `COMPLIANT | NON_COMPLIANT | NOT_APPLICABLE | INSUFFICIENT_DATA`
Required: No

 ** [NextToken](#API_GetComplianceDetailsByResource_RequestSyntax) **   <a name="config-GetComplianceDetailsByResource-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

 ** [ResourceEvaluationId](#API_GetComplianceDetailsByResource_RequestSyntax) **   <a name="config-GetComplianceDetailsByResource-request-ResourceEvaluationId"></a>
The unique ID of AWS resource execution for which you want to retrieve evaluation results.
You need to only provide either a `ResourceEvaluationID` or a `ResourceID `and `ResourceType`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [ResourceId](#API_GetComplianceDetailsByResource_RequestSyntax) **   <a name="config-GetComplianceDetailsByResource-request-ResourceId"></a>
The ID of the AWS resource for which you want compliance information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: No

 ** [ResourceType](#API_GetComplianceDetailsByResource_RequestSyntax) **   <a name="config-GetComplianceDetailsByResource-request-ResourceType"></a>
The type of the AWS resource for which you want compliance information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_GetComplianceDetailsByResource_ResponseSyntax"></a>

```
{
   "EvaluationResults": [
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
         "ResultRecordedTime": number,
         "ResultToken": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetComplianceDetailsByResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EvaluationResults](#API_GetComplianceDetailsByResource_ResponseSyntax) **   <a name="config-GetComplianceDetailsByResource-response-EvaluationResults"></a>
Indicates whether the specified AWS resource complies each AWS Config rule.
Type: Array of [EvaluationResult](API_EvaluationResult.md) objects

 ** [NextToken](#API_GetComplianceDetailsByResource_ResponseSyntax) **   <a name="config-GetComplianceDetailsByResource-response-NextToken"></a>
The string that you use in a subsequent request to get the next page of results in a paginated response.
Type: String

## Errors
<a name="API_GetComplianceDetailsByResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

## See Also
<a name="API_GetComplianceDetailsByResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/GetComplianceDetailsByResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/GetComplianceDetailsByResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GetComplianceDetailsByResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/GetComplianceDetailsByResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GetComplianceDetailsByResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/GetComplianceDetailsByResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/GetComplianceDetailsByResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/GetComplianceDetailsByResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/GetComplianceDetailsByResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GetComplianceDetailsByResource)
