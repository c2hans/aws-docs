---
source_url: https://docs.aws.amazon.com/dcv/latest/adminguide/dcv-server-channels.html
---

# Amazon DCV server channels
<a name="dcv-server-channels"></a>

Counters in this set provide information about individual channels in a client connection. There can be additional channels for extensions.

Channel names are:
+ `dcv::main`
+ `dcv::display`
+ `dcv::input`
+ `dcv::audio`
+ `dcv::filestorage`
+ `dcv::clipboard`

Incoming filestorage traffic is attributed to the `dcv::filestorage` channel.

Outgoing filestorage traffic is included in the **HTTP Download** counters in **DCV Server Connections**.

**Note**
Counters in this set are a subset of the ones in **DCV Server Connections**.

| Counter name | Description |
| --- | --- |
| Receive Rate bits/sec | Rate in bits per second at which data is received via the channel |
| Received Bytes | Total number of bytes received via the channel |
| Send Rate bits/sec | Rate in bits per second at which data is sent via the channel |
| Sent Bytes | Total number of bytes sent via the channel |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
