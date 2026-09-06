---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_evolve_ops_allocate_time_for_imp.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS11-BP09 Allocate time to make improvements
<a name="ops_evolve_ops_allocate_time_for_imp"></a>

 Dedicate time and resources within your processes to make continuous incremental improvements possible.

 On AWS, you can create temporary duplicates of environments, lowering the risk, effort, and cost of experimentation and testing. These duplicated environments can be used to test the conclusions from your analysis, experiment, and develop and test planned improvements.

 **Common anti-patterns:**
+  There is a known performance issue in your application server. It is added to the backlog behind every planned feature implementation. If the rate of planned features being added remains constant, the performance issue will never be addressed.
+  To support continual improvement you approve administrators and developers using all their extra time to select and implement improvements. No improvements are ever completed.

 **Benefits of establishing this best practice:** By dedicating time and resources within your processes you make continuous incremental improvements possible.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Allocate time to make improvements: Dedicate time and resources within your processes to make continuous incremental improvements possible. Implement changes to improve and evaluate the results to determine success. If the results do not satisfy the goals, and the improvement is still a priority, pursue alternative courses of action.
