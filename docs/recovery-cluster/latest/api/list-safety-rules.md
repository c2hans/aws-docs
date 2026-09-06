---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/list-safety-rules.html
---

# List safety rules
<a name="list-safety-rules"></a>

The following is an example of a request to list the safety rules in a control panel, and the response.

```
aws route53-recovery-control-config --region us-west-2 list-safety-rules \
			--control-panel-arn arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx
```

```
{
    "SafetyRules": [
        {
            "ASSERTION": {
                "Arn": "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/safetyrule/333333444444",
                "AssertedControls": [
                    "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/def123def123def"
                ],
                "ControlPanelArn": "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx",
                "Name": "TestSafetyRule",
                "RuleConfig": {
                    "Inverted": false,
                    "Threshold": 1,
                    "Type": "ATLEAST"
                },
                "Status": "DEPLOYED",
                "WaitPeriodMs": 5000
            }
        }
    ]
}
```
