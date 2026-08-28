---
source_url: https://docs.aws.amazon.com/vm-import/latest/userguide/cancel-image-export.html
---

# Cancel an export image task
<a name="cancel-image-export"></a>

After you start an image export using VM Import/Export, you can cancel the export operation if needed. If you attempt to cancel the export task after it is complete or is in the process of transferring the final disk image, the cancel operation fails and returns an error.

To describe your export image tasks, see [Monitor an export image task](monitor-image-export.md).

------
#### [ AWS CLI ]

**To cancel an export image task**
Use the [cancel-export-task](https://docs.aws.amazon.com/cli/latest/reference/ec2/cancel-export-task.html) command. If the command succeeds, no output is returned.

```
aws ec2 cancel-export-task \
    --export-task-id {{export-ami-1234567890abcdef0}}
```

------
#### [ PowerShell ]

**To cancel an export image task**
Use the [Stop-EC2ExportTask](https://docs.aws.amazon.com/powershell/latest/reference/items/Stop-EC2ExportTask.html) cmdlet.

```
Stop-EC2ExportTask `
    -ExportTaskId {{export-ami-1234567890abcdef0}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vm-import` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
