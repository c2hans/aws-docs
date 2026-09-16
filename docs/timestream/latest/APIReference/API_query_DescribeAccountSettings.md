---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_DescribeAccountSettings.html
---

# DescribeAccountSettings
<a name="API_query_DescribeAccountSettings"></a>

Describes the settings for your account that include the query pricing model and the configured maximum TCUs the service can use for your query workload.

You're charged only for the duration of compute units used for your workloads.

## Response Syntax
<a name="API_query_DescribeAccountSettings_ResponseSyntax"></a>

```
{
   "MaxQueryTCU": number,
   "QueryCompute": {
      "ComputeMode": "string",
      "ProvisionedCapacity": {
         "ActiveQueryTCU": number,
         "LastUpdate": {
            "Status": "string",
            "StatusMessage": "string",
            "TargetQueryTCU": number
         },
         "NotificationConfiguration": {
            "RoleArn": "string",
            "SnsConfiguration": {
               "TopicArn": "string"
            }
         }
      }
   },
   "QueryPricingModel": "string"
}
```

## Response Elements
<a name="API_query_DescribeAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MaxQueryTCU](#API_query_DescribeAccountSettings_ResponseSyntax) **   <a name="timestream-query_DescribeAccountSettings-response-MaxQueryTCU"></a>
The maximum number of [Timestream compute units](https://docs.aws.amazon.com/timestream/latest/developerguide/tcu.html) (TCUs) the service will use at any point in time to serve your queries. To run queries, you must set a minimum capacity of 4 TCU. You can set the maximum number of TCU in multiples of 4, for example, 4, 8, 16, 32, and so on. This configuration is applicable only for on-demand usage of (TCUs).
Type: Integer

 ** [QueryCompute](#API_query_DescribeAccountSettings_ResponseSyntax) **   <a name="timestream-query_DescribeAccountSettings-response-QueryCompute"></a>
An object that contains the usage settings for Timestream Compute Units (TCUs) in your account for the query workload. QueryCompute is available only in the Asia Pacific (Mumbai) region.
Type: [QueryComputeResponse](API_query_QueryComputeResponse.md) object

 ** [QueryPricingModel](#API_query_DescribeAccountSettings_ResponseSyntax) **   <a name="timestream-query_DescribeAccountSettings-response-QueryPricingModel"></a>
The pricing model for queries in your account.
The `QueryPricingModel` parameter is used by several Timestream operations; however, the `UpdateAccountSettings` API operation doesn't recognize any values other than `COMPUTE_UNITS`.
Type: String
Valid Values: `BYTES_SCANNED | COMPUTE_UNITS`

## Errors
<a name="API_query_DescribeAccountSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the necessary permissions to access the account settings.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request.
HTTP Status Code: 400

 ** InvalidEndpointException **
The requested endpoint is invalid.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to excessive requests.
HTTP Status Code: 400

## See Also
<a name="API_query_DescribeAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-query-2018-11-01/DescribeAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-query-2018-11-01/DescribeAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/DescribeAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-query-2018-11-01/DescribeAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/DescribeAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-query-2018-11-01/DescribeAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-query-2018-11-01/DescribeAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-query-2018-11-01/DescribeAccountSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/timestream-query-2018-11-01/DescribeAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/DescribeAccountSettings)
