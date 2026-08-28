---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-init.html
---

# Initiating a custom CloudFormation Hooks project
<a name="hooks-init"></a>

The first step in creating your custom Hooks project is to initiate the project. You can use the CloudFormation CLI `init` command to initiate your custom Hooks project.

The `init` command launches a wizard that walks you through setting up the project, including a Hooks schema file. Use this schema file as a starting point for defining the shape and semantics of your Hooks. For more information, see [Schema syntax](hooks-schema.md).

**To inititate a Hook project:**

1. Create a directory for the project.

   ```
   mkdir {{~/mycompany-testing-mytesthook}}
   ```

1. Navigate to the new directory.

   ```
   cd {{~/mycompany-testing-mytesthook}}
   ```

1. Use the CloudFormation CLI `init` command to initiate the project.

   ```
   cfn init
   ```

   The command returns the following output.

   ```
   Initializing new project
   ```

1. The `init` command launches a wizard that walks you through setting up the project. When prompted, enter `h` to specify a Hooks project.

   ```
   Do you want to develop a new resource(r) a module(m) or a hook(h)?
   ```

   ```
   h
   ```

1. Enter a a name for your Hook type.

   ```
   What's the name of your hook type?
   (Organization::Service::Hook)
   ```

   ```
   {{MyCompany}}::{{Testing}}::{{MyTestHook}}
   ```

1. If only one language plugin is installed, it is selected by default. If more than one language plugin is installed, you can choose your desired language. Enter a number selection for the language of your choice.

   ```
   Select a language for code generation:
   [1] java
   [2] python38
   [3] python39
   (enter an integer):
   ```

1. Set up packaging based on chosen development lanaguage.

------
#### [ Python ]

   (*Optional*) Choose Docker for platform-independent packaging. While Docker isn't required, it's highly recommended to make packaging easier.

   ```
   Use docker for platform-independent packaging (Y/n)?
   This is highly recommended unless you are experienced with cross-platform Python packaging.
   ```

------
#### [ Java ]

   Set Java package name and choose a codegen model. You can use the default package name, or create a new one.

   ```
   Enter a package name (empty for default 'com.mycompany.testing.mytesthook'):
   ```

   ```
   Choose codegen model - 1 (default) or 2 (guided-aws):
   ```

------

*Results*: You have successfully initiated the project and have generated the files needed to develop a Hook. The following is an example of the directories and files that make up a Hooks project for Python 3.8.

```
mycompany-testing-mytesthook.json
rpdk.log
README.md
requirements.txt
hook-role.yaml
template.yml
docs
    README.md
src
    __init__.py
    handlers.py
    models.py
    target_models
        aws_s3_bucket.py
```

**Note**
The files in the `src` directory are created based on your language selection. There are some useful comments and examples in the generated files. Some files, such as `models.py`, are automatically updated in a later step when you run the `generate` command to add runtime code for your handlers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
