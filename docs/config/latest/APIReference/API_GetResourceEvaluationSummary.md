---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GetResourceEvaluationSummary.html
---

# GetResourceEvaluationSummary
<a name="API_GetResourceEvaluationSummary"></a>

Returns a summary of resource evaluation for the specified resource evaluation ID from the proactive rules that were run. The results indicate which evaluation context was used to evaluate the rules, which resource details were evaluated, the evaluation mode that was run, and whether the resource details comply with the configuration of the proactive rules.

**Note**
To see additional information about the evaluation result, such as which rule flagged a resource as NON\_COMPLIANT, use the [GetComplianceDetailsByResource](https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceDetailsByResource.html) API. For more information, see the [Examples](https://docs.aws.amazon.com/config/latest/APIReference/API_GetResourceEvaluationSummary.html#API_GetResourceEvaluationSummary_Examples) section.

## Request Syntax
<a name="API_GetResourceEvaluationSummary_RequestSyntax"></a>

```
{
   "ResourceEvaluationId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetResourceEvaluationSummary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceEvaluationId](#API_GetResourceEvaluationSummary_RequestSyntax) **   <a name="config-GetResourceEvaluationSummary-request-ResourceEvaluationId"></a>
The unique `ResourceEvaluationId` of AWS resource execution for which you want to retrieve the evaluation summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Response Syntax
<a name="API_GetResourceEvaluationSummary_ResponseSyntax"></a>

```
{
   "Compliance": "string",
   "EvaluationContext": {
      "EvaluationContextIdentifier": "string"
   },
   "EvaluationMode": "string",
   "EvaluationStartTimestamp": number,
   "EvaluationStatus": {
      "FailureReason": "string",
      "Status": "string"
   },
   "ResourceDetails": {
      "ResourceConfiguration": "string",
      "ResourceConfigurationSchemaType": "string",
      "ResourceId": "string",
      "ResourceType": "string"
   },
   "ResourceEvaluationId": "string"
}
```

## Response Elements
<a name="API_GetResourceEvaluationSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Compliance](#API_GetResourceEvaluationSummary_ResponseSyntax) **   <a name="config-GetResourceEvaluationSummary-response-Compliance"></a>
The compliance status of the resource evaluation summary.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT | NOT_APPLICABLE | INSUFFICIENT_DATA`

 ** [EvaluationContext](#API_GetResourceEvaluationSummary_ResponseSyntax) **   <a name="config-GetResourceEvaluationSummary-response-EvaluationContext"></a>
Returns an `EvaluationContext` object.
Type: [EvaluationContext](API_EvaluationContext.md) object

 ** [EvaluationMode](#API_GetResourceEvaluationSummary_ResponseSyntax) **   <a name="config-GetResourceEvaluationSummary-response-EvaluationMode"></a>
Lists results of the mode that you requested to retrieve the resource evaluation summary. The valid values are Detective or Proactive.
Type: String
Valid Values: `DETECTIVE | PROACTIVE`

 ** [EvaluationStartTimestamp](#API_GetResourceEvaluationSummary_ResponseSyntax) **   <a name="config-GetResourceEvaluationSummary-response-EvaluationStartTimestamp"></a>
The start timestamp when AWS Config rule starts evaluating compliance for the provided resource details.
Type: Timestamp

 ** [EvaluationStatus](#API_GetResourceEvaluationSummary_ResponseSyntax) **   <a name="config-GetResourceEvaluationSummary-response-EvaluationStatus"></a>
Returns an `EvaluationStatus` object.
Type: [EvaluationStatus](API_EvaluationStatus.md) object

 ** [ResourceDetails](#API_GetResourceEvaluationSummary_ResponseSyntax) **   <a name="config-GetResourceEvaluationSummary-response-ResourceDetails"></a>
Returns a `ResourceDetails` object.
Type: [ResourceDetails](API_ResourceDetails.md) object

 ** [ResourceEvaluationId](#API_GetResourceEvaluationSummary_ResponseSyntax) **   <a name="config-GetResourceEvaluationSummary-response-ResourceEvaluationId"></a>
The unique `ResourceEvaluationId` of AWS resource execution for which you want to retrieve the evaluation summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

## Errors
<a name="API_GetResourceEvaluationSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
You have specified a resource that does not exist.
HTTP Status Code: 400

## Examples
<a name="API_GetResourceEvaluationSummary_Examples"></a>

### Example
<a name="API_GetResourceEvaluationSummary_Example_1"></a>

To see additional information about the evaluation result, such as which rule flagged a resource as NON\_COMPLIANT, use the [GetComplianceDetailsByResource](https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceDetailsByResource.html) API. For example:

```
aws configservice get-compliance-details-by-resource --resource-evaluation-id MY-EVALUATION-ID
{
	"EvaluationResults": [
		{
			"EvaluationResultIdentifier": {
				"EvaluationResultQualifier": {
					"ConfigRuleName": "s3-bucket-logging-enabled",
					"ResourceType": "AWS::S3::Bucket",
					"ResourceId": "MY-RESOURCE-ID",
					"EvaluationMode": "PROACTIVE"
				},
				"OrderingTimestamp": "2022-12-23T14:35:40.036000-05:00",
				"ResourceEvaluationId": "MY-EVALUATION-ID"
			},
			"ComplianceType": "NON_COMPLIANT",
			"ResultRecordedTime": "2022-12-23T14:35:11.213000-05:00",
			"ConfigRuleInvokedTime": "2022-12-23T14:35:10.978000-05:00"
		}
	]
}
```

## See Also
<a name="API_GetResourceEvaluationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/GetResourceEvaluationSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/GetResourceEvaluationSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GetResourceEvaluationSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/GetResourceEvaluationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GetResourceEvaluationSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/GetResourceEvaluationSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/GetResourceEvaluationSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/GetResourceEvaluationSummary)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/GetResourceEvaluationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GetResourceEvaluationSummary)
