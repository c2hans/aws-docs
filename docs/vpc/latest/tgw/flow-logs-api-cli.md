---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/flow-logs-api-cli.html
---

# Create and manage AWS Transit Gateway Flow Logs using APIs or the CLI
<a name="flow-logs-api-cli"></a>

You can perform the tasks described on this page using the command line.

The following limitations apply when using the [create-flow-logs](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-flow-logs.html) command:
+ `--resource-ids` has a maximum constraint of 25 `TransitGateway` or `TransitGatewayAttachment` resource types.
+ `--traffic-type` is not a required field by default. An error is returned if you provide this for transit gateway resource types. This limit applies only to transit gateway resource types.
+ `--max-aggregation-interval` has a default value of `60`, and is the only accepted value for transit gateway resource types. An error is returned if you try to pass any other value. This limit applies only to transit gateway resource types.
+ `--resource-type` supports two new resource types, `TransitGateway` and `TransitGatewayAttachment`.
+ `--log-format` includes all log fields for transit gateway resource types if you do not set which fields you want to include. This applies only to transit gateway resource types.

**Create a flow log**
+ [create-flow-logs](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-flow-logs.html) (AWS CLI)
+ [New-EC2FlowLog](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2FlowLog.html) (AWS Tools for Windows PowerShell)

**Describe your flow logs**
+ [describe-flow-logs](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-flow-logs.html) (AWS CLI)
+ [Get-EC2FlowLog](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2FlowLog.html) (AWS Tools for Windows PowerShell)

**View your flow log records (log events)**
+ [get-log-events](https://docs.aws.amazon.com/cli/latest/reference/logs/get-log-events.html) (AWS CLI)
+ [Get-CWLLogEvent](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-CWLLogEvent.html) (AWS Tools for Windows PowerShell)

**Delete a flow log**
+ [delete-flow-logs](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-flow-logs.html) (AWS CLI)
+ [Remove-EC2FlowLog](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2FlowLog.html) (AWS Tools for Windows PowerShell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
