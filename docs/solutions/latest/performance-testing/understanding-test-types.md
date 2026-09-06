---
source_url: https://docs.aws.amazon.com/solutions/latest/performance-testing/understanding-test-types.html
---

# Understanding Test Types
<a name="understanding-test-types"></a>

The term "load test" is often used as a catch-all, but there are eight distinct test types, each answering a different question about your system. Running the wrong type wastes time and produces misleading confidence.

## The Eight Performance Test Types
<a name="eight-performance-test-types"></a>

| Test Type | Question It Answers | Load Pattern | Duration | When to Use |
| --- | --- | --- | --- | --- |
| Smoke Test | Is the system fundamentally working? | Minimal load (1-5 VUs, Virtual Users) | 1-2 min | After every deployment, before running heavier tests |
| Load Test | Can the system handle expected peak traffic? | Ramp to target concurrency, hold steady | 15-60 min | Before every release |
| Baseline Test | What is our normal performance sweet spot? | Expected average load, held steady | 15-30 min | After infra changes, to establish the reference for deviation alerts |
| Stress Test | Where does the system break? | Ramp beyond expected peak until failure | Until breaking point | Quarterly or after architecture changes |
| Endurance (Soak) Test | Does performance degrade over time? | Moderate sustained load | 4-24 hours | Monthly, after memory-leak fixes |
| Scalability Test | Does the system scale linearly? | Stepped increases (1x, 2x, 4x, 8x) | 30 min per step | After Auto Scaling configuration changes |
| Spike Test | Can the system handle sudden bursts? | Instant jump to high load, then back to baseline | 5-15 min | Before flash sales, marketing campaigns |
| Volume Test | How does large data volume affect performance? | Normal user load with large payloads/datasets | 30-60 min | Before data migrations, bulk operations |

## Smoke Tests: Fail Fast Before You Invest
<a name="smoke-tests"></a>

A smoke test is the quickest sanity check in your performance toolkit. It runs minimal traffic (1-5 virtual users) for a short duration against your critical endpoints immediately after deployment. The goal is not to stress the system. The goal is to confirm nothing is fundamentally broken before you invest time in longer, heavier tests.

Think of it as the performance equivalent of a health check. If response times are wildly off or error rates spike under trivial load, something regressed in the deployment. You catch it in 60 seconds instead of discovering it 30 minutes into a full load test, or worse, from real users.

Smoke tests belong at the very start of your CI/CD performance stage: deploy → smoke → proceed to load/stress only if smoke passes.

## Baseline Tests: Know Your Sweet Spot
<a name="baseline-tests"></a>

A baseline test establishes the known-good performance profile of your system under expected average conditions. It captures your p50, p90, p99 latencies, throughput ceiling, error rates, and resource utilization at a steady, sustainable load. This becomes your reference point.

Once a baseline is established, every subsequent test result is compared against it. The question shifts from "is this fast?" to "is this different from what we expect?" A deviation beyond a defined threshold triggers investigation, regardless of whether the absolute number looks acceptable.

| Baseline Metric | Example Value | Investigation Threshold |
| --- | --- | --- |
| p99 Latency | 320ms | > 368ms (\+15%) |
| Throughput | 4,200 RPS | < 3,570 RPS (-15%) |
| Error Rate | 0.02% | > 0.1% |

Baselines are not static. Re-establish them after significant architecture changes, capacity modifications, or major feature releases. Store baseline results alongside your test scripts in version control so the team can trace performance evolution over time.

## Load Tests: Validate Your Peak Capacity
<a name="load-tests"></a>

A load test answers the most fundamental question before any release: can the system handle the traffic you expect? You ramp concurrency to your projected peak (derived from production analytics, campaign forecasts, or contract SLAs), hold it steady for 15-60 minutes, and verify every SLO remains within bounds.

The key to a useful load test is realistic target concurrency. Pulling numbers from thin air leads to false confidence. Use your CloudWatch metrics, Application Load Balancer access logs, or analytics platform to determine your actual peak concurrent users over the last 30 days, then add a 20-30% buffer for organic growth.

Load tests belong at two points in your workflow: before every production release (to catch regressions against the known baseline), and after any infrastructure change (instance type migration, scaling policy update, database engine upgrade). A load test that passes gives your team confidence to ship. A load test that fails gives you specific data about what broke and where.

## Stress Tests: Find Your Breaking Point
<a name="stress-tests"></a>

A stress test is not designed to pass. It deliberately pushes the system beyond expected peak until something fails. The purpose is to discover your weakest link before your customers do.

Ramp concurrency progressively beyond your load test target. Keep increasing until you observe one of these failure signals: error rates spike above your SLO, response times degrade past acceptable thresholds, a component crashes or becomes unresponsive, or Auto Scaling hits a resource quota. The specific failure mode tells you where to invest. A database connection limit hit means you need connection pooling or read replicas. A Lambda concurrency throttle means you need reserved concurrency or architecture redesign. A memory exhaustion crash means you have a leak or undersized instances.

Run stress tests quarterly or after any significant architecture change. Document the breaking point and the failure mode. When the breaking point increases over time, your architecture is improving. When it decreases, something regressed.

## Endurance (Soak) Tests: Catch Time-Dependent Degradation
<a name="endurance-soak-tests"></a>

Some bugs only surface after hours of sustained operation. Memory leaks that accumulate 10MB per hour are invisible in a 30-minute load test but crash your service overnight. Connection pool exhaustion that takes 6 hours to manifest never appears in shorter runs. Log file growth that consumes disk space over days is undetectable in minutes.

An endurance test applies moderate, steady load (your average traffic level, not peak) for an extended duration: 4-24 hours depending on your confidence level. While it runs, you watch for metrics that trend in one direction rather than oscillating around a stable baseline: memory utilization creeping upward, response times slowly degrading, available connections declining, or disk usage growing.

The interpretation is straightforward. If metrics are stable after 8\+ hours, your system handles sustained operation well. If any metric trends monotonically in a bad direction, you have a resource leak that will eventually cause a production incident. Run endurance tests monthly, after deploying memory-related fixes, or when production monitoring shows unexplained gradual degradation.

## Scalability Tests: Verify Linear Scaling
<a name="scalability-tests"></a>

A scalability test answers whether your system scales proportionally. If you double the load, does throughput double? Or does latency more than double, indicating a bottleneck that gets worse with scale?

Run stepped increases: 1x baseline, then 2x, 4x, and 8x. At each step, hold steady for 30 minutes and record throughput, latency, and resource utilization. Plot these on a graph. Linear scaling means throughput increases proportionally with load while latency remains flat. Sub-linear scaling (throughput gains diminish at higher load) indicates a shared resource bottleneck: a database lock, a singleton connection, or a component that cannot be horizontally scaled.

Scalability tests are essential after Auto Scaling configuration changes, when migrating from vertical to horizontal scaling architectures, or when preparing for a known traffic event that exceeds any previous peak. They tell you not just whether your system can handle a specific number, but whether your architecture can grow.

## Spike Tests: Validate Elasticity Under Sudden Bursts
<a name="spike-tests"></a>

A spike test simulates what happens when traffic jumps instantly: a flash sale goes live, a marketing email lands in millions of inboxes, or a viral post sends a flood of visitors in seconds. Unlike a load test that ramps gradually, a spike test jumps directly from baseline to peak with no warm-up period.

The questions it answers: How quickly does Auto Scaling respond? Do requests queue, timeout, or drop during the scaling lag? Does the system recover to baseline performance after the spike subsides? Does any component have a cold-start penalty that compounds under sudden demand?

Run spike tests before any planned high-traffic event (product launches, sales campaigns, live broadcasts) and after changing Auto Scaling policies. The pass criteria are: no requests dropped during the spike, error rate remains below SLO, and the system returns to baseline latency within a defined recovery window (typically 30-60 seconds after scaling completes).

## Volume Tests: Measure Data-Scale Impact
<a name="volume-tests"></a>

A volume test keeps user concurrency normal but dramatically increases data size. Normal traffic with 10x larger payloads, database tables with 100x more rows, or API responses returning full datasets instead of paginated subsets. This catches issues that only appear at data scale, not user scale.

Common findings from volume tests: queries that perform well on 10,000 rows become unacceptable on 10 million rows (missing indexes, full table scans), serialization of large API responses causes memory pressure and garbage collection pauses, file upload processing times grow non-linearly with file size, and batch operations that work fine with 100 items timeout at 10,000 items.

Run volume tests before data migrations, when introducing bulk import/export features, ahead of known data growth milestones (e.g., approaching the first million records), or when production monitoring shows query performance degrading as tables grow. The fix is almost always better indexing, pagination, streaming, or architectural changes to how you handle large datasets.

## Choosing the Right Test for Your Situation
<a name="choosing-right-test"></a>

![Choosing the Right Test for Your Situation](http://docs.aws.amazon.com/solutions/latest/performance-testing/images/perf_decision_tree.png)

## Common Mistakes in Test Type Selection
<a name="common-mistakes-test-type-selection"></a>

Teams frequently make errors that render their test results misleading:

**Running only load tests.** A load test validates expected capacity but tells you nothing about what happens when that capacity is exceeded. Without stress tests, you discover breaking points from customers, not from controlled experiments. Schedule quarterly stress tests alongside your regular load tests.

**Skipping endurance tests.** Memory leaks, connection pool exhaustion, thread starvation, and log file growth are time-dependent failures that never appear in a 15 minute load test. If your application runs 24/7, you need endurance tests that run for at least 4 hours. Many production outages trace back to resource exhaustion that only manifests after sustained operation.

**Confusing spike tests with stress tests.** A stress test gradually increases load to find the ceiling. A spike test jumps instantly to a high level and measures recovery. They answer different questions: "how much can it handle?" versus "can it handle sudden shock?" Flash sales, marketing email blasts, and viral social media moments are spike scenarios, not stress scenarios.

**Using inappropriate test durations.** A 2 minute load test does not exercise Auto Scaling, connection pool recycling, or JIT compilation warm-up. Most load tests need a minimum of 15 minutes at steady state (after ramp-up) to produce meaningful results. Soak tests need a minimum of 4 hours to catch time-dependent degradation.

## Combining Test Types into a Testing Calendar
<a name="combining-test-types-calendar"></a>

Mature teams run multiple test types on different schedules:

Start with the simplest schedule: a smoke load test on every PR merge. This catches the most damaging regressions (a broken endpoint, a missing environment variable, a misconfigured timeout value) before they compound.

| Cadence | Test Type | Purpose |
| --- | --- | --- |
| Every PR merge | Smoke load test (50 VUs, 2 min) | Catch obvious regressions |
| Nightly | Full load test (production-scale, 15 min) | Continuous capacity validation |
| Weekly | Endurance test (moderate load, 4-8 hours) | Detect time-dependent degradation |
| Quarterly | Stress test (ramp to failure) | Update known capacity ceiling |
| Pre-event | Spike test (150% expected peak, instant ramp) | Validate event readiness |

**Go Deeper**
[Load testing applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/introduction.html) (AWS Prescriptive Guidance)
[Validate system reliability with performance testing (QA.NT.2)](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.2-validate-system-reliability-with-performance-testing.html) (Well-Architected DevOps Guidance)
