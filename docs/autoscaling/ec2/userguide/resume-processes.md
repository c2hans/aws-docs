---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/resume-processes.html
---

# Resume processes
<a name="resume-processes"></a>

To resume a suspended process for an Auto Scaling group, use one of the following methods:

------
#### [ Console ]

**To resume a suspended process**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to the Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. On the **Details** tab, choose **Advanced configurations**, **Edit**.

1. For **Suspended processes**, remove the suspended process.

1. Choose **Update**.

------
#### [ AWS CLI ]

To resume a suspended process, use the following [resume-processes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/resume-processes.html) command.

```
aws autoscaling resume-processes --auto-scaling-group-name {{my-asg}} --scaling-processes {{HealthCheck}}
```

To resume all suspended processes, omit the `--scaling-processes` option, as follows.

```
aws autoscaling resume-processes --auto-scaling-group-name {{my-asg}}
```

------
