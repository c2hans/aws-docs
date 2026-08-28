---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-use.html
---

# **eb use**
<a name="eb3-use"></a>

## Description
<a name="eb3-usedescription"></a>

Sets the specified environment as the default environment.

When using Git, **eb use** sets the default environment for the current branch. Run this command once in each branch that you want to deploy to Elastic Beanstalk.

## Syntax
<a name="eb3-usesyntax"></a>

 **eb use {{environment-name}}**

## Options
<a name="eb3-useoptions"></a>

|  Name  |  Description  |
| --- | --- |
| `--source codecommit/{{repository-name}}/{{branch-name}}` | CodeCommit repository and branch. |
| `-r {{region}}`<br />`--region {{region}}` | Change the region in which you create environments. |
| [Common options](eb3-cmd-options.md) |  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
