---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/smartsheet-limitations.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Known limitations for the Smartsheet connector
<a name="smartsheet-limitations"></a>

The Smartsheet connector has the following known limitations:
+  If you remove users’ access to a Smartsheet data source but not to Amazon Q Business, they will be able to receive responses from the data source when they query Amazon Q Business.
+ The Smartsheet connector will provide responses from the most applicable single sheet. That is, it will search across all sheets and find the sheet with the most relevant answer and provide that instead of aggregating data across multiple sheets. For example, it can't answer questions like: "Show me tasks that are past due across all my sheets."
+ For hierarchical sheets, Amazon Q Business accuracy can drop when queries are directly related to the hierarchical structure.

  For example, if a sheet has hierarchical structure about high-level tasks and its subtasks, and a user asks "What's the amount of time needed to finish all tasks?" then Amazon Q Business might add up all times assigned to both high-level tasks and the sub-tasks. This calculation is wrong as the amount of time to finish the high-level task is just a sum up of the sub-tasks.

  However, if the user asks a query such as "How many tasks are assigned to Mary Major?", they would get an accurate response.
+ For sheets with similar names—(for example, “Blockchain Integration - Project Plan” and “Blockchain Integration - Impact Tracker”)—if a query mentions just “Blockchain Integration” then you might not get an accurate response. To get accurate responses, we recommend:
  + providing clearer titles/descriptions of the sheets, or
  +  providing more detailed questions to reduce ambiguity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
