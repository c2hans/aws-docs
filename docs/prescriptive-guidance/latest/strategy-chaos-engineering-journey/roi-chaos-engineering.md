---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-chaos-engineering-journey/roi-chaos-engineering.html
---

# Quantifying the ROI of chaos engineering
<a name="roi-chaos-engineering"></a>

Currently, very few published resources provide comprehensive methodologies or real-world data for quantifying the long-term return on investment (ROI) for chaos engineering.

In the paper [The Business Case for Chaos Engineering](https://ieeexplore.ieee.org/document/8383672), Netflix offers a valuable equation for calculating the ROI for chaos engineering. This equation provides a starting point for organizations embarking on their chaos engineering journey.

The equation requires that you accurately estimate the costs of the following:
+ Preventable and nonpreventable outages
+ Chaos engineering program implementation costs
+ Chaos-induced harm costs

Chaos-induced harm refers to the negative impact or disruption caused by deliberately injecting faults or turbulent conditions into a system as part of chaos engineering experiments. The equation requires estimating the costs of preventable and non-preventable outages, chaos engineering program implementation costs, and chaos-induced harm costs.

Determining with certainty which issues could have been prevented by a chaos engineering program is a difficult task. It requires a hypothetical analysis that involves looking at the root causes of issues and speculating how chaos engineering experiments might have helped to identify them. This analysis is challenging because modern systems are highly complex, with numerous interdependencies and interactions between various components, services, and third-party libraries. Moreover, faults in systems are often nondeterministic, and the conditions that cause faults can be difficult to fully understand in hindsight.

Although the approach suggested by Netflix has some limitations, it serves as a good foundation for organizations beginning to explore chaos engineering. The equation can guide you in estimating costs and potential benefits, which helps you to make decisions about implementing such a program. However, as organizations progress further in their chaos engineering journey, it's important to expand the ROI assessment to incorporate a more holistic perspective.

This holistic approach will not only capture the direct benefits of reduced outages and engineering costs but also highlight the long-term, transformative effects on the organization's overall resilience. It captures the compounding benefits and broader organizational effects of chaos engineering to give a more accurate representation of the true value and impact of chaos engineering.

## A holistic approach to ROI quantification
<a name="holistic-approach-roi"></a>

A holistic ROI assessment must account not only for** ***quantitative measures* but also *qualitative factors*. The holistic approach requires real-world data from organizations that practice chaos engineering at scale over longer periods of time. You can use data starting from the grassroots projects and goals through any equation-approach ROI data that you gathered.

Quantitative measures focus on quantities or frequencies. The measurements are objective, and they can be analyzed statistically. Examples include surveys, experiments, and data analysis. Quantitative measures can include the following:
+ Incident metrics
+ Costs
+ Improvements
+ Compliance
+ Adoption rates
+ Customer satisfaction

Tracking quantitative measures can demonstrate the direct operational benefits of chaos engineering.

Qualitative measures are descriptive, and they focus on understanding experiences and opinions. They are often subjective, and they can't be easily measured numerically. For chaos engineering, qualitative measures capture the broader organizational impacts. Qualitative measures can include the following:
+ Employee confidence
+ Cultural shift
+ Collaboration
+ Training effectiveness
+ Talent retention
+ Brand reputation
+ Competitive advantage

By considering both quantitative financial impacts and qualitative organizational benefits, you can make more-informed decisions about continued chaos engineering investment while fostering a resilience culture.

For more information about these measures and their associated incident classification framework, see [Appendix B](appendix-b.md) and [Appendix C](appendix-c.md).
