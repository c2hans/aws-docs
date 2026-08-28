---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-policy.html
---

# Step 1: Create the AWS IoT policy
<a name="iot-moisture-policy"></a>

Create an AWS IoT policy that allows your Raspberry Pi to connect and send messages to AWS IoT.

1. In the [AWS IoT console](https://console.aws.amazon.com/iot), if a **Get started** button appears, choose it. Otherwise, in the navigation pane, expand ** Security**, and then choose **Policies**.

1. If a **You don't have any policies yet** dialog box appears, choose **Create a policy**. Otherwise, choose **Create**.

1. Enter a name for the AWS IoT policy (for example, **MoistureSensorPolicy**).

1. In the **Add statements** section, replace the existing policy with the following JSON. Replace {{region}} and {{account}} with your AWS Region and AWS account number.
****

   ```
   {
       "Version":"2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "iot:Connect",
               "Resource": "arn:aws:iot:{{us-east-1}}:123456789012:client/RaspberryPi"
           },
           {
               "Effect": "Allow",
               "Action": "iot:Publish",
               "Resource": [
                   "arn:aws:iot:{{us-east-1}}:123456789012:topic/$aws/things/RaspberryPi/shadow/update",
                   "arn:aws:iot:{{us-east-1}}:123456789012:topic/$aws/things/RaspberryPi/shadow/delete",
                   "arn:aws:iot:{{us-east-1}}:123456789012:topic/$aws/things/RaspberryPi/shadow/get"
               ]
           },
           {
               "Effect": "Allow",
               "Action": "iot:Receive",
               "Resource": [
                   "arn:aws:iot:{{us-east-1}}:123456789012:topic/$aws/things/RaspberryPi/shadow/update/accepted",
                   "arn:aws:iot:{{us-east-1}}:123456789012:topic/$aws/things/RaspberryPi/shadow/delete/accepted",
                   "arn:aws:iot:{{us-east-1}}:123456789012:topic/$aws/things/RaspberryPi/shadow/get/accepted",
                   "arn:aws:iot:{{us-east-1}}:123456789012:topic/$aws/things/RaspberryPi/shadow/update/rejected",
                   "arn:aws:iot:{{us-east-1}}:123456789012:topic/$aws/things/RaspberryPi/shadow/delete/rejected"
               ]
           },
           {
               "Effect": "Allow",
               "Action": "iot:Subscribe",
               "Resource": [
                   "arn:aws:iot:{{us-east-1}}:123456789012:topicfilter/$aws/things/RaspberryPi/shadow/update/accepted",
                   "arn:aws:iot:{{us-east-1}}:123456789012:topicfilter/$aws/things/RaspberryPi/shadow/delete/accepted",
                   "arn:aws:iot:{{us-east-1}}:123456789012:topicfilter/$aws/things/RaspberryPi/shadow/get/accepted",
                   "arn:aws:iot:{{us-east-1}}:123456789012:topicfilter/$aws/things/RaspberryPi/shadow/update/rejected",
                   "arn:aws:iot:{{us-east-1}}:123456789012:topicfilter/$aws/things/RaspberryPi/shadow/delete/rejected"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "iot:GetThingShadow",
                   "iot:UpdateThingShadow",
                   "iot:DeleteThingShadow"
               ],
               "Resource": "arn:aws:iot:{{us-east-1}}:123456789012:thing/RaspberryPi"
           }
       ]
   }
   ```

1. Choose **Create**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
