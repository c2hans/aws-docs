---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agent-ops-maturity-roadmap-for-enterprise-ai/best-practices.html
---

# Best practices
<a name="best-practices"></a>
+ **Start small, expand deliberately. **Begin with the single-account model for exploration. Move to multi-account once you need environment separation. Add staging, production, and data lake accounts only when workload maturity justifies the operational overhead. Each additional account adds management surface.
+ **Use infrastructure as code for everything. **Define all account configurations, network topologies, and IAM policies using AWS CloudFormation, AWS CDK, or Terraform. Manual deployments introduce configuration drift. In a multi-account architecture, drift is difficult to detect and expensive to remediate.
+ **Establish tagging conventions before deploying workloads. **Retrofitting cost allocation tags across a multi-account structure after workloads are running is substantially more expensive than enforcing them from day one.
+ **Design for model diversity. **The architecture should accommodate multiple LLM providers through the generative AI gateway accounts. Centralizing model access at the gateway layer across environments avoids vendor lock-in at the platform layer and simplifies the compliance review process when adding new model providers. Mirror provider configurations across gateway-dev, gateway-staging, and gateway-prod to ensure that model integration testing in lower environments remains representative of production behavior.
+ **Design for agent autonomy levels. **Not all agents require the same governance posture. Low-risk information retrieval agents may operate with minimal oversight. Agents performing financial transactions, sending external communications, or modifying infrastructure require human-in-the-loop approval gates. Design tiered controls rather than applying uniform restrictions.
+ **Test cross-account connectivity before deploying workloads. **Validate IAM trust relationships, PrivateLink endpoints, and CloudWatch cross-account configurations as the first operational test of each new account. Debugging connectivity issues after agents are running and producing errors is significantly harder than catching them during the account onboarding sequence.
