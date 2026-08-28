---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/deleting-prefetch-schedules.html
---

# Deleting prefetch schedules
<a name="deleting-prefetch-schedules"></a>

The following procedure explains how to delete a prefetch schedule by using the MediaTailor console. For information about how to delete prefetch schedules programmatically using the MediaTailor API, see [DeletePrefetchSchedule](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DeletePrefetchSchedule.html) in the *AWS Elemental MediaTailor API Reference*.

**Note**
Deletion doesn't occur in real time. You might experience a delay while MediaTailor deletes the prefetch schedule(s), during which time prefetch retrieval and consumption will continue to run in the background.

**To delete a prefetch schedule using the console**

1. Open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/).

1. In the navigation pane, choose **Configurations**. Select the playback configuration that contains the prefetch schedule(s) that you want to delete.

1. On the **Prefetch schedules** tab, select the prefetch schedule that you want to delete. Then, choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
