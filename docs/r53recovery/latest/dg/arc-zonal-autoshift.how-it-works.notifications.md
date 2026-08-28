---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.notifications.html
---

# Notification for practice runs and autoshifts
<a name="arc-zonal-autoshift.how-it-works.notifications"></a>

You can choose to be notified about practice runs and autoshifts for your resource by setting up Amazon EventBridge notifications. You can set up EventBridge notifications even when you haven't enabled zonal autoshift for any resources, known as *autoshift observer notification*. With autoshift observer notification, you are notified about all autoshifts that ARC starts when an Availability Zone is potentially impaired. Note that you must configure this option in each AWS Region that you want to receive notifications about.

To see the steps for enabling autoshift observer notification, see [Enabling or disabling autoshift observer notification](arc-zonal-autoshift.enable-autoshift-observer.md). To learn more about notification options and how to configure them in EventBridge, see [Using zonal autoshift with Amazon EventBridge](eventbridge-zonal-autoshift.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
