---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/userguide/monitor.html
---

# Monitor events and logs in Image Builder
<a name="monitor"></a>

To maintain the reliability, availability, and performance of your EC2 Image Builder pipelines, it's important to monitor events and logs. Events and logs help you see the big picture and dive down into the details when an API call fails. Image Builder integrate with services that can send alerts and kick off automated responses when events match the criteria that you've configured.

The following topics describe monitoring techniques you can use through services that integrate with Image Builder.

**Topics**
+ [Log Image Builder API calls using CloudTrail](log-cloudtrail.md)
+ [Monitor Image Builder logs with Amazon CloudWatch Logs](monitor-cwlogs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
