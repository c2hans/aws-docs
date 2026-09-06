---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-init.html
---

# init
<a name="resource-type-cli-init"></a>

## Description
<a name="resource-type-cli-init-description"></a>

The `init` command launches a wizard that walks you through setting up your project. Once your project is specified, the command generates a new extension project with stub source files.

While the specific folder structure and files generated varies project and by language, in general the project includes the following:
+ Schema file.
+ Handler function source files.
+ Unit test files.
+ Build files for the specified language.

By default, `init` generates the extension project in the current directory.

## Synopsis
<a name="resource-type-cli-init-synopsis"></a>

```
$ cfn init [--force]
```

## Options
<a name="resource-type-cli-init-options"></a>

`--force`

Force project files to be overwritten.

## Output
<a name="resource-type-cli-init-output"></a>

The `init` command launches a wizard that walks you through setting up the project, including specifying the extension name.

```
Initializing new project
Do you want to develop a new resource(r) or a module(m) or a hook(h)?
```
