---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_UpdateAccountSettings.html
---

# UpdateAccountSettings
<a name="API_query_UpdateAccountSettings"></a>

Transitions your account to use TCUs for query pricing and modifies the maximum query compute units that you've configured. If you reduce the value of `MaxQueryTCU` to a desired configuration, the new value can take up to 24 hours to be effective.

**Note**
After you've transitioned your account to use TCUs for query pricing, you can't transition to using bytes scanned for query pricing.

## Request Syntax
<a name="API_query_UpdateAccountSettings_RequestSyntax"></a>

```
{
   "MaxQueryTCU": {{number}},
   "QueryCompute": {
      "ComputeMode": "{{string}}",
      "ProvisionedCapacity": {
         "NotificationConfiguration": {
            "RoleArn": "{{string}}",
            "SnsConfiguration": {
               "TopicArn": "{{string}}"
            }
         },
         "TargetQueryTCU": {{number}}
      }
   },
   "QueryPricingModel": "{{string}}"
}
```

## Request Parameters
<a name="API_query_UpdateAccountSettings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxQueryTCU](#API_query_UpdateAccountSettings_RequestSyntax) **   <a name="timestream-query_UpdateAccountSettings-request-MaxQueryTCU"></a>
The maximum number of compute units the service will use at any point in time to serve your queries. To run queries, you must set a minimum capacity of 4 TCU. You can set the maximum number of TCU in multiples of 4, for example, 4, 8, 16, 32, and so on. The maximum value supported for `MaxQueryTCU` is 1000. To request an increase to this soft limit, contact AWS Support. For information about the default quota for maxQueryTCU, see Default quotas. This configuration is applicable only for on-demand usage of Timestream Compute Units (TCUs).
The maximum value supported for `MaxQueryTCU` is 1000. To request an increase to this soft limit, contact AWS Support. For information about the default quota for `maxQueryTCU`, see [Default quotas](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html#limits.default).
Type: Integer
Required: No

 ** [QueryCompute](#API_query_UpdateAccountSettings_RequestSyntax) **   <a name="timestream-query_UpdateAccountSettings-request-QueryCompute"></a>
Modifies the query compute settings configured in your account, including the query pricing model and provisioned Timestream Compute Units (TCUs) in your account. QueryCompute is available only in the Asia Pacific (Mumbai) region.
This API is idempotent, meaning that making the same request multiple times will have the same effect as making the request once.
Type: [QueryComputeRequest](API_query_QueryComputeRequest.md) object
Required: No

 ** [QueryPricingModel](#API_query_UpdateAccountSettings_RequestSyntax) **   <a name="timestream-query_UpdateAccountSettings-request-QueryPricingModel"></a>
The pricing model for queries in an account.
The `QueryPricingModel` parameter is used by several Timestream operations; however, the `UpdateAccountSettings` API operation doesn't recognize any values other than `COMPUTE_UNITS`.
Type: String
Valid Values: `BYTES_SCANNED | COMPUTE_UNITS`
Required: No

## Response Syntax
<a name="API_query_UpdateAccountSettings_ResponseSyntax"></a>

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
<a name="API_query_UpdateAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MaxQueryTCU](#API_query_UpdateAccountSettings_ResponseSyntax) **   <a name="timestream-query_UpdateAccountSettings-response-MaxQueryTCU"></a>
The configured maximum number of compute units the service will use at any point in time to serve your queries.
Type: Integer

 ** [QueryCompute](#API_query_UpdateAccountSettings_ResponseSyntax) **   <a name="timestream-query_UpdateAccountSettings-response-QueryCompute"></a>
Confirms the updated account settings for querying data in your account. QueryCompute is available only in the Asia Pacific (Mumbai) region.
Type: [QueryComputeResponse](API_query_QueryComputeResponse.md) object

 ** [QueryPricingModel](#API_query_UpdateAccountSettings_ResponseSyntax) **   <a name="timestream-query_UpdateAccountSettings-response-QueryPricingModel"></a>
The pricing model for an account.
Type: String
Valid Values: `BYTES_SCANNED | COMPUTE_UNITS`

## Errors
<a name="API_query_UpdateAccountSettings_Errors"></a>

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

 ** ValidationException **
 Invalid or malformed request.
HTTP Status Code: 400

## See Also
<a name="API_query_UpdateAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-query-2018-11-01/UpdateAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-query-2018-11-01/UpdateAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/UpdateAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-query-2018-11-01/UpdateAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/UpdateAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-query-2018-11-01/UpdateAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-query-2018-11-01/UpdateAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-query-2018-11-01/UpdateAccountSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-query-2018-11-01/UpdateAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/UpdateAccountSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
