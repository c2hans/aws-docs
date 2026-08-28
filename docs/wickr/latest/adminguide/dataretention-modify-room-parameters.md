---
source_url: https://docs.aws.amazon.com/wickr/latest/adminguide/dataretention-modify-room-parameters.html
---

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Modify room parameters message
<a name="dataretention-modify-room-parameters"></a>

Wickr generates this message when room settings change, such as the title, description, expiration timer, or burn-on-read timer.

```
{
  "control": {
    "bor": 0,
    "changemask": 4,
    "description": "",
    "masters": ["user001"],
    "members": ["user001", "user002"],
    "msgtype": 4004,
    "title": "Renamed room",
    "ttl": 2592000
  },
  "message_id": "db805750f89711e8a01ab328ac0b2f04",
  "msg_ts": "1544019174.000000",
  "msgtype": 4004,
  "sender": "user002",
  "sender_type": "normal",
  "time": "12/5/18 2:52 PM",
  "time_iso": "2018-12-05 14:52:54.000",
  "vgroupid": "S58a15186365d2125a9b417e71b99bcb29e3770078e157e953cfbe28443eb750"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
