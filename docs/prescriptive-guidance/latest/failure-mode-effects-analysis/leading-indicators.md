---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/failure-mode-effects-analysis/leading-indicators.html
---

# Leading indicators
<a name="leading-indicators"></a>

*Leading indicators* tell you whether teams are adopting the methodology and acting on what they find. These metrics give you early signals to course-correct before gaps show up in production.

## Risk identification metrics
<a name="risk-identification-metrics"></a>

These metrics track whether teams are finding risks consistently and with sufficient coverage across their sprint work.

### Risk discovery rate
<a name="risk-discovery-rate.515baba8-9bdb-5671-a341-70f497363dfb"></a>
+ **Definition**:** **Number of potential failure modes identified per sprint
+ **Target**:** **Minimum 3-5 risks per sprint for applications using multiple AWS services
+ **Measurement**:** **Count of documented risks in FMEA register per sprint
+ **Frequency**:** **Weekly tracking, monthly reporting

### Risk coverage ratio
<a name="risk-coverage-ratio.dd2f8f21-3297-5729-9ec7-44cdd9d4e97d"></a>
+ **Definition**:** **Percentage of user stories that receive risk assessment
+ **Target**:** **100% for stories involving AWS services or external integrations
+ **Calculation**:** **(Stories with FMEA analysis / Total stories requiring analysis) × 100
+ **Frequency**:** **Sprint-level tracking

### High-risk item identification
<a name="high-risk-item-identification.889aca51-552b-5ca7-aa8c-ef41814c80c7"></a>
+ **Definition**:** **Number of critical risks (RPN > 400) identified per month
+ **Target**:** **Varies by application complexity, establish baseline
+ **Measurement**:** **Count of risks with RPN > 400 in monthly period
+ **Frequency**:** **Monthly tracking and trending

## Process adoption metrics
<a name="process-adoption-metrics"></a>

These metrics measure how broadly and efficiently teams are integrating FMEA into their sprint workflows.

### Team participation rate
<a name="team-participation-rate.2cea3d33-93e6-5f76-a405-3e672a60a805"></a>
+ **Definition**:** **Percentage of development teams actively using FMEA process
+ **Target**:** **100% of teams within 6 weeks of rollout
+ **Calculation**:** **(Teams using FMEA / Total development teams) × 100
+ **Frequency**:** **Weekly tracking during rollout, monthly thereafter

### Sprint planning integration success
<a name="sprint-planning-integration-success.38bdc85a-5dc3-5858-a8ba-a5cfeddc2fb5"></a>
+ **Definition**:** **Percentage of sprint planning sessions that include FMEA analysis
+ **Target**:** **100% for teams that have completed training
+ **Measurement**:** **Count of sprint planning sessions with documented FMEA activities
+ **Frequency**:** **Sprint-level tracking

### Process efficiency
<a name="process-efficiency.d18fe4ec-55e3-5e11-b458-4b9345413bac"></a>
+ **Definition**:** **Average time spent on FMEA activities per sprint
+ **Target**:** **Less than 45 minutes of additional time in sprint planning
+ **Measurement**:** **Time tracking during FMEA activities
+ **Frequency**:** **Sprint-level measurement, monthly trending

## Risk mitigation metrics
<a name="risk-mitigation-metrics"></a>

These metrics track whether identified risks are being addressed on time and whether the mitigations are actually reducing RPN scores.

### Mitigation implementation rate
<a name="mitigation-implementation-rate.fe3d1693-2550-5159-9eac-7ffb249e9149"></a>
+ **Definition**:** **Percentage of identified risks with implemented mitigations
+ **Target**:** **100% for RPN > 400, 85% for RPN 200-399
+ **Calculation**:** **(Risks with completed mitigations / Total identified risks) × 100
+ **Frequency**:** **Sprint-level tracking, monthly reporting

### Mitigation completion timeliness
<a name="mitigation-completion-timeliness.2fba9e75-5059-525d-9000-a5310b3957c3"></a>
+ **Definition**:** **Percentage of mitigations completed within planned timeframe
+ **Target**:** **90% completion within committed sprint
+ **Calculation**:** **(On-time completions / Total planned mitigations) × 100
+ **Frequency**:** **Sprint-level tracking

### Risk reduction effectiveness
<a name="risk-reduction-effectiveness.28bf3ce8-99d2-55a7-9172-56880c9a2c72"></a>
+ **Definition**:** **Average RPN reduction after mitigation implementation
+ **Target**:** **Minimum 50% reduction for high-priority risks
+ **Calculation**:** **((Original RPN - Post-mitigation RPN) / Original RPN) × 100
+ **Frequency**:** **Monthly assessment of completed mitigations

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
