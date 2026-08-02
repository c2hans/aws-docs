---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/establish-logging-monitoring-set-up.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Establish logging and monitoring set up
<a name="establish-logging-monitoring-set-up"></a>

Observability in your network is critical to maintaining optimal performance and mitigating risks. Network logs contain information like IP addresses, ports, protocols, and the kind of traffic being sent through your infrastructure that allows you to understand how your network is operating. Network logs, including application traffic for payload inspection, can be used to identify and perform corrective actions when unauthorized or malicious traffic is discovered. Network logs can also be used to troubleshoot network issues including connectivity and performance. Centralizing the network logs for analysis will help you reduce the complexity of a solution that works across all the devices generating traffic and logs in your network. Another benefit of centralizing these logs is the *ease of use* of a solution that can analyze traffic to identify patterns monitoring your network, and to perform proactive and reactive remediation actions.

During peak traffic and load for your workloads, your underlying infrastructure needs to be resilient and deliver the expected performance for your users. We recommend that you collect performance metrics of your infrastructure, that can help you identify if network is optimized correctly and adjust as needed to enhance its performance. In cloud environments, all these metrics can be pushed to same monitoring dashboard and from single location basically you are monitoring your entire network and performance. These dashboards can also implement alerts and execute different automations based on the data collected when unusual activity is detected. This helps IT teams to reduce the time to remediate events identified in your network, and avoiding issues with your workloads.
