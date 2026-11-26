---
source_url: https://docs.aws.amazon.com//solutions/accelerator-optimized-agentic-bidding-on-aws//index.html
---

---
title: 'Guidance for Accelerator-Optimized Agentic Bidding on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/accelerator-optimized-agentic-bidding-on-aws/
source: aws-documentation
generated_on: 2026-11-26
---

# Guidance for Accelerator-Optimized Agentic Bidding on AWS

## Overview

This Guidance demonstrates how to optimize real-time bidding decisions across multiple machine learning models. It runs GPU-accelerated NVIDIA model architectures as a staged pipeline inside an ARTF-compliant framework (IAB Tech Lab Agentic Real Time Framework), and it keeps those models improving from real auction outcomes without ever touching the real-time bidstream. The default deployment includes both the real-time bidding path (Part 1) and the closed-loop learning system (Part 2). When an OpenRTB bid request arrives, an orchestrator container runs it through six specialized containers, each doing one job, in four stages: enrich, deals, yield, price. Containers within a stage run in parallel, and each stage sees the mutations the previous stages applied, so the yield containers can price a deal the Deal Scorer just activated. On the buy side, a Bid Pricer predicts how likely the paid-for response is and shades the bid to the lowest price still likely to win. An Audience Activator activates high-value audience segments from signals already on the request. A Deal Scorer evaluates private marketplace relevance to activate or suppress deals. A Signals Enricher adds viewability and brand-safety metrics. On the sell side, two Yield Optimizer containers predict a floor-price adjustment and a margin adjustment for each private marketplace deal. Each container applies typed ARTF mutations (BID_SHADE, ACTIVATE_SEGMENTS, ACTIVATE_DEALS and SUPPRESS_DEALS, ADD_METRICS, ADJUST_DEAL_FLOOR, ADJUST_DEAL_MARGIN). The orchestrator consolidates them into a single OpenRTB response within milliseconds. Four of the six containers run inference on NVIDIA Triton Inference Server on an NVIDIA A10G GPU: two deep-learning models served as compiled NVIDIA TensorRT engines, and two XGBoost tree models served by Triton's Forest Inference Library backend. The closed-loop learning system (Part 2) runs beside the real-time path. Every bidding decision emits an outcome event. AWS Glue turns those events into labeled training data. Amazon SageMaker retrains new model versions (a PyTorch trainer on the NVIDIA NeMo Framework image for the bid pricer, built-in XGBoost for the tree models) and registers them with full lineage. A Model Promotion Governance Agent on Amazon Bedrock AgentCore compiles each challenger to a TensorRT engine, stages it as a live canary behind the same Triton model name the containers already call, evaluates it with a statistically rigorous A/B test, and promotes, rejects, or rolls it back automatically. A second AgentCore agent re-tunes the bid-shading parameters on a schedule (daily by default) from live Amazon CloudWatch metrics, within hard bounds the parameter store enforces. An optional Prebid Server deployment places the ARTF call on the critical path of a real auction. You can then see what the enrichment costs in auction time and which seat wins as a result. You can reduce advertising overspend while maintaining win rates, manage private marketplace deals autonomously on both sides of the trade, promote retrained models to production with no downtime and no manual review cycle, and enable AI agents to make and tune real-time bidding decisions through Model Context Protocol integration.

## Benefits

### Accelerate bid decisions with GPU inference

Process real-time bidding requests using GPU-accelerated inference on Amazon Elastic Kubernetes Service, with NVIDIA Triton Inference Server serving compiled TensorRT engines and tree models side by side on one NVIDIA A10G GPU. Dynamic batching keeps model scoring inside OpenRTB timeout budgets so you can win more auctions at optimal prices.

### Enrich both sides of the trade with staged model scoring

Run each bid request through six specialized containers in one call, in stage order: enrich quality signals and activate audience segments, score deal relevance, adjust deal floors and margins on the publisher side, then score the paid-for response and price the bid. Each stage builds on the mutations the one before it applied, and the request completes before the auction continues.

### Keep models improving from real outcomes

Capture every bidding decision and its outcome, retrain daily on Amazon SageMaker (NVIDIA NeMo Framework image and built-in XGBoost), and promote only challengers that beat the incumbent in a live canary A/B test with automatic guardrail rollback. Models compound in accuracy instead of drifting away from a static export.

### Tune bidding strategy autonomously, within bounds

An Amazon Bedrock AgentCore agent reasons over live win-rate and ROI metrics on a configurable schedule (daily by default) and adjusts the shading parameters, subject to hard bounds, a maximum per-update delta, and an append-only audit trail that records every change and the reasoning behind it.

## How it works

This architecture has two parts that run side by side. The real-time bidding path mutates and enriches OpenRTB bid requests in milliseconds using ARTF-compliant container agents and GPU-accelerated inference on NVIDIA Triton Inference Server on Amazon Elastic Kubernetes Service. The closed-loop learning system captures auction outcomes, retrains the models, and uses agents to test, promote, and tune models and bidding strategy without touching the real-time bidstream. [Download the architecture diagram.](downloads/accelerator-optimized-agentic-bidding-on-aws.pdf)

![Architecture diagram for Accelerator-Optimized Agentic Bidding on AWS](/images/solutions/accelerator-optimized-agentic-bidding-on-aws/images/accelerator-optimized-agentic-bidding-on-aws.png)

1. **Step 1**: A bid request originates in the presence of an ad slot and arrives at the Network Load Balancer from the publisher or media owner.
1. **Step 2**: The Network Load Balancer routes the request down one of two paths: directly to the Supply Side Platform (without PBS), or through the Prebid Server endpoint on port 50051 (with PBS).
1. **Step 3**: The request reaches the ARTF Orchestrator, which coordinates enrichment and mutation by fanning out to the model services over gRPC.
1. **Step 4**: Enrichment and scoring services run in Amazon Elastic Kubernetes Service: the Signals Enricher and Audience Activator, the Deal Scorer, the Yield Optimizers (deal floor, margin), and the bidding models, each called over gRPC.
1. **Step 5**: NVIDIA Triton Inference Server (GPU) serves the models behind a stable/canary router. It runs the TensorRT engines (DLRM, NCF) and XGBoost through the FIL backend for floor and margin, and returns mutations to the orchestrator.
1. **Step 6**: Prebid Server and the Publisher-Side Direct Deals Ad Server (artfhouse) apply the returned mutations and resolve direct deals and campaigns against Amazon DynamoDB before the auction happens.
1. **Step 7**: The Supply Side Platform or PBS continues processing the mutated, enriched bid request.
1. **Step 8**: On the bidder's side, ARTF containers can mutate a response similarly before the Ad Server or PBS selects the winning bid.
1. **Step 9**: ARTF outcome events from the bidstream stream into Amazon Kinesis and land in Amazon S3 as raw outcomes.
1. **Step 10**: AWS Glue transforms the outcomes into training data, and a retraining loop triggered by Amazon EventBridge retrains the DLRM, NCF, and XGBoost floor and margin models.
1. **Step 11**: Amazon SageMaker AI registers every retrained model version in the SageMaker AI Model Registry for governance review.
1. **Step 12**: Registration triggers a Governance Agent running on Amazon Bedrock AgentCore that runs a canary and statistical A/B test before any promotion.
1. **Step 13**: The Governance Agent promotes or rolls back the model, writing the decision to an Amazon DynamoDB audit trail.
1. **Step 14**: The Triton router loads each promoted model from the Amazon S3 model repository with no downtime.
1. **Step 15**: The Governance Agent reaches Triton and the ARTF Orchestrator inside the VPC through the VPC optimizer proxy Lambda, which it uses to stage canaries and apply promotions.
1. **Step 16**: The outcome events stream into Amazon Kinesis Data Streams and land in Amazon S3 as raw outcomes, which feed the retraining loop.
1. **Step 17**: On a fixed schedule, an Adaptive Bidding Agent analyzes bidding outcomes and writes tuned parameters back, within bounds, to the Amazon DynamoDB parameter store.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-accelerator-optimized-agentic-bidding-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
