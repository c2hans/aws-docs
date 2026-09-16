---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CreateAnomalySubscription.html
---

# CreateAnomalySubscription
<a name="API_CreateAnomalySubscription"></a>

Adds an alert subscription to a cost anomaly detection monitor. You can use each subscription to define subscribers with email or SNS notifications. Email subscribers can set an absolute or percentage threshold and a time frequency for receiving notifications.

## Request Syntax
<a name="API_CreateAnomalySubscription_RequestSyntax"></a>

```
{
   "AnomalySubscription": {
      "AccountId": "{{string}}",
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
   },
   "ResourceTags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateAnomalySubscription_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AnomalySubscription](#API_CreateAnomalySubscription_RequestSyntax) **   <a name="awscostmanagement-CreateAnomalySubscription-request-AnomalySubscription"></a>
The cost anomaly subscription object that you want to create.
Type: [AnomalySubscription](API_AnomalySubscription.md) object
Required: Yes

 ** [ResourceTags](#API_CreateAnomalySubscription_RequestSyntax) **   <a name="awscostmanagement-CreateAnomalySubscription-request-ResourceTags"></a>
An optional list of tags to associate with the specified [`AnomalySubscription`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html). You can use resource tags to control access to your `subscription` using IAM policies.
Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags:
+ Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for AWS use
+ The maximum length of a key is 128 characters
+ The maximum length of a value is 256 characters
+ Keys and values can only contain alphanumeric characters, spaces, and any of the following: `_.:/=+@-`
+ Keys and values are case sensitive
+ Keys and values are trimmed for any leading or trailing whitespaces
+ Don’t use `aws:` as a prefix for your keys. This prefix is reserved for AWS use
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateAnomalySubscription_ResponseSyntax"></a>

```
{
   "SubscriptionArn": "string"
}
```

## Response Elements
<a name="API_CreateAnomalySubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SubscriptionArn](#API_CreateAnomalySubscription_ResponseSyntax) **   <a name="awscostmanagement-CreateAnomalySubscription-response-SubscriptionArn"></a>
The unique identifier of your newly created cost anomaly subscription.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`

## Errors
<a name="API_CreateAnomalySubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** UnknownMonitorException **
The cost anomaly monitor does not exist for the account.
HTTP Status Code: 400

## See Also
<a name="API_CreateAnomalySubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/CreateAnomalySubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/CreateAnomalySubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CreateAnomalySubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/CreateAnomalySubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CreateAnomalySubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/CreateAnomalySubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/CreateAnomalySubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/CreateAnomalySubscription)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/CreateAnomalySubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CreateAnomalySubscription)
