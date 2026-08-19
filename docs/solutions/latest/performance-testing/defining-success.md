---
source_url: https://docs.aws.amazon.com/solutions/latest/performance-testing/defining-success.html
---

# Defining Success: SLIs, SLOs, and Performance Budgets
<a name="defining-success"></a>

Before running a single test, you need to define what "good" looks like. Without clear success criteria, load test results become interesting data that never drives decisions. Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets provide the framework.

## SLI, SLO, SLA: The Measurement Stack
<a name="sli-slo-sla-measurement-stack"></a>

| Concept | Definition | Example | Who Owns It |
| --- | --- | --- | --- |
| SLI (Service Level Indicator) | A quantitative measure of service performance | p99 latency of the /checkout API | Engineering team |
| SLO (Service Level Objective) | The target value for an SLI | p99 latency < 500ms over a 30-day window | Engineering \+ Product |
| SLA (Service Level Agreement) | A contractual commitment with consequences | 99.9% availability or service credits issued | Business \+ Legal |

SLIs are what you measure. SLOs are what you target internally. SLAs are what you promise externally. Your load tests should validate SLOs, not SLAs. SLOs are always tighter than SLAs to provide a safety buffer.

## Understanding Percentiles (p50, p90, p95, p99)
<a name="understanding-percentiles"></a>

Performance metrics reported as averages hide critical information. An average response time of 200ms might mean all requests complete in 200ms, or it might mean 99% complete in 100ms while 1% take 10 seconds. Percentiles reveal the distribution.

| Percentile | What It Tells You | Example |
| --- | --- | --- |
| p50 (median) | The typical experience. Half of requests are faster, half are slower | p50 = 120ms means the "normal" user sees 120ms |
| p90 | How the slower end of normal behaves. 10% of requests are slower than this | p90 = 250ms means 1 in 10 requests takes longer than 250ms |
| p95 | The experience for users who are unlucky but not extreme outliers | p95 = 400ms means 1 in 20 requests is this slow or worse |
| p99 | The tail: the worst 1% of experiences. Often where real pain lives | p99 = 1200ms means 1 in 100 requests takes over a second |

Why p99 matters more than average: A system serving 1 million requests per day with p99 = 1200ms means 10,000 requests per day are painfully slow. At scale, tail latency affects real users in real numbers.

Throughout this journey, SLOs and pass/fail criteria are defined in terms of **p99** because it captures the experience of your most affected users, not just the majority.

## Choosing the Right SLIs for Load Testing
<a name="choosing-right-slis"></a>

Not every metric matters equally. Focus load test validation on these categories:

| SLI Category | Metric | Why It Matters for Load Testing |
| --- | --- | --- |
| Latency | p50, p90, p95, p99 response time | Reveals how the system degrades as load increases |
| Throughput | Requests per second (RPS) sustained | Identifies the ceiling before degradation begins |
| Error Rate | Percentage of 5xx responses | Shows when the system breaks, not just slows |
| Saturation | CPU, memory, connection pool utilization | Predicts when autoscaling or limits will trigger |

## Error Budgets and Performance Budgets
<a name="error-budgets-performance-budgets"></a>

An error budget is the acceptable amount of SLO violation within a time window. If your SLO is p99 < 500ms over 30 days, you can tolerate roughly 7 hours of violation per month. When load tests show you are consuming error budget faster than expected, it is a signal to halt feature work and invest in performance.

Apply the same concept to performance budgets in CI/CD:
+ Define a baseline p99 from your last stable release
+ Set a performance budget: new deployments must not exceed baseline \+ 10%
+ Automate this check in your pipeline using DLT scheduled tests with baseline comparison

**Go Deeper**
[Improve application reliability with effective SLOs](https://aws.amazon.com/blogs/mt/improve-application-reliability-with-effective-slos/) (AWS Blog)
[AWS Observability Best Practices: SLI/SLO/SLA](https://aws-observability.github.io/observability-best-practices/guides/operational/business/key-performance-indicators) (AWS Observability)
