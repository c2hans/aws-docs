---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/call-architecture.html
---

# Learn about using Amazon Chime SDK PSTN audio service call legs
<a name="call-architecture"></a>

**Note**
Amazon Chime SDK SIP media applications will no longer be open to new customers starting October 29, 2026. If you would like to use SIP media applications, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon Chime SDK SIP media applications availability change](https://docs.aws.amazon.com/chime-sdk/latest/ag/sip-applications-maintenance-mode.html).

The PSTN audio service can operate on one or more call legs. For example, you have a single call leg when you record or deliver a voice mail, and you have multiple call legs when you join an Amazon Chime SDK meeting.

The following diagram shows the flow of a single-leg call.

![Diagram of the architecture of a single call leg.](https://docs.aws.amazon.com/chime-sdk/latest/dg/images/single-leg-architecture.png)

The following diagram shows the architecture of a multi-leg call.

![Diagram of the architecture of a multi-leg call.](https://docs.aws.amazon.com/chime-sdk/latest/dg/images/multi-leg-architecture.png)

The following diagram shows the flow of a multi-leg bridged call.

![Diagram of the architecture of a multi-leg bridged call.](https://docs.aws.amazon.com/chime-sdk/latest/dg/images/Multi-Leg-Architecture-w-Bridge.png)
