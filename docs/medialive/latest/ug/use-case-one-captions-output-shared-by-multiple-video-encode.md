---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/use-case-one-captions-output-shared-by-multiple-video-encode.html
---

# Use case D: One captions output shared by multiple video encodes
<a name="use-case-one-captions-output-shared-by-multiple-video-encode"></a>

This example for captions in MediaLive shows how to set up captions in an ABR workflow.

The first setup shows how to set up an ABR workflow when the captions are in the same output as the video, meaning that the captions are either embedded or captions style.

The second setup shows how to set up an ABR workflow when the captions belong to the sidecar category, in which case each captions encode is in its own output.

**Topics**
+ [Setup with Embedded or object-style captions](setup-with-procedure-a-captions.md)
+ [Setup with sidecar captions](setup-with-procedure-b-captions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
