---
source_url: https://docs.aws.amazon.com/solutions/guidance-for-automotive-retail-operations-using-agentic-ai/index.html
---

---
title: 'Guidance for Automotive Retail Operations using Agentic AI on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/guidance-for-automotive-retail-operations-using-agentic-ai/
source: aws-documentation
generated_on: 2026-11-20
---

# Guidance for Automotive Retail Operations using Agentic AI on AWS

## Overview

This Guidance shows how automotive OEMs and dealer networks can orchestrate the complete vehicle lifecycle — from a customer's first inquiry through purchase, ownership, and every service visit back to the next sale — as a single event-driven architecture on AWS. It gives the retail purchase funnel and service operations each a dedicated AI supervisor, backed by a shared identity layer, event bus, and data model, so context carries across handoffs instead of resetting. Seven cooperating agents advance a journey only when an event is recorded, and customer-facing figures come from traceable tool calls checked by a per-action autonomy guardrail. Positive-equity and lease-end signals feed the next purchase journey.

## Benefits

### Answer customers instantly from one source

The Sales Agent drafts a grounded first reply to each new lead right away, and the Discovery Agent turns lifestyle and budget into a ranked, explained shortlist of in-stock vehicles with price, incentives, and cost of ownership. The shopper and advisor work from the same explained shortlist, so advisors spend the conversation on the customer instead of looking things up.

### Complete handoffs and surface opportunities

The Journey Agent checks each handoff and picks the next best action, so handoffs arrive complete and stalled journeys surface on their own. The Trade-In Agent flags customers turning equity-positive or nearing lease-end and the Service Agent routes that signal to sales, so each handoff becomes a record and a task and the department that earned the sale keeps the credit.

### Prepare work ahead, keep decisions human

Scheduled agent jobs write recommendation cards, leads, and drafts before the shift — the Field Sales Agent prepares the district manager's week and the Campaign Agent attributes marketing spend to delivered vehicles, every figure cited. As shipped, agents recommend only: they never publish a plan, change spend, or contact a customer, estimate approval stays with the customer, and every agent is validated with the AWS Universal Agent Evaluation Framework (UAEF).

## How it works

This architecture diagram illustrates how to build and operate Automotive Retail Operations using Agentic AI on AWS. It shows the key components and their interactions. [Download the architecture diagram](downloads/automotive-retail-operations-using-agentic-ai.pdf)

### End-to-End Overview

Step 1Sales state machine. The Purchase supervisor advances an 8-state journey (DISCOVER→…→OWN) persisted in the journeys table, and AWS Lambda validates each transition server-side. Shoppers and staff work in Customer Web, Lead Desk, live advisor coaching, Discovery, Trade Desk, the finance and insurance (F&I) desk, Delivery Board and My Garage.

Step 2Service state machine. The Service supervisor runs a separate 8-state repair order (RO) lifecycle (BOOK→…→FOLLOW-UP) in the repair-order table, with no synchronous call to sales. Owners book in My Garage; staff use the check-in tablet, parts desk, RO view and declined-work register.

Step 3Cross-domain read model. The sales floor queries a read-only projection of open repair orders (ROs); the handler role is IAM-scoped with no write to repair order (RO) items.

Step 4Event handoff. An equity event on the Amazon EventBridge event bus matches a rule that invokes an AWS Lambda function to insert a journeys-table item plus a tasks-table row.

Step 5Ownership coupling. The DELIVER→OWN transition emits an event that seeds service eligibility; the only link between journeys is asynchronous events.

Step 6Handoff record. The handoffs table uses handoff_id as its key and carries correlation_id; the writer AWS Lambda function is idempotent on event replay.

### Sales Flow

Step 1Edge & API. Amazon CloudFront serves the console from a private Amazon S3 bucket; Amazon API Gateway, with an AWS Lambda token authorizer, routes requests to role-scoped AWS Lambda handlers over Amazon DynamoDB, with no model call on page load.

Step 2Lead ingest. Inbound leads write to the leads table; an Advisor-agent AWS Lambda calls Amazon Bedrock to draft a reply, sent through Amazon Simple Email Service (Amazon SES) or Amazon Simple Notification Service (Amazon SNS).

Step 3Live assist (<2s). Amazon Transcribe streams audio to text; Amazon Bedrock classifies the utterance and returns a suggested response; Amazon SageMaker AI serves vehicle identification number (VIN)-level match ranking from a real-time endpoint.

Step 4Deal math. Amazon Bedrock AgentCore Code Interpreter runs total cost of ownership (TCO), equity and payment calc; an AWS Lambda writes the deals table and pushes to the dealer management system (DMS) and lender using credentials from AWS Secrets Manager.

Step 5Stage gate. A handoff validation AWS Lambda enforces checklist preconditions; Amazon EventBridge publishes the stage change; AWS Step Functions runs approvals above the autonomy ceiling; Amazon EventBridge Scheduler runs nurture/equity jobs.

Step 6Deliver / own. Amazon SES or Amazon SNS sends delivery and survey messages; the DELIVER→OWN write in Amazon DynamoDB updates the journey item that My Garage reads.

Step 7Trace & lake. Each tool call appends to the agent-trace table with a correlation_id; Amazon Data Firehose delivers events to the Amazon S3 lake that AWS Glue catalogs and Amazon Athena queries; Amazon CloudWatch collects AWS Lambda logs and metrics.

### Service Flow

Step 1Edge & API. Same request path: Amazon CloudFront + Amazon API Gateway + AWS Lambda over Amazon DynamoDB read models; no generative call in the page load.

Step 2Booking. My Garage reads due maintenance, open recalls and prior declines from Amazon DynamoDB; an AWS Lambda computes bay capacity and writes the promised time onto the repair order (RO) item.

Step 3Inspect / diagnose. Amazon Transcribe captures concerns; the Service supervisor on Amazon Bedrock emits the repair order (RO) brief and diagnostic trouble code (DTC) causes joined to cited technical service bulletins (TSBs) from the region-keyed diagnostic-reference table.

Step 4Estimate. Amazon Bedrock AgentCore Code Interpreter prices labor ops, parts and coverage; an estimate-builder AWS Lambda function assembles lines, each carrying a source_ref — no figure computed client-side.

Step 5Approval. The customer authenticates through an Amazon Cognito magic link and approves line items on mobile against the same read model; decisions and declines persist to Amazon DynamoDB.

Step 6Repair resume. A parts-received event on Amazon EventBridge transitions the repair order (RO) to REPAIR; the supervisor re-forecasts the promise; Amazon Simple Email Service (Amazon SES) or Amazon Simple Notification Service (Amazon SNS) sends the invoice at pickup.

Step 7Schedules & trace. Amazon EventBridge Scheduler drives dispatch, approval-chase and 30/60/90-day follow-up; actions log to the agent-trace table with autonomy level; Amazon Athena backs the fixed-ops cockpit.

### Service to Sales Handoff

Step 1Edge & API. Amazon Cognito sign-in; Amazon CloudFront + Amazon API Gateway + AWS Lambda serve the Service Lane and kanban from Amazon DynamoDB read models.

Step 2Equity compute. An Amazon EventBridge Scheduler job (equity-monitor-nightly) plus service/payoff events invoke the Trade-agent AWS Lambda, which writes equity to the valuations table.

Step 3Lane scoring. A service-lane-monitor schedule invokes an AWS Lambda that flags positive equity, high mileage and approaching lease-end on today's repair orders (ROs).

Step 4Brief generation. The Advisor agent on Amazon Bedrock generates an upsell brief grounded on inspection and declined-work rows, each with a source_ref.

Step 5Handoff write. An AWS Lambda writes a handoffs-table row and a tasks-table row to Amazon DynamoDB; Amazon EventBridge publishes the handoff; Amazon Simple Email Service (Amazon SES) or Amazon Simple Notification Service (Amazon SNS) notifies the receiver.

Step 6Journey open. A Purchase-supervisor AWS Lambda inserts a DISCOVER journey; Amazon EventBridge is the sole coupling between the two state machines.

Step 7Attribution. Both sides share one correlation_id in the agent-trace table; Amazon Data Firehose lands handoff events in the lake so Amazon Athena joins the handoff to the eventual delivery.

### Marketing Analytics

Step 1Edge & API. Amazon Cognito sign-in; the original equipment manufacturer (OEM) Workspace and Marketing Studio load from Amazon CloudFront and read Amazon DynamoDB through Amazon API Gateway + AWS Lambda.

Step 2Ingest. Amazon Data Firehose delivers journey and service events to the raw Amazon S3 event lake, which AWS Glue partitions and catalogs.

Step 3Attribution job. A nightly Amazon EventBridge Scheduler job runs the Campaign-return on investment (ROI) agent, which issues Amazon Athena structured query language (SQL) joining marketing spend to delivered vehicle identification numbers (VINs).

Step 4Recommendation. The agent drafts a budget-shift on Amazon Bedrock; Amazon Personalize refreshes target audiences. The output carries a source_ref for each figure.

Step 5Approval. AWS Step Functions routes the plan to finance with projected impact; the decision and audit trail persist in Amazon DynamoDB.

Step 6Policy publish. An AWS Lambda writes approved policy as versioned config; OEM teams use AWS Quick (OEM document agent, Flows, Index) reaching Purchase-supervisor tools through Amazon Bedrock AgentCore Gateway — no redeploy.

Step 7Execute / govern. A nurture-tick Amazon EventBridge Scheduler job executes policy; Amazon SES or Amazon SNS sends the dealer digest; AWS Secrets Manager holds Quick OAuth and advertising-provider credentials; the app logs guardrail decisions.

### OEM Field Sales

Step 1Access. OEM district managers, regional leads, planners, marketing and finance sign in to AWS Quick, or open the OEM Workspace from Amazon CloudFront, where AWS Lambda returns an embed URL for the dashboard.

Step 2Shared space. One AWS Quick space holds the Field Sales chat agent, eight Flows, the Journey Funnel topic, the Campaign ROI & Funnel dashboard and nine knowledge bases, shared through a viewer group for each role.

Step 3Connect. A Model Context Protocol (MCP) action connector gets a JSON Web Token (JWT) from Amazon Cognito with a client secret kept in AWS Secrets Manager.

Step 4Scoped read. Amazon Bedrock AgentCore Gateway checks the token and calls AWS Lambda, which derives the OEM scope from the token, strips internal fields and returns cited rows from Amazon DynamoDB through four read-only tools.

Step 5Analytics. Amazon Data Firehose streams every journey and service event to an Amazon S3 lake. AWS Glue catalogs 13 tables that Quick datasets query directly through Amazon Athena, with no copy.

Step 6Knowledge. The knowledge corpus documents are exported from Amazon DynamoDB to Amazon S3 with email and phone masked, then synced into the nine Quick knowledge bases.

Step 7Answer. The chat agent checks each question and draft against OEM policy rules GR-001 to GR-008. Every Flow ends in a cited draft that a person reviews before it is sent.

## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-automotive-retail-operations-using-agentic-ai-on-aws)
[AWS Universal Agent Evaluation Framework (UAEF)](https://github.com/awslabs/uaef)

[Read usage guidelines](/solutions/guidance-disclaimers/)
