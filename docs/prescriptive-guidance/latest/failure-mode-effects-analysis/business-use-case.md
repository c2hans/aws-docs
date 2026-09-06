---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/failure-mode-effects-analysis/business-use-case.html
---

# Business use case for FMEA
<a name="business-use-case"></a>

Organizations building applications on AWS face potential failure modes that can disrupt business operations, degrade customer experience, and reduce system reliability. Without a structured approach, teams tend to manage risk reactively — responding to production incidents rather than preventing them. Risk assessment activities often happen in isolation from development workflows, and different teams apply inconsistent criteria when evaluating risk.

This guidance addresses these challenges by adapting Failure Mode and Effects Analysis (FMEA) for software applications running on AWS. The methodology uses a quantitative *risk priority number* to identify, assess, and prioritize potential failure modes, and integrates directly into agile sprint ceremonies.

## How it works
<a name="how-it-works"></a>

The core of this methodology is the risk priority number (RPN), a quantitative score that helps teams consistently evaluate and compare risks. Each potential failure mode is scored across three dimensions:
+ **Severity (S)**:** **How much damage would this failure cause? A score of 1 means minimal business impact with no customer effect. A score of 10 means a critical outage or data loss that directly affects customers.
+ **Occurrence (O)**:** **How likely is this failure to happen? Low scores represent rare events (less than once per year), while high scores represent failures that occur daily or weekly.
+ **Detection (D)**:** **How hard is it to catch this failure before customers are affected? Automated alerts and dashboards score low (easy to detect), while failures that surface only through customer reports score high.

The three scores are multiplied together to produce the RPN:

**RPN = severity × occurrence × detection**

Because each factor ranges from 1 to 10, the RPN ranges from 1 to 1,000. A high RPN means the failure is severe, likely, and hard to detect, which is exactly the combination that warrants immediate attention. Teams use the following thresholds to decide how urgently to act:
+ **Critical (800-1000)**:** **Immediate action required (current sprint)
+ **High (400-799)**:** **Priority action (1-2 sprints)
+ **Medium (200-399)**:** **Planned action (2-4 sprints)
+ **Low (100-199)**:** **Monitor and track (backlog)
+ **Minimal (1-99)**:** **Accept risk with documentation

After mitigations are implemented, teams rescore the failure mode. The goal is to drive down the RPN by reducing the severity, occurrence, or detection difficulty (or, ideally, all three).

## Key components of the FMEA approach
<a name="key-components"></a>
+ **Risk assessment framework**: Traditional 1-10 scale for severity, occurrence, and detection
+ **Sprint integration process**: Integration with agile development workflows
+ **Analysis specific to AWS**: Pre-analyzed failure modes for common AWS services
+ **Action thresholds**: Clear criteria for when and how to address identified risks
+ **Continuous improvement**: Feedback loops for refining risk assessments
