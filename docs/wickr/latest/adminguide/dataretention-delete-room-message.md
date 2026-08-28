---
source_url: https://docs.aws.amazon.com/wickr/latest/adminguide/dataretention-delete-room-message.html
---

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Delete room message
<a name="dataretention-delete-room-message"></a>

Wickr generates this message when a room is permanently deleted.

```
{
  "message_id": "06364710f89811e899418b6723464a0c",
  "msg_ts": "1544019245.000000",
  "msgtype": 4005,
  "sender": "user002",
  "sender_type": "normal",
  "time": "12/5/18 2:54 PM",
  "time_iso": "2018-12-05 14:54:05.000",
  "vgroupid": "S7879eb406958d83b991a5f2acb29e5ad8565a4faa41e1c5cbd7004c5586ddd5"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
