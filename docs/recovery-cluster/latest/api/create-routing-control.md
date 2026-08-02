---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/create-routing-control.html
---

# Create a routing control
<a name="create-routing-control"></a>

When you create a routing control, at a minimum you must specify the Amazon Resource Name (ARN) of the cluster that you want the routing control to be in. You can also specify the ARN of a control panel for the routing control. You'll also need to specify the cluster where the control panel is located.

If you don't specify a control panel, your routing control is added to the automatically created control panel, `DefaultControlPanel`.

The following is an example of a request to create a routing control in a control panel, and the response.

```
aws route53-recovery-control-config --region us-west-2 create-routing-control \
			--routing-control-name NewRc1 \
			--cluster-arn arn:aws:route53-recovery-control::888888888888:cluster/5678abcd-abcd-5678-abcd-5678abcdefgh
```

```
{
    "RoutingControl": {
        "ControlPanelArn": " arn:aws:route53-recovery-control::888888888888:controlpanel/0123456bbbbbbb0123456bbbbbb0123456",
        "Name": "NewRc1",
        "RoutingControlArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567",
        "Status": "PENDING"
    }
}
```
