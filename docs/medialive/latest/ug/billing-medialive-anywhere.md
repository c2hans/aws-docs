---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/billing-medialive-anywhere.html
---

# MediaLive Anywhere usage types
<a name="billing-medialive-anywhere"></a>

MediaLive Anywhere (EMLA) uses a simpler format than cloud-based channels:

```
EMLA-{Region}-{Codec}-{Resolution}
EMLA-{Region}-AUDIO
```

MediaLive Anywhere usage types do not include level, framerate, or quality suffixes. All MediaLive Anywhere charges appear under the CHANNEL\_ACTIVE operation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
