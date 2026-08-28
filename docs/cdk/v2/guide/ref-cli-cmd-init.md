---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-init.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# `cdk init`
<a name="ref-cli-cmd-init"></a>

Create a new AWS CDK project from a template.

## Usage
<a name="ref-cli-cmd-init-usage"></a>

```
$ cdk init <arguments> <options>
```

## Arguments
<a name="ref-cli-cmd-init-args"></a><a name="ref-cli-cmd-init-args-template-type"></a>

 **Template type**
The CDK template type to initialize a new CDK project from.
+  `app` – Template for a CDK application.
+  `lib` – Template for an AWS Construct Library.
+  `sample-app` – Example CDK application that includes some constructs.
 *Valid values*: `app`, `lib`, `sample-app`

## Options
<a name="ref-cli-cmd-init-options"></a>

For a list of global options that work with all CDK CLI commands, see [Global options](ref-cli-cmd.md#ref-cli-cmd-options).<a name="ref-cli-cmd-init-options-generate-only"></a>

 `--generate-only <BOOLEAN>`
Specify this option to generate project files without initiating additional operations such as setting up a git repository, installing dependencies, or compiling the project.
 *Default value*: `false` <a name="ref-cli-cmd-init-options-help"></a>

 `--help, -h <BOOLEAN>`
Show command reference information for the `cdk init` command.<a name="ref-cli-cmd-init-options-language"></a>

 `--language, -l <STRING>`
The language to be used for the new project. This option can be configured in the project’s `cdk.json` configuration file or at `~/.cdk.json` on your local development machine.
 *Valid values*: `csharp`, `fsharp`, `go`, `java`, `javascript`, `python`, `typescript` <a name="ref-cli-cmd-init-options-list"></a>

 `--list <BOOLEAN>`
List the available template types and languages.

## Examples
<a name="ref-cli-cmd-init-examples"></a>

### List the available template types and languages
<a name="ref-cli-cmd-init-examples-1"></a>

```
$ cdk init --list
Available templates:
* app: Template for a CDK Application
   └─ cdk init app --language=[csharp|fsharp|go|java|javascript|python|typescript]
* lib: Template for a CDK Construct Library
   └─ cdk init lib --language=typescript
* sample-app: Example CDK Application with some constructs
   └─ cdk init sample-app --language=[csharp|fsharp|go|java|javascript|python|typescript]
```

### Create a new CDK app in TypeScript from the library template
<a name="ref-cli-cmd-init-examples-2"></a>

```
$ cdk init lib --language=typescript
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
