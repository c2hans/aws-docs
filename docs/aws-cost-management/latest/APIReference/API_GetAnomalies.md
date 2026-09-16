---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetAnomalies.html
---

# GetAnomalies
<a name="API_GetAnomalies"></a>

Retrieves all of the cost anomalies detected on your account during the time period that's specified by the `DateInterval` object. Anomalies are available for up to 90 days.

## Request Syntax
<a name="API_GetAnomalies_RequestSyntax"></a>

```
{
   "DateInterval": {
      "EndDate": "{{string}}",
      "StartDate": "{{string}}"
   },
   "Feedback": "{{string}}",
   "MaxResults": {{number}},
   "MonitorArn": "{{string}}",
   "NextPageToken": "{{string}}",
   "TotalImpact": {
      "EndValue": {{number}},
      "NumericOperator": "{{string}}",
      "StartValue": {{number}}
   }
}
```

## Request Parameters
<a name="API_GetAnomalies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DateInterval](#API_GetAnomalies_RequestSyntax) **   <a name="awscostmanagement-GetAnomalies-request-DateInterval"></a>
Assigns the start and end dates for retrieving cost anomalies. The returned anomaly object will have an `AnomalyEndDate` in the specified time range.
Type: [AnomalyDateInterval](API_AnomalyDateInterval.md) object
Required: Yes

 ** [Feedback](#API_GetAnomalies_RequestSyntax) **   <a name="awscostmanagement-GetAnomalies-request-Feedback"></a>
Filters anomaly results by the feedback field on the anomaly object.
Type: String
Valid Values: `YES | NO | PLANNED_ACTIVITY`
Required: No

 ** [MaxResults](#API_GetAnomalies_RequestSyntax) **   <a name="awscostmanagement-GetAnomalies-request-MaxResults"></a>
The number of entries a paginated response contains.
Type: Integer
Required: No

 ** [MonitorArn](#API_GetAnomalies_RequestSyntax) **   <a name="awscostmanagement-GetAnomalies-request-MonitorArn"></a>
Retrieves all of the cost anomalies detected for a specific cost anomaly monitor Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** [NextPageToken](#API_GetAnomalies_RequestSyntax) **   <a name="awscostmanagement-GetAnomalies-request-NextPageToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [TotalImpact](#API_GetAnomalies_RequestSyntax) **   <a name="awscostmanagement-GetAnomalies-request-TotalImpact"></a>
Filters anomaly results by the total impact field on the anomaly object. For example, you can filter anomalies `GREATER_THAN 200.00` to retrieve anomalies, with an estimated dollar impact greater than 200.
Type: [TotalImpactFilter](API_TotalImpactFilter.md) object
Required: No

## Response Syntax
<a name="API_GetAnomalies_ResponseSyntax"></a>

```
{
   "Anomalies": [
      {
         "AnomalyEndDate": "string",
         "AnomalyId": "string",
         "AnomalyScore": {
            "CurrentScore": number,
            "MaxScore": number
         },
         "AnomalyStartDate": "string",
         "DimensionValue": "string",
         "Feedback": "string",
         "Impact": {
            "MaxImpact": number,
            "TotalActualSpend": number,
            "TotalExpectedSpend": number,
            "TotalImpact": number,
            "TotalImpactPercentage": number
         },
         "MonitorArn": "string",
         "RootCauses": [
            {
               "Impact": {
                  "Contribution": number
               },
               "LinkedAccount": "string",
               "LinkedAccountName": "string",
               "Region": "string",
               "Service": "string",
               "UsageType": "string"
            }
         ]
      }
   ],
   "NextPageToken": "string"
}
```

## Response Elements
<a name="API_GetAnomalies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Anomalies](#API_GetAnomalies_ResponseSyntax) **   <a name="awscostmanagement-GetAnomalies-response-Anomalies"></a>
A list of cost anomalies.
Type: Array of [Anomaly](API_Anomaly.md) objects

 ** [NextPageToken](#API_GetAnomalies_ResponseSyntax) **   <a name="awscostmanagement-GetAnomalies-response-NextPageToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

## Errors
<a name="API_GetAnomalies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The pagination token is invalid. Try again without a pagination token.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## See Also
<a name="API_GetAnomalies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetAnomalies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetAnomalies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetAnomalies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetAnomalies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetAnomalies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetAnomalies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetAnomalies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetAnomalies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetAnomalies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetAnomalies)
