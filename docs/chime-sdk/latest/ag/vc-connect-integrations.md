---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/vc-connect-integrations.html
---

# Amazon Chime SDK Voice Connector and Amazon Connect Customer integrations
<a name="vc-connect-integrations"></a>

In some scenarios, you can use Amazon Chime SDK Voice Connector as part of an Amazon Connect Customer architecture. However, these integrations are tightly controlled, and an Amazon Connect specialist must validate them.

**Important**
**Amazon Chime SDK Voice Connector is not a method to route calls from a separate provider into Amazon Connect through the PSTN.** Using Amazon Chime SDK Voice Connector to bridge calls from an external carrier or third-party system into Amazon Connect is not a supported pattern without prior architecture review and approval. These configurations introduce latency, reduce observability, and can degrade the customer experience.

## Why architecture review is required
<a name="why-architecture-review"></a>

With Amazon Connect Customer, you get native PSTN connectivity. You do not need an intermediary SIP trunk to receive or place calls. When you introduce Amazon Chime SDK Voice Connector as a bridge between an external system and Connect, this often indicates one of the following:
+ A misunderstanding of what Connect supports natively, which might eliminate the need for Amazon Chime SDK Voice Connector entirely
+ An architecture that adds unnecessary SIP hops, increasing latency and reducing call quality
+ A configuration that limits the ability of Connect to provide full observability, analytics, and AI capabilities on the call
+ A potential PSTN resale or multi-tenant pattern that is not supported

## What you must do before implementing
<a name="builder-prerequisites"></a>

Before you implement a Amazon Chime SDK Voice Connector to Connect integration, complete the following steps:

1. **Engage your AWS account team** (Solutions Architect or Technical Account Manager).

1. **Request a Connect specialist review** of the proposed architecture.

1. **Demonstrate awareness** of what Connect Customer supports natively. The specialist confirms whether the integration is necessary or whether Connect can serve the use case directly.

1. **Receive approval** before proceeding with any Amazon Chime SDK Voice Connector to Connect integration.

**Note**
**In most cases, if you believe you need both Amazon Chime SDK Voice Connector and Connect, you find that Connect Customer already supports your use case natively**, with better performance, full observability, and no additional SIP infrastructure to manage. The architecture review exists to help you find the simplest, most reliable path to your goal.
