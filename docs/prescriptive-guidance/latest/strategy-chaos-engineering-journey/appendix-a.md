---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-chaos-engineering-journey/appendix-a.html
---

# Appendix A ‒ Goal types for chaos engineering
<a name="appendix-a"></a>

The following descriptions of goal types include real-world examples of how Amazon and other organizations have designed goals for chaos engineering.

## Resilient architecture goals
<a name="resilient-architecture"></a>

One of the initial drivers for adopting chaos engineering is to identify and reduce single points of failure (SPOF) across systems and infrastructure. Goals are set to validate the resilience of critical systems and architectures, particularly for new services or applications.

Resilient-architecture goals involve running chaos experiments that simulate failures in service dependencies. The experiments confirm whether timeouts, retries, caching behavior, and circuit-breaker configurations are functioning correctly. These experiments help uncover issues for remediation, preventing customer-impacting incidents. For an example, see [Building resilient services at Prime Video with chaos engineering](https://aws.amazon.com/blogs/opensource/building-resilient-services-at-prime-video-with-chaos-engineering/).

## Service-recovery goals
<a name="service-recovery"></a>

Service-recovery goals focus on improving the ability to recover from operational disruptions or infrastructure failures. For example, your organization might aim to achieve a specific recovery time objective (RTO) for your core services in the event of an outage. Teams can design chaos experiments to validate and optimize evacuation strategies, failover mechanisms, and automated recovery processes. The optimizations ultimately reduce the time required for service restoration. For an example, see [AWS Lambda: Resilience under-the-hood](https://aws.amazon.com/blogs/compute/aws-lambda-resilience-under-the-hood/).

## User-experience goals
<a name="ux"></a>

Maintaining a consistent and reliable user experience is paramount, especially during high-traffic periods or critical events. In such cases, set goals centered around meeting specific service-level objectives (SLOs). This customer-centric approach ensures that resilience efforts are directly aligned with delivering a superior user experience, even in the face of failures or degraded conditions. For an example, see [Engineering Resilience: Lessons from Amazon Search's Chaos Engineering Journey](https://community.aws/posts/amazon-search-chaos-engineering-journey).

## Metric-driven goals
<a name="metrics"></a>

You can establish goals based on quantitative metrics, such as a resilience score that is calculated by awarding points to services that adopt proven resilience best practices. You can then use particular chaos experiments to determine the resilience score. This score can serve as a measure for teams to track their progress in mitigating known availability risks and implementing recommended resilience measures. However, it's crucial to interpret such scores cautiously and avoid overemphasizing a single metric at the expense of broader resilience objectives. For an example, see [Understanding resiliency scores](https://docs.aws.amazon.com/resilience-hub/latest/userguide/resil-score.html).

## Regulatory-compliance goals
<a name="compliance"></a>

The financial services industry has emerged as a front runner in embracing chaos engineering, driven primarily by stringent regulatory requirements that mandate robust resilience capabilities. Regulations will demand that financial institutions proactively identify, test, and remediate vulnerabilities in their critical systems and processes. These regulations include the following:
+ The Interagency Paper on Sound Practices to Strengthen Operational Resilience issued by US federal agencies
+ The European Central Bank's guidelines on operational resilience
+ The European Commission's proposal for a Digital Operational Resilience Act (DORA)

If your organization is a financial institution, comply with these regulations by setting explicit goals for demonstrating operational resilience through comprehensive testing and validation strategies. For an example, see [London Stock Exchange Group uses chaos engineering on AWS to improve resilience](https://aws.amazon.com/blogs/architecture/london-stock-exchange-group-uses-chaos-engineering-on-aws-to-improve-resilience/).
