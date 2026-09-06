---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/describe-control-panel.html
---

# Describe a control panel
<a name="describe-control-panel"></a>

The following is an example of a request to describe a control panel, and the response.

```
aws route53-recovery-control-config --region us-west-2 describe-control-panel \
			--control-panel-arn arn:aws:route53-recovery-control::012345678901:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/5362908c4c734c2b
```

```
{
    "ControlPanel": {
        "ControlPanelArn": "arn:aws:route53-recovery-control::012345678901:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx",
        "ClusterArn": "arn:aws:route53-recovery-control::012345678901:cluster/a2002f8b-e664-4671-bf4d-42e185241731",
        "DefaultControlPanel": true,
        "Name": "DefaultControlPanel",
        "RoutingControlCount": 3,
        "Status": "DEPLOYED"
    }
}
```
