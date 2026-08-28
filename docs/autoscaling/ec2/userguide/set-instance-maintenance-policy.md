---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/set-instance-maintenance-policy.html
---

# Set an instance maintenance policy
<a name="set-instance-maintenance-policy"></a>

To set an instance maintenance policy on an Auto Scaling group, use one of the following methods:

------
#### [ Console ]

**To set an instance maintenance policy on a new group (console)**

1. Follow the instructions in [Create an Auto Scaling group using a launch template](create-asg-launch-template.md) and complete each step in the procedure, up to step 11.

1. On the **Configure group size and scaling policies**, for **Desired capacity**, enter the initial number of instances to launch.

1. In the **Scaling** section, under **Scaling limits**, if your new value for **Desired capacity** is greater than **Min desired capacity** and **Max desired capacity**, the **Max desired capacity** is automatically increased to the new desired capacity value. You can change these limits as needed.

1. For **Automatic scaling**, choose whether you want to create a target tracking scaling policy. You can also create this policy after your create your Auto Scaling group.

   If you choose **Target tracking scaling policy**, follow the directions in [Create a target tracking scaling policy](policy_creating.md) to create the policy.

1. In the **Instance maintenance policy** section, choose one of the available options:
   + **Launch before terminating**: A new instance must be provisioned first before an existing instance can be terminated. This is a good choice for applications that favor availability over cost savings.
   + **Terminate and launch**: New instances are provisioned at the same time your existing instances are terminated. This is a good choice for applications that favor cost savings over availability. It's also a good choice for applications that should not launch more capacity than is currently available.
   + **Custom policy**: This option lets you set up your policy with a custom minimum and maximum range for the amount of capacity that you want available when replacing instances. This can help you achieve the right balance between cost and availability.

1. For **Set healthy percentage**, enter values for one or both of the following fields. The enabled fields vary depending on the option that you chose in the preceding step.
   + **Min**: Sets the minimum healthy percentage that's required to proceed with replacing instances.
   + **Max**: Sets the maximum healthy percentage that's possible when replacing instances.

1. Expand the **View capacity during replacements based on your desired capacity** section to confirm how the values for **Min** and **Max** apply to your group. The exact values used depend on the desired capacity value, which will change if the group scales.

1. Continue with the steps in [Create an Auto Scaling group using a launch template](create-asg-launch-template.md).

------
#### [ AWS CLI ]

**To set an instance maintenance policy on a new group (AWS CLI)**
Add the `--instance-maintenance-policy` option to the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command. The following example set an instance maintenance policy on a new Auto Scaling group named `{{my-asg}}`.

```
aws autoscaling create-auto-scaling-group \
  --launch-template LaunchTemplateName={{my-launch-template}},Version='{{1}}' \
  --auto-scaling-group-name {{my-asg}} \
  --min-size {{1}} \
  --max-size {{10}} \
  --desired-capacity {{5}} \
  --default-instance-warmup {{20}} \
  --instance-maintenance-policy '{
      "MinHealthyPercentage": {{90}},
      "MaxHealthyPercentage": {{120}}
    }' \
  --vpc-zone-identifier "{{subnet-5e6example}},{{subnet-613example}},{{subnet-c93example}}"
```

------

------
#### [ Console ]

**To set an instance maintenance policy on an existing group (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. On the navigation bar at the top of the screen, choose the AWS Region that you created your Auto Scaling group in.

1. Select the check box next to the Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. On the **Details** tab, choose **Instance maintenance policy**, **Edit**.

1. To set an instance maintenance policy on the group, choose one of the available options:
   + **Launch before terminating**: A new instance must be provisioned first before an existing instance can be terminated. This is a good choice for applications that favor availability over cost savings.
   + **Terminate and launch**: New instances are provisioned at the same time your existing instances are terminated. This is a good choice for applications that favor cost savings over availability. It's also a good choice for applications that should not launch more capacity than is currently available.
   + **Custom policy**: This option lets you set up your policy with a custom minimum and maximum range for the amount of capacity that you want available when replacing instances. This can help you achieve the right balance between cost and availability.

1. For **Set healthy percentage**, enter values for one or both of the following fields. The enabled fields vary depending on the option that you chose in the preceding step.
   + **Min**: Sets the minimum healthy percentage that's required to proceed with replacing instances.
   + **Max**: Sets the maximum healthy percentage that's possible when replacing instances.

1. Expand the **View capacity during replacements based on your desired capacity** section to confirm how the values for **Min** and **Max** apply to your group. The exact values used depend on the desired capacity value, which will change if the group scales.

1. Choose **Update**.

------
#### [ AWS CLI ]

**To set an instance maintenance policy on an existing group (AWS CLI)**
Add the `--instance-maintenance-policy` option to the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command. The following example sets an instance maintenance policy on the specified Auto Scaling group.

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-asg}} \
  --instance-maintenance-policy '{
      "MinHealthyPercentage": {{90}},
      "MaxHealthyPercentage": {{120}}
    }'
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
