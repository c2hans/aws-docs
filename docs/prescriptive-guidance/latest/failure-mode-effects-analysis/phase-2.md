---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/failure-mode-effects-analysis/phase-2.html
---

# Phase 2: Process integration (weeks 3-4)
<a name="phase-2"></a>

With the foundation in place, weeks 3-4 embed FMEA into the sprint cycle itself. This means adding a dedicated risk analysis block to sprint planning, updating your definition of done to include mitigation requirements, and making risk status a regular part of standups. The goal is to make risk assessment a natural step in how the team plans and delivers work — not a separate activity bolted on afterward.

## Pre-planning preparation
<a name="phase-2-prep"></a>

Complete the following checklist one day before sprint planning:
+ Review existing risk backlog
  + Identify open risk items from previous sprints
  + Update status of ongoing mitigation efforts
  + Prioritize unresolved high-RPN items (>400)
  + Prepare risk context for new sprint planning
+ Analyze upcoming user stories
  + Review sprint candidate stories for risk potential
  + Identify stories involving new AWS services or configurations
  + Flag stories with external dependencies or integrations
  + Prepare initial risk assessment materials
+ Prepare FMEA materials
  + Ensure FMEA templates are accessible to all team members
  + Update AWS service failure mode reference guide
  + Prepare RPN calculation tools and examples
  + Review organization-specific risk criteria

## Sprint planning meeting structure
<a name="phase-2-meeting-structure"></a>

After your team completes its regular sprint planning activities (goal setting, story selection, estimation, and task breakdown), add a 45-minute FMEA block led by the Scrum Master or FMEA champion. The block has three parts: risk identification, risk analysis, and mitigation planning.

### Risk identification (15 minutes)
<a name="risk-identification--15-minutes-.3e1661f2-849e-5308-a0de-2a6c42011113"></a>

Screen each selected story for risk potential. Flag any story that involves:
+ A new AWS service implementation
+ An external system integration
+ Security-sensitive functionality
+ Performance-critical features
+ Data migration or schema changes

For each flagged story, identify potential failure modes. To surface risks the team might overlook, work through these questions:
+ What could go wrong with this story implementation?
+ Which AWS services are involved and what are their common failure modes?
+ What external dependencies could fail?
+ How would failure impact our customers and business?

### Risk analysis (20 minutes)
<a name="risk-analysis--20-minutes-.8847be6d-505e-5230-b791-5365d44a9753"></a>

Score each identified failure mode across severity, occurrence, and detection (1-10 each), then calculate the RPN. Focus detailed discussion on items with RPN greater than 200. Document the rationale behind each score so future teams can calibrate consistently. Aim to identify the top 3-5 risks for the sprint.

Use the following template to capture each assessment:

```
Story: [Story title/ID]
Failure mode: [Description of what could go wrong]
Severity (1-10): [Score] - [Justification]
Occurrence (1-10): [Score] - [Justification]
Detection (1-10): [Score] - [Justification]
RPN: [S × O × D] = [Total score]
Action required: [Based on RPN thresholds]
```

### Mitigation planning (10 minutes)
<a name="mitigation-planning--10-minutes-.8aa6c3a8-a350-52a8-839e-ada92222ea75"></a>

For each high-RPN item, choose a mitigation approach (prevention, detection, mitigation, or recovery), estimate the effort, and assign an owner. Then update the sprint backlog: add mitigation tasks, revise story acceptance criteria to reflect risk considerations, and allocate story points for the mitigation work.

Use the following template to capture each plan:

```
Risk: [Risk description]
RPN: [Score]
Mitigation strategy: [Prevention, detection, or recovery approach]
Implementation tasks:
- Task 1 [Owner] [Effort estimate]
- Task 2 [Owner] [Effort estimate]
- Task 3 [Owner] [Effort estimate]
Target completion: [Sprint timeline]
Success criteria: [How to measure mitigation effectiveness]
```

## Definition of done updates
<a name="phase-2-dod"></a>

For all stories with identified risks (RPN > 100), add the following to your definition of done:
+ Risk assessment completed
  + FMEA analysis documented in project management tool
  + RPN calculated and justified
  + Risk mitigation strategy defined
+ Mitigation implementation (RPN > 100)
  + Identified mitigation measures implemented
  + Mitigation effectiveness validated through testing
  + Monitoring and alerting configured for risk scenarios
+ Documentation updates (RPN > 200)
  + Runbook updated with failure scenarios and response procedures
  + Architecture documentation updated with risk considerations
  + Team knowledge base updated with lessons learned
+ Risk register maintenance
  + Risk status updated in tracking system
  + Mitigation completion documented
  + Residual risk assessment completed

## Daily standup integration
<a name="phase-2-standups"></a>

Add the following risk-focused questions to your daily standup:
+ **Risk status update**:** **"Any updates on risk mitigation tasks?"
+ **New risk identification**:** **"Did you discover any new risks while working?"
+ **Mitigation blockers**:** **"Are there any blockers preventing risk mitigation completion?"

Use this format for risk status updates:

```
Risk mitigation update:
- Risk: [Brief description]
- Status: [In progress/Completed/Blocked]
- Progress: [What was accomplished]
- Next steps: [Planned activities]
- Blockers: [Any impediments]
- Help needed: [Support required from team]
```

## Sprint review enhancement
<a name="phase-2-sprint-review"></a>

Add 15 minutes to your sprint review for risk mitigation validation:
+ **Mitigation demonstration**:** **Demo implemented risk mitigations, show monitoring and alerting configurations, and validate mitigation effectiveness through testing.
+ **Risk status summary**:** **Review all risks identified during the sprint, confirm mitigation completion status, and document any residual or newly discovered risks.
+ **Stakeholder risk communication**:** **Communicate risk management activities to stakeholders, highlight proactive risk prevention measures, and discuss any risks requiring stakeholder attention.

## Sprint retrospective enhancement
<a name="phase-2-sprint-retros"></a>

Add the following questions to your retrospective to continuously improve the FMEA process:
+ **Risk assessment effectiveness**:** **How accurate were our risk predictions? Did we miss any significant risks that materialized? Were our RPN calculations realistic?
+ **Process integration**:** **How well did FMEA integrate with our existing processes? What slowed down our risk assessment activities? How can we make risk analysis more efficient?
+ **Mitigation success**:** **Were our risk mitigations effective? What mitigation strategies worked best? How can we improve our mitigation planning?

Use this template to capture improvement actions:

```
FMEA process improvement:
Issue: [What didn't work well]
Root cause: [Why it happened]
Improvement action: [What we'll do differently]
Owner: [Who will implement]
Timeline: [When it will be done]
Success measure: [How we'll know it worked]
```

## Continuous monitoring
<a name="phase-2-continuous-monitoring"></a>
+ Establish regular risk review cycles (bi-weekly or monthly)
+ Implement automated risk tracking and reporting
+ Create feedback mechanisms for risk assessment accuracy
+ Set up post-incident FMEA review process

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
