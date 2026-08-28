---
source_url: https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/management-and-monitoring.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Management and monitoring
<a name="management-and-monitoring"></a>

 The approach you adopt for multitenant storage can have a significant impact on the management and monitoring profile of your SaaS solution. In fact, the complexity and approach you take to aggregate and analyze system health can vary significantly for each storage model and AWS technology.

## Aggregating storage trends
<a name="aggregating-storage-trends"></a>

 To build an effective operational view of SaaS storage, you need metrics and dashboards that provide you with an aggregated view of tenant activity. You have to be able to proactively identify storage trends that could be influencing the experience spanning all of your tenants. The mechanisms you need to create this aggregated view look very different in the silo and pool models. With siloed storage, you must put tooling in place to collect the data from each isolated database and surface that information in an aggregated model. In contrast, the pool model, by its nature, already has an aggregated view of tenant activity.

## Tenant-centric views of activity
<a name="tenant-centric-views-of-activity"></a>

 Your management and monitoring storage solution should provide a way to create tenant-centric views of your storage activity. If a particular tenant is experiencing a storage issue, you’ll want to be able to drill into the storage metrics and profile data to identify what could be impacting that individual tenant. Here, the silo model aligns more naturally with constructing a tenant-centric view of storage activity. A pooled storage strategy will require some tenant filtering mechanism to extract storage activity for a given tenant.

## Policies and alarms
<a name="policies-and-alarms"></a>

 Each AWS storage service has its own mechanisms for evaluating and tuning your application’s storage performance. Because storage can often represent a key bottleneck of your system, you should introduce monitoring policies and alarms that will allow you to surface and respond to changes in the health of your application’s storage.

 The partitioning model you choose will also impact the complexity and manageability of your storage monitoring strategy. The more siloed your solution, the more moving parts to manage and maintain on a tenant-by-tenant basis. In contrast, the shared nature of a pooled storage strategy makes it simpler to have a more centralized, cross-tenant collection of policies and alarms.

 The overall goal with these storage policies is to put in place a set of proactive rules that can help you anticipate and react to health events. As you select a multitenant storage model, consider how each approach might influence how you implement your system’s storage policies and alarms.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
