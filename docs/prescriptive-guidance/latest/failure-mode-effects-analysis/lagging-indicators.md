---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/failure-mode-effects-analysis/lagging-indicators.html
---

# Lagging indicators
<a name="lagging-indicators"></a>

*Lagging indicators* confirm whether the effort is paying off. Fewer production incidents, faster recovery times, and reduced customer impact are the outcomes that justify the investment.

## Incident reduction metrics
<a name="incident-reduction-metrics"></a>

These metrics show whether proactive risk management is translating into fewer and less severe production incidents.

### Production incident frequency
<a name="production-incident-frequency.612e9fff-bcde-54e4-8bdc-ebb487a4bf82"></a>
+ **Definition**:** **Number of production incidents per month
+ **Target**:** **20% reduction within 6 months of FMEA implementation
+ **Measurement**:** **Count of production incidents from monitoring systems
+ **Frequency**:** **Monthly tracking with quarterly trend analysis

### Preventable incident rate
<a name="preventable-incident-rate.e71e2efb-6db2-5730-bc23-07f5060ba412"></a>
+ **Definition**:** **Percentage of incidents that were identified as risks in FMEA analysis
+ **Target**:** **Increase to 60% of incidents having been pre-identified as risks
+ **Calculation**:** **(Incidents matching FMEA risks / Total incidents) × 100
+ **Frequency**:** **Monthly analysis of incident correlation

### Critical incident reduction
<a name="critical-incident-reduction.e7db7d58-f93c-5188-811c-82a496880439"></a>
+ **Definition**:** **Number of severity 1/2 incidents per quarter
+ **Target**:** **30% reduction within 12 months
+ **Measurement**:** **Count of high-severity incidents from incident management system
+ **Frequency**:** **Quarterly tracking and trending

## Recovery and response metrics
<a name="recovery-and-response-metrics"></a>

These metrics measure how quickly your team detects and resolves incidents when they do occur.

### Mean time to recovery (MTTR)
<a name="mean-time-to-recovery--mttr-.8ae319ff-9ed2-5683-b913-38f9d6b37e93"></a>
+ **Definition**:** **Average time to restore service after incident
+ **Target**:** **15% improvement within 6 months
+ **Measurement**:** **Time from incident start to resolution
+ **Frequency**:** **Monthly calculation, quarterly trending

### Mean time to detection (MTTD)
<a name="mean-time-to-detection--mttd-.36ec0543-cc39-5d08-9a6a-cee175d3488b"></a>
+ **Definition**:** **Average time to detect incidents after occurrence
+ **Target**:** **25% improvement through enhanced monitoring from FMEA
+ **Measurement**:** **Time from incident occurrence to detection
+ **Frequency**:** **Monthly calculation, quarterly trending

### First-time fix rate
<a name="first-time-fix-rate.693824ba-1e56-55de-966e-acf88728396d"></a>
+ **Definition**:** **Percentage of incidents resolved without recurrence within 30 days
+ **Target**:** **10% improvement through better root cause understanding
+ **Calculation**:** **(Incidents with no recurrence / Total resolved incidents) × 100
+ **Frequency**:** **Monthly tracking with 30-day lag

## Customer impact metrics
<a name="customer-impact-metrics"></a>

These metrics capture how effectively FMEA is protecting the end-user experience from service disruptions.

### Customer-affecting incidents
<a name="customer-affecting-incidents.236e1757-1ec5-5103-b3c6-d6ed33a69cae"></a>
+ **Definition**:** **Number of incidents that impact customer experience
+ **Target**:** **25% reduction within 9 months
+ **Measurement**:** **Count of incidents with customer impact classification
+ **Frequency**:** **Monthly tracking, quarterly business review

### Service availability
<a name="service-availability.b24cf20f-9ece-5f41-81b5-572d4ff7b46a"></a>
+ **Definition**:** **Percentage uptime of critical application services
+ **Target**:** **Maintain or improve existing SLA commitments
+ **Calculation**:** **(Total uptime / Total time) × 100
+ **Frequency**:** **Real-time monitoring, monthly reporting

### Customer satisfaction impact
<a name="customer-satisfaction-impact.b11aa10f-b593-5cda-851c-8b263992ac96"></a>
+ **Definition**:** **Customer satisfaction scores related to service reliability
+ **Target**:** **Maintain or improve baseline scores
+ **Measurement**:** **Customer survey responses and support ticket sentiment
+ **Frequency**:** **Quarterly assessment

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
