---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/delete-thing.html
---

# Delete a thing
<a name="delete-thing"></a>

You can use the **DeleteThing** command to delete a thing:

```
$ aws iot delete-thing --thing-name "MyThing"
```

This command returns successfully with no error if the deletion is successful or you specify a thing that doesn't exist.

For more information, see [delete-thing](https://docs.aws.amazon.com/cli/latest/reference/iot/delete-thing.html) from the AWS CLI Command Reference.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
