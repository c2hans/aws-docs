---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cost-modeling-data-lakes/visualization-api-access.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Visualization and API access
<a name="visualization-api-access"></a>

 Visualization is used to graphically present the enormous amount of data in data lake in a human consumable format. API access refers to allowing developers to integrate your data in their apps to make it meaningful for consumers. The rate at which data is refreshed or request affects the number of queries being fired (and cost) in the analytics stage.

## Cost factors
<a name="visualizationo-cost-factors"></a>

 The primary cost of this stage includes:
+  **Per user license cost** - Most of SaaS visualization tools charge per user license cost.
+  **Processing unit cost** - The cost required to host the visualization software is applicable only for hosted visualization tools.
+  **In-memory processing cost** - This is the cost of the visualization need to load huge amount of data in memory for quick performance. The amount of data required to be loaded also has a direct impact on cost, for example, Super-fast, Parallel, In-memory Calculation Engine (SPICE) in Quick.
+  **Number of requests through an API** - As developers integrate with their apps the number of requests made for data will increase.

## Cost optimization factors
<a name="visualization-cost-optimization-factors"></a>

 We recommend that you consider the following actions to reduce cost:
+  Choose the right tool for the job
+  Choose serverless services
+  Use automatic scaling
+  Use Reserved Instances
+  Right size your instances
