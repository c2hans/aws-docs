---
source_url: https://docs.aws.amazon.com/lightsail-for-research/latest/ug/create-computer.html
---

# Create a Lightsail for Research virtual computer
<a name="create-computer"></a>

Complete the following steps to create a Lightsail for Research virtual computer running an application.

1. Sign in to the [Lightsail for Research console](https://lfr.console.aws.amazon.com/ls/research).

1. On the home page, choose **Create virtual computer**.

1. Select an AWS Region for your virtual computer that is near your physical location.

1. Choose an application and hardware plan. For more information, see [Choose application images and hardware plans for Lightsail for Research](blueprints-plans.md).

1. Enter a name for your virtual computer. Valid characters include alphanumeric characters, numbers, periods, hyphens, and underscores.

   Virtual computer names must also meet the following requirements:
   + Be unique within each AWS Region in your Lightsail for Research account.
   + Contain 2–255 characters.
   + Start and end with an alphanumeric character or number.

1. Choose **Create virtual computer** in the **Summary** panel.

Within minutes, your Lightsail for Research virtual computer is ready and you can connect to it through a graphical user interface (GUI) session. For more information about connecting to your Lightsail for Research virtual computer, see [Access a Lightsail for Research virtual computer application](open-computer-application.md).

**Important**
Newly created virtual computers have a set of firewall ports open by default. For more information about these ports, see [Manage firewall ports for Lightsail for Research virtual computers](manage-ports.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail for Research. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail-for-research` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
