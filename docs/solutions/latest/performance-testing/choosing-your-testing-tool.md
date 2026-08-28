---
source_url: https://docs.aws.amazon.com/solutions/latest/performance-testing/choosing-your-testing-tool.html
---

# Choosing Your Testing Tool
<a name="choosing-your-testing-tool"></a>

Performance testing tools fall into two categories: scripting frameworks (how you define test scenarios) and runtime infrastructure (how you execute them at scale). Most teams start with an open-source scripting framework like K6, Locust, or JMeter. The challenge is not writing the script. It is operating the infrastructure to run that script at production-scale concurrency: provisioning load generators, distributing traffic across regions, collecting results, and tearing everything down afterward. That infrastructure management becomes a project in itself.

[Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/distributed-load-testing-on-aws/) (DLT) eliminates that operational burden entirely. DLT handles all infrastructure provisioning, scaling, orchestration, monitoring, and reporting. You write a test script in the framework you already know; DLT runs it at any scale you need. No servers to manage, no load generator fleets to maintain, no scaling logic to build.

Distributed Load Testing on AWS (DLT) is an open-source, fully supported AWS Solution that automates performance testing at scale. It deploys as a self-contained stack in your AWS account, providing a web console, REST API, CLI, and optional MCP server for AI-assisted analysis. You do not need to provision or manage any testing infrastructure. DLT is actively maintained by AWS and receives regular updates, security patches, and feature enhancements. The latest release (v4.2) introduces native integration with AWS DevOps Agent, enabling automated root cause analysis of load test results directly from the DLT console. When a test completes, you can send the full run context to a registered Agent Space, which correlates CloudWatch metrics, logs, and traces to identify bottlenecks and suggest remediation steps without manual investigation.

If your organization uses commercial load testing platforms, DLT is worth evaluating as a complement or replacement, particularly for teams looking to reduce licensing costs while maintaining the same scripting flexibility. DLT is fully open-source and supported by AWS at no additional software cost (you pay only for the underlying compute).

DLT supports scripts written in three open-source frameworks natively:

| Framework | Script Language |
| --- | --- |
| K6 | JavaScript / TypeScript |
| Locust | Python |
| JMeter | .jmx (XML) |

**Network dependency for K6**
K6 binaries are downloaded from Grafana's CDN at test runtime. If your VPC has restricted outbound internet access (private subnets without NAT, strict egress security groups, or proxy-only configurations), K6 tests will fail at the download step. Ensure outbound HTTPS access to `github.com/grafana/k6/releases` from your Fargate tasks, or consider Locust/JMeter which are bundled in the container image. A third option is to customize the container image to include K6 directly. However, K6 is licensed under AGPL-3.0, so you must confirm that bundling it complies with your organization's licensing policies.

If your team already has test scripts in any of these frameworks, bring them directly to DLT. No migration, no rewrite. DLT runs .js, .py, and .jmx files through its Taurus testing engine.

**Traffic shape awareness**
DLT's Traffic Shape configuration controls concurrency, ramp-up duration, and hold duration for your test. Taurus, the underlying execution engine, applies these values and overrides any multi-step or dynamic traffic patterns defined inside your script (K6 stages, Locust custom load shapes, JMeter Ultimate Thread Group configurations). This means complex traffic shaping such as spike tests, stepped ramps, or sawtooth curves cannot be driven from script-level logic alone when running through DLT. If your scenario requires dynamic traffic patterns, use K6 or Locust directly on self-managed infrastructure where the framework controls execution end-to-end, or model the pattern using multiple sequential DLT test runs with different Traffic Shape configurations for each phase. This is a known limitation in the current release (4.2.x). The DLT team is continuously improving the solution and dynamic traffic shaping is an area of active interest. We encourage you to check the latest release notes for updates.

## Running Scripts at Scale with DLT
<a name="running-scripts-at-scale"></a>

DLT executes each script inside an Amazon ECS task on AWS Fargate. We recommend up to 200 virtual users (VUs) on each ECS task. However, based on your needs, the ECS task can be sized to support more users.

As a starting guideline:
+ 1,000 concurrent users → 5 tasks
+ 10,000 concurrent users → 50 tasks
+ 100,000 concurrent users → 500 tasks

DLT also supports generating traffic from multiple AWS Regions simultaneously, allowing you to simulate geographically distributed user traffic and validate how your application performs for users in different locations.

**Example: 1,000,000 concurrent users across 5 Regions**

Traffic distribution should mirror your actual user base. If 40% of your customers are in North America, 25% in Europe, and the rest spread across Asia and Latin America, your test should reflect that:

| Region | VUs | Tasks (at 200 VUs/task) | Rationale |
| --- | --- | --- | --- |
| us-east-1 | 400,000 | 2,000 | 40% of traffic from North America |
| eu-west-1 | 250,000 | 1,250 | 25% of traffic from Europe |
| ap-southeast-1 | 150,000 | 750 | 15% from Southeast Asia |
| ap-northeast-1 | 150,000 | 750 | 15% from Northeast Asia |
| sa-east-1 | 50,000 | 250 | 5% from Latin America |
| Total | 1,000,000 | 5,000 |  |

Distribute VUs proportionally based on real market share, customer geography, or historical traffic analytics. This ensures your test validates performance where your users actually are, not just under idealized uniform load.

Monitor task-level CPU and memory to determine if you need to adjust task count or sizing. DLT handles task orchestration, scheduling, and result aggregation automatically across all regions.

## Architecture Overview
<a name="architecture-overview"></a>

DLT consists of two main components:

**Front End:** A React-based web console (hosted on Amazon CloudFront \+ Amazon S3, or ALB \+ ECS) that provides test management, real-time monitoring, and result visualization. Authentication is handled by Amazon Cognito.

**Back End:** An orchestration engine that uses AWS Step Functions to coordinate test execution. When you start a test, the engine launches Amazon ECS tasks on AWS Fargate, each running your test script inside a container with the Taurus load testing framework. Results flow back through Amazon DynamoDB and Amazon S3.

![Distributed Load Testing on AWS — Architecture](http://docs.aws.amazon.com/solutions/latest/performance-testing/images/perf_dlt_architecture.png)

## Deployment Options
<a name="deployment-options"></a>

DLT offers multiple deployment paths: a guided wizard experience and direct CloudFormation templates for teams that prefer infrastructure-as-code control.

| Deployment Method | Use Case | Experience |
| --- | --- | --- |
| [AWS Launch Wizard](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/deploy-using-aws-launch-wizard.html) (Recommended) | First-time deployments, teams unfamiliar with CloudFormation | Step-by-step guided wizard in the AWS Console with validation and version management |
| CloudFormation: Default (CloudFront \+ S3) | Most self-service deployments | Web console hosted via CloudFront |
| CloudFormation: ALB \+ ECS | Regions without CloudFront, network restrictions, private deployments | Web console via Application Load Balancer |
| CloudFormation: Headless | CI/CD only, no web UI needed | Backend services only (API \+ CLI access) |

AWS Launch Wizard handles prerequisite validation, parameter configuration, and stack deployment in a single guided flow. It also simplifies upgrades: when a new DLT version is available, Launch Wizard presents the update path without requiring manual template URL management.

## Deployment Checklist
<a name="deployment-checklist"></a>
+ Review the [Amazon EC2 Testing Policy](https://aws.amazon.com/ec2/testing/) (required before running large-scale tests)
+ Determine your primary deployment region (this is where orchestration runs)
+ Identify additional regions for multi-region testing (optional)
+ Deploy the main CloudFormation stack (takes approximately 15 minutes)
+ Verify you received the admin invitation email from Amazon Cognito
+ Log in to the web console and create your first test scenario
+ For multi-region: deploy the regional stack in each additional region

## Multi-Region Testing
<a name="multi-region-testing"></a>

DLT supports distributing load from multiple AWS Regions simultaneously. This is critical for validating:
+ Global application performance from different geographies
+ CDN cache behavior under distributed load
+ Regional failover and routing policies

Deploy the regional CloudFormation template in each additional region. Regional stacks register themselves with the main stack and appear in the web console automatically.

## DLT CLI for CI/CD Integration
<a name="dlt-cli-cicd-integration"></a>

The DLT CLI provides headless interaction for pipeline automation:
+ Start test scenarios programmatically
+ Query test results and compare against baselines
+ Download test artifacts for analysis
+ Supports browser OAuth, SRP headless, and IAM authentication modes

## Put It Into Practice
<a name="put-it-into-practice-tool"></a>
+ Deploy DLT in your preferred region using the [deployment guide](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/deploy-the-solution.html)
+ Create a simple HTTP test scenario in the web console (no script required for basic HTTP endpoint testing)
+ Run the test with 1 task and review the results dashboard
+ Explore the percentile metrics (p50, p90, p95, p99) and error rates
+ Set up the DLT CLI for your CI/CD tool of choice

## Troubleshooting Common Deployment Issues
<a name="troubleshooting-common-deployment-issues"></a>

Teams occasionally encounter issues during initial DLT deployment. These are the most common:

| Symptom | Cause | Fix |
| --- | --- | --- |
| CloudFormation stack fails during deployment | Insufficient IAM permissions for the deploying principal | Ensure the deploying role has permissions for ECS, Step Functions, DynamoDB, S3, Cognito, API Gateway, Lambda, and CloudWatch |
| Cannot log in after deployment | Cognito invitation email went to spam or expired | Check spam folder, or manually set the password in the Cognito User Pool console |
| Test tasks fail immediately | Fargate task cannot pull container image | Verify NAT Gateway or VPC endpoints for ECR access in private subnets |
| Results show 0 requests | Test script has errors that prevent execution | Download the task logs from CloudWatch (/aws/ecs/DLT) and check for script syntax errors |
| Test never completes | Step Functions execution timeout | Check the test duration configuration; default execution timeout may be too short for long soak tests |

If deploying in a private subnet configuration (no internet egress), ensure VPC endpoints exist for Amazon ECR, Amazon S3 (gateway endpoint), Amazon DynamoDB (gateway endpoint), and CloudWatch Logs. Without these, Fargate tasks cannot pull images or write results.

**Go Deeper**
[Distributed Load Testing on AWS: Implementation Guide](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/solution-overview.html)
[Ensure Optimal Application Performance with DLT](https://aws.amazon.com/blogs/architecture/ensure-optimal-application-performance-with-distributed-load-testing-on-aws/) (Architecture Blog)
[DLT Features: Test Framework Support](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/features.html) (DLT Documentation)
[Performance Testing on AWS (re:Invent 2025, CMP351)](https://www.youtube.com/watch?v=tyjc6Mknacc) (Video, 20 min)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Performance Testing on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
