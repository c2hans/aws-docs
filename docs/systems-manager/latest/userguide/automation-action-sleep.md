---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-sleep.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# `aws:sleep` – Delay an automation
<a name="automation-action-sleep"></a>

Delays an automation for a specified amount of time. This action uses the International Organization for Standardization (ISO) 8601 date and time format. For more information about this date and time format, see [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html).

**Input**
You can delay an automation for a specified duration.

------
#### [ YAML ]

```
name: sleep
action: aws:sleep
inputs:
  Duration: PT10M
```

------
#### [ JSON ]

```
{
   "name":"sleep",
   "action":"aws:sleep",
   "inputs":{
      "Duration":"PT10M"
   }
}
```

------

You can also delay an automation until a specified date and time. If the specified date and time has passed, the action proceeds immediately.

------
#### [ YAML ]

```
name: sleep
action: aws:sleep
inputs:
  Timestamp: '2020-01-01T01:00:00Z'
```

------
#### [ JSON ]

```
{
    "name": "sleep",
    "action": "aws:sleep",
    "inputs": {
        "Timestamp": "2020-01-01T01:00:00Z"
    }
}
```

------

**Note**
Automation supports a maximum delay of 604799 seconds (7 days).

Duration
An ISO 8601 duration. You can't specify a negative duration.
Type: String
Required: No

Timestamp
An ISO 8601 timestamp. If you don't specify a value for this parameter, then you must specify a value for the `Duration` parameter.
Type: String
Required: NoOutput

None

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
