---
source_url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/automated-infrastructure-activities.html
---

# Automated infrastructure activities
<a name="automated-infrastructure-activities"></a>

 Tags can be used in a wide range of automation activities when managing infrastructure. Use of [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/index.html), for example, will allow you to manage automations and runbooks on resources specified by the defined key-value pair you create. For managed nodes, you could define a set of tags to track or target nodes by operating system and environment. You could then run an update script for all nodes in a group or review the status of those nodes. [Systems Manager Resources](https://docs.aws.amazon.com/systems-manager/latest/userguide/taggable-resources.html) can also be tagged to further refine and track your automated activities.

 Automating the start and stop lifecycle of environment resources can provide a significant cost reduction to any organization. [Instance scheduler on AWS](https://aws.amazon.com/solutions/implementations/instance-scheduler/) is an example of a solution that can start and stop Amazon EC2 and Amazon RDS instances when they are not required. For example, developer environments utilizing Amazon EC2 or Amazon RDS instances that are not required to be running on weekends are not utilizing the cost saving potential that the shutting down of those instances can provide. By analyzing the needs of teams and their environments, and properly tagging these resources to automate their management, you can utilize your budget effectively.

 *An example schedule tag used by instance scheduler on an Amazon EC2 instance:*

```
{
    "Tags": [
        {
            "Key": "Schedule",
            "ResourceId": "i-1234567890abcdef8",
            "ResourceType": "instance",
            "Value": "mon-9am-fri-5pm"
        }
    ]
}
```
