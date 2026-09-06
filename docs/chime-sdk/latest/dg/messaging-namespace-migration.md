---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/messaging-namespace-migration.html
---

# Migrating to the Amazon Chime SDK messaging namespace
<a name="messaging-namespace-migration"></a>

The [Amazon Chime SDK Messaging](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Messaging.html) namespace is a dedicated place for the APIs that create and manage Amazon Chime SDK messaging resources. You use the namespace to address Amazon Chime SDK messaging API endpoints in any AWS Region in which they're available. Use this namespace if you're just starting to use the Amazon Chime SDK. For more information about Regions, refer to [Available AWS Regions for the Amazon Chime SDK](sdk-available-regions.md) in this guide.

Existing applications that use the [Amazon Chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime.html) namespace should plan to migrate to the dedicated namespace.

**Topics**
+ [Reasons to migrate](#migration-reasons)
+ [Before you migrate](#before-migrating)
+ [Differences between the namespaces](#namespace-differences)

## Reasons to migrate
<a name="migration-reasons"></a>

We encourage you to migrate to the [Amazon Chime SDK Messaging](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Messaging.html) namespace for these reasons:

**Choice of API Endpoint**
The Amazon Chime SDK Messaging namespace is the only API namespace which can use API endpoints in any [Region that makes them available](https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-available-regions.html). If you want to use API endpoints other than US East (N. Virginia), you must use the Amazon Chime SDK Messaging namespace.
For more information about how Amazon Chime SDK messaging uses AWS Regions, refer to [Available Regions](https://docs.aws.amazon.com/chime-sdk/latest/dg/available-regions.html) in this guide.

**Updated and new messaging APIs**
We only add or update messaging APIs in the Amazon Chime SDK Messaging namespace.

## Before you migrate
<a name="before-migrating"></a>

Before you migrate, be aware of the differences between the namespaces. The following table lists and describes them.

|  | Amazon Chime SDK Messaging namespace | Amazon Chime namespace |
| --- | --- | --- |
| AWS SDK namespace | ChimeSDKMessaging | Chime |
| Regions | Multiple | US East (N. Virginia) only |
| APIs | Only APIs for messaging | APIs for messaging and other parts of Amazon Chime |
| Flows | Available | Not available |
| Elastic channels | Available | Not available |

## Differences between the namespaces
<a name="namespace-differences"></a>

The following sections explain the differences between the `Amazon Chime` and `Amazon Chime SDK Messaging` namespaces.

**AWS SDK namespace**
The Amazon Chime SDK namespace uses the `Chime` formal name. The Amazon Chime SDK Messaging namespace uses the `ChimeSDKMessaging` formal name. The precise format of the name varies by platform.

For example, if you use the AWS SDK in Node.js to create messaging, you use a line of code to address the namespace.

```
const chimeMessaging = AWS.Chime();
```

To migrate to the Amazon Chime Messaging SDK, update this line of code with the new namespace and the endpoint region.

```
const chimeMessaging = AWS.ChimeSDKMessaging({ region: "{{Europe (Frankfurt)}}" });
```

**Regions**
The [Amazon Chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime.html) namespace can only address API endpoints in the `US East (N. Virginia)` Region. The [Amazon Chime SDK Messaging](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Messaging.html) namespace can address Amazon Chime SDK messaging API endpoints in any Region they're available. For a current list of messaging Regions, refer to [Available AWS Regions for the Amazon Chime SDK](sdk-available-regions.md) in this guide.

**Endpoints**
The [Amazon Chime SDK Messaging](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Messaging.html) namespace uses different API endpoints than the [Amazon Chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime.html) namespace.

Only the endpoint used to create a messaging resource can be used to modify it. This means a messaging resource created via an endpoint in `Europe (Frankfurt)` can only be modified via `Europe (Frankfurt)`. This means that a channel created via an endpoint in Europe (Frankfurt) can only be modified via Europe (Frankfurt). It also means that you cannot address a channel created via the `Chime` namespace with the `ChimeSDKMessaging` namespace in US East (N. Virginia). For more information about the current endpoints, refer to [API mapping](migrate-from-chm-namespace.md#name-end-map) in this guide.

**Service principal**
The [Amazon Chime SDK Messaging](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Messaging.html) namespace uses a new service principal: `messaging.chime.amazonaws.com`. If you have SQS, SNS, or other IAM access policies that grant access to the service, you need to update those polices to grant access to the new service principal.

**APIs**
The [Amazon Chime SDK Messaging](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Messaging.html) namespace only contains APIs for creating and managing messaging resources, and for sending and receiving messages. The [Amazon Chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime.html) namespace includes APIs for other parts of the Amazon Chime service as well as messaging.

**Channel flows**
Channel flows allow developers to run business logic on in-flight messages before they are delivered to members of a messaging channel. For example, you can create flows that remove sensitive data such as government ID numbers, phone numbers, or profanity from messages before they are delivered. That can help implement corporate communications policies or other communication guidelines.

You can also use channel flows to perform functions such as aggregating responses to a poll before sending the results back to participants, or sending messages via SMS.

Channel Flows are only available in the `ChimeSDKMessaging` namespace. For more information about them, refer to [Using channel flows to process messages for Amazon Chime SDK messaging](using-channel-flows.md) in this guide.

**Elastic channels**
Elastic channels support large scale chat experiences with up to one million chat users automatically balanced across a defined number of sub-channels. Elastic channels are only available in the `ChimeSDKMessaging` endpoint. For more information about elastic channels, refer to [Using elastic channels to host live events in Amazon Chime SDK meetings](elastic-channels.md) in this guide.

**Additional APIs**
The Messaging namespace has a growing list of APIs that the `Chime` namespace does not have. If you are getting started with the Amazon Chime SDK use the messaging namespace for access to all of the latest features. For more information about the current APIs, refer to [Amazon Chime SDK Messaging](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Messaging.html) in the *Amazon Chime SDK API Reference*.
