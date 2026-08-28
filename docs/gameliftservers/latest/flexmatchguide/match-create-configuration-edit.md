---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-create-configuration-edit.html
---

# Tutorial: Edit a matchmaking configuration
<a name="match-create-configuration-edit"></a>

To edit a matchmaking configuration, choose **Matchmaking configurations** from the navigation bar and choose the configuration you want to edit. You can update any field in an existing configuration except for it's name.

When updating a configurations rule set, a new rule set can be incompatible if there are existing active matchmaking tickets for the following reasons:
+ New or different team names or number of teams
+ New player attributes
+ Changes to existing player attribute types

To make any of the these changes to your rule set, create a new matchmaking configuration with the updated rule set.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
