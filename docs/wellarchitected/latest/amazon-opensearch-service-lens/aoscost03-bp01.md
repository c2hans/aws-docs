---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/aoscost03-bp01.html
---

# AOSCOST03-BP01 Evaluate forecasting for your workloads
<a name="aoscost03-bp01"></a>

 Reduce costs and improve predictability by setting up Reserved Instances for consistent workloads over one to three years, which can result in significant cost savings.

 **Level of risk exposed if this best practice is not established:** Low

 **Desired outcome**: The workload is consistent for the next one to three years, allowing for Reserved Instances to be set up and used effectively.

 **Benefits of establishing this best practice:**
+  **Significant cost savings:** Using Reserved Instances for a consistent workload over one to three years can result in significant cost savings, as you're committing to a fixed price for that period.
+  **Predictable expenses:** By reserving instances upfront, you can improve the predictability of your expenses for the next one to three years, which can help with budgeting and financial planning.

## Implementation guidance
<a name="implementation-guidance-53"></a>

 Maximize savings for your OpenSearch Service domain by using Reserved Instances (RIs) if your workload is consistent over the next one to three years. You can reserve instance using AWS CLI, AWS Management Console, or AWS SDKs. You can also use AWS Cost Explorer to examine the usage pattern and then decide to buy Reserved Instances (RIs).

### Implementation steps
<a name="implementation-steps-33"></a>
+  Log in to AWS Management Console.
+  Navigate to the Amazon OpenSearch Service console.
+  Choose **Reserved Instance leases**, located under **Managed clusters** in the left navigation pane.
+  Choose **Order Reserved Instances**.
+  Proceed with the options of your choice.

## Resources
<a name="resources-52"></a>
+  [Reserved Instances in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
