---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/create-control-panel.html
---

# Create a control panel
<a name="create-control-panel"></a>

A control panel is a logical grouping for organizing your Amazon Application Recovery Controller routing controls. When you create a cluster, Amazon Application Recovery Controller automatically provides a control panel for you called `DefaultControlPanel`. You can use this control panel right away.

Optionally, create your own control panel by calling `create-control-panel`. A control panel can only exist in one cluster. If you want to move a control panel to another cluster, you must delete it and then create it in the second cluster.

The following is an example of a request to create a control panel in a cluster, and the response.

```
aws route53-recovery-control-config --region us-west-2 create-control-panel \
			--control-panel-name NewControlPanel2 \
			--cluster-arn arn:aws:route53-recovery-control::012345678901:cluster/abc123456-aa11-bb22-cc33-abc123456
```

```
{
    "ControlPanel": {
        "ControlPanelArn": "arn:aws:route53-recovery-control::012345678901:controlpanel/d22190fdbfca4845804e3f76457d57c9",
        "ClusterArn": "arn:aws:route53-recovery-control::012345678901:cluster/abc123456-aa11-bb22-cc33-abc123456",
        "DefaultControlPanel": false,
        "Name": "NewControlPanel2",
        "RoutingControlCount": 0,
        "Status": "PENDING"
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-cluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
