---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetApproximateUsageRecords.html
---

# GetApproximateUsageRecords
<a name="API_GetApproximateUsageRecords"></a>

Retrieves estimated usage records for hourly granularity or resource-level data at daily granularity.

## Request Syntax
<a name="API_GetApproximateUsageRecords_RequestSyntax"></a>

```
{
   "ApproximationDimension": "{{string}}",
   "Granularity": "{{string}}",
   "Services": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetApproximateUsageRecords_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApproximationDimension](#API_GetApproximateUsageRecords_RequestSyntax) **   <a name="awscostmanagement-GetApproximateUsageRecords-request-ApproximationDimension"></a>
The service to evaluate for the usage records. You can choose resource-level data at daily granularity, or hourly granularity with or without resource-level data.
Type: String
Valid Values: `SERVICE | RESOURCE`
Required: Yes

 ** [Granularity](#API_GetApproximateUsageRecords_RequestSyntax) **   <a name="awscostmanagement-GetApproximateUsageRecords-request-Granularity"></a>
How granular you want the data to be. You can enable data at hourly or daily granularity.
Type: String
Valid Values: `DAILY | MONTHLY | HOURLY`
Required: Yes

 ** [Services](#API_GetApproximateUsageRecords_RequestSyntax) **   <a name="awscostmanagement-GetApproximateUsageRecords-request-Services"></a>
The service metadata for the service or services you want to query. If not specified, all elements are returned.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_GetApproximateUsageRecords_ResponseSyntax"></a>

```
{
   "LookbackPeriod": {
      "End": "string",
      "Start": "string"
   },
   "Services": {
      "string" : number
   },
   "TotalRecords": number
}
```

## Response Elements
<a name="API_GetApproximateUsageRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LookbackPeriod](#API_GetApproximateUsageRecords_ResponseSyntax) **   <a name="awscostmanagement-GetApproximateUsageRecords-response-LookbackPeriod"></a>
The lookback period that's used for the estimation.
Type: [DateInterval](API_DateInterval.md) object

 ** [Services](#API_GetApproximateUsageRecords_ResponseSyntax) **   <a name="awscostmanagement-GetApproximateUsageRecords-response-Services"></a>
The service metadata for the service or services in the response.
Type: String to long map
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[\S\s]*`
Valid Range: Minimum value of 0.

 ** [TotalRecords](#API_GetApproximateUsageRecords_ResponseSyntax) **   <a name="awscostmanagement-GetApproximateUsageRecords-response-TotalRecords"></a>
The total number of usage records for all services in the services list.
Type: Long
Valid Range: Minimum value of 0.

## Errors
<a name="API_GetApproximateUsageRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DataUnavailableException **
The requested data is unavailable.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## Examples
<a name="API_GetApproximateUsageRecords_Examples"></a>

### The following is a sample request of the GetApproximateUsageRecords operation.
<a name="API_GetApproximateUsageRecords_Example_1"></a>

This example illustrates one usage of GetApproximateUsageRecords.

#### Sample Request
<a name="API_GetApproximateUsageRecords_Example_1_Request"></a>

```
{
    "ApproximationDimension":"SERVICE",
    "Granularity": "HOURLY"
 }
```

### The following is a sample response of the GetApproximateUsageRecords operation.
<a name="API_GetApproximateUsageRecords_Example_2"></a>

This example illustrates one usage of GetApproximateUsageRecords.

#### Sample Response
<a name="API_GetApproximateUsageRecords_Example_2_Response"></a>

```
{
    "LookbackPeriod": {
        "End": "2023-12-31",
        "Start": "2023-12-01"
    },
    "Services": {
        "Amazon Virtual Private Cloud": 336,
        "Amazon Relational Database Service": 1344,
        "AmazonCloudWatch": 350,
        "Tax": 0,
        "Amazon DynamoDB": 672
    },
    "TotalRecords": 2702
}
```

## See Also
<a name="API_GetApproximateUsageRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetApproximateUsageRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetApproximateUsageRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetApproximateUsageRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetApproximateUsageRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetApproximateUsageRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetApproximateUsageRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetApproximateUsageRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetApproximateUsageRecords)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetApproximateUsageRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetApproximateUsageRecords)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
