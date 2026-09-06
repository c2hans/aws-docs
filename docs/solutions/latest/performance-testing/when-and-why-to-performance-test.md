---
source_url: https://docs.aws.amazon.com/solutions/latest/performance-testing/when-and-why-to-performance-test.html
---

# When and Why to Performance Test
<a name="when-and-why-to-performance-test"></a>

Every team that invests in performance testing arrives with a specific question. Some are preparing for a launch that cannot afford to fail. Others have inherited a system that occasionally degrades under load and need to understand why. Some are migrating workloads to AWS and need proof that the new architecture meets or exceeds what they had on premises. The question you bring determines where you focus first, but the discipline you build serves all of them.

Performance testing is not a single activity. It is a practice that spans seven distinct use cases, each with its own trigger, stakeholders, and definition of success.

## The Seven Use Cases
<a name="when-and-why-to-performance-test-seven-use-cases"></a>

| Use Case | Who Typically Drives It | The Core Question |
| --- | --- | --- |
| Launch and High-Traffic Event Prep | Platform Eng, SRE, Product | Can the system handle projected peak load on day one? |
| Reliability Validation | SRE, Platform Eng, Architects | How does the system behave under different load conditions? |
| SRE and Continuous Reliability | SRE, DevOps | Are we meeting our SLOs? Will we catch degradation before customers do? |
| SDLC and Developer Testing | App Developers, DevOps | Did my code change introduce a performance regression? |
| Migration from On-Premises to AWS | Cloud Architects, Platform Eng | Does the new architecture match or exceed on-prem performance baselines? |
| Capacity and Sizing Validation | Cloud Architects, FinOps | Are we right-sized? What is our headroom before we hit limits? |
| Cost Optimization | FinOps, Platform Eng | Can we reduce instance sizes or shift to Graviton without degrading performance? |

## What Each Use Case Looks Like in Practice
<a name="when-and-why-to-performance-test-what-each-use-case-looks-like"></a>

**Launch and High-Traffic Event Prep.** Your product is launching in six weeks, or Prime Day is approaching, or you are running a marketing campaign expected to triple normal traffic. You need to prove, with data, that the system handles the projected peak. Success means running a full-scale load test that simulates the expected concurrency, validating that latency stays within SLOs, and identifying the breaking point so you know your margin. This use case is time-bounded: you test, you validate, you launch.

**Reliability Validation.** You need to understand how the system behaves as load increases, decreases, and fluctuates. This goes beyond "can it handle peak" to "what happens at 50% capacity, at 80%, at 110%?" You are mapping the system's performance envelope: where it performs optimally, where it degrades gracefully, and where it fails. This is the foundation that informs architecture decisions, Auto Scaling configurations, and operational runbooks.

**SRE and Continuous Reliability.** Performance testing is not a one-time event for your team. It is a recurring signal, like uptime monitoring or error rate tracking. You run scheduled load tests against production-like environments to validate SLOs continuously. When a test shows degradation against the baseline, you investigate before customers notice. This transforms performance from a reactive discipline (something broke) into a proactive one (we caught it early).

**SDLC and Developer Testing.** Every pull request is a potential performance regression. You want developers to know, within minutes of merging, whether their change degraded response times or increased resource consumption. This requires lightweight, fast-executing tests integrated into CI/CD that compare each build against a known baseline. The goal is shifting performance accountability left, into the hands of the engineers writing the code.

**Migration from On-Premises to AWS.** You are moving workloads from on-premises infrastructure to AWS. Stakeholders need evidence that the migrated system performs at least as well as what it replaces. This means establishing baselines on the existing on-prem system, replicating equivalent test scenarios on AWS, and producing a comparison that demonstrates parity or improvement. Migrations often reveal latency differences from network path changes, storage I/O characteristics, or instance sizing mismatches that only surface under load.

**Capacity and Sizing Validation.** You have deployed the architecture, but are the instance types, container resource limits, and database configurations right-sized for your workload? Under-provisioning risks degradation at peak; over-provisioning wastes money. Load testing at progressively increasing concurrency reveals where each component saturates, what your actual headroom is, and whether Auto Scaling policies respond fast enough to protect the user experience.

**Cost Optimization.** You suspect you are over-provisioned but cannot reduce capacity without proof that performance holds. Performance testing provides that proof. Run your standard load profile on smaller instances, on Graviton processors, on Spot-backed capacity, or with reduced replica counts. If the test passes your SLOs, you have data-driven justification to right-size. If it fails, you know exactly where the boundary is.

## Mapping Use Cases to This Journey
<a name="when-and-why-to-performance-test-mapping-use-cases"></a>

## Why Every Stage Matters
<a name="when-and-why-to-performance-test-why-every-stage-matters"></a>

Most teams begin with one of these use cases and discover the others along the way. A team preparing for a product launch will establish baselines and SLOs that naturally feed into continuous SRE practice. A team validating a migration will uncover capacity and sizing questions that lead to ongoing cost optimization. A team running developer-level regression tests will realize those same tests, scaled up, become their reliability validation suite.

The stages that follow build a progressive discipline that serves all seven use cases. Defining success criteria, choosing the right test types, designing realistic scenarios, interpreting results, and automating the entire cycle are not optional steps you pick from a menu. They are layers that compound. Skip one and the others lose their foundation. The journey is designed to be read and applied end to end, because performance testing done well is not a checklist — it is a practice that strengthens every time you add a layer.

**Go Deeper**
[AWS Well-Architected Framework: Performance Efficiency Pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)
[AWS Well-Architected Framework: Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
[Operational Readiness Reviews (ORR)](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html)
