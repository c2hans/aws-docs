---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/voice-namespace-migration.html
---

# Migrating to the Amazon Chime SDK voice namespace
<a name="voice-namespace-migration"></a>

The [Amazon Chime SDK Voice](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Voice.html) namespace is a dedicated place for the APIs that create and manage Amazon Chime SDK voice resources. You use the namespace to address Amazon Chime SDK voice API endpoints in any AWS Region that makes them available. If you're just starting to use the Amazon Chime SDK, use this namespace. For more information about Regions, refer to [Available AWS Regions for the Amazon Chime SDK](sdk-available-regions.md) in this guide.

Existing applications that use the [Amazon Chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime.html) namespace should plan to migrate to the dedicated namespace in order to use updated APIs and new features.

**Topics**
+ [Reasons to migrate](#first-concept-chapter)
+ [Before you migrate](#voice-before-migrate)
+ [Differences between the namespaces](#voice-namespace-diffs)

## Reasons to migrate
<a name="first-concept-chapter"></a>

We recommend migrating to the [Amazon Chime SDK Voice](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Voice.html) namespace for the following reasons:

**Choice of API endpoint**
The Amazon Chime SDK Voice namespace allows you to use API endpoints in any [Region that makes them available](https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-available-regions.html). If you want to use API endpoints other than `us-east-1`, you must use the Amazon Chime SDK Voice namespace. For more information about the current endpoints, refer to [API mapping](migrate-from-chm-namespace.md#name-end-map) in this guide.

**Updated and new voice APIs**
We only add or update voice APIs in the Amazon Chime SDK Voice namespace.

## Before you migrate
<a name="voice-before-migrate"></a>

Before you migrate, be aware of the differences between the namespaces. The following table lists and describes them.

|  | Amazon Chime SDK Voice namespace | Amazon Chime namespace |
| --- | --- | --- |
| **AWS namespace** | `ChimeSDKVoice` | `Chime` |
| **Regions** | Multiple | `us-east-1` only |
| **Endpoints** | `https://voice-chime.region.amazonaws.com` | `service.chime.aws.amazon.com` |
| **Service principal** | `chime.amazonaws.com` | `chime.amazonaws.com` |
| **APIs** | Only APIs for the PSTN audio service | APIs for PSTN audio and other parts of Amazon Chime |
| Voice Connector management | Multiple Regions | us-east-1 |
| Voice Connector group management | Multiple Regions | us-east-1 |
| SIP media application and SIP rule management | Multiple Regions | us-east-1 |
| Phone number management | Multiple Regions | us-east-1 |
| Call Analytics | Available | Not available |
| Voice Profile Domains | Available | Not available |
| Emergency calling management | Multiple Regions | us-east-1 |
| Proxy phone session management | Multiple Regions | us-east-1 |
| Streaming management | Multiple Regions | us-east-1 |
| Logging and metrics management | Multiple Regions | us-east-1 |

For more information about the available Regions, refer to [Voice Regions](sdk-available-regions.md#voice-regions).

## Differences between the namespaces
<a name="voice-namespace-diffs"></a>

The following sections explain the differences between the `Amazon Chime SDK Voice` and `Amazon Chime` namespaces.

**AWS namespace**
The Amazon Chime SDK namespace uses the `Chime` formal name. The Amazon Chime SDK Voice namespace uses the `ChimeSDKVoice` formal name. The precise format of the name varies by platform.

For example, if you use the AWS SDK in Node.js to create meetings, you use the following line of code to address the namespace.

```
const chimeVoice = AWS.Chime();
```

To migrate to the Amazon Chime SDK Voice namespace, update this line of code with the new namespace and the endpoint region.

```
const chimeVoice = AWS.ChimeSDKVoice({ region: "{{eu-central-1}}" });
```

**Regions**
The [Amazon Chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime.html) namespace can only address API endpoints in the `us-east-1` Region. The [Amazon Chime SDK Voice](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Meetings.html) namespace can address Amazon Chime SDK voice API endpoints in any Region they are available. For a current list of voice Regions, refer to [Available AWS Regions for the Amazon Chime SDK](sdk-available-regions.md) in this guide.

**Endpoints**
The [Amazon Chime SDK Voice](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Voice.html) namespace uses different API endpoints than the [Amazon Chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime.html) namespace.

Only the endpoint used to create a voice action can be used to modify it. This means a voice action created via an endpoint in `eu-central-1` can only be modified via `eu-central-1`. It also means you cannot address a voice action created via the `Chime` namespace with the `ChimeSDKVoice` namespace in `us-east-1`. For more information about the current endpoints, refer to [API mapping](migrate-from-chm-namespace.md#name-end-map) in this guide.

**Service principal**
Both namespaces uses the `chime.amazonaws.com` service principal. If you have access policies that grant access to the service, you do not need to update those polices.

**APIs**
The [Amazon Chime SDK Voice](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Voice.html) namespace only contains APIs to create and manage voice actions. The [Amazon Chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime.html) namespace includes APIs for voice and other parts of the Amazon Chime service, such as meetings.

**Tagging**
Only the [Amazon Chime SDK Voice](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Voice.html) namespace supports tags. For more information about tags, refer to [TagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UntagResource.html).

**Media Regions**
If you use the `Chime` namespace to create resources such as Voice Connectors and SIP media application, you can only do so in `us-east-1` and `us-west-2`, and you must use the `us-east-1` endpoint.

In contrast, the `ChimeSDKVoice` namespace allows resource creation in all supported Regions, not just `us-east-1` and `us-west-2`. For more information about regional coverage, refer to [Available AWS Regions for the Amazon Chime SDK](sdk-available-regions.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
