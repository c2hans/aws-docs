---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/dynamic-inputs.html
---

# Setting up dynamic inputs
<a name="dynamic-inputs"></a>

In MediaLive, you can set up a multiple-input channel with static and dynamic file inputs. You can then use the input switching feature of the channel schedule to switch from one input to another. A static input always connects to the same file. A dynamic input points to a different file each time it is used in an input switch in the schedule.

Using dynamic inputs lets you increase the number of video sources that you can use in the channel, while still observing the limit on the number of inputs that you can attach to the channel.

Only MP4 or Transport Stream (TS) file inputs that are stored in one of the following locations can be set up as dynamic inputs:
+ Amazon S3
+ AWS Elemental MediaStore

## Setting up dynamic inputs
<a name="setup-dynamic-inputs"></a>

 For information about planning and creating dynamic inputs, see [Static inputs and dynamic inputs](how-dynamic-inputs-work.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
