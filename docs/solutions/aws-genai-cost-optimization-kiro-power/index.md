---
source_url: https://docs.aws.amazon.com/solutions/aws-genai-cost-optimization-kiro-power/index.html
---

---
title: 'Guidance for AWS GenAI Cost Optimization Kiro Power'
canonical_url: https://docs.aws.amazon.com/solutions/aws-genai-cost-optimization-kiro-power/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for AWS GenAI Cost Optimization Kiro Power

## Overview

This Guidance helps developers identify costly AWS GenAI configurations in their codebase by automating the detection of inefficient usage patterns through static code analysis. The MCP server scans local code to detect patterns across Amazon Bedrock and AgentCore services, then combines these findings with real-time AWS pricing data to generate a detailed cost optimization report. Each finding includes specific file locations, line numbers, and estimated savings for issues like missed prompt caching opportunities, model tier mismatches, and lifecycle misconfigurations. You can automatically discover cost reduction opportunities—ranging from 30% to 90% savings—without manual code review or runtime execution.

## Benefits

### Reduce your GenAI spend automatically

Scan your codebase for costly model usage patterns and receive quantified savings estimates with actionable recommendations. Identify opportunities to substitute expensive models without sacrificing application functionality.

### Optimize costs without leaving your IDE

Run cost analysis directly from your developer workstation using Kiro, Claude, or Cursor. Get near real-time pricing insights combined with static code analysis—no infrastructure changes or deployments required.

### Detect hidden cost inefficiencies in code

Leverage AST parsing and pattern matching to uncover missed lifecycle configurations, suboptimal prompt patterns, and overprovisioned model selections across your Amazon Bedrock and AgentCore implementations.

## How it works

This architecture diagram illustrates how the aws-labs-genai-cost-optimizer MCP server scans user code for AWS GenAI patterns and coordinates with companion MCP servers to generate cost optimization reports. [Download the architecture diagram](downloads/aws-genai-cost-optimization-kiro-power.pdf)

![Architecture diagram for Guidance for AWS GenAI Cost Optimization Kiro Power](/images/solutions/aws-genai-cost-optimization-kiro-power/images/aws-genai-cost-optimization-kiro-power.png)

1. **Step 1**: The MCP Client (Kiro, Claude, or Cursor) calls the genai-cost-optimizer server's scan_project tool over stdio transport (runs as a local process).
1. **Step 2**: The client calls AWS MCP Server and AWS Pricing MCP Server in AWS Cloud for documentation and per-model pricing.
1. **Step 3**: The MCP server performs static code analysis (AST + regex) on the local codebase, detecting patterns for Amazon Bedrock and AgentCore.
1. **Step 4**: Structured findings (model usage, lifecycle configs, prompt patterns, VSC format) return to the client as JSON.
1. **Step 5**: AWS Pricing returns per-model token costs and AWS MCP Server returns best practices and feature docs back to the MCP client.
1. **Step 6**: The MCP client combines findings + pricing to generate a cost optimization report with savings estimates and actionable recommendations.
## Related content

- **Sample code**: Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-samples/sample-aws-genai-ops-demos/tree/main/cost-optimization/aws-genai-cost-optimization-mcp-server)

[Read usage guidelines](/solutions/guidance-disclaimers/)
