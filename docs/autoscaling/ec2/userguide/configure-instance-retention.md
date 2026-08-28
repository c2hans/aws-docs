---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/configure-instance-retention.html
---

# Configure instance retention
<a name="configure-instance-retention"></a>

Set up your Amazon EC2 Auto Scaling group to retain instances when termination lifecycle actions fail.

 To use instance lifecycle policies in your Auto Scaling group, you must also configure a termination lifecycle hook. If you configure an instance lifecycle policy but don't have any termination lifecycle hooks, the policy has no effect. Instance lifecycle policies will only apply when termination lifecycle actions are abandoned, not when they complete successfully with the `CONTINUE` result.

 Instance lifecycle policies use retention triggers to determine when to retain an instance. The `TerminateHookAbandon` trigger causes retention in several scenarios:
+  When you explicitly call the [ CompleteLifecycleAction ](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CompleteLifecycleAction.html) API with the `ABANDON` result.
+  When a termination lifecycle action with default result `ABANDON` times out because the heartbeat timeout is reached without receiving a heartbeat.
+  When the global timeout is reached on a termination lifecycle action with default result `ABANDON`, which is 48 hours or 100 times the heartbeat timeout, whichever is smaller

------
#### [ Console ]

**To configure instance retention**

1. Open the Amazon EC2 Auto Scaling console

1. Create your Auto Scaling group (instance lifecycle policy defaults to Terminate)

1. Go to your Auto Scaling group details page and choose the **Instance Management** tab

1. In **Instance lifecycle policy for lifecycle hooks**, choose **Retain**

1. Create your termination lifecycle hooks with:
   + Lifecycle transition set to **Instance terminate**
   + Default result set to **Abandon**

------
#### [ AWS CLI ]

**To configure instance retention**
 Use the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command with an instance lifecycle policy:

```
aws autoscaling create-auto-scaling-group \
--auto-scaling-group-name {{my-asg}} \
--launch-template LaunchTemplateName={{my-template}},Version='$Latest' \
--min-size {{1}} \
--max-size {{3}} \
--desired-capacity {{2}} \
--vpc-zone-identifier {{subnet-12345678}} \
--instance-lifecycle-policy {{file://lifecycle-policy.json}}
```

Contents of lifecycle-policy.json:

```
{
    "RetentionTriggers": {
        "TerminateHookAbandon": "retain"
    }
}
```

**To add a termination lifecycle hook**
Use the [put-lifecycle-hook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-lifecycle-hook.html) command:

```
aws autoscaling put-lifecycle-hook \
--lifecycle-hook-name {{my-termination-hook}} \
--auto-scaling-group-name {{my-asg}} \
--lifecycle-transition {{autoscaling:EC2_INSTANCE_TERMINATING}} \
--default-result {{ABANDON}} \
--heartbeat-timeout {{300}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
