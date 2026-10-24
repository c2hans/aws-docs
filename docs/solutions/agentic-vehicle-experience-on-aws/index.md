---
source_url: https://docs.aws.amazon.com/solutions/agentic-vehicle-experience-on-aws/index.html
---

---
title: 'Guidance for Agentic Vehicle Experience on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/agentic-vehicle-experience-on-aws/
source: aws-documentation
generated_on: 2026-10-23
---

# Guidance for Agentic Vehicle Experience on AWS

## Overview

This Guidance demonstrates how to build an AI agent layer that delivers conversational, multi-channel customer experiences across the connected vehicle ownership lifecycle. By unifying real-time vehicle telemetry with curated automotive reference and customer data, it grounds every interaction in the vehicle's actual state and domain knowledge. Built on Amazon Bedrock AgentCore with Nova Sonic voice and Amazon Connect Customer, it enables six personas—from fleet drivers to technicians—to decode VINs, read diagnostic codes, match service bulletins, quote repairs, locate service centers, book appointments, and confirm warranty coverage in a single conversation across voice, text, web, and contact center touchpoints.

## Benefits

### Serve every driver faster

Deliver sub-100ms conversational responses across six distinct user personas — from drivers to service technicians — by loading governed vehicle data once at session start rather than re-querying on every turn. Your customers get accurate, personalized answers without the wait.

### Unify data without owning it

Compose live vehicle telemetry, service history, and Lake Formation-governed analytical data products into a single agentic experience, while each data owner retains control of their own lake, catalog, and encryption keys. Your organization gains cross-account insights without duplicating or centralizing sensitive automotive data.

### Scale voice and text confidently

Support simultaneous voice and text interactions through a single supervisor code base, with Bedrock Guardrails applied to voice transcripts before playback to help protect against harmful content. Your teams can expand connected vehicle services across channels without rebuilding the underlying AI runtime.

## How it works

This architecture diagram shows how to unify governed automotive data products across accounts and the ownership journey—from onboarding through services—into a single grounded agentic experience that delivers consistent, contextual customer interactions. [Download the architecture diagram](downloads/agentic-vehicle-experience-on-aws.pdf)

![Architecture diagram for Agentic Vehicle Experience on AWS](/images/solutions/agentic-vehicle-experience-on-aws/images/agentic-vehicle-experience-on-aws-1.png)

1. **Step 1**: Client initiates. A driver, service advisor, or technician opens a session: voice through iOS, text through the web UI. The client authenticates through CMS Amazon Cognito and sends the prompt with a bearer token.
1. **Step 2**: Amazon API Gateway authorizes. The Cognito authorizer validates the token and injects claims; persona is inferred server-side, not client-supplied. Six personas are supported (driver, service advisor, technician, consumer, retail advisor, owner), each with a persona-scoped tool set.
1. **Step 3**: Runtime is invoked. For text, the route Lambda calls the CVX text runtime running a Amazon Bedrock model; for voice, the iOS client opens a bidirectional stream to the AgentCore bidi runtime running Amazon Nova Sonic. One supervisor code base runs both modes. Session init hydrates AgentCore Memory.
1. **Step 4**: The persona loader runs one cross-account Amazon Athena query (~6–7s) against ADP's AWS Lake Formation-governed data products, then seeds Memory. AWS Lake Formation grants CVX per-database read access and session-scoped Amazon S3 tokens; ADP owns the lake, catalog, and AWS KMS keys. CVX holds no data of its own; it composes ADP analytical data with CMS operational state at conversation time.
1. **Step 5**: Tools dispatch from Memory or Knowledge Base. Turns read from AgentCore Memory (sub-100ms lookups filtered by persona and vehicle) or Amazon Bedrock Knowledge Base Retrieve. Amazon Athena is never re-queried per turn, the invariant that keeps conversations fast. If Retrieve is down, DTC tools fall back to local rules; if Memory is unavailable, tools return "not yet available" so the session continues.
1. **Step 6**: CMS provides live state. Telemetry snapshots (engine, tire pressure, battery) are read once at session init from Amazon ElastiCache; service-history writes and NHTSA recall status flow through Lambda-fronted Amazon DynamoDB APIs. If Amazon ElastiCache is unreachable, triage defaults to a conservative P1.
1. **Step 7**: Terminal tools reach external partners. Booking, finance qualification, payment initiation, and reservation handoff leave AWS entirely, reaching partner systems via webhook or REST: ticket sinks, dealer management, payment providers, subscription platforms. CVX generates envelopes; partners retain ownership.
1. **Step 8**: Response returns to client. For text, the runtime returns JSON through API Gateway and the browser renders through a sanitizing allowlist. For voice, Amazon Nova Sonic streams audio and transcript deltas back through the bidi runtime to iOS. Bedrock Guardrails apply to voice transcripts before playback, since audio cannot be retracted once spoken.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](/guidance/latest/agentic-vehicle-experience-on-aws/guidance-overview.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-agentic-vehicle-experience-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
