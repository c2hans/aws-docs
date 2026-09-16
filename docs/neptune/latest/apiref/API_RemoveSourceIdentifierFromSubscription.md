---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_RemoveSourceIdentifierFromSubscription.html
---

# RemoveSourceIdentifierFromSubscription
<a name="API_RemoveSourceIdentifierFromSubscription"></a>

Removes a source identifier from an existing event notification subscription.

## Request Parameters
<a name="API_RemoveSourceIdentifierFromSubscription_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceIdentifier **
 The source identifier to be removed from the subscription, such as the **DB instance identifier** for a DB instance or the name of a security group.
Type: String
Required: Yes

 ** SubscriptionName **
The name of the event notification subscription you want to remove a source identifier from.
Type: String
Required: Yes

## Response Elements
<a name="API_RemoveSourceIdentifierFromSubscription_ResponseElements"></a>

The following element is returned by the service.

 ** EventSubscription **
Contains the results of a successful invocation of the [DescribeEventSubscriptions](API_DescribeEventSubscriptions.md) action.
Type: [EventSubscription](API_EventSubscription.md) object

## Errors
<a name="API_RemoveSourceIdentifierFromSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** SourceNotFound **
The source could not be found.
HTTP Status Code: 404

 ** SubscriptionNotFound **
The designated subscription could not be found.
HTTP Status Code: 404

## See Also
<a name="API_RemoveSourceIdentifierFromSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/RemoveSourceIdentifierFromSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/RemoveSourceIdentifierFromSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/RemoveSourceIdentifierFromSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/RemoveSourceIdentifierFromSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/RemoveSourceIdentifierFromSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/RemoveSourceIdentifierFromSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/RemoveSourceIdentifierFromSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/RemoveSourceIdentifierFromSubscription)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/RemoveSourceIdentifierFromSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/RemoveSourceIdentifierFromSubscription)
