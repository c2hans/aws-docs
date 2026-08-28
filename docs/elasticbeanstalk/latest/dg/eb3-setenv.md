---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-setenv.html
---

# **eb setenv**
<a name="eb3-setenv"></a>

## Description
<a name="eb3-setenv-description"></a>

Sets [environment properties](environments-cfg-softwaresettings.md) for the default environment.

## Syntax
<a name="eb3-setenv-syntax"></a>

**eb setenv {{key}}={{value}}**

You can include as many properties as you want, but the total size of all properties cannot exceed 4096 bytes. You can delete a variable by leaving the value blank. See [Configuring environment properties (environment variables)](environments-cfg-softwaresettings.md#environments-cfg-softwaresettings-console) for limits.

**Note**
If the `value` contains a [special character](http://tldp.org/LDP/abs/html/special-chars.html), you must escape that character by preceding it with a `\` character.

## Options
<a name="eb3-setenvoptions"></a>

|  Name  |  Description  |
| --- | --- |
| --timeout | The number of minutes before the command times out. |
| [Common options](eb3-cmd-options.md) |  |

## Output
<a name="eb3-setenv-output"></a>

If successful, the command displays that the environment update succeeded.

## Example
<a name="eb3-setenv-example"></a>

The following example sets the environment variable ExampleVar.

```
$ eb setenv ExampleVar=ExampleValue
2018-07-11 21:05:25    INFO: Environment update is starting.
2018-07-11 21:05:29    INFO: Updating environment tmp-dev's configuration settings.
2018-07-11 21:06:50    INFO: Successfully deployed new configuration to environment.
2018-07-11 21:06:51    INFO: Environment update completed successfully.
```

The following command sets multiple environment properties. It adds the environment property named `foo` and sets its value to `bar`, changes the value of the `JDBC_CONNECTION_STRING` property, and deletes the `PARAM4` and `PARAM5` properties.

```
$ eb setenv foo=bar JDBC_CONNECTION_STRING=hello PARAM4= PARAM5=
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
