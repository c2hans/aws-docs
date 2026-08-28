---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-prerequisites.html
---

# Prerequisites for developing custom CloudFormation Hooks
<a name="hooks-prerequisites"></a>

You can develop a custom Hook with Java or Python. The following are the prerequisites for developing custom Hooks:

**Java prerequisites**
+ [Apache Maven](https://maven.apache.org/install.html)
+ [JDK 17](https://www.oracle.com/java/technologies/downloads/#java17)
**Note**
If you intend to use the [CloudFormation Command Line Interface (CLI)](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html) to initiate a Hooks project for Java, you must install Python 3.8 or later as well. The Java plugin for the CloudFormation CLI can be installed through `pip` (Python's package manager), which is distrubted with Python.

To implement Hook handlers for your Java Hooks project, you can download the [Java Hook handler example files](samples/java-handlers.zip).

**Python prerequisites**
+ [Python version 3.8](https://www.python.org/downloads/) or later.

To implement Hook handlers for your Python Hooks project, you can download the [Python Hook handler example files](samples/python-handlers.zip).

## Permissions for developing Hooks
<a name="hooks-development-permissions"></a>

In addition to the CloudFormation `Create`, `Update`, and `Delete` stack permissions, you'll need access to the following AWS CloudFormation operations. Access to these operations is managed through your IAM role's CloudFormation policy.
+ [register-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/register-type.html)
+ [list-types](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-types.html)
+ [deregister-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deregister-type.html)
+ [set-type-configuration](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html)

For more information, see [Grant IAM permissions for CloudFormation Hooks](grant-iam-permissions-for-hooks.md).

## Set up a development environment for Hooks
<a name="hooks-environment"></a>

To develop Hooks, you should be familiar with [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html), and either Python or Java.

**To install the CloudFormation CLI, and the associated plugins:**

1. Install the the CloudFormation CLI with `pip`, the Python package manager.

   ```
   pip3 install cloudformation-cli
   ```

1. Install either the Python or Java plugin for the CloudFormation CLI.

------
#### [ Python ]

   ```
   pip3 install cloudformation-cli-python-plugin
   ```

------
#### [ Java ]

   ```
   pip3 install cloudformation-cli-java-plugin
   ```

------

To upgrade the CloudFormation CLI and the plugin, you can use the upgrade option.

------
#### [ Python ]

```
pip3 install --upgrade cloudformation-cli cloudformation-cli-python-plugin
```

------
#### [ Java ]

```
pip3 install --upgrade cloudformation-cli cloudformation-cli-java-plugin
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
