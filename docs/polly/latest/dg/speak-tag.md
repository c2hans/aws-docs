---
source_url: https://docs.aws.amazon.com/polly/latest/dg/speak-tag.html
---

# Identifying SSML-enhanced text
<a name="speak-tag"></a>

*<speak>*

This tag is supported by generative, long-form, neural, and standard TTS formats.

The `<speak>` tag is the root element of all Amazon Polly SSML text. All SSML-enhanced text must be enclosed within a pair of <speak> tags.

```
<speak>Mary had a little lamb.</speak>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
