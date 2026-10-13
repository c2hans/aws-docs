---
source_url: https://docs.aws.amazon.com/solutions/ai-powered-devops-agent-for-prometheus-anomaly-detection/index.html
---

---
title: 'Guidance for AI-Powered DevOps Agent for Prometheus Anomaly Detection'
canonical_url: https://docs.aws.amazon.com/solutions/ai-powered-devops-agent-for-prometheus-anomaly-detection/
source: aws-documentation
generated_on: 2026-10-13
---

# Guidance for AI-Powered DevOps Agent for Prometheus Anomaly Detection

## Overview

This Guidance demonstrates how to shift 5G network operations from reactive troubleshooting to intelligent, automated incident prevention using an AI-powered proactive Root Cause Analysis pipeline. By combining Amazon Managed Prometheus with built-in Random Cut Forest (RCF) anomaly detection and DevOps agents with MCP tool support, it automatically detects performance anomalies, investigates root causes, and initiates resolution before end users are impacted. This approach significantly reduces mean time to detection (MTTD) and mean time to resolution (MTTR), enabling telecom operators to maintain mission-critical 5G infrastructure with greater reliability, lower operational costs, and reduced dependency on specialized troubleshooting expertise.

## Benefits

### Accelerate 5G incident resolution

Automatically detect network anomalies and trigger autonomous root cause analysis without waiting for manual intervention. Reduce mean time to resolution by routing alerts directly to an AI-driven investigation agent that queries live metrics on demand.

### Operate networks with fewer resources

Replace time-consuming manual triage with an autonomous investigation workflow that identifies failing 5G network functions and delivers findings to your engineers. Your operations team can focus on remediation rather than spending hours diagnosing the source of subscriber registration failures.

### Build on a secure, scalable foundation

Protect sensitive network telemetry and investigation credentials using IAM role-based access controls, Secrets Manager, and OAuth2-secured API endpoints. Scale metric ingestion and anomaly detection across hundreds of base stations and thousands of connected devices without managing additional infrastructure.

## How it works

This architecture diagram shows how Amazon Managed Prometheus detects 5G core anomalies and automatically triggers the AWS DevOps Agent to investigate and identify the failing network function. [Download the architecture diagram](downloads/ai-powered-devops-agent-for-prometheus-anomaly-detection.pdf)

![Architecture diagram for AI-Powered DevOps Agent for Prometheus Anomaly Detection](/images/solutions/ai-powered-devops-agent-for-prometheus-anomaly-detection/images/ai-powered-devops-agent-for-prometheus-anomaly-detection-1.png)

1. **Step 1**: Amazon Elastic Kubernetes Service (Amazon EKS) hosts the open5gs 5G core and the UERANSIM radio access network (100 gNodeBs, 1,000 user equipment), which emit registration and session metrics.
1. **Step 2**: A Prometheus agent scrapes the metrics and remote-writes them to Amazon Managed Prometheus using SigV4 signing and IAM Roles for Service Accounts.
1. **Step 3**: Amazon Managed Prometheus runs a Random Cut Forest (RCF) anomaly detector on the registered-subscriber count, emitting an anomaly score every 30 seconds.
1. **Step 4**: When the score crosses the threshold, Alertmanager publishes to an Amazon Simple Notification Service (Amazon SNS) topic.
1. **Step 5**: Amazon SNS invokes the forwarder AWS Lambda function.
1. **Step 6**: AWS Lambda reads the DevOps Agent webhook URL and token from AWS Secrets Manager, then posts the incident. It does not investigate.
1. **Step 7**: AWS Lambda posts the incident to the AWS DevOps Agent, which investigates autonomously: it queries Amazon Managed Prometheus through a Model Context Protocol server on Amazon API Gateway, secured by Amazon Cognito.
1. **Step 8**: Engineers run the guided demo and interactive analysis from an Amazon SageMaker notebook.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-ai-powered-devops-agent-for-prometheus-anomaly-detection)

[Read usage guidelines](/solutions/guidance-disclaimers/)
