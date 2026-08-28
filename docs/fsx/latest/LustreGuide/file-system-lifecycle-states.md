---
source_url: https://docs.aws.amazon.com/fsx/latest/LustreGuide/file-system-lifecycle-states.html
---

# FSx for Lustre file system status
<a name="file-system-lifecycle-states"></a>

You can view the status of an Amazon FSx file system by using the Amazon FSx console, the AWS CLI command [describe-file-systems](https://docs.aws.amazon.com/cli/latest/reference/fsx/describe-file-systems.html), or the API operation [DescribeFileSystems](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystems.html).

| File system status  | Description |
| --- | --- |
| AVAILABLE | The file system is in a healthy state, and is reachable and available for use. |
| CREATING | Amazon FSx is creating a new file system. |
| DELETING | Amazon FSx is deleting an existing file system. |
| UPDATING | The file system is undergoing a customer-initiated update. |
| MISCONFIGURED | The file system is in a failed but recoverable state. |
| FAILED | This status can mean either of the following:+ The file system has failed and Amazon FSx can't recover it.<br />+ When creating a new file system, Amazon FSx couldn't create the file system. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
