---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/sip-applications-maintenance-mode.html
---

# Amazon Chime SDK SIP media applications availability change
<a name="sip-applications-maintenance-mode"></a>

After careful consideration, we have made the decision to put the Amazon Chime SDK PSTN Audio service into Maintenance Mode, effective September 29, 2026. As of this date, there is no new feature or capability development for the service, and as of October 29, 2026, the service is no longer open to new customers.

During Maintenance Mode, the service remains fully supported and AWS will continue to provide bug fixes and security updates for existing customers, however new feature requests will no longer be considered.

We recommend that customers migrate their PSTN Audio applications and implement any new telephony workloads on Amazon Connect Customer for similar capabilities to PSTN Audio and more advanced features for IVR design, managed compliance, and agentic AI customer engagement. Amazon Connect Customer is a purpose-built agentic AI solution that delivers personalized customer experiences at enterprise scale. It offers visual no-code flow design, built-in carrier-grade telephony, real-time analytics, and AI capabilities including agentic voice and agent assist, all with pay-per-use pricing and no minimum commitments.

## What is changing
<a name="what-is-changing"></a>

The Amazon Chime SDK PSTN Audio service is entering maintenance mode. This means:
+ Existing customers can continue to use PSTN Audio as they do today. Your existing call flows, Lambda integrations, SIP media applications, and phone number assignments remain fully functional.
+ New customers will no longer be able to onboard to the PSTN Audio service after October 29, 2026.
+ No new features will be developed for PSTN Audio. AWS will continue to provide security updates, bug fixes, and operational support.
+ Exception: Customers using PSTN Audio exclusively for Amazon Chime SDK Meetings dial-in/dial-out (Join Meeting) or programmatic outbound calling with DTMF for PSTN testing may request access through an exception process. Contact AWS Support referencing "PSTN Audio Maintenance Mode Exception" for review.

## Why we are making this change
<a name="why-we-are-making-this-change"></a>

We understand that this decision may require you to evaluate changes to your telephony architecture, and we want to ensure you have the time, resources, and support to plan accordingly.

Amazon Connect Customer provides the purpose-built IVR, visual flow design, managed compliance, and AI integration that customers need at production scale. As telephony regulations continue to evolve with stronger consumer protections, maintaining a direct SIP-layer control model has become increasingly complex. Amazon Connect Customer addresses PSTN Audio's core use cases, including call forwarding, IVR, automated calling, and call recording, with additional capabilities, compliance frameworks, and an active feature roadmap.

By consolidating telephony workloads on Amazon Connect Customer, we provide customers with a single, fully managed solution that reduces operational complexity, strengthens compliance posture, and delivers continuous innovation.

## Migration plan
<a name="migration-plan"></a>

Migrating from Amazon Chime SDK PSTN Audio to Amazon Connect Customer is achievable for most telephony workloads with some careful planning. Not all PSTN Audio capabilities are directly replicated in Amazon Connect Customer, but all core use cases can be addressed through its flow-based architecture. This guide provides a comprehensive migration path including architecture mapping, action-to-block translation, and recommended approaches for each use case.

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

### How to Migrate
<a name="how-to-migrate"></a>

The following resources are available:

1. Migration Guide: For step-by-step migration instructions, see [Migrating Amazon Chime SDK PSTN Audio to Amazon Connect](migrate-pstn-audio-to-connect.md).
   + Step-by-step instructions for converting your SIP media application Lambda configurations to Flows.
   + Mapping guide from PSTN Audio actions to Amazon Connect Customer flow blocks.
   + Phone number porting guidance.

1. AWS Support: Open a support case through the AWS Support Center referencing "PSTN Audio to Connect Customer Migration" for personalized guidance.
