---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/add-tags.html
---

# Tag your Auto Scaling groups
<a name="add-tags"></a>

When you add a tag to your Auto Scaling group, you can specify whether it should be added to instances launched in the Auto Scaling group. If you modify a tag, the updated version of the tag is added to instances launched in the Auto Scaling group after the change. If you create or modify a tag for an Auto Scaling group, these changes are not made to instances that are already running in the Auto Scaling group.

**Topics**
+ [Add or modify tags (console)](#add-tags-console)
+ [Add or modify tags (AWS CLI)](#add-tags-aws-cli)

## Add or modify tags (console)
<a name="add-tags-console"></a>

**To tag an Auto Scaling group on creation**
When you use the Amazon EC2 console to create an Auto Scaling group, you can specify tag keys and values on the **Add tags** page of the Create Auto Scaling group wizard. To propagate a tag to the instances launched in the Auto Scaling group, make sure that you keep the **Tag new instances** option for that tag selected. Otherwise, you can deselect it.

**To add or modify tags for an existing Auto Scaling group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to the Auto Scaling group.

   A split pane opens up in the bottom of the **Auto Scaling groups** page.

1. On the **Details** tab, choose **Tags**, **Edit**.

1. To modify existing tags, edit **Key** and **Value**.

1. To add a new tag, choose **Add tag** and edit **Key** and **Value**. You can keep **Tag new instances** selected to add the tag to the instances launched in the Auto Scaling group automatically, and deselect it otherwise.

1. When you have finished adding tags, choose **Update**.

## Add or modify tags (AWS CLI)
<a name="add-tags-aws-cli"></a>

The following examples show how to use the AWS CLI to add tags when you create Auto Scaling groups, and to add or modify tags for existing Auto Scaling groups.

**To tag an Auto Scaling group on creation**
Use the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command to create a new Auto Scaling group and add a tag, for example, **environment=production**, to the Auto Scaling group. The tag is also added to any instances launched in the Auto Scaling group.

```
aws autoscaling create-auto-scaling-group --auto-scaling-group-name {{my-asg}} \
  --launch-configuration-name {{my-launch-config}} --min-size {{1}} --max-size {{3}} \
  --vpc-zone-identifier "{{subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782}}" \
  --tags Key={{environment}},Value={{production}},PropagateAtLaunch=true
```

**To create or modify tags for an existing Auto Scaling group**
Use the [create-or-update-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-or-update-tags.html) command to create or modify a tag. For example, the following command adds the `Name=my-asg` and `costcenter=cc123` tags. The tags are also added to any instances launched in the Auto Scaling group after this change. If a tag with either key already exists, the existing tag is replaced. The Amazon EC2 console associates the display name for each instance with the name that is specified for the `Name` key (case-sensitive).

```
aws autoscaling create-or-update-tags \
  --tags ResourceId={{my-asg}},ResourceType=auto-scaling-group,Key=Name,Value={{my-asg}},PropagateAtLaunch=true \
  ResourceId={{my-asg}},ResourceType=auto-scaling-group,Key={{costcenter}},Value={{cc123}},PropagateAtLaunch=true
```

### Describe the tags for an Auto Scaling group (AWS CLI)
<a name="describe-tags-aws-cli"></a>

If you want to view the tags that are applied to a specific Auto Scaling group, you can use either of the following commands:
+ [describe-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-tags.html) – You supply your Auto Scaling group name to view a list of the tags for the specified group.

  ```
  aws autoscaling describe-tags --filters Name=auto-scaling-group,Values={{my-asg}}
  ```

  The following is an example response.

  ```
  {
      "Tags": [
          {
              "ResourceType": "auto-scaling-group",
              "ResourceId": "my-asg",
              "PropagateAtLaunch": true,
              "Value": "production",
              "Key": "environment"
          }
      ]
  }
  ```
+ [describe-auto-scaling-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html) – You supply your Auto Scaling group name to view the attributes of the specified group, including any tags.

  ```
  aws autoscaling describe-auto-scaling-groups --auto-scaling-group-name {{my-asg}}
  ```

  The following is an example response.

  ```
  {
      "AutoScalingGroups": [
          {
              "AutoScalingGroupName": "my-asg",
              "AutoScalingGroupARN": "{{arn}}",
              "LaunchTemplate": {
                  "LaunchTemplateId": "lt-0b97f1e282EXAMPLE",
                  "LaunchTemplateName": "my-launch-template",
                  "Version": "$Latest"
              },
              "MinSize": 1,
              "MaxSize": 5,
              "DesiredCapacity": 1,
              ...
              "Tags": [
                  {
                      "ResourceType": "auto-scaling-group",
                      "ResourceId": "my-asg",
                      "PropagateAtLaunch": true,
                      "Value": "production",
                      "Key": "environment"
                  }
              ],
              ...
          }
      ]
  }
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
