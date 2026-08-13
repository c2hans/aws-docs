---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-14.html
---

# ACCT.14 Enable Amazon GuardDuty
<a name="acct-14"></a>

Enable [Amazon GuardDuty](https://aws.amazon.com/guardduty/) in your AWS account. GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behavior. It analyzes [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) management events, [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) flow logs, and DNS query logs to identify threats such as compromised credentials, unauthorized resource access, and cryptocurrency mining. GuardDuty requires no infrastructure to deploy and no detection rules to write or maintain.

Enable GuardDuty in all supported AWS Regions. Doing so allows GuardDuty to generate findings about unauthorized or unusual activity, even in Regions that you do not actively use. This also allows GuardDuty to monitor AWS CloudTrail events for global AWS services such as IAM. Attackers frequently create resources in Regions where you have no workloads deployed, specifically because those Regions are less likely to be monitored. GuardDuty pricing is based on the volume of data analyzed, so Regions with no active workloads typically generate minimal cost. The cost difference between enabling GuardDuty only in Regions with active resources versus all supported Regions is typically negligible.

*Please review GuardDuty pricing to understand its consumption model: *[*https://aws.amazon.com/guardduty/pricing/*](https://aws.amazon.com/guardduty/pricing/) *If you decide to not enable GuardDuty, it will be important to be thorough with the permission restrictions recommend in ACCT.17.*

**To enable GuardDuty:**

1. Open the [GuardDuty console](https://console.aws.amazon.com/guardduty/).

1. Choose **Get started**.

1. On the **Welcome to GuardDuty** page, review the service permissions.

1. Choose **Enable GuardDuty**.

Review findings in the GuardDuty console and take action on high-severity findings first. For more information, see [Getting started with GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html) in the GuardDuty documentation.

**Note**
GuardDuty includes a 30-day free trial per Region when you enable it for the first time. After the free trial, you are charged based on the volume of data analyzed. For most early-stage startups, this cost is minimal. For more information, see [Amazon GuardDuty pricing](https://aws.amazon.com/guardduty/pricing/).
