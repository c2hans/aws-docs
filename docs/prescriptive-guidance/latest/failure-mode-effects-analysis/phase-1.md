---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/failure-mode-effects-analysis/phase-1.html
---

# Phase 1: Foundation setup (weeks 1-2)
<a name="phase-1"></a>

The first two weeks focus on building the knowledge, tooling, and baseline data your teams need before FMEA becomes part of the sprint cycle. You'll designate champions, train the team on RPN scoring, wire up your project management tools for risk tracking, and run a pilot analysis on one or two applications to calibrate your scoring criteria against real-world conditions.

## Week 1: Team preparation
<a name="week-1"></a>
+ Identify FMEA champions
  + Select 1-2 team members per development team
  + Ensure champions have risk management interest/experience
  + Provide champion-specific training materials
+ Conduct initial training
  + Schedule a 2-hour FMEA methodology workshop
  + Cover RPN calculation and scoring criteria
  + Practice with sample AWS failure scenarios
  + Distribute reference materials and templates
+ Establish risk assessment criteria
  + Customize severity scale for business context
  + Define occurrence probability ranges
  + Set detection difficulty criteria
  + Document organization-specific examples

## Week 2: Tool setup and baseline
<a name="week-2"></a>
+ Configure project management tools
  + Configure FMEA templates in existing project management tools (such as Jira)
  + Create custom fields for RPN tracking
  + Set up risk dashboard views
  + Configure automated reporting
+ Establish baseline metrics
  + Document current incident frequency (last 6 months)
  + Categorize incidents by AWS service and impact
  + Calculate baseline MTTR and customer impact
  + Create measurement framework
+ Pilot application selection
  + Choose 1–2 applications for initial analysis
  + Ensure applications use common AWS services
  + Select applications with engaged development teams
  + Document application architecture and dependencies

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
