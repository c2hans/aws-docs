---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-programs.html
---

# Adding a program to a channel's schedule
<a name="channel-assembly-programs"></a>

Each program contains a VOD source or a live source that's part of a source location in your account. You add your programs to your channel's schedule to control the order that they play in your channel's stream.

A program that contains a VOD source can be configured with one or more ad breaks. Each ad break contains a slate, which is a VOD source from a source location. To create the ad break, you add the slate at an offset in milliseconds into the program.

**Topics**
+ [Creating a program within a channel schedule using the MediaTailor console](channel-assembly-adding-programs.md)
+ [Defining audience cohorts and alternate content with Program Rules](working-with-program-rules.md)
+ [Generating audience-specific manifests](generating-audience-specific-manifests.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
