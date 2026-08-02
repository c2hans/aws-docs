---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/failure-mode-effects-analysis/implementation-guidelines.html
---

# Implementation guidelines for FMEA
<a name="implementation-guidelines"></a>

This section provides the reference material teams need when conducting Failure Mode and Effects Analysis (FMEA) in practice. It covers how to tailor the methodology to your environment, detailed scoring scales for severity, occurrence, and detection, and guidance on choosing the right mitigation strategy for a given risk.

## Using the FMEA approach
<a name="using-the-fmea-approach"></a>

The scoring scales and templates in this guide are a starting point. They are not a fixed standard. Every organization has different risk tolerances, service architectures, and team structures. Follow these principles to adapt the methodology to your context:

1. **Customize for your environment**:** **Adjust severity, occurrence, and detection scores based on your specific business context and technical environment.

1. **Prioritize by RPN**:** **Focus first on failure modes with RPN greater than 200, then work down to lower-priority items.

1. **Validate assumptions**:** **Test the likelihood (occurrence) and detection difficulty in your environment through controlled experiments or historical analysis.

1. **Update regularly**:** **Review and update RPN scores based on implemented mitigations and real-world experience.

## RPN scoring guidelines
<a name="rpn-scoring-guidelines"></a>

Use the following scales when scoring each dimension of a failure mode. Each factor is rated from 1 to 10. Consistent scoring across teams depends on everyone using the same definitions, so calibrate these scales against real incidents and near-misses from your own environment during initial training.

### Severity (business impact)
<a name="severity--business-impact-.d6cc0e32-726f-5251-a5d3-902044b9e725"></a>
+ **1-2**:** **Minimal impact, no customer effect
+ **3-4**:** **Minor impact, limited customer effect
+ **5-6**:** **Moderate impact, noticeable customer effect
+ **7-8**:** **Major impact, significant customer effect
+ **9-10**:** **Critical impact, severe customer effect or business disruption

### Occurrence (likelihood)
<a name="occurrence--likelihood-.de0fdc92-354e-5485-a450-dc6604acdac2"></a>
+ **1-2**:** **Very rare (less than once per year)
+ **3-4**:** **Rare (once per year)
+ **5-6**:** **Occasional (monthly)
+ **7-8**:** **Frequent (weekly)
+ **9-10**:** **Very frequent (daily)

### Detection (difficulty to detect)
<a name="detection--difficulty-to-detect-.9471b4cd-e401-5ac7-9a51-b6666913e93a"></a>
+ **1-2**:** **Very easy to detect (automated alerts, immediate visibility)
+ **3-4**:** **Easy to detect (monitoring dashboards, quick identification)
+ **5-6**:** **Moderate detection (requires investigation, some delay)
+ **7-8**:** **Difficult to detect (manual investigation required, significant delay)
+ **9-10**:** **Very difficult to detect (often discovered by customers, major delay)

## Mitigation strategy selection
<a name="mitigation-strategy-selection"></a>

After you've identified and scored a failure mode, the next step is choosing how to address it. There are four broad approaches, and the right choice depends on which RPN factor offers the most room for improvement:
+ **Prevention**:** **Eliminate or reduce the likelihood of failure occurrence
+ **Detection**:** **Improve ability to detect failures quickly
+ **Scope of impact**:** **Reduce the impact when failures occur
+ **Recovery**:** **Improve speed and effectiveness of failure recovery

Focus mitigation efforts on strategies that provide the greatest RPN reduction for the available investment of time and resources.

## Team roles and responsibilities
<a name="team-roles-and-responsibilities"></a>

### Scrum Master
<a name="scrum-master.e183649a-4263-5b9f-91ce-63288e7e11f1"></a>
+ Facilitate FMEA integration in sprint planning
+ Track risk mitigation progress during sprint execution
+ Ensure process adherence and continuous improvement
+ Remove impediments blocking risk mitigation activities

### Product owner
<a name="product-owner.398a8e74-dce0-58ca-b9bc-6ae11e7a0de7"></a>
+ Provide business context for risk severity assessment
+ Prioritize risk mitigation against feature development
+ Communicate risk status to stakeholders
+ Make trade-off decisions when risks impact delivery

### Development team
<a name="development-team.534ee23c-4385-5b8a-b6f8-de488570b021"></a>
+ Identify technical risks during story analysis
+ Implement risk mitigations as part of story completion
+ Monitor risk indicators during development
+ Share risk knowledge and lessons learned

### FMEA champion
<a name="fmea-champion.b0ea2677-5039-53bb-aece-e621977f87b7"></a>
+ Lead risk assessment activities during sprint planning
+ Maintain risk documentation and tracking
+ Provide FMEA expertise and guidance to team
+ Coordinate with other teams on shared risks

## Success criteria for implementation
<a name="success-criteria-for-implementation"></a>

Use the following criteria to validate that your FMEA rollout is on track across all three phases.

The following are technical criteria:
+ All development teams actively using FMEA in sprint planning
+ Risk register maintained with current status for all teams
+ Automated risk tracking and reporting operational
+ Integration with existing tools completed successfully

The following are business criteria:
+ Baseline metrics established and tracking initiated
+ At least 80% of high-risk items (RPN > 400) have mitigations
+ Team satisfaction with process integration > 7/10
+ Executive stakeholder approval for organization-wide rollout

The following are process criteria:
+ Sprint planning duration increased by no more than 45 minutes
+ Risk assessment completion rate > 90% for applicable stories
+ Mitigation implementation rate > 85% within planned timeframes
+ Process documentation complete and accessible to all teams
