---
source_url: https://docs.aws.amazon.com/dcv/latest/adminguide/security-authorization-file-create-alias.html
---

# Creating aliases
<a name="security-authorization-file-create-alias"></a>

You can use the `[aliases]` section of the permissions file to create sets of Amazon DCV features. After an alias was defined, you can grant or deny groups or individual users permissions to use it. Granting or denying permissions to an alias grants or denies permissions to all of the features that are included in it.

To create aliases in your permissions file, you must first add the aliases section heading to the file.

```
[aliases]
```

You can then create your aliases under the section heading. To create an alias, provide the alias name, and then specify the alias members in a comma-separated list. Alias members can be individual Amazon DCV features or other aliases.

```
{{alias_name}}={{member_1}}, {{member_2}}, {{member_3}}
```

**Example**
The following example adds the aliases section heading and creates an alias that's named `file-management`. It includes the `file-upload` and `file-download` features and an existing alias that's named `clipboard-management`.

```
[aliases]
file-management=file-upload, file-download, clipboard-management
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
