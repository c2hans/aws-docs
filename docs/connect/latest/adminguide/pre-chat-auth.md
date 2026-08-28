---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/pre-chat-auth.html
---

# Pre-chat authentication using the Connect Customer StartChatContact API
<a name="pre-chat-auth"></a>

Customers who authenticate in your website or mobile application before starting a chat can be recognized as authenticated when a chat is initiated. You can do this by using the [StartChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html) API.

After an authenticated customer starts a chat, set their status using the parameters in the [StartChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html) API, as shown in the following code snippet:

```
"SegmentAttributes": {
    "connect:CustomerAuthentication" : {
        "ValueMap": {
            "Status": {
                "ValueString": "AUTHENTICATED"
            }
        }
    },
    "CustomerId": "{{12345}}"
```

`CustomerId` is an optional field to identify the customer. This can be either an Connect Customer Customer Profiles ID or a custom identifier from an external system, such as a CRM.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
