---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-printenv.html
---

# **eb printenv**
<a name="eb3-printenv"></a>

## Description
<a name="eb3-printenvdescription"></a>

Prints all the environment properties in the command window.

## Syntax
<a name="eb3-printenvsyntax"></a>

 **eb printenv**

 **eb printenv {{environment-name}}**

## Options
<a name="eb3-printenvoptions"></a>

|  Name  |  Description  |
| --- | --- |
| [Common options](eb3-cmd-options.md) |  |

## Output
<a name="eb3-printenvoutput"></a>

If successful, the command returns the status of the `printenv` operation.

## Example
<a name="eb3-printenvexample"></a>

The following example prints environment properties for the specified environment.

```
$ eb printenv
Environment Variables:
     PARAM1 = Value1
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
