---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-docs.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# `cdk docs`
<a name="ref-cli-cmd-docs"></a>

Open AWS CDK documentation in your browser.

## Usage
<a name="ref-cli-cmd-docs-usage"></a>

```
$ cdk docs <options>
```

## Options
<a name="ref-cli-cmd-docs-options"></a>

For a list of global options that work with all CDK CLI commands, see [Global options](ref-cli-cmd.md#ref-cli-cmd-options).<a name="ref-cli-cmd-docs-options-browser"></a>

 `--browser, -b <STRING>`
The command to use to open the browser, using `%u` as a placeholder for the path of the file to open.
 *Default value*: `open %u` <a name="ref-cli-cmd-docs-options-help"></a>

 `--help, -h <BOOLEAN>`
Show command reference information for the `cdk docs` command.

## Examples
<a name="ref-cli-cmd-docs-examples"></a>

### Open AWS CDK documentation in Google Chrome
<a name="ref-cli-cmd-docs-examples-1"></a>

```
$ cdk docs --browser='chrome %u'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
