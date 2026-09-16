---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_UpdateSubscriptionsToEventBridge.html
---

# UpdateSubscriptionsToEventBridge
<a name="API_UpdateSubscriptionsToEventBridge"></a>

Migrates 10 active and enabled Amazon SNS subscriptions at a time and converts them to corresponding Amazon EventBridge rules. By default, this operation migrates subscriptions only when all your replication instance versions are 3.4.5 or higher. If any replication instances are from versions earlier than 3.4.5, the operation raises an error and tells you to upgrade these instances to version 3.4.5 or higher. To enable migration regardless of version, set the `Force` option to true. However, if you don't upgrade instances earlier than version 3.4.5, some types of events might not be available when you use Amazon EventBridge.

To call this operation, make sure that you have certain permissions added to your user account. For more information, see [Migrating event subscriptions to Amazon EventBridge](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html#CHAP_Events-migrate-to-eventbridge) in the * AWS Database Migration Service User Guide*.

## Request Syntax
<a name="API_UpdateSubscriptionsToEventBridge_RequestSyntax"></a>

```
{
   "ForceMove": {{boolean}}
}
```

## Request Parameters
<a name="API_UpdateSubscriptionsToEventBridge_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ForceMove](#API_UpdateSubscriptionsToEventBridge_RequestSyntax) **   <a name="DMS-UpdateSubscriptionsToEventBridge-request-ForceMove"></a>
When set to true, this operation migrates AWS DMS subscriptions for Amazon SNS notifications no matter what your replication instance version is. If not set or set to false, this operation runs only when all your replication instances are from AWS DMS version 3.4.5 or higher.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateSubscriptionsToEventBridge_ResponseSyntax"></a>

```
{
   "Result": "string"
}
```

## Response Elements
<a name="API_UpdateSubscriptionsToEventBridge_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Result](#API_UpdateSubscriptionsToEventBridge_ResponseSyntax) **   <a name="DMS-UpdateSubscriptionsToEventBridge-response-Result"></a>
A string that indicates how many event subscriptions were migrated and how many remain to be migrated.
Type: String

## Errors
<a name="API_UpdateSubscriptionsToEventBridge_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_UpdateSubscriptionsToEventBridge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/UpdateSubscriptionsToEventBridge)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/UpdateSubscriptionsToEventBridge)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/UpdateSubscriptionsToEventBridge)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/UpdateSubscriptionsToEventBridge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/UpdateSubscriptionsToEventBridge)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/UpdateSubscriptionsToEventBridge)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/UpdateSubscriptionsToEventBridge)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/UpdateSubscriptionsToEventBridge)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/UpdateSubscriptionsToEventBridge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/UpdateSubscriptionsToEventBridge)
