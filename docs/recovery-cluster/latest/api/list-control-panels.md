---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/list-control-panels.html
---

# List control panels
<a name="list-control-panels"></a>

A control panel is a logical grouping for organizing your Amazon Application Recovery Controller routing controls. When you create a cluster, Amazon Application Recovery Controller automatically provides a control panel for you called `DefaultControlPanel`. You can use this control panel right away.

You can see all of the control panels in your account by calling `list-control-panels`. To see just the control panels in a specific cluster, add the `--cluster-arn` field.

The following is an example of a request to list the control panels in your account, and the response.

```
aws route53-recovery-control-config --region us-west-2 list-control-panels \
			--cluster-arn arn:aws:route53-recovery-control::012345678901:cluster/abc123456-aa11-bb22-cc33-abc123456
```

```
{
    "ControlPanels": [
        {
            "ControlPanelArn": "arn:aws:route53-recovery-control::012345678901:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx789",
            "ClusterArn": "arn:aws:route53-recovery-control::012345678901:cluster/abc123456-aa11-bb22-cc33-abc123456",
            "DefaultControlPanel": true,
            "Name": "DefaultControlPanel",
            "RoutingControlCount": 0,
            "Status": "PENDING"
        },
        {
            "ControlPanelArn": "arn:aws:route53-recovery-control::012345678901:controlpanel/aaa123bbb456ccc789aaa123bbb456ccc789",
            "ClusterArn": "arn:aws:route53-recovery-control::012345678901:cluster/abc123456-aa11-bb22-cc33-abc123456",
            "DefaultControlPanel": false,
            "Name": "SecondControlPanel",
            "RoutingControlCount": 0,
            "Status": "PENDING"
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-cluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
