---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/principle-3-separation-between-users.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Principle 3: Separation between users
<a name="principle-3-separation-between-users"></a>

****
 A malicious or compromised user of the service should not be able to affect the service or data of another.

 **Applicable risk classes:** All

****
 The Service User Should undertake end-to-end penetration testing of the solution.
+  **Separation of customer environments** — AWS provides robust boundaries between different customer accounts and the resources they contain. The means by which this is accomplished are detailed in the SOC 2 reports for the relevant services, available to customers under nondisclosure agreement (NDA).

   AWS Customers may also benefit from the advanced isolation properties of the [Nitro System](https://pages.awscloud.com/The-Nitro-Project-Next-Generation-EC2-Infrastructure_0119-CMP_OD.html?trk=JB), including the Nitro Security Chip, hardware EBS processing, hardware support for the software-defined network inside each VPC, and hardware support for local storage. The Nitro system builds hardware implementations of components that are typically found in software-based virtualization technology, offloading the work from the processors used by customers, increasing performance, and raising the bar for security.
+  **Penetration testing** — AWS customers can perform penetration testing as a risk identification measure, but for certain services, they must notify AWS before doing so. Otherwise, the test may be regarded by the automated threat response systems as a genuine attack, which may result in action that has a negative impact on customer systems.

   For details of current policy and procedures, see [Penetration Testing](https://aws.amazon.com/security/penetration-testing/).

****
 The Service User should implement a GPG13 compliant Protective Monitoring solution.

 AWS offers various monitoring services enabling customers to implement protective and holistic solutions in line with businesses risks and expectations and tailored for specific applications or system risks.

 These solutions can cover monitoring phases such as event collection, alerting and notification, compliance, management and operational reporting, incident response, and forensics, in addition to monitoring infrastructure-related controls such as integrity protection and retention.

 A high-level overview of the [Native AWS Security-Logging Capabilities](https://aws.amazon.com/answers/logging/aws-native-security-logging-capabilities/) can be found on the associated AWS Answers page.

 [Amazon GuardDuty](https://aws.amazon.com/guardduty/) is a threat detection service that continuously monitors for malicious or unauthorised behaviour to help customers protect customer AWS accounts and workloads.

 [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) provides a comprehensive view of high-priority security alerts and compliance status across AWS accounts.

 The services above can be combined with [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS) to receive notifications, and with AWS Lambda and AWS System Manager for automated alert responses.

 For more information on protective monitoring, see [Section 5.3: Protective monitoring](principle-5-operational-security.md#section-5.3-protective-monitoring) and [Section 5.4: Incident management](principle-5-operational-security.md#section-5.4-incident-management) in this document.
