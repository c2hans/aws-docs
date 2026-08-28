---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/viewing-flows-maintenance.html
---

# Viewing flow maintenance status
<a name="viewing-flows-maintenance"></a>

You can view the maintenance status of your flows in the MediaConnect console or by using the AWS CLI.

**To view flow maintenance status (console)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Flows**.

1. The **Maintenance window** column displays the maintenance status for each flow. If maintenance is required, the column shows the scheduled date.

1. To view detailed maintenance information for a specific flow, choose the flow name to open its details page.

**To view flow maintenance status (AWS CLI)**
Use the `list-flows` command to see maintenance status across all flows, or the `describe-flow` command for detailed information about a specific flow.

The response includes maintenance details in the `Maintenance` object:

```
{
    "Flows": [
        {
            "AvailabilityZone": "us-west-2d",
            "Description": "Example flow description",
            "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame",
            "Name": "BasketballGame",
            "SourceType": "OWNED",
            "Status": "STANDBY",
            "Maintenance": {
                "MaintenanceDay": "Monday",
                "MaintenanceStartHour": "08:00"
            }
        },
        {
            "AvailabilityZone": "us-west-2b",
            "Description": "Example flow description",
            "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:2-3aBC45dEF67hiJ8k-2AbC34DE5fGa6:AwardsShow",
            "Name": "AwardsShow",
            "SourceType": "OWNED",
            "Status": "ACTIVE",
            "Maintenance": {
                "MaintenanceDay": "Saturday",
                "MaintenanceDeadline": "2025-10-25T22:15:56Z",
                "MaintenanceScheduledDate": "2025-10-18",
                "MaintenanceStartHour": "23:00"
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
