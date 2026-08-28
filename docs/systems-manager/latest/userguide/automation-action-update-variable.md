---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-update-variable.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# `aws:updateVariable` – Updates a value for a runbook variable
<a name="automation-action-update-variable"></a>

This action updates a value for a runbook variable. The data type of the value must match the data type of the variable you want to update. Data type conversions aren't supported. The `onCancel` property isn't supported for the `aws:updateVariable` action.

**Input**
The input is as follows.

------
#### [ YAML ]

```
name: updateStringList
action: aws:updateVariable
inputs:
    Name: variable:{{variable name}}
    Value:
    - "1"
    - "2"
```

------
#### [ JSON ]

```
{
    "name": "updateStringList",
    "action": "aws:updateVariable",
    "inputs": {
        "Name": "variable:{{variable name}}",
        "Value": ["1","2"]
    }
}
```

------

Name
The name of the variable whose value you want to update. You must use the format `variable:{{variable name}}`
Type: String
Required: Yes

Value
The new value to assign to the variable. The value must match the data type of the variable. Data type conversions aren't supported.
Type: Boolean \| Integer \| MapList \| String \| StringList \| StringMap
Required: Yes
Constraints:
+ MapList can contain a maximum number of 200 items.
+ Key lengths can be a minimum length of 1 and a maximum length of 50.
+ StringList can be a minimum number of 0 items and a maximum number of 50 items.
+ String lengths can be a minimum length of 1 and a maximum length of 512.Output

None

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
