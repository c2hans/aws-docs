---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/custom-policy-engine.html
---

# Using a custom policy engine
<a name="custom-policy-engine"></a>

An alternative method for implementing a PDP is to create a custom policy engine. The goal of this policy engine is to decouple authorization logic from an application. The custom policy engine is responsible for making authorization decisions, similar to Verified Permissions or OPA, to achieve *policy decoupling*. The primary difference between this solution and using Verified Permissions or OPA is that the logic for writing and evaluating policies is custom-built for a custom policy engine. Any interactions with the engine must be exposed through an API or some other method to enable authorization decisions to reach an application. You can write a custom policy engine in any programming language or use other mechanisms for policy evaluation, such as the [Common Expression Language (CEL)](https://opensource.google/projects/cel).
