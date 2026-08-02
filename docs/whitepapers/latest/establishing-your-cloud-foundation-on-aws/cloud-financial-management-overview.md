---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/cloud-financial-management-overview.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Overview
<a name="cloud-financial-management-overview"></a>

Having visibility and understanding of the spend in your cloud environment is critical to your business. Setting up the right measures to monitor your resources will allow you to create reports, dashboards, and anomaly detection of the cloud spend of your budget and plan for cost optimization to avoid or reduce unnecessary spend.

Implementing these mechanisms and tools will help you support business decisions and establish cloud financial operations in your environment to socialize cost awareness across different business units, application teams, and other stakeholders without affecting the innovation of your teams.

In order to implement a cloud financial management function, you need to implement a tagging strategy for your environment. Refer to the [tagging capability](tagging-capability.md), to find recommended tags for your environment. Some of these tags within the tagging capability can be used to track spend in your cloud environment, and allow you to create dashboards, reporting for individual business units, workloads, and types of environments

You need to incorporate the tags and the values for these tags defined within your cloud financial management capability into the tagging dictionary defined as part of your [tagging capability](https://aws.amazon.com/solutions/guidance/tagging-on-aws/). We recommend that you make these tags widely available across your different stakeholders and teams in order to enable them to track spend back. This will allow your cloud team or your FinOps team to analyze the usage and work towards building a cost allocation strategy.
