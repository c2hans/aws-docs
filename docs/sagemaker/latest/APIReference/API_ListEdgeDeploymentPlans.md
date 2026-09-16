---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListEdgeDeploymentPlans.html
---

# ListEdgeDeploymentPlans
<a name="API_ListEdgeDeploymentPlans"></a>

Lists all edge deployment plans.

## Request Syntax
<a name="API_ListEdgeDeploymentPlans_RequestSyntax"></a>

```
{
   "DeviceFleetNameContains": "{{string}}",
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEdgeDeploymentPlans_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeviceFleetNameContains](#API_ListEdgeDeploymentPlans_RequestSyntax) **   <a name="sagemaker-ListEdgeDeploymentPlans-request-DeviceFleetNameContains"></a>
Selects edge deployment plans with a device fleet name containing this name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [MaxResults](#API_ListEdgeDeploymentPlans_RequestSyntax) **   <a name="sagemaker-ListEdgeDeploymentPlans-request-MaxResults"></a>
The maximum number of results to select (50 by default).
Type: Integer
Valid Range: Maximum value of 100.
Required: No

 ** [NameContains](#API_ListEdgeDeploymentPlans_RequestSyntax) **   <a name="sagemaker-ListEdgeDeploymentPlans-request-NameContains"></a>
Selects edge deployment plans with names containing this name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListEdgeDeploymentPlans_RequestSyntax) **   <a name="sagemaker-ListEdgeDeploymentPlans-request-NextToken"></a>
The response from the last list when returning a list large enough to need tokening.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListEdgeDeploymentPlans_RequestSyntax) **   <a name="sagemaker-ListEdgeDeploymentPlans-request-SortBy"></a>
The column by which to sort the edge deployment plans. Can be one of `NAME`, `DEVICEFLEETNAME`, `CREATIONTIME`, `LASTMODIFIEDTIME`.
Type: String
Valid Values: `NAME | DEVICE_FLEET_NAME | CREATION_TIME | LAST_MODIFIED_TIME`
Required: No

 ** [SortOrder](#API_ListEdgeDeploymentPlans_RequestSyntax) **   <a name="sagemaker-ListEdgeDeploymentPlans-request-SortOrder"></a>
The direction of the sorting (ascending or descending).
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListEdgeDeploymentPlans_ResponseSyntax"></a>

```
{
   "EdgeDeploymentPlanSummaries": [
      {
         "DeviceFleetName": "string",
         "EdgeDeploymentFailed": number,
         "EdgeDeploymentPending": number,
         "EdgeDeploymentPlanArn": "string",
         "EdgeDeploymentPlanName": "string",
         "EdgeDeploymentSuccess": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEdgeDeploymentPlans_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EdgeDeploymentPlanSummaries](#API_ListEdgeDeploymentPlans_ResponseSyntax) **   <a name="sagemaker-ListEdgeDeploymentPlans-response-EdgeDeploymentPlanSummaries"></a>
List of summaries of edge deployment plans.
Type: Array of [EdgeDeploymentPlanSummary](API_EdgeDeploymentPlanSummary.md) objects

 ** [NextToken](#API_ListEdgeDeploymentPlans_ResponseSyntax) **   <a name="sagemaker-ListEdgeDeploymentPlans-response-NextToken"></a>
The token to use when calling the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListEdgeDeploymentPlans_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListEdgeDeploymentPlans_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListEdgeDeploymentPlans)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListEdgeDeploymentPlans)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListEdgeDeploymentPlans)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListEdgeDeploymentPlans)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListEdgeDeploymentPlans)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListEdgeDeploymentPlans)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListEdgeDeploymentPlans)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListEdgeDeploymentPlans)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListEdgeDeploymentPlans)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListEdgeDeploymentPlans)
