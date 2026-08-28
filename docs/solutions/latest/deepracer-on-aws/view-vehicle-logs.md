---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/view-vehicle-logs.html
---

# View vehicle logs
<a name="view-vehicle-logs"></a>

Your AWS DeepRacer vehicle logs operational events that can be helpful for troubleshooting issues encountered in running your vehicle. There are two types of AWS DeepRacer vehicle logs:
+ The system event log keeps track of operations taking place in the vehicle’s computer operating system, such as process managing, Wi-Fi connecting or password reset events.
+ The robot operating system logs record statuses of operations taking place in the vehicle’s operating system node for robotic operations, including vehicle driving, video streaming and policy inferencing operations.

To view the device logs, follow the steps below.

 **To view your AWS DeepRacer vehicle logs**

1. With your AWS DeepRacer vehicle connected to the Wi-Fi network, follow the instructions to sign into the vehicle’s device control console.

1. Choose **Logs** from the device console’s main navigation pane.

1. To view the system events, scroll down the event list under **System event log**.
![System event log display](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/operatingthevehicle-system-event-log.png)

1. To view the robot operating system events, scroll down the event list under **Robot operating system log**.
![Robot operating system log display](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/operatingthevehicle-robot-os-log.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
