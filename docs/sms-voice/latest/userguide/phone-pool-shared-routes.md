---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-pool-shared-routes.html
---

# Update shared routes in AWS End User Messaging SMS
<a name="phone-pool-shared-routes"></a>

In some countries, AWS End User Messaging SMS maintains a pool of shared origination identities. When you activate shared routes, AWS End User Messaging SMS makes an effort to deliver your message using one of the shared identities. The origination identity could be a sender ID, long code or short code and could vary within each country. When shared routes uses a sender ID as the origination identity, the sender ID will be a generic sender ID, such as `NOTICE`. Shared identities are unavailable in some countries, including the United States.

**Note**
Shared routes can be subject to increased downstream filtering and dedicated routes, where available, are preferred.

**Turn on shared routes (AWS Management Console)**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Phone pools**.

1. On the **Phone Pools** page, choose the pool that will have shared routes enabled.

1. On the **Shared routes** tab, choose the **Edit settings** button.

1. Choose **Enable shared routes** and then **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
