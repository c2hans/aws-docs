---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyEventSubscription.html
---

# ModifyEventSubscription
<a name="API_ModifyEventSubscription"></a>

Modifies an existing AWS DMS event notification subscription.

## Request Syntax
<a name="API_ModifyEventSubscription_RequestSyntax"></a>

```
{
   "Enabled": {{boolean}},
   "EventCategories": [ "{{string}}" ],
   "SnsTopicArn": "{{string}}",
   "SourceType": "{{string}}",
   "SubscriptionName": "{{string}}"
}
```

## Request Parameters
<a name="API_ModifyEventSubscription_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Enabled](#API_ModifyEventSubscription_RequestSyntax) **   <a name="DMS-ModifyEventSubscription-request-Enabled"></a>
 A Boolean value; set to **true** to activate the subscription.
Type: Boolean
Required: No

 ** [EventCategories](#API_ModifyEventSubscription_RequestSyntax) **   <a name="DMS-ModifyEventSubscription-request-EventCategories"></a>
 A list of event categories for a source type that you want to subscribe to. Use the `DescribeEventCategories` action to see a list of event categories.
Type: Array of strings
Required: No

 ** [SnsTopicArn](#API_ModifyEventSubscription_RequestSyntax) **   <a name="DMS-ModifyEventSubscription-request-SnsTopicArn"></a>
 The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
Type: String
Required: No

 ** [SourceType](#API_ModifyEventSubscription_RequestSyntax) **   <a name="DMS-ModifyEventSubscription-request-SourceType"></a>
 The type of AWS DMS resource that generates the events you want to subscribe to.
Valid values: replication-instance \| replication-task
Type: String
Required: No

 ** [SubscriptionName](#API_ModifyEventSubscription_RequestSyntax) **   <a name="DMS-ModifyEventSubscription-request-SubscriptionName"></a>
The name of the AWS DMS event notification subscription to be modified.
Type: String
Required: Yes

## Response Syntax
<a name="API_ModifyEventSubscription_ResponseSyntax"></a>

```
{
   "EventSubscription": {
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
}
```

## Response Elements
<a name="API_ModifyEventSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventSubscription](#API_ModifyEventSubscription_ResponseSyntax) **   <a name="DMS-ModifyEventSubscription-response-EventSubscription"></a>
The modified event subscription.
Type: [EventSubscription](API_EventSubscription.md) object

## Errors
<a name="API_ModifyEventSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** KMSAccessDeniedFault **
The ciphertext references a key that doesn't exist or that the DMS account doesn't have access to.
HTTP Status Code: 400

 ** KMSDisabledFault **
The specified KMS key isn't enabled.
HTTP Status Code: 400

 ** KMSInvalidStateFault **
The state of the specified AWS KMS resource isn't valid for this request.
HTTP Status Code: 400

 ** KMSNotFoundFault **
The specified AWS KMS entity or resource can't be found.
HTTP Status Code: 400

 ** KMSThrottlingFault **
This request triggered AWS KMS request throttling.
HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

 ** ResourceQuotaExceededFault **
The quota for this resource quota has been exceeded.
 ** message **

HTTP Status Code: 400

 ** SNSInvalidTopicFault **
The SNS topic is invalid.
 ** message **

HTTP Status Code: 400

 ** SNSNoAuthorizationFault **
You are not authorized for the SNS subscription.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_ModifyEventSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/ModifyEventSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/ModifyEventSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ModifyEventSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/ModifyEventSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ModifyEventSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/ModifyEventSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/ModifyEventSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/ModifyEventSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/ModifyEventSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ModifyEventSubscription)
