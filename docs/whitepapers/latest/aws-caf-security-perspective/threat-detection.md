---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-security-perspective/threat-detection.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Threat detection
<a name="threat-detection"></a>

**Note**
Understand security threats and detect malicious activity, data breaches, or other security events.

 Understanding the threats that are applicable to your organization and identifying the services and controls to implement is key to an effective threat detection program. This helps you identify possible threats early, reduces the dwell time of unauthorized users, and enables you to respond more quickly to mitigate the event.

## Start
<a name="threat-detection-start"></a>

 When creating *directive*, *preventative*, *detective*, and *responsive* controls, you should adhere to the governing controls and requirements relevant to your organization. Threat modeling can help you map and understand the severity and business criticality of components within a workload. You can then effectively address the risks and impacts, and identify the specific controls and mitigations that can be implemented. Establish a team of individuals responsible for monitoring and responding to events, tuning detections, and proactively looking for anomalous behavior. This team should be actively involved and consulted to review the architecture for enabling *threat detection* and *incident response.* It should provide the logging requirements needed for building detections and alerting. Log ingestion should be verified periodically to validate that all logs necessary for detection are enabled and available, log ingestion pipelines are functioning, and alerts are initiating as intended. A security review will provide insight into which types of logs should be collected and centralized to a restricted AWS account for effective threat monitoring and detection, including what applicable detective controls will generate findings (such as GuardDuty findings). Examples of such logs may include, but are not limited to:
+  Service-level logs, with alerting and associated automated response, including:
  +  [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html) logs, Command Line Interface and APIs
  +  [Amazon GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html)
  +  [Elastic Load Balancing logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html)
  +  [Amazon Route 53 resolver query logs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs.html)
  +  [Amazon S3 data event logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-examples) or [server access logs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html)
  +  [Virtual Private Cloud (VPC) Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
+  Host-level logs, including:
  +  Application specific logs, such as [web server logs](https://aws.amazon.com/blogs/mt/simplifying-apache-server-logs-with-amazon-cloudwatch-logs-insights/)
  +  Audit logs
  +  Endpoint detection logs
  +  System logs

 Enabling detective controls on an AWS account or across AWS Organizations should be carefully planned with scaling in mind. Use AWS Organizations functionalities built-in to [AWS Security Services](https://aws.amazon.com/products/security/) such as Amazon GuardDuty, AWS Config, and AWS Security Hub CSPM. This will provide the security teams the visibility into the services' functionality into each account, permitting them to audit their detection capabilities. Organizations should plan for how custom controls can be deployed and audited at scale, and provide teams the ability to audit those controls.

 Using automation for the deployment of detective controls and logging services will allow the threat detection team to match the growth as an organization expands and creates new accounts. Tools like [Assisted Log Enabler for AWS](https://aws.amazon.com/blogs/opensource/introducing-assisted-log-enabler-for-aws/) give threat detection teams the ability to enable and audit [AWS CloudTrail logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-examples.html), [Amazon Elastic Kubernetes Service (Amazon EKS) logs](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html), Amazon Route 53 resolver query logs, Elastic Load Balancing logs, Amazon S3 server access logs, and VPC Flow Logs across accounts, within a single account, or across AWS Organizations.

 Individuals responsible for threat detection should be trained and knowledgeable with hands-on experience in both the operation and security of [AWS Cloud Products](https://aws.amazon.com/products/?aws-products-all.sort-by=item.additionalFields.productNameLowercase&aws-products-all.sort-order=asc&awsf.re%3AInvent=*all&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all). This knowledge and experience will aid in understanding the shared responsibility across AWS Cloud services and how to build the most effective detective controls with those responsibilities in mind.

## Advance
<a name="threat-detection-advance"></a>

 At this stage, consider analyzing logs to identify configurations that do not follow best practices.

 When building new detections to proactively identify threats, use a dedicated testing environment. Teams can use DevOps methods for building detections with version control, backlog tracking, testing, and deployment. Apply a DevOps framework for the detection development process. This will promote the ability to fail fast and roll back to a known functioning version should an update or new detection have unintended effects.

 Detections are implemented at each layer of an application, including:
+  Operating system detection:
  +  Unauthorized software is installed
  +  Outdated software is installed
  +  Abnormal audit/system activity
+  Application detection:
  +  An SQL injection is performed against a web server
  +  A vulnerability in an application is exploited
  +  An application is leveraged for malicious purposes
+  Control plane detection:
  +  CloudTrail logs are disabled
  +  Amazon EC2 instance is deployed using an earlier or unauthorized [Amazon Machine Image](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/AMIs.html) (AMI)
  +  A [security group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) that allows all inbound and outbound traffic is created and applied to an EC2 instance
  +  An S3 bucket is made public

     Finally, close the loop by ensuring that any identified issues feed into your *lessons learned* mechanism so that corresponding preventative controls can be implemented or adjusted as required.

## Excel
<a name="threat-detection-excel"></a>

 Threat detection teams should exercise and test detections regularly through real-world scenarios and production environments to confirm detections are operating as intended. Incorporate lessons learned into the threat detection development process, as well as current and future architectures for detecting threats. To proactively identify threats, threat detection teams should implement and perform regular threat hunting (searching) throughout their AWS environments. This will allow the team to proactively identify and deploy new detections and measures otherwise unknown, further reducing dwell time of unauthorized users within an environment.

 The threat detection team should employ mechanisms to share artifacts and intelligence to inform and educate internal teams on the applicable threats. This will help internal development and operational teams build more informed and effective threat models to better protect and defend their environments. The threat detection team should also consider joining and participating in external threat intelligence sharing communities. They can contribute intelligence to the community and gain additional insights and data into the threats targeting their specific business, applications, and industry vertical.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
