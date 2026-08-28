---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/setup-input-link-obtain-info.html
---

# Obtain information
<a name="setup-input-link-obtain-info"></a>

Obtain the following information from the operator of the AWS Elemental Link device:
+ The name of the device or devices that will provide your source. For example:

  **hd-re87jr7crey**

  You need two device names for a standard-class input, or one device name for a single-class input. For information about input classes and their uses, see [Choosing the channel class and input class](class-channel-input.md).
+ The Region that the device is configured for, so that you can set MediaLive for that Region. These rules apply:
  + Both devices must be in the same Region.
  + The device, the input for that device, and the channel that uses the input must all be in the same Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
