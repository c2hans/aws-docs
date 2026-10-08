---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostForecast.html
---

# GetCostForecast
<a name="API_GetCostForecast"></a>

Retrieves a forecast for how much Amazon Web Services predicts that you will spend over the forecast time period that you select, based on your past costs.

## Request Syntax
<a name="API_GetCostForecast_RequestSyntax"></a>

```
{
   "BillingViewArn": "{{string}}",
   "Filter": {
      "And": [
         "Expression"
      ],
      "CostCategories": {
         "Key": "{{string}}",
         "MatchOptions": [ "{{string}}" ],
         "Values": [ "{{string}}" ]
      },
      "Dimensions": {
         "Key": "{{string}}",
         "MatchOptions": [ "{{string}}" ],
         "Values": [ "{{string}}" ]
      },
      "Not": "Expression",
      "Or": [
         "Expression"
      ],
      "ProductAttributes": {
         "Key": "{{string}}",
         "MatchOptions": [ "{{string}}" ],
         "Values": [ "{{string}}" ]
      },
      "Tags": {
         "Key": "{{string}}",
         "MatchOptions": [ "{{string}}" ],
         "Values": [ "{{string}}" ]
      }
   },
   "Granularity": "{{string}}",
   "Metric": "{{string}}",
   "PredictionIntervalLevel": {{number}},
   "TimePeriod": {
      "End": "{{string}}",
      "Start": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GetCostForecast_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BillingViewArn](#API_GetCostForecast_RequestSyntax) **   <a name="awscostmanagement-GetCostForecast-request-BillingViewArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to AWS Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[-a-zA-Z0-9/:_+=.-@]{1,43}$`
Required: No

 ** [Filter](#API_GetCostForecast_RequestSyntax) **   <a name="awscostmanagement-GetCostForecast-request-Filter"></a>
The filters that you want to use to filter your forecast. The `GetCostForecast` API supports filtering by the following dimensions:
+  `AZ`
+  `INSTANCE_TYPE`
+  `LINKED_ACCOUNT`
+  `OPERATION`
+  `PURCHASE_TYPE`
+  `REGION`
+  `SERVICE`
+  `USAGE_TYPE`
+  `USAGE_TYPE_GROUP`
+  `RECORD_TYPE`
+  `OPERATING_SYSTEM`
+  `TENANCY`
+  `SCOPE`
+  `PLATFORM`
+  `SUBSCRIPTION_ID`
+  `LEGAL_ENTITY_NAME`
+  `DEPLOYMENT_OPTION`
+  `DATABASE_ENGINE`
+  `INSTANCE_TYPE_FAMILY`
+  `BILLING_ENTITY`
+  `RESERVATION_ID`
+  `SAVINGS_PLAN_ARN`
Type: [Expression](API_Expression.md) object
Required: No

 ** [Granularity](#API_GetCostForecast_RequestSyntax) **   <a name="awscostmanagement-GetCostForecast-request-Granularity"></a>
How granular you want the forecast to be. You can get 3 months of `DAILY` forecasts or 18 months of `MONTHLY` forecasts.
The `GetCostForecast` operation supports only `DAILY` and `MONTHLY` granularities.
Type: String
Valid Values: `DAILY | MONTHLY | HOURLY`
Required: Yes

 ** [Metric](#API_GetCostForecast_RequestSyntax) **   <a name="awscostmanagement-GetCostForecast-request-Metric"></a>
Which metric Cost Explorer uses to create your forecast. For more information about blended and unblended rates, see [Why does the "blended" annotation appear on some line items in my bill?](http://aws.amazon.com/premiumsupport/knowledge-center/blended-rates-intro/).
Valid values for a `GetCostForecast` call are the following:
+ AMORTIZED\_COST
+ BLENDED\_COST
+ NET\_AMORTIZED\_COST
+ NET\_UNBLENDED\_COST
+ UNBLENDED\_COST
Type: String
Valid Values: `BLENDED_COST | UNBLENDED_COST | AMORTIZED_COST | NET_UNBLENDED_COST | NET_AMORTIZED_COST | USAGE_QUANTITY | NORMALIZED_USAGE_AMOUNT`
Required: Yes

 ** [PredictionIntervalLevel](#API_GetCostForecast_RequestSyntax) **   <a name="awscostmanagement-GetCostForecast-request-PredictionIntervalLevel"></a>
Cost Explorer always returns the mean forecast as a single point. You can request a prediction interval around the mean by specifying a confidence level. The higher the confidence level, the more confident Cost Explorer is about the actual value falling in the prediction interval. Higher confidence levels result in wider prediction intervals.
Type: Integer
Valid Range: Minimum value of 51. Maximum value of 99.
Required: No

 ** [TimePeriod](#API_GetCostForecast_RequestSyntax) **   <a name="awscostmanagement-GetCostForecast-request-TimePeriod"></a>
The period of time that you want the forecast to cover. The start date must be equal to or no later than the current date to avoid a validation error.
Type: [DateInterval](API_DateInterval.md) object
Required: Yes

## Response Syntax
<a name="API_GetCostForecast_ResponseSyntax"></a>

```
{
   "ForecastResultsByTime": [
      {
         "MeanValue": "string",
         "PredictionIntervalLowerBound": "string",
         "PredictionIntervalUpperBound": "string",
         "TimePeriod": {
            "End": "string",
            "Start": "string"
         }
      }
   ],
   "Total": {
      "Amount": "string",
      "Unit": "string"
   }
}
```

## Response Elements
<a name="API_GetCostForecast_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ForecastResultsByTime](#API_GetCostForecast_ResponseSyntax) **   <a name="awscostmanagement-GetCostForecast-response-ForecastResultsByTime"></a>
The forecasts for your query, in order. For `DAILY` forecasts, this is a list of days. For `MONTHLY` forecasts, this is a list of months.
Type: Array of [ForecastResult](API_ForecastResult.md) objects

 ** [Total](#API_GetCostForecast_ResponseSyntax) **   <a name="awscostmanagement-GetCostForecast-response-Total"></a>
How much you are forecasted to spend over the forecast period, in `USD`.
Type: [MetricValue](API_MetricValue.md) object

## Errors
<a name="API_GetCostForecast_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BillingViewHealthStatusException **
 The billing view status must be `HEALTHY` to perform this action. Try again when the status is `HEALTHY`.
HTTP Status Code: 400

 ** DataUnavailableException **
The requested data is unavailable.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_GetCostForecast_Examples"></a>

### Example
<a name="API_GetCostForecast_Example_1"></a>

The following example shows how to retrieve a forecast using the `GetCostForecast` operation.

#### Sample Request
<a name="API_GetCostForecast_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ce.us-east-1.amazonaws.com
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSInsightsIndexService.GetCostForecast
{
  "TimePeriod": {
    "Start":"2017-10-25",
    "End": "2017-10-27"
  },
  "Granularity": "DAILY",
  "Filter": {
    "Dimensions": {
      "Key": "SERVICE",
      "Values": [
        "Amazon Simple Storage Service"
      ]
    }
  },
  "Metric":"BLENDED_COST",
  "PredictionIntervalLevel":85
}
```

#### Sample Response
<a name="API_GetCostForecast_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "ForecastResultsByTime": [
    {
      "MeanValue": "37.0786663399",
      "PredictionIntervalLowerBound": "34.9970026341",
      "PredictionIntervalUpperBound": "39.1603300457",
      "TimePeriod": {
        "End": "2018-10-26",
        "Start": "2018-10-25"
      }
    },
    {
      "MeanValue": "37.0786663399",
      "PredictionIntervalLowerBound": "34.9970026341",
      "PredictionIntervalUpperBound": "39.1603300457",
      "TimePeriod": {
        "End": "2018-10-27",
        "Start": "2018-10-26"
      }
    }
  ],
  "Total": {
      "Amount": "74.1573326798",
      "Unit": "USD"
  }
}
```

## See Also
<a name="API_GetCostForecast_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetCostForecast)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetCostForecast)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetCostForecast)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetCostForecast)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetCostForecast)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetCostForecast)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetCostForecast)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetCostForecast)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetCostForecast)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetCostForecast)
