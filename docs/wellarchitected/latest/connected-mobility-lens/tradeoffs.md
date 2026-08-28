---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/tradeoffs.html
---

# Tradeoffs
<a name="tradeoffs"></a>

| CMPERF\_14: What criteria have you identified where tradeoffs can be made?  |
| --- |
|   |

**[CMPERF\_BP14.1] Develop criteria where trade-offs can be made based on the type of functionality.**

 For example, infotainment functionality brings higher customer satisfaction where certain tradeoffs are acceptable (for example, retry actions are configurable to avoid draining battery). But when it comes to vehicle safety critical OTA updates are not inhibited by tradeoffs. Additional criteria can be applied:
+  Ensure data collection concerning predictive maintenance are not being hindered
+  Develop a revision process on actionable insights received from monitoring

**[CMPERF\_BP14.2] Architecture design and trade-offs**

The following options have benefits which bring scalability, higher performance, faster response but the tradeoff is cost. With volume of vehicles that connect to a connected vehicle platform increases the cost to maintain them is critical in the long run. In addition, the amount of data that gets offloaded from vehicle continues to grow.
+  Self-managed option
+  AWS Managed Service option
+  Serverless option

 It is critical to identify and categorize the functions, vehicle signals and states, software updates that are needed to support the connected vehicle platform by processing and storing them.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
