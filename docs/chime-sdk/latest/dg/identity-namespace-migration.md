---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/identity-namespace-migration.html
---

# Migrating to the Amazon Chime SDK identity namespace
<a name="identity-namespace-migration"></a>

The [Amazon Chime SDK Identity](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Identity.html) namespace is a dedicated place for the APIs used to create and manage Amazon Chime SDK identity resources, including AppInstances and AppInstanceUsers. You use the namespace to address Amazon Chime SDK identity API endpoints in any AWS Region in which they're available. Use this namespace if you're just starting to use the Amazon Chime SDK. For more information about Regions, refer to [Available AWS Regions for the Amazon Chime SDK](sdk-available-regions.md) in this guide.

Existing applications that use the [Amazon Chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime.html) namespace should plan to migrate to the dedicated namespace.

**Topics**
+ [Reasons to migrate](#identity-migration-reasons)
+ [Before you migrate](#id-before-migrating)
+ [Differences between the namespaces](#id-namespace-differences)

## Reasons to migrate
<a name="identity-migration-reasons"></a>

We encourage you to migrate to the [Amazon Chime SDK Identity](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Identity.html) namespace for these reasons:

**Choice of API Endpoint**
The Amazon Chime SDK Identity namespace is the only API namespace that can use API endpoints in any [Region that makes them available](https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-available-regions.html). If you want to use API endpoints other than `us-east-1`, you must use the Amazon Chime SDK Identity namespace. For more information about the current endpoints, refer to [API mapping](migrate-from-chm-namespace.md#name-end-map) in this guide.

**Updated and new messaging APIs**
We only add or update identity APIs in the Amazon Chime SDK Identity namespace.

## Before you migrate
<a name="id-before-migrating"></a>

Before you migrate, be aware of the differences between the namespaces. The following table lists and describes them.

|  | Amazon Chime SDK Identity namespace | Amazon Chime namespace |
| --- | --- | --- |
| AWS SDK namespace | ChimeSDKIdentity | Chime |
| Regions | Multiple | us-east-1 only |
| Service principal | https://identity.chime.amazonaws.com | https://chime.amazonaws.com |
| APIs | Only APIs for identity | APIs for identity and other parts of Amazon Chime |
| User Expiration | Available | Not available |
| Bots | Available | Not available |

## Differences between the namespaces
<a name="id-namespace-differences"></a>

The following sections explain the differences between the `Chime` and `ChimeSDKIdentity` namespaces.

**AWS SDK namespace**
The Amazon Chime SDK namespace uses the `Chime` formal name. The Amazon Chime SDK Identity namespace uses the `ChimeSDKIdentity` formal name. The precise format of the name varies by platform.

For example, if you use the AWS SDK in Node.js to create identities, you use a line of code to address the namespace.

```
const chimeIdentity = AWS.Chime();
```

To migrate to the `ChimeSDKIdentity` namespace, update this line of code with the new namespace and the endpoint region.

```
const chimeIdentity = AWS.ChimeSDKIdentity({ region: "{{eu-central-1}}" });
```

**Regions**
The [Amazon Chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime.html) namespace can only address API endpoints in the `us-east-1` Region. The [Amazon Chime SDK Identity](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Identity.html) namespace can address Amazon Chime SDK Identity API endpoints in any Region they are available. For a current list of endpoints Regions, refer to [Available AWS Regions for the Amazon Chime SDK](sdk-available-regions.md) in this guide.

**Endpoints**
The [Amazon Chime SDK Identity](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Identity.html) namespace uses different API endpoints than the [Amazon Chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime.html) namespace.

Only the endpoint used to create identity resources can be used to update them. This means an AppInstance created via an endpoint in `eu-central-1` can only be modified via `eu-central-1`. It also means you cannot address an AppInstance created via the Chime namespace with the ChimeSDKIdentity namespace in `us-east-1`, or create a channel in a Region other than the region where the AppInstance and AppInstanceUser members were created. For more information about the current endpoints, refer to [API mapping](migrate-from-chm-namespace.md#name-end-map) in this guide.

**Service principal**
The [Amazon Chime SDK Identity](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Messaging.html) namespace uses a new service principal: `Identity.chime.amazonaws.com`. If you have SQS, SNS, or other IAM access policies that grant access to the service, you need to update those polices to grant access to the new service principal.

**APIs**
The [Amazon Chime SDK Identity](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Identity.html) namespace only contains APIs for creating and managing messaging resources, and for sending and receiving messages. The [Amazon Chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime.html) namespace includes APIs for other parts of the Amazon Chime service as well as messaging.

**User expiration**
Expiration settings on creation of AppInstanceUsers allow you to create temporary users. For example, you can create chat users that only exist for the duration of a large broadcast. Only the Identity namespace supports expiration settings for AppInstanceUsers.

**Bots**
You use the [AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_AppInstanceBot.html) API to add chat bots powered by Amazon Lex V2 into your applications. You can only use AppInstanceBots in the Identity namespace. For more information about bots, refer to [Using AppInstanceBots as intelligent channel agents for Amazon Chime SDK messaging](appinstance-bots.md) in this guide.

**Additional APIs**
The Identity namespace has a growing list of additional APIs that the Chime namespace does not have. If you are getting started with the Amazon Chime SDK, use the Identity namespace to have access to all of the latest features. For more information about the current APIs, refer to [Amazon Chime SDK Identity](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Identity.html) in the *Amazon Chime SDK API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
