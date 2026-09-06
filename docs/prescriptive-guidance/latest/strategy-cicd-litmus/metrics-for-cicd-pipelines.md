---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cicd-litmus/metrics-for-cicd-pipelines.html
---

# Metrics for CI/CD pipelines
<a name="metrics-for-cicd-pipelines"></a>

According to the [AWS Deployment Pipeline Reference Architecture](https://pipelines.devops.aws.dev/application-pipeline/), you should, at a minimum, track the following four metrics for CI/CD pipelines:
+ **Lead time** – The average amount of time it takes for a single commit to get all the way into production. We recommend targeting a lead time between 1 hour and 1 day, as appropriate for your use case.
+ **Deployment frequency** – The number of production deployments within a given period of time. We recommend targeting deployment frequencies between multiple times each day to twice each week, as appropriate for your use case.
+ **Mean time between failure (MTBF)** – The average amount of time between the start of a successful pipeline and the start of a failed pipeline. We recommending targeting an MTBF that is as high as possible. For more information, see [Increasing MTBF](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/increasing-mtbf.html).
+ **Mean time to recovery (MTTR)** – The average amount of time between the start of a failed pipeline and the start of the next successful pipeline. We recommending targeting an MTTR that is as low as possible. For more information, see [Reducing MTTR](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/reducing-mttr.html).

These metrics help teams track their progress toward becoming fully CI/CD. Teams should have open discussions with the organization's stakeholders regarding what the optimal goals should be. Situations and needs vary greatly from organization to organization, and even from team to team.

It's very important to remember that rapid, drastic change usually increases the risk of problems arising. Set goals to aim for small, incremental improvements. A common optimal lead time for fully CI/CD pipelines is less than 3 hours. A team that starts with a lead time of 5.2 days should target a reduction of one day every few weeks. After this team reaches a lead time of one day or less, they can stay there for several months and move to a more aggressive lead time only if the team and organization stakeholders deem it necessary.
