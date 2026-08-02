---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_incident_response_auto_contain.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC10-BP04 Automate containment capability
<a name="sec_incident_response_auto_contain"></a>

Automate containment and recovery of an incident to reduce response times and organizational impact.

Once you create and practice the processes and tools from your playbooks, you can deconstruct the logic into a code-based solution, which can be used as a tool by many responders to automate the response and remove variance or guess-work by your responders. This can speed up the lifecycle of a response. The next goal is to enable this code to be fully automated by being invoked by the alerts or events themselves, rather than by a human responder, to create an event-driven response. These processes should also automatically add relevant data to your security systems. For example, an incident involving traffic from an unwanted IP address can automatically populate an AWS WAF block list or Network Firewall rule group to prevent further activity.

![WAF WebACL logs flow through Kinesis Firehose , Lambda , and Event Bridge to update IPset.](http://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/images/aws-waf-automate-block.png)

*Figure 3: AWS WAF automate blocking of known malicious IP addresses.*

With an event-driven response system, a detective mechanism triggers a responsive mechanism to automatically remediate the event. You can use event-driven response capabilities to reduce the time-to-value between detective mechanisms and responsive mechanisms. To create this event-driven architecture, you can use AWS Lambda, which is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources for you. For example, assume that you have an AWS account with the AWS CloudTrail service enabled. If CloudTrail is ever disabled (through the `cloudtrail:StopLogging` API call), you can use Amazon EventBridge to monitor for the specific `cloudtrail:StopLogging` event, and invoke a Lambda function to call `cloudtrail:StartLogging` to restart logging.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Automate containment capability.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [AWS Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html)

 **Related videos:**
+  [Prepare for and respond to security incidents in your AWS environment](https://youtu.be/8uiO0Z5meCs)
