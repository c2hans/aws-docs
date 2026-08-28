---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/rtm-refresh.html
---

# How often real-time metrics refresh in Connect Customer
<a name="rtm-refresh"></a>

Data in real-time metrics reports is refreshed as follows:
+ The **Real-time metrics** page refreshes every 15 seconds, as long as the page is active. For example, if you have multiple tabs open in your browser and navigate to a different tab, the real-time metric page won't be updated until you return to it.
+ Metrics such as **Active** and **Availability** refresh as activity occurs, with a small system delay for processing the activity.
+ Agent near real-time metrics, such as **Missed** and **Occupancy**, refresh as activity occurs, with a small delay for processing.
+ Contact near real-time metrics refresh about a minute after a contact ends.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
