---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-limitations-rcs.html
---

# RCS limits and restrictions
<a name="sms-limitations-rcs"></a>

RCS messages are subject to the following limits. RCS messaging, including rich cards, carousels, file messages, suggestions, per-message fallback, and message expiration, is available in all countries where RCS is supported. For more information, see [Sending rich RCS messages](rcs-rich-messaging.md).

**RCS message limits**

| Limit | Value |
| --- | --- |
| Text message body | 3,072 characters |
| Rich card title | 200 characters |
| Rich card description | 2,000 characters |
| Carousel cards | 2 to 10 cards |
| Suggestions per message | 11 |
| Suggestions per card | 4 |
| Suggestion display text | 25 characters |
| Postback data | 2,048 characters |
| Media file size | 100 MB (carriers commonly limit video to 5 MB) |
| Media URL length | 2,000 characters |
| Total message payload | 250 KB |
| Message expiration (time-to-live) | 1 second to 172,800 seconds (48 hours) |
| Per-message fallback body (SMS or MMS) | 1,600 characters |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
