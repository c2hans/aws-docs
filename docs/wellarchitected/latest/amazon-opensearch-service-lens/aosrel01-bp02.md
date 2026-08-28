---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/aosrel01-bp02.html
---

# AOSREL01-BP02 Regularly update your OpenSearch Service domain to the latest version
<a name="aosrel01-bp02"></a>

 Keep your OpenSearch Service domain current by regularly updating it to the latest available version, which provides improved performance, issue resolution, and access to new features.

 **Level of risk exposed if this best practice is not established:** Medium

 **Desired outcome:** Your OpenSearch Service domain is updated to the latest available version.

 **Benefits of establishing this best practice**: Keeping your OpenSearch Service domain up to date with the latest version can improve performance, resolve known issues with bug fixes, and unlock new features and capabilities.

## Implementation guidance
<a name="implementation-guidance-21"></a>

 OpenSearch releases new versions regularly. Always keep your domains updated to apply improvements to your domains.

### Implementation steps
<a name="implementation-steps-12"></a>
+  Open the Amazon OpenSearch Service console.
+  Select the domain name to open its configuration.
+  Choose **Actions**, then **Update**, and select one of the following options:
  +  **Apply update now**: Immediately schedules the action to happen in the current hour if there's capacity available. If capacity isn't available, we provide other available time slots to choose from.
  +  **Schedule it in off-peak window**: Only available if the off-peak window is enabled for the domain. Schedules the update to take place during the domain's configured off-peak window. There's no guarantee that the update will happen during the next immediate window. Depending on capacity, it might happen in subsequent days. For more information, see [Scheduling software updates during off-peak windows.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html)
  +  **Schedule for specific date and time**: Schedules the update to take place at a specific date and time. If the time that you specify is unavailable for capacity reasons, you can select a different time slot.
+  If you schedule the update for a later date (within or outside the domain's off-peak window), you can reschedule it at any time. For instructions, see [Rescheduling actions](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html#off-peak-reschedule).
+  Choose **Confirm**.

## Resources
<a name="resources-20"></a>
+  [Service software updates in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
