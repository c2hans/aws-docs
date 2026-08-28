---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-development-kit-cli-config.html
---

# config
<a name="greengrass-development-kit-cli-config"></a>

Use the `config` command in the AWS IoT Greengrass Development Kit Command-Line Interface (GDK CLI) to modify the configuration for the GDK in the configuration file, `gdk-config.json`.

**Topics**
+ [update](#greengrass-development-kit-cli-config-update)

## update
<a name="greengrass-development-kit-cli-config-update"></a>

Start an interactive prompt to modify fields within an existing GDK configuration file.

**Synopsis**

```
$ gdk config update
    [--component]
```

**Arguments**
+ `-c`, `--component` – To update component-related fields in the `gdk-config.json` file. This argument is required since it is the only option.

**Output**
The following example shows the output produced when you run this command to configure a component.

```
$ gdk config update --component
Current value of the REQUIRED component_name is (default: com.example.PythonHelloWorld):
Current value of the REQUIRED author is (default: author):
Current value of the REQUIRED version is (default: NEXT_PATCH):
Do you want to change the build configurations? (y/n)
Do you want to change the publish configurations? (y/n)
[2023-09-26 10:19:48] INFO - Config file has been updated. Exiting...
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
