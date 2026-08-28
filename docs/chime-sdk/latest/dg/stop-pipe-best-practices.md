---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/stop-pipe-best-practices.html
---

# Best practices for stopping Amazon Chime SDK media pipelines
<a name="stop-pipe-best-practices"></a>

As a best practice for stopping media pipelines, call the [DeleteMediaPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaPipeline.html) API. The API allows you to delete media capture and media live connector pipelines. You can also call the [DeleteMediaCapturePipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaCapturePipeline.html) API to delete media capture pipelines. All media pipelines stop when the meeting ends.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
