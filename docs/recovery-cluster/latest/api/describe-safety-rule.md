---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/describe-safety-rule.html
---

# Describe a safety rule
<a name="describe-safety-rule"></a>

The following is an example of a request to describe a type of safety rule, and the response. This safety rule is an assertion rule.

```
aws route53-recovery-control-config --region us-west-2 describe-safety-rule \
			--safety-rule-arn arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/safetyrule/333333444444
```

```
{
    "SafetyRule": {
        "ASSERTION": {
            "Arn": "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/safetyrule/333333444444",
            "AssertedControls": [
                "arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/abcdefg1234567"
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
}
```
