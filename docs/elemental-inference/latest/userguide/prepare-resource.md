---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/userguide/prepare-resource.html
---

# Reference
<a name="prepare-resource"></a>

## Media requirements
<a name="source-media-reqs"></a>

- **Container**
  - **Characteristic:** Live or VOD?
  - **Requirements:** Live only

- ** Video **
  - **Characteristic:** Codec / **Requirements:**  H.264 or H.265
  - **Characteristic:** Framerate / **Requirements:** 30 frames per second
  - **Characteristic:** Aspect ratio / **Requirements:** Any
  - **Characteristic:** Resolution / **Requirements:** 1280x720

- ** Audio **
  - **Characteristic:** Codec
  - **Requirements:** AAC

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Inference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-inference` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
