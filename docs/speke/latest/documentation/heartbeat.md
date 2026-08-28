---
source_url: https://docs.aws.amazon.com/speke/latest/documentation/heartbeat.html
---

# SPEKE API v1 - Heartbeat
<a name="heartbeat"></a>

 *Request Syntax Example*

The following URL is an example and does not indicate a fixed format:

```
GET https://speke-compatible-server/speke/v1.0/heartbeat
```

 *Request Response*

| HTTP CODE | Payload Name | Occurs | Description |
| --- | --- | --- | --- |
|  `200 (Success)`  | statusMessage | 1..1 | Message that describes the status |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Packager and Encoder Key Exchange API Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query speke` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
