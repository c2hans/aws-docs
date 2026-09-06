---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-semicon-workloads/aws-security-services.html
---

# AWS security services for semiconductor development environments
<a name="aws-security-services"></a>

AWS has developed security services designed to protect your workloads and applications in the AWS Cloud. These services can help protect any type of workload operating in the cloud, not just semiconductor workloads. By using these AWS services, companies can establish strong preventative and detective controls, monitor their security posture in near real-time, and quickly remediate security risks and incidents as they arise. These services are capable of automatically scaling with the environment as it grows in order to maintain coverage and the established security posture. Also, while these services might focus on specific functionality, they support a common messaging bus known as [Amazon EventBridge](https://aws.amazon.com/eventbridge/) so that you can integrate the services and automatically response to security risks.

The following AWS services and features can help you manage access and policies, detect and respond to security risks and events, and implement monitoring and logging in your AWS environment:
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) helps you audit the governance, compliance, and operational risk of your AWS account.
+ [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) is a continuous security monitoring service that analyzes and processes logs to identify unexpected and potentially unauthorized activity in your AWS environment.
+ [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) is a vulnerability management service that continuously scans your AWS workloads for software vulnerabilities and unintended network exposure.
+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides a comprehensive view of your security state in AWS. It also helps you check your AWS environment against security industry standards and best practices.
+ [Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) automatically centralizes security data from cloud, on-premises, and custom sources into a purpose-built data lake stored in your AWS account. You can query and analyze this security data to discover trends and anomalies.
+ [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) are a type of policy in AWS Organizations that helps you centrally manage the use of AWS services across multiple accounts.
+ [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) is a feature of Amazon Virtual Private Cloud (Amazon VPC) that captures information about the IP traffic going to and from network interfaces in your VPC. You can use this data to troubleshoot and respond to incidents.
