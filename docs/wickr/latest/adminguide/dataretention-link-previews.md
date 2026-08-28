---
source_url: https://docs.aws.amazon.com/wickr/latest/adminguide/dataretention-link-previews.html
---

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Link previews
<a name="dataretention-link-previews"></a>

When a user shares a link and has "Link Previews" enabled, Wickr generates an **edit** message with the preview content.

```
{
  "edit": {
    "originalmessageid": "11457fa08da211ea881baffab0b42745",
    "text": "https://example.com",
    "type": "text"
  },
  "message_id": "1163e5b08da211eab775a5032a0322ca",
  "msg_ts": "1588553780.000000",
  "msgtype": 9000,
  "sender": "user001",
  "sender_type": "normal",
  "time": "5/3/20 5:56 PM",
  "time_iso": "2020-05-03 17:56:20.000",
  "vgroupid": "S243f2ec645d3961bdd531f51f3244205d292b8d0fbd41802827746271d31d41"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
