---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/create-namespace.html
---

# CreateNamespace
<a name="create-namespace"></a>

Use the `CreateNamespace` API operation to create a new namespace for you to use with Amazon Quick Sight.

You can create a namespace after your AWS account is subscribed to Amazon Quick Sight. The namespace must be unique within the AWS account. By default, there is a limit of 100 namespaces per AWS account. To increase your limit, create a ticket with AWS Support.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight create-namespace
    --aws-account-id {{AWSACCOUNTID}}
    --namespace {{NAMESPACE}} \
    --identity-store {{QUICKSIGHT}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-namespace
    --cli-input-json file://{{createnamespace}}.json
```

------

For more information about the `CreateNamespace` API operation, see [CreateNamespace](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateNamespace.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
