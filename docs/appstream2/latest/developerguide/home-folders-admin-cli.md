---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders-admin-cli.html
---

# Using the AWS Command Line Interface or AWS SDKs
<a name="home-folders-admin-cli"></a>

You can enable and disable home folders for a stack by using the AWS CLI or AWS SDKs.

Use the following [create-stack](https://docs.aws.amazon.com/cli/latest/reference/appstream/create-stack.html) command to enable home folders while creating a new stack:

```
aws appstream create-stack --name {{ExampleStack}} --storage-connectors ConnectorType=HOMEFOLDERS
```

Use the following [update-stack](https://docs.aws.amazon.com/cli/latest/reference/appstream/update-stack.html) command to enable home folders for an existing stack:

```
aws appstream update-stack --name {{ExistingStack}} --storage-connectors ConnectorType=HOMEFOLDERS
```

Use the following command to disable home folders for an existing stack. This command does not delete any user data.

```
aws appstream update-stack --name {{ExistingStack}} --delete-storage-connectors
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
