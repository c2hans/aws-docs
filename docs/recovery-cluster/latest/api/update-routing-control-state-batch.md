---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/update-routing-control-state-batch.html
---

# Update state for two routing controls at the same time, in a batch
<a name="update-routing-control-state-batch"></a>

The following is an example of a request to update two routing control states at the same time. It sets one to the state OFF and the other to the state ON. Updating routing control states with this command doesn't return a response.

For more information, see [UpdateRoutingControlStates](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlStates.html) in the Recovery Control Configuration API Reference Guide for Amazon Application Recovery Controller.

```
aws route53-recovery-cluster update-routing-control-states \
				--update-routing-control-state-entries \
				'[{"RoutingControlArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567",
				"RoutingControlState": "Off"}, \
				{"RoutingControlArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/hijklmnop987654321",
				"RoutingControlState": "On"}]' \
				--region us-west-2 \
				--endpoint-url https://host-dddddd.us-west-2.example.com/v1
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-cluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
