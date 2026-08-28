---
source_url: https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/perform-detailed-monitoring.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Perform detailed monitoring
<a name="perform-detailed-monitoring"></a>

 End users of real-time voice and video applications expect the same level of performance as they achieve with traditional telephony services. So, when they experience issues with an application, it ends up hurting the provider’s reputation. To be proactive rather than reactive, it is imperative that detailed monitoring be deployed at every part of the system that serves end users.

![A diagram depicting using SIPp to monitor VoIP infrastructure .](http://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/images/using-sipp-to-monitor-voip.png)

 Many open source tools, such as [iPerf](https://iperf.fr/) or [SIPp](http://sipp.sourceforge.net/), and [VOIPMonitor](http://www.voipmonitor.org), are available to use in monitoring SIP/RTP traffic. In the preceding example, nodes running SIP in client and server modes are measuring SIP metrics such as Successful Calls and SIP Retransmits between all four US AWS Regions. These metrics can then be exported into Amazon CloudWatch using a custom script. Using CloudWatch, customers can create alarms on these custom metrics based on a certain threshold value. Automatic or manual remediation actions can then be taken based on the state of these CloudWatch alarms.

 For customers not wanting to allocate engineering resources needed to develop and maintain a custom monitoring system, many good VoIP monitoring solutions are available on the market, such as [ThousandEyes](https://www.thousandeyes.com). An example of a remediation action is changing the SIP routing based on increased SIP retransmits.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
