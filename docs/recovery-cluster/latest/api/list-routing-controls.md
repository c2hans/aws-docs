---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/list-routing-controls.html
---

# List routing controls
<a name="list-routing-controls"></a>

The following is an example of a request to list the routing controls in a control panel, and the response.

```
aws route53-recovery-control-config --region us-west-2 list-routing-controls \
			--control-panel-arn arn:aws:route53-recovery-control::888888888888:controlpanel/0123456bbbbbbb0123456bbbbbb0123456
```

```
{
    "RoutingControls": [
        {
            "ControlPanelArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/0123456bbbbbbb0123456bbbbbb0123456",
            "Name": "Rc1",
            "RoutingControlArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567",
            "Status": "DEPLOYED"
        },
        {
            "ControlPanelArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/0123456bbbbbbb0123456bbbbbb0123456",
            "Name": "Rc2",
            "RoutingControlArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/hijklmnop987654321",
            "Status": "DEPLOYED"
        }
    ]
}
```
