---
source_url: https://docs.aws.amazon.com/solutions/latest/performance-testing/designing-realistic-test-scenarios.html
---

# Designing Realistic Test Scenarios
<a name="designing-realistic-test-scenarios"></a>

A load test is only as useful as the traffic pattern it simulates. Testing with uniform request patterns against a single endpoint produces misleading results. Real users navigate flows, carry sessions, generate varied payloads, and arrive in unpredictable patterns.

## Principles of Realistic Workload Design
<a name="principles-realistic-workload-design"></a>

**Model real user journeys, not individual requests.** A checkout flow involves authentication, product browsing, cart operations, and payment. Test the full sequence.

**Use production traffic analysis to determine request ratios.** If 60% of traffic hits your product catalog, 25% hits search, and 15% hits checkout, your test script should reflect these proportions.

**Include think time between requests.** Real users pause between actions. Without think time, your test generates artificial burst patterns that do not represent production behavior. A 1-5 second think time between requests is typical for web applications.

**Vary data inputs.** Use parameterized test data. If every virtual user searches for the same product ID, you are testing your cache, not your system. CSV data files with varied inputs produce more realistic database and service load.

## Test Data Strategy
<a name="test-data-strategy"></a>

| Data Need | Approach |
| --- | --- |
| User credentials | Generate test accounts in bulk, never use production credentials |
| Product/entity IDs | Extract a representative sample from production, sanitize PII |
| Geographic distribution | Deploy DLT regional stacks to simulate users from multiple regions |
| Payload variety | Create parameterized templates that inject random but valid data |
| Session state | Use cookie handling and token management in your scripts |

## Environment Considerations
<a name="environment-considerations"></a>

| Factor | Recommendation |
| --- | --- |
| Infrastructure parity | Test environment should match production instance types, replica counts, and configuration |
| Database state | Pre-load test data that represents production data volume |
| External dependencies | Use stubs for third-party services, or coordinate testing windows |
| Auto Scaling | Verify scaling policies match production (or test them) |
| Service quotas | Check AWS service quotas before generating large load |
| Cost monitoring | Set AWS Budgets with automated actions (stop instances, halt deployments) before long-running tests. Note: Cost Explorer data can lag up to 8 hours, so billing alerts alone may not catch runaway costs in time. Use Budgets Actions for hard stops. |

## Common Pitfalls
<a name="common-pitfalls"></a>
+ **Testing only the happy path.** Include error scenarios: invalid tokens, 404 pages, timeout flows.
+ **Ignoring warm-up.** JIT compilation, connection pool initialization, and cache warming affect early metrics. Include a ramp-up period and exclude warm-up data from analysis.
+ **Testing in isolation.** If your production system depends on downstream services, the load test should include those interactions.
+ **Using unrealistic concurrency ramps.** Real traffic rarely jumps from 0 to 10,000 instantly (unless you are testing spike scenarios specifically). Model gradual ramp patterns.

## Script Structure Best Practices
<a name="script-structure-best-practices"></a>

Regardless of which tool you choose (K6, Locust, or JMeter), well-structured test scripts share common patterns:

| Pattern | What It Does | Why It Matters |
| --- | --- | --- |
| Setup/teardown phases | Create test data before load, clean up after | Prevents test pollution across runs |
| Transaction grouping | Group related requests into named transactions | Enables per-flow latency analysis |
| Parameterized data | Load inputs from CSV/JSON files | Prevents cache-only testing |
| Assertions within script | Check response codes and body content | Catches functional errors under load |
| Custom metrics | Tag business operations (e.g., "checkout\_complete") | Connects technical metrics to business outcomes |

A common anti-pattern is testing individual API endpoints in isolation (unless you are Unit Testing). Real users execute multi-step flows. If your checkout API depends on a session created by the login API, test the full flow. Session dependencies, cookie propagation, and token refresh all affect real-world performance and must be modeled in your scripts.

## Determining the Right Concurrency Target
<a name="determining-right-concurrency-target"></a>

One of the most frequent questions: "how many virtual users should I simulate?" The answer comes from your production analytics:

1. **Find peak concurrent sessions.** Check your ALB or CloudFront access logs for the highest simultaneous active connections in the past 90 days.

1. **Apply a safety multiplier.** Test at 1.5x to 2x your observed peak to account for growth and unexpected spikes.

1. **Convert sessions to VUs.** Each DLT virtual user represents one concurrent session executing your scripted flow.

1. **Calculate task count.** Divide your target VU count by 200 (the VUs-per-task guideline) to determine how many Fargate tasks you need.

Example: If your peak is 3,000 concurrent sessions, test at 4,500 to 6,000 VUs (23 to 30 DLT tasks).

## Put It Into Practice
<a name="put-it-into-practice-scenarios"></a>
+ Export one hour of peak production access logs from your ALB or CloudFront distribution
+ Identify the top 5 request paths by volume percentage and use these ratios in your test script
+ Add think time to your test script: `sleep(randomBetween(1, 5))` between each request in K6, or `time.sleep(random.uniform(1, 5))` in Locust
+ Create a CSV file with at least 1,000 unique parameterized inputs (user IDs, product IDs, search terms)
+ Run two tests: one with parameterized data and one without. Compare the p99 difference to see how much your cache was masking

**Go Deeper**
[Load testing applications: Design realistic scenarios](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/design-realistic-scenarios.html) (AWS Prescriptive Guidance)
