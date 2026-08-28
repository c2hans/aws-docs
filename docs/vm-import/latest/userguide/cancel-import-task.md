---
source_url: https://docs.aws.amazon.com/vm-import/latest/userguide/cancel-import-task.html
---

# Cancel an import snapshot task
<a name="cancel-import-task"></a>

After you start an import snapshot task using VM Import/Export, you can cancel the import operation if needed.

To describe your snapshot import tasks, see [Monitor an import snapshot task](check-status-import-task.md).

------
#### [ AWS CLI ]

**To cancel an import snapshot task**
Use the [cancel-import-task](https://docs.aws.amazon.com/cli/latest/reference/ec2/cancel-import-task.html) command.

```
aws ec2 cancel-import-task \
    --import-task-id {{import-snap-1234567890abcdef0}}
```

------
#### [ PowerShell ]

**To cancel an import snapshot task**
Use the [Stop-EC2ImportTask](https://docs.aws.amazon.com/powershell/latest/reference/items/Stop-EC2ImportTask.html) cmdlet.

```
Stop-EC2ImportTask `
    -ImportTaskId {{import-snap-1234567890abcdef0}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vm-import` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
