---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-pool-add.html
---

# Add a keyword to a phone pool in AWS End User Messaging SMS
<a name="keywords-pool-add"></a>

Use the AWS End User Messaging SMS console or AWS CLI to customize the keyword responses for your phone pool.

------
#### [ Add a keyword (Console) ]

Use the AWS End User Messaging SMS console to add keywords to your pool.

**Add a keyword**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Phone pools**.

1. On the **Phone Pools** page, choose the pool to add a keyword to.

1. On the **Keywords** tab, choose **Add keyword**.

1. In the **Custom Keyword** pane do the following:
   + **Keyword** – The new keyword to add.
   + **Response message** – The message to send back to the recipient.
   + **Keyword action** – The action to perform when the keyword is received.

1. Choose **Add keyword**.

------
#### [ Add or edit a keyword (AWS CLI) ]

You can use the [put-keyword](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/put-keyword.html) command to create a new keyword or edit. If the keyword already exists then it will be over written.

To create a keyword, run the following command in the AWS CLI:

```
$ aws pinpoint-sms-voice-v2 put-keyword \
> --origination-identity {{OriginationIdentity}} \
> --keyword {{Keyword}} \
> --keyword-message {{KeywordMessage}} \
> --keyword-action {{KeywordAction}}
```

In the preceding command, make the following changes:
+ Replace {{OriginationIdentity}} with the unique ID or Amazon Resource Name (ARN) of the pool that you want to add the keyword to.
+ Replace {{Keyword}} with the new keyword.
+ Replace {{KeywordMessage}} with the message to use when responding to the keyword.
+ Replace {{KeywordAction}} the action (`AUTOMATIC_RESPONSE`, `OPT_OUT`, `OPT_IN`) to perform when the keyword is received.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
