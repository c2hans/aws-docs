---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/eml-multiplex.html
---

# Working with multiplexes
<a name="eml-multiplex"></a>

A MediaLive multiplex creates a multi-program transport stream (MPTS). You might be interested in creating a MediaLive multiplex if you are a service provider who has experience with distributing transport stream (TS) content over RTP or UDP.

To set up a multiplex, you create a MediaLive multiplex. You then add MediaLive programs to the multiplex. Finally, you create one MediaLive channel for each program, and associate each channel with its program.

For conceptual information about setting up a multiplex, see [Using MediaLive multiplex to create an MPTS](feature-multiplex.md).

**Topics**
+ [Summary of actions](multiplex-create-delete-edit-summary.md)
+ [Creating a multiplex and program](multiplex-create.md)
+ [Creating a channel](multiplex-channel-create.md)
+ [Editing multiplexes, programs, and channels](edit-multiplex-program-channel.md)
+ [Deleting multiplexes, programs, and channels](delete-multiplex-program.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
