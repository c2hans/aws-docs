---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-customize-the-omni-agent-with-skills.html
---

# Customize the Omni agent with skills

A skill is a set of instructions that teaches the Omni agent how your team works, such as a runbook for triaging errors on a service or the steps your team follows for an on-call handoff. When a request matches a skill, the Omni agent loads the skill and follows its instructions in the conversation.

**Note**
These skills customize the Omni agent in the Omni web UI. To use Omni from your own coding agent, see [Use Omni skills](omni-use-omni-skills.md).

## Where you work with skills
<a name="omni-customize-the-omni-agent-with-skills-where"></a>

You work with skills from the command center, the input bar at the bottom of the Omni web UI. Enter a `/skill` command there, or ask the Omni agent in plain language. To browse your skills, you can also enter `?` in the command center to open the Library, where you find services, dashboards, tools, and alerts, and then choose **Skills**.

## Skill visibility
<a name="omni-customize-the-omni-agent-with-skills-visibility"></a>

Each skill has a visibility. The following table describes who can use and change a skill with each visibility.

| Visibility | Who can use it | Who can create, edit, or delete it |
| --- | --- | --- |
| Private | Only you | You |
| Space | Everyone in the space | Space admins |

When a space skill and one of your private skills have the same name, the Omni agent uses the space skill.

## When the Omni agent uses a skill
<a name="omni-customize-the-omni-agent-with-skills-when-the-agent-uses-a-skill"></a>

You choose when the Omni agent uses each skill:
+ **Automatically, when a request matches its description.** The Omni agent reads the description of each active skill and loads the skill when your request matches it. Keep the description short and specific about when to use the skill.
+ **Only when run with `/skill use` or included by another skill.** The Omni agent uses the skill only when you run it, or when another skill includes it.

## Create a skill
<a name="omni-customize-the-omni-agent-with-skills-create-a-skill"></a>

1. In the command center, do one of the following:
   + Enter `/skill new`.
   + Enter `/skill list`, or open **Skills** in the Library, and choose **Create skill**.
   + Ask the Omni agent to draft a skill, for example "Create a skill for triaging 5xx errors on payment-api." The Omni agent fills in the form for you to review.

1. For **Name**, enter a name that uses lowercase letters, numbers, and hyphens, such as `error-triage`.

1. For **Description**, describe when Omni should use the skill. The Omni agent uses the description to decide when to load the skill, so keep it short and specific.

1. (Optional) For **When Omni uses this skill**, choose whether Omni uses the skill automatically or only on request. The default is automatically.

1. For **Instructions**, describe what the Omni agent should do. Markdown is supported. To include another skill, enter `@` and choose the skill.

1. (Optional) For **Visibility**, choose **Private** or **Space**. The default is **Private**.

1. Choose **Create skill**.

The skill applies to your next message.

## Run a skill
<a name="omni-customize-the-omni-agent-with-skills-run-a-skill"></a>

To run a skill directly, enter `/skill use`, the skill name, and your request in the command center. The following example runs the `error-triage` skill to check recent errors on `payment-api`:

```
/skill use error-triage Check the errors on payment-api from the last hour
```

## Include other skills
<a name="omni-customize-the-omni-agent-with-skills-include-other-skills"></a>

A skill can include other active skills, so the Omni agent loads them together. In the instructions, enter `@` and choose a skill. The skills that you include appear under **Included skills**. A space skill can't include a private skill.

## Manage skills
<a name="omni-customize-the-omni-agent-with-skills-manage-skills"></a>

To see your skills, enter `/skill list` in the command center, or open **Skills** in the Library. The list shows the space's skills and your private skills, with their visibility, version, and status. You can filter by **Status** and **Visibility**, and search by name or description.

From the list, or from a skill that you open with `/skill open`, you can:
+ **Edit** the name, description, instructions, usage, or visibility.
+ **Deactivate** a skill so that the Omni agent stops using it, and **Activate** it again later.
+ **Delete** a skill.

**Skills that need attention.** In the skills list, the **Status** column shows **Needs attention** next to **Active** or **Inactive** when the Omni agent can't use a skill as written. Hover over it to see the reasons. When you open the skill, a warning at the top lists what to fix. Edit the skill to fix it. Until then, the Omni agent doesn't use the skill, and you can't include it in another skill.

If someone saves a skill after you open it, saving your change fails. Choose **Reload current version**, and then make your change again.

## Limits
<a name="omni-customize-the-omni-agent-with-skills-limits"></a>

| Resource | Limit |
| --- | --- |
| Private skills per user | 25 |
| Space skills per space | 100 |
| Skill name | Up to 64 characters (lowercase letters, numbers, and hyphens) |
| Description | Up to 500 characters |
| Skill size | 32 KiB |
| Included skills per skill | 5 |

Inactive skills count toward these limits. You can't raise these limits.

## Permissions
<a name="omni-customize-the-omni-agent-with-skills-permissions"></a>

Your access grants in the space determine whether you can view, create, change, and delete skills. Only a space admin can create, change, or delete a space skill. For more information, see [Control access to your space](omni-control-access-to-your-space.md).

## Skill commands
<a name="omni-customize-the-omni-agent-with-skills-commands"></a>

| Command | What it does |
| --- | --- |
| /skill list | Opens the list of skills |
| /skill new | Opens the form to create a skill |
| /skill open {{name}} | Opens a skill |
| /skill use {{name}} {{request}} | Runs a skill with your request |
