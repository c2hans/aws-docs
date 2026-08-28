---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/setup-trusted-entity-complex.html
---

# Create the trusted entity - complex option
<a name="setup-trusted-entity-complex"></a>

Read this section if you decided that you should use the [complex option](scenarios-for-medialive-role.md) for setting up the trusted entity.

With the complex option, you must perform these tasks:
+ Create policies and roles, and use those policies and roles to set up MediaLive as a trusted entity. This task is covered in steps A, B, and C.
+ Set up all MediaLive users with permissions that let them attach a specific trust policy to a channel, when they create or edit the channel. This task is covered in step D.

**Topics**
+ [Identify the access requirements](complex-scenario-create-trusted-entity-role-step1.md)
+ [Create policies](complex-scenario-create-trusted-entity-role-step2.md)
+ [Create roles](complex-scenario-create-trusted-entity-role-step3.md)
+ [Set up user permissions](requirements-medialiverole-complex-permissions.md)
+ [Access requirements for the trusted entity](trusted-entity-requirements.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
