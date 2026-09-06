---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/canary-deployments.html
---

# Canary deployments
<a name="canary-deployments"></a>

 [Canary deployments](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/deployment-strategies.html#canary-deployments) are a type of blue/green deployment strategy that is more risk-averse. This strategy involves a phased approach in which traffic is shifted to a new version of the application in two increments. The first increment is a small percentage of the traffic, which is referred to as the canary group. This group is used to test the new version, and if it is successful, the traffic is shifted to the new version in the second increment.

 Canary deployments can be implemented in two steps or linearly. In the two-step approach, the new application code is deployed and exposed for trial. Upon acceptance, it is rolled out either to the rest of the environment or in a linear fashion. The linear approach involves incrementally increasing traffic to the new version of the application until all traffic flows to the new release.
