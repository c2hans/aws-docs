---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameSessionQueueLogConfiguration.html
---

# GameSessionQueueLogConfiguration
<a name="API_GameSessionQueueLogConfiguration"></a>

A configuration that delivers game session placement insight logs to one or more destinations of your choice.

## Contents
<a name="API_GameSessionQueueLogConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DeliveryDestinations **   <a name="gameliftservers-Type-GameSessionQueueLogConfiguration-DeliveryDestinations"></a>
The destinations that receive game session placement insight logs for the queue. You can specify up to 3 destinations. Each destination must have a unique ARN.
Type: Array of [LogDeliveryDestination](API_LogDeliveryDestination.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: Yes

## See Also
<a name="API_GameSessionQueueLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GameSessionQueueLogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GameSessionQueueLogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GameSessionQueueLogConfiguration)
