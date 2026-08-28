---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/template-alias-operations.html
---

# Template alias operations
<a name="template-alias-operations"></a>

A *template alias* is a reference to a version of a template. For example, suppose that you create the template alias `exampleAlias` for version 1 of the template `exampleTemp`. You can use the template alias `exampleAlias` to reference version 1 of template `exampleTemp` in a `DescribeTemplate` API operation, as in the following example.

```
aws quicksight describe-template
    --aws-account-id {{AWSACCOUNTID}}
    --template-id {{exampleTempID}}
    --alias-name {{exampleAlias}}
```

With template alias API operations, you can perform actions on Quick Sight template aliases. For more information, see the following API operations.

**Topics**
+ [CreateTemplateAlias](create-template-alias.md)
+ [DeleteTemplateAlias](delete-template-alais.md)
+ [DescribeTemplateAlias](describe-template-alias.md)
+ [ListTemplateAliases](list-template-aliases.md)
+ [UpdateTemplateAlias](update-template-alias.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
