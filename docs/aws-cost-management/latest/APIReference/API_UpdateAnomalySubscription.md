---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateAnomalySubscription.html
---

# UpdateAnomalySubscription
<a name="API_UpdateAnomalySubscription"></a>

Updates an existing cost anomaly subscription. Specify the fields that you want to update. Omitted fields are unchanged.

**Note**
The JSON below describes the generic construct for each type. See [Request Parameters](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateAnomalySubscription.html#API_UpdateAnomalySubscription_RequestParameters) for possible values as they apply to `AnomalySubscription`.

## Request Syntax
<a name="API_UpdateAnomalySubscription_RequestSyntax"></a>

```
{
   "Frequency": "{{string}}",
   "MonitorArnList": [ "{{string}}" ],
   "Subscribers": [
      {
         "Address": "{{string}}",
         "Status": "{{string}}",
         "Type": "{{string}}"
      }
   ],
   "SubscriptionArn": "{{string}}",
   "SubscriptionName": "{{string}}",
   "Threshold": {{number}},
   "ThresholdExpression": {
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
      "Tags": {
         "Key": "{{string}}",
         "MatchOptions": [ "{{string}}" ],
         "Values": [ "{{string}}" ]
      }
   }
}
```

## Request Parameters
<a name="API_UpdateAnomalySubscription_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Frequency](#API_UpdateAnomalySubscription_RequestSyntax) **   <a name="awscostmanagement-UpdateAnomalySubscription-request-Frequency"></a>
The update to the frequency value that subscribers receive notifications.
Type: String
Valid Values: `DAILY | IMMEDIATE | WEEKLY`
Required: No

 ** [MonitorArnList](#API_UpdateAnomalySubscription_RequestSyntax) **   <a name="awscostmanagement-UpdateAnomalySubscription-request-MonitorArnList"></a>
A list of cost anomaly monitor ARNs.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: No

 ** [Subscribers](#API_UpdateAnomalySubscription_RequestSyntax) **   <a name="awscostmanagement-UpdateAnomalySubscription-request-Subscribers"></a>
The update to the subscriber list.
Type: Array of [Subscriber](API_Subscriber.md) objects
Required: No

 ** [SubscriptionArn](#API_UpdateAnomalySubscription_RequestSyntax) **   <a name="awscostmanagement-UpdateAnomalySubscription-request-SubscriptionArn"></a>
A cost anomaly subscription Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** [SubscriptionName](#API_UpdateAnomalySubscription_RequestSyntax) **   <a name="awscostmanagement-UpdateAnomalySubscription-request-SubscriptionName"></a>
The new name of the subscription.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** [Threshold](#API_UpdateAnomalySubscription_RequestSyntax) **   <a name="awscostmanagement-UpdateAnomalySubscription-request-Threshold"></a>
(deprecated)
The update to the threshold value for receiving notifications.
This field has been deprecated. To update a threshold, use ThresholdExpression. Continued use of Threshold will be treated as shorthand syntax for a ThresholdExpression.
You can specify either Threshold or ThresholdExpression, but not both.
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** [ThresholdExpression](#API_UpdateAnomalySubscription_RequestSyntax) **   <a name="awscostmanagement-UpdateAnomalySubscription-request-ThresholdExpression"></a>
The update to the [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html) object used to specify the anomalies that you want to generate alerts for. This supports dimensions and nested expressions. The supported dimensions are `ANOMALY_TOTAL_IMPACT_ABSOLUTE` and `ANOMALY_TOTAL_IMPACT_PERCENTAGE`, corresponding to an anomaly’s TotalImpact and TotalImpactPercentage, respectively (see [Impact](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html) for more details). The supported nested expression types are `AND` and `OR`. The match option `GREATER_THAN_OR_EQUAL` is required. Values must be numbers between 0 and 10,000,000,000 in string format.
You can specify either Threshold or ThresholdExpression, but not both.
The following are examples of valid ThresholdExpressions:
+ Absolute threshold: `{ "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_ABSOLUTE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }`
+ Percentage threshold: `{ "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_PERCENTAGE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }`
+  `AND` two thresholds together: `{ "And": [ { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_ABSOLUTE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }, { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_PERCENTAGE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } } ] }`
+  `OR` two thresholds together: `{ "Or": [ { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_ABSOLUTE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }, { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_PERCENTAGE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } } ] }`
Type: [Expression](API_Expression.md) object
Required: No

## Response Syntax
<a name="API_UpdateAnomalySubscription_ResponseSyntax"></a>

```
{
   "SubscriptionArn": "string"
}
```

## Response Elements
<a name="API_UpdateAnomalySubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SubscriptionArn](#API_UpdateAnomalySubscription_ResponseSyntax) **   <a name="awscostmanagement-UpdateAnomalySubscription-response-SubscriptionArn"></a>
A cost anomaly subscription ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`

## Errors
<a name="API_UpdateAnomalySubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** UnknownMonitorException **
The cost anomaly monitor does not exist for the account.
HTTP Status Code: 400

 ** UnknownSubscriptionException **
The cost anomaly subscription does not exist for the account.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAnomalySubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/UpdateAnomalySubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/UpdateAnomalySubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/UpdateAnomalySubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/UpdateAnomalySubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/UpdateAnomalySubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/UpdateAnomalySubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/UpdateAnomalySubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/UpdateAnomalySubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/UpdateAnomalySubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/UpdateAnomalySubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
