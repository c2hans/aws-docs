---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/sip-applications-service-change.html
---

# SIP media applications service change
<a name="sip-applications-service-change"></a>

After careful consideration, we decided to close Amazon Chime SDK SIP media applications to new customers starting October 29, 2026. To use the SIP media applications, sign up before that date. If you are an existing customer, you can continue using the service as usual.

We recommend that you migrate your PSTN Audio applications to Amazon Connect Customer. Build any new telephony workloads there too. Amazon Connect Customer offers the same core features as PSTN Audio. It also adds more advanced features for interactive voice response (IVR) design, managed compliance, and agentic AI customer engagement. Amazon Connect Customer is a purpose-built agentic AI solution. With it, you can design personalized customer experiences at enterprise scale. It provides visual no-code flow design and built-in carrier-grade telephony. You also get real-time analytics and AI features such as agentic voice and agent assist. You pay per use, with no minimum commitments.

## Migration plan
<a name="migration-plan"></a>

You can migrate most telephony workloads from Amazon Chime SDK PSTN Audio to Amazon Connect Customer. It takes some careful planning. Amazon Connect Customer does not replace every PSTN Audio capability. But its flow-based design can handle all core use cases. This guide maps out a migration path. It covers architecture mapping, action-to-block translation, and an approach for each use case.

### Recommended Alternative: Amazon Connect Customer
<a name="recommended-alternative"></a>

Amazon Connect Customer is the recommended migration path for all PSTN Audio use cases:

**PSTN Audio use cases and Amazon Connect Customer equivalents**

| PSTN Audio Use Case | Amazon Connect Customer Equivalent |
| --- | --- |
| Call Forwarding (IVR routing) | Flows |
| IVR / Interactive Voice Response | Flows with visual designer |
| Automated Calling (outbound) | Outbound Campaigns |
| Call Recording | Built-in recording and conversational analytics |
| Transcription & Analytics | Conversational analytics |
| Bot / NLU Integration | Get customer input (Lex) |
| Lambda-based call logic | Invoke AWS Lambda function block in Contact Flows |

Key benefits of Amazon Connect Customer:
+ Visual, no-code flow designer for IVR and routing
+ Built-in compliance (HIPAA, SOC)
+ Agentic AI features: agentic voice, real-time agent assist, post-contact analytics
+ Managed telephony with carrier-grade reliability
+ Pay-per-use pricing with no minimum commitments
