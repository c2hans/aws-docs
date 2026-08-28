---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/verify-delivery-status.html
---

# Verifying Delivery Status
<a name="verify-delivery-status"></a>

Enter the [`describe-delivery-channel-status`](http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-delivery-channel-status.html) command to verify that the AWS Config has started delivering the configurations to the specified delivery channel:

```
aws configservice describe-delivery-channel-status
```

The response lists the status of all the three delivery formats that AWS Config uses to deliver configurations to your bucket and topic.

```
{
    "DeliveryChannelsStatus": [
        {
            "configStreamDeliveryInfo": {
                "lastStatusChangeTime": 1415138614.125,
                "lastStatus": "SUCCESS"
            },
            "configHistoryDeliveryInfo": {
                "lastSuccessfulTime": 1415148744.267,
                "lastStatus": "SUCCESS",
                "lastAttemptTime": 1415148744.267
            },
            "configSnapshotDeliveryInfo": {
                "lastSuccessfulTime": 1415333113.4159999,
                "lastStatus": "SUCCESS",
                "lastAttemptTime": 1415333113.4159999
            },
            "name": "default"
        }
    ]
}
```

View the `lastSuccessfulTime` field in `configSnapshotDeliveryInfo`. The time should match the time you last requested the delivery of the configuration snapshot.

**Note**
AWS Config uses the UTC format (Coordinated Universal Time) to record the time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
