---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/connect-use-cases.html
---

# Amazon Connect Customer for customer-facing interactions
<a name="connect-use-cases"></a>

If your solution involves customers or consumers interacting with your business, use Amazon Connect Customer. This applies whether the interaction uses AI agents, agentic self-service, live agents, or automated handling.

Customer support and service desk
Customers calling your business for help, support, or service

Agentic self-service (voice and chat)
AI-powered experiences that understand context, solve problems autonomously, and know when human expertise adds value

AI agents and agentic voice
AI-powered systems that handle customer calls end-to-end (reservations, order status, FAQs, virtual receptionists)

Agent routing and queuing
Directing calls to the right agent or team based on skills, availability, or customer intent

Outbound campaigns
Predictive, progressive, or preview dialing for customer outreach

Omnichannel
Voice, chat, email, SMS, WhatsApp, and video in a unified platform

Conversational analytics
Transcription, sentiment analysis, quality monitoring, compliance

Workforce management
Agent scheduling, forecasting, performance evaluation

Number masking
Anonymous calling for marketplace and rideshare applications

Call forwarding
Routing calls to multiple destinations based on caller intent or context

**Important**
**Architecture doesn't change the answer.** The determining factor is what the **end user experiences**, not how you architect it. This holds true even if you use your own SBC (Kamailio, AudioCodes, Oracle), your own media server (Asterisk, FreeSWITCH), or your own AI platform. If customers call a business and receive automated handling or agent service, that is a customer engagement use case, and Amazon Connect Customer is the right service.

## Examples that should always use Amazon Connect Customer
<a name="connect-always-examples"></a>

The following scenarios always require Amazon Connect Customer.

AI voice agent answering calls for restaurants
Customer-facing automated call handling

Virtual receptionist or front desk bot
Customer-facing automated call handling

Third-party AI voicebot handling inbound customer calls
Customer-facing automated call handling

Automated outbound notifications to customers
Outbound customer engagement

Multi-tenant voice platform for businesses
Customer engagement as a service
