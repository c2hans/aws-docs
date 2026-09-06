---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/describe-routing-control.html
---

# Describe a routing control
<a name="describe-routing-control"></a>

The following is an example of a request to describe a routing control, and the response.

```
aws route53-recovery-control-config --region us-west-2 describe-routing-control \
			--routing-control-arn arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/def123def123def
```

```
{
    "RoutingControl": {
        "ControlPanelArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx",
        "Name": "NewRc1",
        "RoutingControlArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/def123def123def",
        "Status": "DEPLOYED"
    }
}
```
