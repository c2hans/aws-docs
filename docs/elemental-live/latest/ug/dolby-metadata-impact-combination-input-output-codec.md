---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-metadata-impact-combination-input-output-codec.html
---

# Combinations of input and output codec
<a name="dolby-metadata-impact-combination-input-output-codec"></a>

The possible input and output codec combinations (in which at least one codec is a Dolby codec) are as follows. All these combinations support including metadata in the output.

| Input codec | Output codec |
| --- | --- |
| Dolby Digital or Dolby Digital Plus | Dolby Digital or Dolby Digital Plus |
| Dolby Digital | Dolby Digital Passthrough (so Dolby Digital audio is passed through; it is not transcoded) |
| Dolby Digital Plus | Dolby Digital Passthrough (so Dolby Digital Plus audio is passed through; it is not transcoded) |
| Mix of Dolby Digital Plus and another codec | Dolby Digital Plus (with the Automatic Passthrough field checked) |
| Dolby E | Dolby Digital  |
| Dolby E | Dolby Digital Plus |
| Dolby E | Dolby E (passthrough ) |
| A non-Dolby codec | Dolby Digital or Dolby Digital Plus |

The sample rate when encoding with a Dolby codec is always 48000.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
