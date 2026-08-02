---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/observability.html
---

# Failure mode observability
<a name="observability"></a>

To mitigate a failure mode, you first have to detect that it is currently impacting, or is about to impact, your workload. A mitigation is effective only if there is a signal that an action has to be taken. This means that part of creating any mitigation includes, at the very least, verifying that you have or are building the observability that's necessary to detect the impact of the failure.

You should consider the observable symptoms of the failure mode in two dimensions:
+ What are the *leading indicators* that inform you that the system is approaching a condition where an impact might be seen soon?
+ What are the *lagging indicators* that can show the failure mode's impact as quickly as possible after it has occurred?

For example, an excessive load failure that's applied to a database element could have a connection count as a leading indicator. You can see the steady increase in connection counts as a leading indicator that the database might soon exceed the connection limit, so you can take action, such as terminating the least recently used connections, to reduce the connection count. The lagging indicator indicates when the database connection limit has been exceeded and database connection errors elevate. In addition to collecting application and infrastructure metrics, consider gathering [key performance indicators (KPI)](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.html) to detect when failures impact your customer experience.

When possible, we recommend that you include both types of indicators in your observability strategy. In some cases, you might not be able to create leading indicators, but you should always plan to have a lagging indicator for each failure that you want to mitigate. To choose the right mitigation, you also should consider whether a leading or a lagging indicator detected the failure. For example, consider a sudden spike in traffic to your website. You would likely see only a lagging indicator. In this case, automatic scaling alone might not be the best mitigation because it takes time to deploy new resources, whereas throttling could prevent the overload almost immediately and give your application time to scale or reduce the load. Conversely, for a gradual increase in traffic, you would see a leading indicator. In this case, throttling wouldn't be appropriate because you have time to respond by automatically scaling your system.
