---
source_url: https://docs.aws.amazon.com/solutions/latest/performance-testing/chaos-engineering-meets-load-testing.html
---

# Chaos Engineering Meets Load Testing
<a name="chaos-engineering-meets-load-testing"></a>

Load testing tells you how the system performs under expected conditions. Chaos engineering tells you how it performs when things go wrong. Combining both reveals whether your system degrades gracefully or catastrophically when failures occur under load.

## The Combined Pattern: DLT \+ AWS Fault Injection Service
<a name="combined-pattern-dlt-fis"></a>

AWS Fault Injection Service (FIS) lets you inject controlled faults into your AWS environment: terminate instances, throttle APIs, add network latency, disrupt AZ connectivity. Running FIS experiments during an active DLT load test creates the most realistic validation of system resilience.

![Chaos Engineering Meets Load Testing](https://docs.aws.amazon.com/solutions/latest/performance-testing/images/perf_chaos_load.png)

## Common DLT \+ FIS Experiment Combinations
<a name="common-dlt-fis-combinations"></a>

| Scenario | DLT Configuration | FIS Action | What You Learn |
| --- | --- | --- | --- |
| AZ failure under load | Steady-state load at 70% capacity | Disrupt one AZ | Does traffic rebalance without user impact? |
| Database failover | Normal transactional load | Force RDS failover | How long is the brownout during failover? |
| Network degradation | Full production-scale load | Add 200ms latency to VPC | Does the system timeout or gracefully degrade? |
| Instance termination | Peak load simulation | Terminate 30% of EC2 instances | Does Auto Scaling recover before SLOs breach? |
| Dependency throttling | Normal load | Throttle downstream API calls | Does circuit breaking activate correctly? |

## Designing Your First Chaos \+ Load Experiment
<a name="designing-first-chaos-load-experiment"></a>

1. **Start with a steady-state hypothesis.** Example: "Under 5000 VUs, if one AZ fails, p99 latency will not exceed 1 second and error rate will not exceed 0.5% after a 60-second recovery window."

1. **Establish the baseline.** Run the DLT load test without any faults. Record p99, p50, error rate, and throughput.

1. **Inject the fault.** While DLT is running at steady state, trigger the FIS experiment. Observe the delta from baseline.

1. **Validate recovery.** After the FIS experiment completes, the system should return to baseline metrics within your recovery time objective.

1. **Document findings.** Record whether the hypothesis held, what the actual impact was, and what improvements are needed.

## Starter FIS Experiment: AZ Failure Under Load
<a name="starter-fis-experiment"></a>

This CloudFormation snippet defines a reusable FIS experiment template that disrupts connectivity to a single Availability Zone. Run it while a DLT load test is active to validate multi-AZ resilience.

```
# fis-az-failure-template.yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  AZFailureExperiment:
    Type: AWS::FIS::ExperimentTemplate
    Properties:
      Description: "Simulate single-AZ failure during active load test"
      RoleArn: !GetAtt FISRole.Arn
      StopConditions:
        - Source: aws:cloudwatch:alarm
          Value: !GetAtt SafetyAlarm.Arn
      Targets:
        TargetSubnets:
          ResourceType: aws:ec2:subnet
          ResourceTags:
            az-chaos-target: "enabled"
          SelectionMode: COUNT(2)
      Actions:
        DisruptConnectivity:
          ActionId: aws:network:disrupt-connectivity
          Parameters:
            scope: all
          Targets:
            Subnets: TargetSubnets
      Tags:
        experiment-type: resilience-validation
```

**Safety guardrails:** The `StopConditions` alarm should fire if error rate exceeds 10% or if a business-critical health check fails. This automatically halts the experiment before it causes real customer impact. Tag subnets you want FIS to target with `az-chaos-target: enabled` so the blast radius is always explicit and auditable.

**Running the combined test:**

1. Start a DLT load test and wait for steady-state metrics to stabilize (typically 2-3 minutes)

1. Trigger the FIS experiment via the console, CLI (`aws fis start-experiment`), or your CI/CD pipeline

1. Monitor the DLT real-time dashboard alongside CloudWatch Application Signals service map

1. After FIS completes, observe the recovery curve: how long until metrics return to pre-fault levels?

## Interpreting Chaos Results
<a name="interpreting-chaos-results"></a>

The most valuable output of a chaos experiment is not whether the test "passed" but what the degradation curve looked like during the fault:

| Observation | Implication | Action |
| --- | --- | --- |
| p99 spiked briefly then recovered within 30 seconds | Health checks and routing are working correctly | Document as expected behavior, add to runbook |
| Error rate increased but never exceeded SLO | System degrades gracefully under partial failure | Increase blast radius in next experiment |
| Metrics never recovered until fault was manually stopped | Auto-healing is not working as expected | Fix health checks, scaling triggers, or circuit breakers before the next production deployment |
| No observable impact at all | Either the fault did not reach the right component, or redundancy is working perfectly | Verify fault reached target, then celebrate if redundancy confirmed |

## Put It Into Practice
<a name="put-it-into-practice-chaos"></a>
+ Deploy AWS Fault Injection Service in your test environment
+ Create a simple FIS experiment template (start with: terminate one ECS task)
+ Run a DLT load test at moderate load (50% expected peak)
+ While the load test is running, trigger the FIS experiment
+ Compare the "with fault" results against your "no fault" baseline
+ Document the system's actual behavior vs. your hypothesis

**Go Deeper**
[Chaos Testing with AWS Fault Injection Service and AWS CodePipeline](https://aws.amazon.com/blogs/architecture/chaos-testing-with-aws-fault-injection-simulator-and-aws-codepipeline) (Architecture Blog)
[Simulating partial failures with AWS Fault Injection Service](https://aws.amazon.com/blogs/mt/simulating-partial-failures-with-aws-fault-injection-service/) (Management & Governance Blog)
