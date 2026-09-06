---
source_url: https://docs.aws.amazon.com/solutions/latest/performance-testing/scaling-to-production-grade.html
---

# Scaling to Production-Grade Testing
<a name="scaling-to-production-grade"></a>

Moving from "my first load test" to "production-grade performance engineering" requires addressing multi-region distribution, cost optimization, organizational governance, and pre-event readiness.

## Multi-Region Load Distribution
<a name="multi-region-load-distribution"></a>

For applications serving global users, single-region testing produces incomplete results. CDN caching, geographic routing, and regional database replicas behave differently under distributed load.

DLT supports multi-region testing through regional stack deployments. The main stack orchestrates tests across all registered regions simultaneously, aggregating results in a single dashboard.

| Consideration | Guidance |
| --- | --- |
| Region selection | Match your actual user distribution (use CloudFront or ALB access logs) |
| Load distribution | Weight traffic by region proportional to real user patterns |
| Network effects | Each region adds authentic network latency to results |
| Cost optimization | Deploy regional stacks only when running multi-region tests |

## Cost Management for Load Testing
<a name="cost-management-load-testing"></a>

Load testing consumes compute resources proportional to test scale and duration. Plan costs carefully:

| Cost Driver | Mitigation |
| --- | --- |
| Fargate task-hours | Right-size task count using the 200 VU guideline; avoid over-provisioning |
| NAT Gateway data transfer | Use VPC endpoints for AWS service targets when possible |
| CloudWatch data ingestion | Disable live monitoring for routine automated tests |
| Test environment infrastructure | Tear down environments after testing (infrastructure as code) |
| Long-running soak tests | Schedule during off-peak hours for potential Spot pricing on target infra |

## AWS Countdown Premium for Critical Events
<a name="aws-countdown-premium"></a>

When preparing for high-stakes events (product launches, seasonal peaks, migration go-lives), AWS Countdown Premium Short Term Engagements provide expert guidance alongside your DLT implementation.

**What Countdown Premium engineers provide:**
+ Performance testing strategy and methodology guidance
+ JMeter, K6, and Locust script structure review
+ Results analysis and performance optimization recommendations
+ Resource utilization analysis and best practices alignment
+ End-to-end guidance from setup through results interpretation

**Your team maintains:** Test script development, execution, and operations. This is a "do-it-yourself with expert guidance" model that builds internal capability.

**When to engage Countdown Premium:**

If your team lacks in-house performance testing expertise, or if the stakes are high enough that you want expert guidance, consider engaging AWS Countdown Premium when:
+ Preparing for a launch event with >10x normal traffic expected
+ First large-scale performance test for a new workload
+ After discovering production performance issues that need systematic investigation
+ Before peak retail seasons, gaming launches, or media events

**Ready to validate at production scale?** For critical launches and peak events, [AWS Countdown Premium Short Term Engagements](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/cdp.html) provide expert AWS engineers to guide your performance testing strategy. Sign up directly through [AWS Countdown](https://aws.amazon.com/premiumsupport/programs/aws-countdown/) and select "Use Case Implementation."

## Governance and Organizational Patterns
<a name="governance-organizational-patterns"></a>

As performance testing matures across your organization:
+ **Establish a performance testing Center of Excellence (CoE)** that maintains shared DLT infrastructure, script templates, and baseline standards
+ **Define ownership:** Each service team owns their performance SLOs and scripts; the platform team owns shared infrastructure
+ **Create a test catalog:** Document standard test scenarios (smoke, load, stress, soak) with predefined configurations
+ **Automate reporting:** Publish weekly performance trend reports from DLT results to stakeholders
+ **Track improvement:** Use DLT baseline comparison to demonstrate performance improvements quarter over quarter

## Pre-Event Testing Playbook
<a name="pre-event-testing-playbook"></a>

For high-stakes events (product launches, Black Friday, gaming tournaments, marketing campaigns), follow this structured approach:

| Timeline | Action | Outcome |
| --- | --- | --- |
| T-8 weeks | Define event traffic model (expected peak, duration, geographic distribution) | Clear test parameters |
| T-6 weeks | Deploy multi-region DLT stacks matching user distribution | Test infrastructure ready |
| T-4 weeks | Run first full-scale test, identify bottlenecks | Baseline and gap list |
| T-3 weeks | Address bottlenecks (scaling, caching, pre-warming) | Architecture hardened |
| T-2 weeks | Re-test at 150% expected peak, run chaos experiments | Confidence in resilience |
| T-1 week | Final validation test, pre-warm caches and connection pools | Go/no-go decision |
| T-1 day | Smoke test infrastructure, verify monitoring dashboards | Operational readiness |

## Service Quota Planning for Large Tests
<a name="service-quota-planning"></a>

Large-scale load tests often fail due to AWS service quotas, not application bottlenecks. Before running tests above 10,000 VUs, verify these quotas:
+ **ECS Fargate tasks per cluster** (default: varies by region, request increase 2 weeks in advance)
+ **NAT Gateway bandwidth** (default: 100 Gbps per NAT, but burst behavior matters)
+ **Elastic IP addresses** (if using multiple NAT Gateways for source IP distribution)
+ **Target application quotas** (API Gateway throttling, Lambda concurrency, RDS max connections)
+ **CloudWatch PutMetricData TPS** (can throttle at very high test volumes)

Request quota increases at least two weeks before your planned test date. AWS Trusted Advisor provides a quota usage dashboard that shows current consumption against limits.

## Put It Into Practice
<a name="put-it-into-practice-scaling"></a>
+ Create a "Pre-Event Runbook" document in your team wiki using the timeline table above as a template
+ Run `aws service-quotas list-service-quotas --service-code ecs` to check your current Fargate task limits
+ Deploy DLT regional stacks in at least 2 regions matching your top user geographies
+ Run a multi-region test distributing load proportionally (e.g., 60% us-east-1, 25% eu-west-1, 15% ap-southeast-1) and compare regional latency differences
+ Document your organization's performance testing governance model: who owns infrastructure, who owns scripts, who reviews results

```
# Check ECS Fargate task quota in your region
aws service-quotas get-service-quota \
  --service-code ecs \
  --quota-code L-4FC25E62 \
  --region us-east-1

# Request a quota increase for large-scale testing
aws service-quotas request-service-quota-increase \
  --service-code ecs \
  --quota-code L-4FC25E62 \
  --desired-value 500
```

## Investigation at Scale with AWS DevOps Agent
<a name="investigation-at-scale-devops-agent"></a>

Moving from "my first load test" to "production-grade performance engineering" requires not just larger tests but also mature analysis practices. Manual investigation of test results becomes impractical as test frequency and complexity increase. DLT's native AWS DevOps Agent integration transforms post-test analysis from a labor-intensive, manual process into an automated, repeatable workflow.

**Scaling investigation across environments:**

Register multiple Agent Spaces for different purposes. A dedicated Agent Space per environment (development, staging, production) allows each team to investigate independently without cross-contamination of findings:

| Agent Space | Purpose | When to Investigate |
| --- | --- | --- |
| Dev Agent Space | Early regression detection | After every PR merge smoke test |
| Staging Agent Space | Pre-release validation | After full load tests on staging |
| Production Agent Space | Production incident correlation | After canary tests or observed degradation |

**Building a historical investigation record:**

Every DevOps Agent investigation is stored in the DLT Investigations tab for the lifetime of the test run record. Over time, this builds a searchable knowledge base of performance findings. Use this history to:
+ **Track regression patterns.** If the same component appears as a bottleneck across multiple investigations, it signals a systemic architectural issue rather than a one-time configuration problem
+ **Validate remediation effectiveness.** After implementing a fix, compare the investigation findings from the next test run against the original. If the root cause no longer appears, the fix was effective
+ **Inform capacity planning.** Historical investigations reveal which components hit limits first under increasing load, helping you prioritize scaling investments

**Integrating DevOps Agent into CI/CD pipelines:**

Combine the DLT CLI with DevOps Agent for fully automated performance gate workflows:

1. **CI/CD pipeline triggers a load test** via the DLT CLI after deployment to staging

1. **DLT compares results against baseline** and detects if any SLO is violated

1. **If a regression is detected**, the pipeline automatically triggers a DevOps Agent investigation

1. **The investigation findings** are captured and attached to the deployment record

1. **The pipeline fails the deployment** with actionable root-cause information, not just a "latency exceeded threshold" error

This pattern transforms performance gates from binary pass/fail signals into diagnostic workflows that tell engineers *why* performance degraded and *what to fix*, eliminating the manual triage step that typically adds hours or days to incident resolution.

**Providing context for better investigations:**

When triggering an investigation (either manually or via CLI), provide additional context to improve the quality of findings:
+ Recent infrastructure changes (new deployment, scaling policy change, instance type migration)
+ Expected performance baseline (the target SLOs for this test)
+ Known environmental differences (reduced replica count in staging, stubbed external services)

Context helps the agent distinguish between expected behavior and genuine anomalies, reducing false positives and focusing findings on actionable issues.

**Go Deeper**
[AWS DevOps Agent Integration](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/devops-agent-integration.html) (DLT Documentation)
[AWS Service Quotas: Managing your quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) (Service Quotas Documentation)
[AWS Countdown Premium for DLT](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/cdp.html) (DLT Documentation)
[Imagine Learning Case Study: Performance Testing at Scale](https://aws.amazon.com/solutions/case-studies/imagine-learning/) (Customer Case Study)
