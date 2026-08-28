---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/create-account-customization.html
---

# CreateAccountCustomization
<a name="create-account-customization"></a>

Use the `CreateAccountCustomization` API operation to create Amazon Quick Sight customizations in the current AWS Region. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight create-account-customization
    --aws-account-id {{555555555555}}
    --account-customization {{DEFAULTTHEME}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-account-customization
    --cli-input-json file://{{createaccountcustomization}}.json
```

------

For more information about the `CreateAccountCustomization` API operation, see [CreateAccountCustomization](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateAccountCustomization.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
