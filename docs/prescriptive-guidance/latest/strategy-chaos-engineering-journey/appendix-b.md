---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-chaos-engineering-journey/appendix-b.html
---

# Appendix B ‒ Quantitative and qualitative measures
<a name="appendix-b"></a>

This section outlines quantitative metrics to track operational improvements and qualitative measures to assess broader organizational results from chaos engineering practices.

## Quantitative measures
<a name="quantitative"></a>

The following quantitative measures provide a framework for tracking key metrics that can demonstrate the direct incident and operational improvements achieved through chaos engineering practices:
+ **Incidents**:
  + **Incident frequency** ‒ Track the number of incidents within an incident classification framework and classify them by their criticality (critical, major, minor) over a period of time. For more information about the incident classification framework, see [Appendix C](appendix-c.md).
  + **Downtime and degradation** ‒ Measure the total duration of downtime or service degradation for each incident classification.
  + **Incident response metrics** ‒ To understand incidents, measure Time to Detect, Time to Identification, Time to Mitigate, Time to Recover, Time to Escalation, and other related metrics for each incident classification.
  + **Customer-impacting incidents** ‒ Track the number of incidents that impact customers or the percentage of incidents that were contained before customer impact.
  + **Runbook changes** ‒ Track the number of runbook updates or revisions resulting from insights gained through chaos experiments. A runbook provides detailed instructions for performing a particular operation or procedure to recover from a particular type of incident.
+ **Costs**:
  + **Infrastructure costs** ‒ Collect data on infrastructure costs, including cloud computing resources and redundancy measures that are required by the actions taken to improve resilience.
  + **Customer impact** ‒ Measure impacts to the customer experience, churn rates, and revenue loss associated with system failures or downtime.
  + **Staff productivity** ‒ Track the time spent by engineering and operations teams on incident response, firefighting, writing postmortems, and other reactive tasks related to system failures.
+ **Continuous system improvements** ‒ Count the number of process improvements, architectural changes, or automated recovery mechanisms implemented as a direct result of insights from chaos experiments.
+ **Compliance** ‒ Track the costs and work to meet regulatory requirements or industry standards related to operational resilience.
+ **Adoption** ‒ Track the adoption rate of chaos practices across the organization.
+ **Customer satisfaction** ‒ Measure changes in customer satisfaction metrics to gauge how improved system reliability affects the business.

## Qualitative measures
<a name="qualitative"></a>

The following qualitative measures provide a framework for tracking the broader organizational results achieved through chaos engineering practices:
+ **Employee confidence and preparedness**:
  + Survey teams periodically to measure their confidence levels in handling real-world incidents and their perceived preparedness for on-call rotations.
  + Track the percentage of on-call engineers who have participated in chaos experiments as part of their training.
+ **Cultural shift**:
  + Assess the degree to which a resilience mindset has permeated the organization through surveys, feedback sessions, or audits.
  + Track the number of teams actively championing and advocating for chaos engineering practices.
+ **Cross-functional collaboration and knowledge sharing**:
  + Track the frequency and attendance of cross-team knowledge-sharing sessions or workshops related to chaos engineering learning.
  + Track the number of joint chaos engineering initiatives involving multiple teams or departments.
+ **Training effectiveness**:
  + Evaluate the effectiveness of chaos engineering training programs by conducting post-training surveys or assessments.
  + Track the number of engineers that participate in chaos engineering training programs and read postmortems.
+ **Talent attraction and retention**:
  + Evaluate whether the chaos engineering program helps attract and retain top engineering talent by reducing the time and effort spent on fixing outages.
+ **Brand reputation**:
  + Track any changes in brand perception or reputation related to the organization's demonstrated commitment to operational resilience.
+ **Competitive advantage**:
  + Track the competitive edge over industry peers in terms of system availability.
