---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/endpoints-regions-third-party-stt.html
---

# Endpoints and Regions for third-party STT providers
<a name="endpoints-regions-third-party-stt"></a>

By default, Connect Customer communicates with the following endpoints:

**Deepgram**: [https://api.deepgram.com](https://api.deepgram.com)

**ElevenLabs**: [https://api.elevenlabs.io](https://api.elevenlabs.io)

You can specify a different provider Region alongside your API key as part of the JSON object:

```
{
  "apiToken": "XXXXX",
  "apiTokenRegion": "xx"
}
```

The following Regions are supported:

| **Provider** | **apiTokenRegion** | **Endpoint** |
| --- | --- | --- |
| Deepgram | eu | [https://api.eu.deepgram.com](https://api.eu.deepgram.com) (only supported for speech-to-text) |
| Deepgram | {SHORT\_UID}.{REGION\_SUBDOMAIN} | https://{SHORT\_UID}.{REGION\_SUBDOMAIN}.api.deepgram.com (Deepgram Dedicated endpoints) |
| ElevenLabs | us | [https://api.us.elevenlabs.io](https://api.us.elevenlabs.io) |
| ElevenLabs | eu | [https://api.eu.residency.elevenlabs.io](https://api.eu.residency.elevenlabs.io) |
| ElevenLabs | in | [https://api.in.residency.elevenlabs.io](https://api.in.residency.elevenlabs.io) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
