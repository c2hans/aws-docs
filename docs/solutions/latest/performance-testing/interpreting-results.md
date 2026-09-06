---
source_url: https://docs.aws.amazon.com/solutions/latest/performance-testing/interpreting-results.html
---

# Interpreting Results and Taking Action
<a name="interpreting-results"></a>

Raw load test data is noise without a framework for interpretation. The goal is not to generate graphs but to make decisions: is this release safe to deploy? Do we need to scale differently? Which component is the bottleneck?

## The Results Hierarchy
<a name="results-hierarchy"></a>

**Step 1: Did it pass?** Compare p99 latency, error rate, and throughput against your SLOs. If all metrics are within bounds, the test passes. Use DLT's baseline comparison feature to detect regressions automatically.

**Step 2: Where did it degrade?** Look for inflection points in the results timeline. The moment p99 jumps from 200ms to 800ms often correlates with a specific concurrency level or time in the test. This is your system's practical capacity ceiling.

**Step 3: Why did it degrade?** Correlate DLT results with infrastructure metrics:

| Symptom in DLT | Likely Cause | Where to Look |
| --- | --- | --- |
| p99 increases while p50 stays flat | Resource contention affecting tail requests | CPU utilization, garbage collection, thread pool saturation |
| Error rate spikes at specific concurrency | Hard limit reached | Database connections, service quotas, load balancer limits |
| Throughput plateaus despite more VUs | Bottleneck somewhere in the path | CloudWatch Application Signals service map, queue depths, downstream service metrics |
| Latency increases linearly with load | Insufficient horizontal scaling | Auto Scaling policies, ECS task count, Lambda concurrency |
| Intermittent timeouts | Network or DNS issues | VPC flow logs, NAT gateway throughput, DNS resolution times |

## Observability During Load Tests
<a name="observability-during-load-tests"></a>

Effective load test analysis requires instrumentation beyond what DLT provides. Set up these observability layers before your test:

| Layer | Tool | What It Reveals |
| --- | --- | --- |
| Distributed Tracing | AWS X-Ray (instrumented via ADOT) | Which service in the call chain is slow, with vendor-neutral OpenTelemetry instrumentation |
| Infrastructure Metrics | Amazon CloudWatch | CPU, memory, network, disk I/O per component |
| Application Observability | CloudWatch Application Signals | End-to-end service map, automatic service discovery and metric collection (latency, availability) with user-defined SLOs tracked against those metrics |
| Log Analysis | Amazon CloudWatch Logs Insights | Error patterns, slow query identification |

OpenTelemetry is the recommended instrumentation standard (the X-Ray SDK entered maintenance mode in February 2026). ADOT collects traces, metrics, and logs using the OpenTelemetry SDK and exports them to the appropriate AWS backends: traces to AWS X-Ray, metrics and logs to CloudWatch. CloudWatch Application Signals consumes this telemetry to provide a unified service map, automatically collected service-level indicators, and user-defined SLO tracking. Traces are accessible via Transaction Search directly in the CloudWatch console, so you do not need to switch between X-Ray and CloudWatch during post-test analysis.

## Service-Specific Insights
<a name="service-specific-insights"></a>

Beyond general-purpose CloudWatch metrics, AWS provides specialized observability tools that surface performance data specific to each compute and data layer. Enable these before running load tests to get deeper visibility into service-level bottlenecks:

| Service | Insight Tool | What It Reveals During Load Tests |
| --- | --- | --- |
| Amazon ECS / EKS | Container Insights | Per-task and per-pod CPU, memory, network, and disk metrics. Identifies which containers are saturated, which tasks are restarting, and whether cluster Auto Scaling is keeping pace with demand. |
| AWS Lambda | Lambda Insights \+ standard CloudWatch metrics | Cold start frequency and duration, init duration, memory utilized vs. allocated, CPU time, disk and network I/O per invocation. Throttle monitoring (concurrency limit rejections) comes from the standard CloudWatch Lambda Throttles metric, not from Lambda Insights. When concurrency limits are hit, Lambda rejects synchronous invocations immediately rather than queuing them. |
| Amazon RDS / Aurora | Performance Insights | Top SQL queries by load (Active Sessions), wait events (I/O, lock, CPU), and database load decomposition. Pinpoints exactly which queries degrade under concurrent access. |
| Amazon DynamoDB | CloudWatch Contributor Insights | Hot partition keys and throttled items. Reveals uneven access patterns that only surface at scale when certain partition keys receive disproportionate traffic. Note: Contributor Insights offers two modes: full access pattern visibility (accessed and throttled keys) and a cost-optimized throttled-keys-only mode that emits data only during throttling events. The throttled-keys-only mode is the AWS-recommended default for always-on monitoring. |

Enable these tools in your staging environment before running tests. The overhead varies by service: DynamoDB Contributor Insights introduces no performance impact per AWS documentation, Lambda Insights adds a lightweight extension per invocation, and Container Insights and Performance Insights are designed for always-on production use. The diagnostic value during post-test analysis far exceeds what aggregate CloudWatch metrics alone can provide.

## Building a Performance Analysis Workflow
<a name="building-performance-analysis-workflow"></a>

Raw DLT output provides aggregate percentiles and throughput curves. Turning those numbers into architectural decisions requires a systematic analysis workflow:

**Step 1: Identify the inflection point.** In the DLT results timeline, find the exact moment where p99 diverges from p50. This concurrency level is your system's "knee" where contention begins. Note the timestamp and correlate it with infrastructure metrics.

**Step 2: Isolate the bottleneck layer.** Use the CloudWatch Application Signals service map to identify which service in the call chain contributed the most latency at the inflection point. Application Signals correlates traces, metrics, and SLO status in a single view, so you can pinpoint the degrading service without switching between consoles. Common bottlenecks: database queries that lack indexes, synchronous calls to downstream services that should be async, connection pools that are too small for the concurrency level.

**Step 3: Quantify the impact.** Calculate the "latency budget breakdown" at peak load:

| Component | Latency at Baseline | Latency at Peak | Delta |
| --- | --- | --- | --- |
| API Gateway | 5ms | 8ms | \+3ms |
| Lambda cold start | 0ms (warm) | 200ms (cold starts under scale) | \+200ms |
| DynamoDB query | 10ms | 10ms | \+0ms |
| Downstream API | 50ms | 450ms | \+400ms |
| Total | 65ms | 668ms | \+603ms |

This breakdown immediately reveals that the downstream API is the dominant contributor to degradation. Without this breakdown, teams often optimize the wrong component.

**Step 4: Classify the finding.** Is the bottleneck fixable by you (code, configuration, architecture), or does it require an external dependency change? Route each finding to the right team immediately, not after the full analysis is complete.

## CloudWatch Logs Insights Queries for Post-Test Analysis
<a name="cloudwatch-logs-insights-queries"></a>

After a load test, these CloudWatch Logs Insights queries help pinpoint issues:

```
# Find the slowest requests during the test window
fields @timestamp, @message
| filter @timestamp between '2026-07-01T10:00:00Z' and '2026-07-01T11:00:00Z'
| filter latency_ms > 1000
| sort latency_ms desc
| limit 20
```

## Put It Into Practice
<a name="put-it-into-practice-results"></a>
+ Before running your next load test, define pass/fail criteria tied to SLOs
+ Instrument your application with OpenTelemetry (via ADOT) and enable CloudWatch Application Signals
+ Create a CloudWatch dashboard with key metrics for your application
+ Run a load test and practice correlating DLT results with CloudWatch metrics
+ Identify the first bottleneck and document it as a performance improvement backlog item

## Automated Root Cause Analysis with AWS DevOps Agent
<a name="automated-root-cause-analysis"></a>

Manually correlating metrics, logs, and traces after a load test is time-consuming and error-prone. DLT v4.2 introduces native integration with AWS DevOps Agent, enabling automated investigation of load test results directly from the DLT console.

When you connect an Agent Space to your DLT deployment, you can send any completed test run to the agent for analysis. The agent proactively identifies performance bottlenecks, determines root causes, and suggests remediation steps without requiring you to manually parse CloudWatch metrics, dig through log groups, or trace individual requests through your service graph.

**How it works:**

| Step | Action | What Happens |
| --- | --- | --- |
| 1 | Register an Agent Space | Tag your Agent Space with dlt-integration: allowed, then register its ARN in the DLT console under Agent Integration |
| 2 | Run a load test | Execute any test scenario (load, stress, endurance, spike) and wait for completion |
| 3 | Investigate | Click "Investigate with DevOps Agent" on the test run detail page. Optionally provide context about recent infrastructure changes |
| 4 | Review findings | The agent produces a structured root-cause analysis with symptoms, contributing components, and concrete remediation suggestions |

**When to use automated investigation:**

Use DevOps Agent as your **first-pass triage** after every test run. Let the agent surface likely causes, then validate its findings using the manual correlation techniques described in the previous sections. The agent excels at identifying patterns across hundreds of metrics and log streams simultaneously, a task that would take a human analyst significantly longer.

Automated investigation is particularly valuable for:
+ **Post-regression detection.** When your CI/CD pipeline flags a performance regression, immediately trigger an investigation to understand *why* the regression occurred before it reaches production
+ **Endurance test analysis.** After multi-hour soak tests, the volume of metrics data makes manual analysis impractical. DevOps Agent can identify time-dependent degradation patterns (memory leaks, connection pool exhaustion, log file growth) that emerge gradually
+ **Multi-service bottleneck identification.** When your application spans dozens of microservices, the agent correlates signals across all components to pinpoint which service in the chain is the true root cause

**Prerequisites for DevOps Agent integration:**
+ The Agent Space must be in the same AWS account as your DLT deployment
+ The Agent Space must be tagged with the key `dlt-integration` and value `allowed` (this establishes dual consent between the DLT operator and the Agent Space administrator)
+ The tag must be present before DLT will accept connection or investigation requests

**What findings include:**
+ A structured root-cause analysis identifying which components contributed to latency or errors
+ A list of symptoms observed during the test window (CPU saturation, connection pool exhaustion, throttling events, error spikes)
+ Concrete remediation suggestions with specific configuration changes, architectural adjustments, or scaling actions
+ Investigations remain in the DLT Investigations tab for the lifetime of the test run record, building a historical knowledge base as your application evolves

**Go Deeper**
[AWS DevOps Agent Integration](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/devops-agent-integration.html) (DLT Documentation)
[Amazon CloudWatch Service Level Objectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) (CloudWatch Documentation)
[Monitor application health using SLOs with CloudWatch Application Signals](https://aws.amazon.com/blogs/mt/how-to-monitor-application-health-using-slos-with-amazon-cloudwatch-application-signals/) (AWS Blog)
