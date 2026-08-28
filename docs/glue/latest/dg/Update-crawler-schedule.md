---
source_url: https://docs.aws.amazon.com/glue/latest/dg/Update-crawler-schedule.html
---

# Create a schedule for an existing crawler
<a name="Update-crawler-schedule"></a>

Follow these steps to set up a recurring schedule for an existing crawler.

------
#### [ AWS Management Console ]

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue\).

1. Choose **Crawlers** in the navigation pane.

1. Choose a crawler that you want to schedule from the available list.

1. Choose **Edit** from the **Actions menu.**

1. Scroll down to **Step 4: Set output and scheduling**, and choose **Edit**.

1.  Update your crawler schedule under **Crawler schedule**.

1. Choose **Update**.

------
#### [ AWS CLI ]

Use the following CLI command to update an existing crawler configuration:

```
aws glue update-crawler-schedule
   --crawler-name {{myCrawler}}
   --schedule {{cron(15 12 * * ? *)}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
