---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/best-practices-3.html
---

# Best practices
<a name="best-practices-3"></a>

The performance efficiency pillar includes the ability to use computing resources efficiently to meet system requirements, and to maintain that efficiency as demand changes and technologies evolve. In the context of containers, there are two different aspects of performance: the build-time performance for your container image, and the runtime performance. In this section, we’ll focus on build-time performance in order to reduce the time that is necessary to create a container image from a Dockerfile. Reducing the build-time of a container image has a huge impact on developer productivity, and it reduces the amount of time that is necessary to roll out new versions of your application to production. Optimizing the performance at runtime has a direct impact on customer experience, latency, and costs, but is outside the scope of this lens. The following guidance is in addition to the best practice guidance found in the [Performance Efficiency Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).

**Topics**
+ [Selection](selection.md)
+ [Review](review.md)
+ [Monitoring](monitoring.md)
+ [Tradeoffs](tradeoffs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
