---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_detect_investigate_events_auto_response.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC04-BP03 Automate response to events
<a name="sec_detect_investigate_events_auto_response"></a>

 Using automation to investigate and remediate events reduces human effort and error, and allows you to scale investigation capabilities. Regular reviews will help you tune automation tools, and continuously iterate.

In AWS, investigating events of interest and information on potentially unexpected changes into an automated workflow can be achieved using Amazon EventBridge. This service provides a scalable rules engine designed to broker both native AWS event formats (such as AWS CloudTrail events), as well as custom events you can generate from your application. Amazon GuardDuty also allows you to route events to a workflow system for those building incident response systems (AWS Step Functions), or to a central Security Account, or to a bucket for further analysis.

Detecting change and routing this information to the correct workflow can also be accomplished using AWS Config Rules and [Conformance Packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html). AWS Config detects changes to in-scope services (though with higher latency than EventBridge) and generates events that can be parsed using AWS Config Rules for rollback, enforcement of compliance policy, and forwarding of information to systems, such as change management platforms and operational ticketing systems. As well as writing your own Lambda functions to respond to AWS Config events, you can also take advantage of the [AWS Config Rules Development Kit](https://github.com/awslabs/aws-config-rdk), and a [library of open source](https://github.com/awslabs/aws-config-rules) AWS Config Rules. Conformance packs are a collection of AWS Config Rules and remediation actions you deploy as a single entity authored as a YAML template. A [sample conformance pack template](https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-wa-Security-Pillar.html) is available for the Well-Architected Security Pillar.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Implement automated alerting with GuardDuty: GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts and workloads. Turn on GuardDuty and configure automated alerts.
+  Automate investigation processes: Develop automated processes that investigate an event and report information to an administrator to save time.
  + [ Lab: Amazon GuardDuty hands on ](https://hands-on-guardduty.awssecworkshops.com/)

## Resources
<a name="resources"></a>

 **Related documents:**
+ [AWS Answers: Centralized Logging ](https://aws.amazon.com/answers/logging/centralized-logging/)
+  [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
+ [ Amazon CloudWatch ](https://aws.amazon.com/cloudwatch/)
+  [Amazon EventBridge ](https://aws.amazon.com/eventbridge)
+ [ Getting started: Amazon CloudWatch Logs ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_GettingStarted.html)
+  [Security Partner Solutions: Logging and Monitoring](https://aws.amazon.com/security/partner-solutions/#logging-monitoring)
+ [ Setting up Amazon GuardDuty ](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html)

 **Related videos:**
+ [ Centrally Monitoring Resource Configuration and Compliance ](https://youtu.be/kErRv4YB_T4)
+  [Remediating Amazon GuardDuty and AWS Security Hub CSPM Findings ](https://youtu.be/nyh4imv8zuk)
+ [ Threat management in the cloud: Amazon GuardDuty and AWS Security Hub CSPM](https://youtu.be/vhYsm5gq9jE)

 **Related examples:**
+  [Lab: Automated Deployment of Detective Controls ](https://wellarchitectedlabs.com/Security/200_Automated_Deployment_of_Detective_Controls/README.html)
