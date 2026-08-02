---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/get-routing-control-state.html
---

# Get routing control state
<a name="get-routing-control-state"></a>

The following is an example of a request to get a routing control state, and the response.

For more information, see [GetRoutingControlState](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_GetRoutingControlState.html) in the Recovery Control Configuration API Reference Guide for Amazon Application Recovery Controller.

```
aws route53-recovery-cluster get-routing-control-state \
			--routing-control-arn arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/abcdefg1234567 \
			--region us-west-2 \
			--endpoint-url https://host-dddddd.us-west-2.example.com/v1
```

```
{
    "RoutingControlArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/abcdefg1234567",
    "RoutingControlState": "On"
}
```
