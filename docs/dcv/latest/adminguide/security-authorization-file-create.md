---
source_url: https://docs.aws.amazon.com/dcv/latest/adminguide/security-authorization-file-create.html
---

# Understanding permissions files
<a name="security-authorization-file-create"></a>

You can create a custom permissions file or update an existing permissions file using your preferred text editor. A permissions file typically takes the following format:

```
#import {{file_to_import}}

[groups]
{{group_definitions}}

[aliases]
{{alias_definitions}}

[permissions]
{{user_permissions}}
```

The following sections explain how to populate the sections when updating or creating a permissions file.

**Topics**
+ [Importing a permissions file](security-authorization-file-create-import.md)
+ [Creating groups](security-authorization-file-create-group.md)
+ [Creating aliases](security-authorization-file-create-alias.md)
+ [Adding permissions](security-authorization-file-create-permission.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
