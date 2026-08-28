---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/codec-outputs-supported-conversions.html
---

# Audio codecs and supported conversions
<a name="codec-outputs-supported-conversions"></a>

Generally, Elemental Live can convert any audio codec that is supported as a source to any audio codec that is supported as an output. However, there are some constraints, as follows.
+ Constraint when Dolby Digital with Atmos is the source. Conversion to another codec isn't supported. You can only pass through this source codec.
+ Constraint when converting to another codec (other than Dolby Digital with Atmos) and changing the coding mode. The following rules apply:
  + The source must contain at least as many channels as the output. For example, to produce Dolby 5.1 (6 channels), the source must contain 6 channels.
  + The source can contain fewer channels. For example, you can convert Dolby 5.1 to AAC 2.0.

  In both cases, you might need to remix the channels in the output.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
