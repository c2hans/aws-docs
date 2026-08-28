---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/security-mgmt.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Security management
<a name="security-mgmt"></a>

AWS Managed Services (AMS) security management is the process by which AMS identifies an organization's assets and implements policies and procedures to protect those assets.

**Note**
AMS now has a change type (CT), Deployment \| Advanced stack components \| ACM certificate with additional SANs \| Create (ct-3l14e139i5p50), that you can use to submit a request for an AWS Certificate Manager certificate. For information, see [AWS::CertificateManager::Certificate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html). This CT provides for the creation of additional subject alternative name (SAN).

To better understand general AWS security, see [Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/).

AMS categorizes security risks as follows:
+ Known risks detected by anti-malware, which the malware mitigation process handles.
+ Security events including access breaches, which the security event management process handles.

**Topics**
+ [Data protection in AMS](sec-data-protect.md)
+ [Identity and access management](sec-iam.md)
+ [Security Incident Response in AMS](security-incident-response.md)
+ [Change request security reviews in AMS Advanced](ams-sec-change-request-review.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
