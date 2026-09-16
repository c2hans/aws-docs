---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEventSubscriptions.html
---

# DescribeEventSubscriptions
<a name="API_DescribeEventSubscriptions"></a>

Lists all the event subscriptions for a customer account. The description of a subscription includes `SubscriptionName`, `SNSTopicARN`, `CustomerID`, `SourceType`, `SourceID`, `CreationTime`, and `Status`.

If you specify `SubscriptionName`, this action lists the description for that subscription.

## Request Syntax
<a name="API_DescribeEventSubscriptions_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxRecords": {{number}},
   "SubscriptionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEventSubscriptions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeEventSubscriptions_RequestSyntax) **   <a name="DMS-DescribeEventSubscriptions-request-Filters"></a>
Filters applied to event subscriptions.
Valid filter names: `event-subscription-arn` \| `event-subscription-id`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeEventSubscriptions_RequestSyntax) **   <a name="DMS-DescribeEventSubscriptions-request-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeEventSubscriptions_RequestSyntax) **   <a name="DMS-DescribeEventSubscriptions-request-MaxRecords"></a>
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

 ** [SubscriptionName](#API_DescribeEventSubscriptions_RequestSyntax) **   <a name="DMS-DescribeEventSubscriptions-request-SubscriptionName"></a>
The name of the AWS DMS event subscription to be described.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeEventSubscriptions_ResponseSyntax"></a>

```
{
   "EventSubscriptionsList": [
      {
         "CustomerAwsId": "string",
         "CustSubscriptionId": "string",
         "Enabled": boolean,
         "EventCategoriesList": [ "string" ],
         "SnsTopicArn": "string",
         "SourceIdsList": [ "string" ],
         "SourceType": "string",
         "Status": "string",
         "SubscriptionCreationTime": "string"
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_DescribeEventSubscriptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventSubscriptionsList](#API_DescribeEventSubscriptions_ResponseSyntax) **   <a name="DMS-DescribeEventSubscriptions-response-EventSubscriptionsList"></a>
A list of event subscriptions.
Type: Array of [EventSubscription](API_EventSubscription.md) objects

 ** [Marker](#API_DescribeEventSubscriptions_ResponseSyntax) **   <a name="DMS-DescribeEventSubscriptions-response-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

## Errors
<a name="API_DescribeEventSubscriptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_DescribeEventSubscriptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeEventSubscriptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeEventSubscriptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeEventSubscriptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeEventSubscriptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeEventSubscriptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeEventSubscriptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeEventSubscriptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeEventSubscriptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeEventSubscriptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeEventSubscriptions)
