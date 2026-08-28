---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetAnomalySubscriptions.html
---

# GetAnomalySubscriptions
<a name="API_GetAnomalySubscriptions"></a>

Retrieves the cost anomaly subscription objects for your account. You can filter using a list of cost anomaly monitor Amazon Resource Names (ARNs).

## Request Syntax
<a name="API_GetAnomalySubscriptions_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "MonitorArn": "{{string}}",
   "NextPageToken": "{{string}}",
   "SubscriptionArnList": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetAnomalySubscriptions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetAnomalySubscriptions_RequestSyntax) **   <a name="awscostmanagement-GetAnomalySubscriptions-request-MaxResults"></a>
The number of entries a paginated response contains.
Type: Integer
Required: No

 ** [MonitorArn](#API_GetAnomalySubscriptions_RequestSyntax) **   <a name="awscostmanagement-GetAnomalySubscriptions-request-MonitorArn"></a>
Cost anomaly monitor ARNs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** [NextPageToken](#API_GetAnomalySubscriptions_RequestSyntax) **   <a name="awscostmanagement-GetAnomalySubscriptions-request-NextPageToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [SubscriptionArnList](#API_GetAnomalySubscriptions_RequestSyntax) **   <a name="awscostmanagement-GetAnomalySubscriptions-request-SubscriptionArnList"></a>
A list of cost anomaly subscription ARNs.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_GetAnomalySubscriptions_ResponseSyntax"></a>

```
{
   "AnomalySubscriptions": [
      {
         "AccountId": "string",
         "Frequency": "string",
         "MonitorArnList": [ "string" ],
         "Subscribers": [
            {
               "Address": "string",
               "Status": "string",
               "Type": "string"
            }
         ],
         "SubscriptionArn": "string",
         "SubscriptionName": "string",
         "Threshold": number,
         "ThresholdExpression": {
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
         }
      }
   ],
   "NextPageToken": "string"
}
```

## Response Elements
<a name="API_GetAnomalySubscriptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AnomalySubscriptions](#API_GetAnomalySubscriptions_ResponseSyntax) **   <a name="awscostmanagement-GetAnomalySubscriptions-response-AnomalySubscriptions"></a>
A list of cost anomaly subscriptions that includes the detailed metadata for each one.
Type: Array of [AnomalySubscription](API_AnomalySubscription.md) objects

 ** [NextPageToken](#API_GetAnomalySubscriptions_ResponseSyntax) **   <a name="awscostmanagement-GetAnomalySubscriptions-response-NextPageToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

## Errors
<a name="API_GetAnomalySubscriptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The pagination token is invalid. Try again without a pagination token.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** UnknownSubscriptionException **
The cost anomaly subscription does not exist for the account.
HTTP Status Code: 400

## See Also
<a name="API_GetAnomalySubscriptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetAnomalySubscriptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetAnomalySubscriptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetAnomalySubscriptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetAnomalySubscriptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetAnomalySubscriptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetAnomalySubscriptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetAnomalySubscriptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetAnomalySubscriptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetAnomalySubscriptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetAnomalySubscriptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
