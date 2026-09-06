---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_mitigate_interaction_failure_emergency_levers.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL05-BP07 Implement emergency levers
<a name="rel_mitigate_interaction_failure_emergency_levers"></a>

 Emergency levers are rapid processes that can mitigate availability impact on your workload.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Implement emergency levers. These are rapid processes that may mitigate availability impact on your workload. They can be operated in the absence of a root cause. An ideal emergency lever reduces the cognitive burden on the resolvers to zero by providing fully deterministic activation and deactivation criteria. Levers are often manual, but they can also be automated
  +  Example levers include
    +  Block all robot traffic
    +  Serve static pages instead of dynamic ones
    +  Reduce frequency of calls to a dependency
    +  Throttle calls from dependencies
  +  Tips for implementing and using emergency levers
    +  When levers are activated, do LESS, not more
    +  Keep it simple, avoid bimodal behavior
    +  Test your levers periodically
  +  These are examples of actions that are NOT emergency levers
    +  Add capacity
    +  Call up service owners of clients that depend on your service and ask them to reduce calls
    +  Making a change to code and releasing it
