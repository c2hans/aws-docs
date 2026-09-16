---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetAnomalyMonitors.html
---

# GetAnomalyMonitors
<a name="API_GetAnomalyMonitors"></a>

Retrieves the cost anomaly monitor definitions for your account. You can filter using a list of cost anomaly monitor Amazon Resource Names (ARNs).

## Request Syntax
<a name="API_GetAnomalyMonitors_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "MonitorArnList": [ "{{string}}" ],
   "NextPageToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAnomalyMonitors_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetAnomalyMonitors_RequestSyntax) **   <a name="awscostmanagement-GetAnomalyMonitors-request-MaxResults"></a>
The number of entries that a paginated response contains.
Type: Integer
Required: No

 ** [MonitorArnList](#API_GetAnomalyMonitors_RequestSyntax) **   <a name="awscostmanagement-GetAnomalyMonitors-request-MonitorArnList"></a>
A list of cost anomaly monitor ARNs.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** [NextPageToken](#API_GetAnomalyMonitors_RequestSyntax) **   <a name="awscostmanagement-GetAnomalyMonitors-request-NextPageToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_GetAnomalyMonitors_ResponseSyntax"></a>

```
{
   "AnomalyMonitors": [
      {
         "CreationDate": "string",
         "DimensionalValueCount": number,
         "LastEvaluatedDate": "string",
         "LastUpdatedDate": "string",
         "MonitorArn": "string",
         "MonitorDimension": "string",
         "MonitorName": "string",
         "MonitorSpecification": {
            "And": [
               "Expression"
            ],
            "CostCategories": {
               "Key": "string",
               "MatchOptions": [ "string" ],
               "Values": [ "string" ]
            },
            "Dimensions": {
               "Key": "string",
               "MatchOptions": [ "string" ],
               "Values": [ "string" ]
            },
            "Not": "Expression",
            "Or": [
               "Expression"
            ],
            "Tags": {
               "Key": "string",
               "MatchOptions": [ "string" ],
               "Values": [ "string" ]
            }
         },
         "MonitorType": "string"
      }
   ],
   "NextPageToken": "string"
}
```

## Response Elements
<a name="API_GetAnomalyMonitors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AnomalyMonitors](#API_GetAnomalyMonitors_ResponseSyntax) **   <a name="awscostmanagement-GetAnomalyMonitors-response-AnomalyMonitors"></a>
A list of cost anomaly monitors that includes the detailed metadata for each monitor.
Type: Array of [AnomalyMonitor](API_AnomalyMonitor.md) objects

 ** [NextPageToken](#API_GetAnomalyMonitors_ResponseSyntax) **   <a name="awscostmanagement-GetAnomalyMonitors-response-NextPageToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

## Errors
<a name="API_GetAnomalyMonitors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The pagination token is invalid. Try again without a pagination token.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** UnknownMonitorException **
The cost anomaly monitor does not exist for the account.
HTTP Status Code: 400

## See Also
<a name="API_GetAnomalyMonitors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetAnomalyMonitors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetAnomalyMonitors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetAnomalyMonitors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetAnomalyMonitors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetAnomalyMonitors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetAnomalyMonitors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetAnomalyMonitors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetAnomalyMonitors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetAnomalyMonitors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetAnomalyMonitors)
