---
source_url: https://docs.aws.amazon.com/solutions/scheduling-batch-jobs-for-aws-mainframe-modernization/index.html
---

---
title: 'Guidance for Scheduling Batch Jobs for AWS Mainframe Modernization'
canonical_url: https://docs.aws.amazon.com/solutions/scheduling-batch-jobs-for-aws-mainframe-modernization/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Scheduling Batch Jobs for AWS Mainframe Modernization

## Overview

This Guidance demonstrates how to build a simple scheduler for batch jobs migrated to AWS Mainframe Modernization using AWS services such as Amazon EventBridge scheduler and AWS Step Functions. Batch processing is an important component of enterprise applications running on mainframe, and as these batch processes are migrated from mainframe to AWS, they require similar integration between batch processing and scheduling functions. This scheduler pattern can be used for both re-platform migrations, with Common Business Oriented Language (COBOL) or PL1 applications, and re-factor migrations, with the COBOL/PL1 code converted to Java. This Guidance includes two architectures to show how Amazon EventBridge initiates the AWS Step Functions workflow for a single batch job and an orchestration with multiple batch jobs.

## How it works

### Single run

This architecture shows the AWS Step Functions workflow for BatchJobExecution for a single batch job.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/scheduling-batch-jobs-for-aws-mainframe-modernization-single-run.pdf?target=_blank)Step 1The Step Function BatchJobExecution StateMachine performs the AWS Mainframe Modernization batch job execution using the Job Poller pattern. This includes actions such as StartBatchJob, GetBatchJobExecution, and GetLogEvents. Input parameters to the StateMachine include AWS Mainframe Modernization actions such as ApplicationId and JobNameIdentifier.Step 2JobOrchestration StateMachine performs the StartExecution action. Each of the StartExecution actions will execute BatchJobExecution StateMachine. ApplicationId and JobNameIdentifier are set in the input parameters.Step 3StartExecution actions can run serially.Step 4Use "Parallel state" to define the jobs that can execute concurrently.Step 5BatchJobExecution actions are triggered individually or as part of the JobOrchestration flow. Running the actions individually allows you to re-start or re-run any job if needed. For re-start, copy and modify the job flow to start from the next step as a one-time process once the failed job is re-executed separately.### Batch run

This architecture shows the AWS Step Functions workflow for JobOrchestration for multiple batch jobs.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/scheduling-batch-jobs-for-aws-mainframe-modernization-batch-run.pdf?target=_blank)Step 1The Step Function BatchJobExecution StateMachine performs the AWS Mainframe Modernization batch job execution using the Job Poller pattern. This includes actions such as StartBatchJob, GetBatchJobExecution, and GetLogEvents. Input parameters to the StateMachine include AWS Mainframe Modernization actions such as ApplicationId and JobNameIdentifier.Step 2JobOrchestration StateMachine performs the StartExecution action. Each of the StartExecution actions will execute BatchJobExecution StateMachine. ApplicationId and JobNameIdentifier are set in the input parameters.Step 3StartExecution actions can run serially.Step 4Use "Parallel state" to define the jobs that can execute concurrently.Step 5BatchJobExecution actions are triggered individually or as part of the JobOrchestration flow. Running the actions individually allows you to re-start or re-run any job if needed. For re-start, copy and modify the job flow to start from the next step as a one-time process once the failed job is re-executed separately.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-scheduling-batch-jobs-for-mainframe-modernization-service-on-aws/tree/main)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

EventBridge and Step Functions integrate with CloudWatch alarms. In case of an AWS Mainframe Modernization batch job failure or any other type of failure, Amazon Simple Notification Service (Amazon SNS) can send alerts to the user. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

IAM policies manage user access, providing minimum permissions for users to create new schedules or modify existing schedules. The IAM execution role controls service access for services that invoke a batch job on AWS Mainframe Modernization. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Step Functions comes with retry and catch mechanisms, which allow you to implement automated retries of a particular batch job. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Scheduling batch job flows is mostly pre-defined. This Guidance is built on serverless technologies such as EventBridge and Step Functions, so there is no need to provision new hardware or software to set up additional jobs. You can schedule new jobs can by defining additional Step Functions and setting up triggers from EventBridge. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Step Functions cost is based on the number of state transitions only. Because Step Functions is serverless, costs will be based on usage instead scheduler instances that are continuously running. There is no separate cost for hardware or software. Additionally, AWS Free Tier offers 4,000 Step Functions state transitions. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

EventBridge scheduler invokes Step Functions only when it is scheduled to run. Further, the underlying hardware and software component are only provisioned when Step Functions is invoked. This helps you keep resource utilization to a minimum. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
