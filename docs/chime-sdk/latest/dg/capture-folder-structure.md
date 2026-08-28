---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/capture-folder-structure.html
---

# Understanding the Amazon S3 bucket folder structure for Amazon Chime SDK media capture pipelines
<a name="capture-folder-structure"></a>

The Amazon S3 buckets for media capture pipelines use this folder structure.

```
{{S3 bucket path}}/
  audio
  video
  data-channel
  meeting-events
  transcription-messages
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
