---
source_url: https://docs.aws.amazon.com/wickr/latest/adminguide/dataretention-message-attribute-change.html
---

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Message attribute change
<a name="dataretention-message-attribute-change"></a>

These control messages show when a message is starred or unstarred.

```
{
  "control": {
    "attributes": [
      {
        "isstarred": true,
        "msgid": "93cf81608bbd11ea9a16b7554e31eed2"
      }
    ],
    "msgtype": 4012
  },
  "message_id": "b0d284d08be311eaaf7f51713016a94c",
  "msg_ts": "1588362062.000000",
  "msgtype": 4012,
  "receiver": "user001",
  "sender": "user002",
  "sender_type": "normal",
  "time": "5/1/20 12:41 PM",
  "time_iso": "2020-05-01 12:41:02.000",
  "vgroupid": "4ebf561eb2214c4e6f924d09e37bf80b6f9b85cb96b72badb03753d9ed26f7f4"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
