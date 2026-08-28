---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-create-mediaconnect-router.html
---

# Setting up a MediaConnect Router input
<a name="input-create-mediaconnect-router"></a>

This section describes how to create a MediaConnect Router input. With a MediaConnect Router input, the service provider pushes content through AWS Elemental MediaConnect to MediaLive. (From the point of view of MediaLive, the upstream system is MediaConnect. The upstream system is not the service provider.)

To perform this setup, you must work with an AWS Elemental MediaConnect user or a user with rights to both services.

It's important to note there are several considerations to consider when you want to use a MediaConnect Router input.
+ First, a MediaConnect Router Input can not be updated. That means its settings are set at creation.
+ Second, you cannot delete the MediaConnect Router Input if its connected to a router output in MediaConnect.
+ Finally, a MediaConnect Router Input can only be attached to one router output in MediaConnect.

**Topics**
+ [Create a MediaConnect Router input](setup-input-mediaconnect-router.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
