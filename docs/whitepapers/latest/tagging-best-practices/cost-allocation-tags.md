---
source_url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/cost-allocation-tags.html
---

# Cost allocation tags
<a name="cost-allocation-tags"></a>

 Cost allocation refers to the assignment or distribution of incurred costs to the users or beneficiaries of those costs following a defined process. In the context of this whitepaper, we divide cost allocation into two types: *showback* and *chargeback*.

 *Showback* tools and mechanisms help increase cost awareness. *Chargeback* helps with cost recovery and drives enablement of cost awareness. *Showback* is about presentation, calculation, and reporting of charges incurred by a specific entity, such as business unit, application, user, or cost center. For example: “the infrastructure engineering team was responsible for $X of AWS spend last month”. *Chargeback* is about an actual charging of incurred costs to those entities via an organization’s internal accounting processes, such as financial systems or journal vouchers. For example: “$X was deducted from the infrastructure engineering team's AWS budget.” In both cases, tagging resources appropriately can help allocate the cost to an entity, the only difference being whether or not someone is expected to make a payment.

 Your organization's financial governance might require transparent accounting of costs incurred at the application, business unit, cost center, and team level. Performing cost attribution supported by [Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) provides you the data necessary to accurately attribute the costs incurred by an entity from appropriately tagged resources.
+  **Accountability** — Ensure that cost is allocated to those who are responsible for resource usage. A single point of service or group can be accountable for spend reviews and reporting.
+  **Financial transparency** — Show a clear view into cash allocations towards IT by creating effective dashboards and meaningful cost analysis for leadership.
+  **Informed IT investments** — Track ROI based on project, application, or business line, and empower teams to make better business decisions, for example, allocate more funding to revenue generating applications.

 In summary, cost allocation tags can help to tell you:
+  Who owns the spend and is responsible for optimizing it?
+  What workload, application, or product is incurring the spend? Which environment or stage?
+  What spend areas are growing fastest?
+  How much spend can be deducted from an AWS budget based on past trends?
+  What was the impact of cost optimization efforts within particular workloads, applications, or products?

 Activating resource tags for cost allocation helps with the definition of measurement practices within the organization that can be used to provide the visibility of AWS usage that increases transparency into accountability for spend. It also focuses on creating an appropriate level of granularity with respect to cost and usage visibility and inﬂuencing cloud consumption behaviors through cost allocation reporting and KPI tracking.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
