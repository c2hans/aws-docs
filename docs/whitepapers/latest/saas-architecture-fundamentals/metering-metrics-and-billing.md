---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/metering-metrics-and-billing.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Metering, metrics, and billing
<a name="metering-metrics-and-billing"></a>

 Discussions of SaaS also tend to include the notion of *metering*, *metrics*, and *billing*. These concepts often get folded together into one concept. However, it’s important to distinguish the different roles that metering, metrics, and billing play in a SaaS environment.

 The challenge of these concepts is that they often have overlapping uses of the same word. For example, we can talk about metering that is used to generate your bill. At the same time, we can also talk about metering that is used to track internal consumption of resources that is not connected to billing. We also talk about metrics and SaaS in many contexts that can get mixed into this discussion.

 To help sort this out, let’s associate some specific concepts with each of these terms (knowing there are not absolutes here).
+  **Metering** – This concept, while it has many definitions, fits best in the SaaS billing domain. The idea is that you meter tenant activity or consumption of resources to collect the data needed to generate a bill.
+  **Metrics** – Metrics represent all the data that you capture to analyze trends across your business, operations, and technology domains. This data is used to across many contexts and roles within the SaaS team.

 This distinction isn’t critical, but helps simplify how we think about the role of metering and metrics in a SaaS environment.

 Now, if we connect these two concepts to examples, you can think of instrumenting your application with specific metering events used to surface the data needed to generate a bill. This could be number of requests, number of active users, or it could map to some aggregate of consumption (requests, CPU, memory) that correlates to some unit that makes sense to your customers.

 In your SaaS environment, you’ll publish these billing events from your application and they will be ingested and applied by the billing construct employed by your SaaS system. This could be a third-party billing system or something custom.

 In contrast, the mindset behind metrics is to capture those actions, activities, consumption patterns, and so on that are essential to evaluating the health and operational footprint imposed on your system by different tenants. The metrics you publish and aggregate here are dictated more by the need of different personas (operational teams, product owners, architects, and so on). Here, this metric data is published and aggregated into some analytics tooling that allows these different users to build the views of system activity that analyze the aspects of the system that best align with their persona. A product owner may want to understand how different tenants are consuming features. An architect might need views that help them understand how tenants are consuming infrastructure resources, and so on.
