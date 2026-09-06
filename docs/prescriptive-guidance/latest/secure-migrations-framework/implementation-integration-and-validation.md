---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-migrations-framework/implementation-integration-and-validation.html
---

# Security implementation, integration, and validation
<a name="implementation-integration-and-validation"></a>

After mapping out your security, risk, and compliance requirements, the next domain is *security implementation, integration, and validation*. Based on the identified requirements, choose appropriate security controls and measures to mitigate risks effectively. This might include encryption, access controls, intrusion detection systems, or firewalls. Integrate security solutions, such as intrusion detection and prevention systems, endpoint protection, and identity management, into the existing IT infrastructure in order to provide comprehensive security coverage. Conduct regular security assessments, including vulnerability scanning, penetration testing, and code reviews, to validate the effectiveness of security controls and identify weaknesses or gaps. By focusing on security implementation, integration, and validation, organizations can strengthen their security posture, reduce the likelihood of security breaches, and demonstrate compliance with regulatory requirements and industry standards.

## Implementation
<a name="implementation"></a>

First, update the documentation for your current security, risk and compliance threshold or appetite. This allows you to implement the planned security and compliance requirements, controls, policies, and tooling in the cloud. This step is needed only if you have an existing risk register and appetite defined, which would have been identified during the discovery workshops.

Next, you implement the planned security and compliance requirements, controls, policies, and tooling in the cloud. We recommend that you implement these in the following order: infrastructure, AWS services, operating system, and then application or database. Use the information in the following table to make sure that you've addressed all required areas of security and compliance.

|
|
| Area | Security and compliance requirements |
| --- |--- |
| Infrastructure | + AWS account+ Landing zonePreventative controlsDetective controls<br />+ Network segmentation+ Access control+ Encryption+ Logging, monitoring, and alerting |
| AWS services | + AWS service configuration+ InstancesStorageNetwork<br />+ Access control+ Encryption+ Updates and patches+ Logging, monitoring, and alerting |
| Operating system | + Antivirus+ Malware and worm protection+ Configuration+ Network protection+ Access control+ Encryption+ Updates and patches+ Logging, monitoring, and alerting |
| Application or database | + Configuration+ Code and schema+ Access control+ Encryption+ Updates and patches+ Logging, monitoring, and alerting |

## Integration
<a name="integration"></a>

Security implementation often requires integration with the following:
+ **Networking** – Networking within and external to the AWS Cloud
+ **Hybrid IT landscape **– IT environments other than the AWS Cloud, such as on premises, public clouds, private clouds, and colocations
+ **External software or services **– Software and services that are managed by independent software vendors (ISVs) and are not hosted in your environment.
+ **Cloud operating model services** – AWS cloud operating model services that provide DevSecOps capabilities.

During the assess phase of your migration project, use discovery tools, existing documentation, or application interview workshops to identify and confirm these security integration points. When designing and implementing the workloads in the AWS Cloud, establish these integrations according to the security and compliance policies and processes that you defined during the mapping workshops.

## Validation
<a name="validation"></a>

After implementation and integration, the next activity is to validate the implementation. You make sure that the setup is aligned to AWS best practices for security and compliance. We recommend that you validate security from two coverage areas:
+ **Workload-specific vulnerability assessment and penetration testing **- Validate the operating system, application, database or network security of workloads that run on AWS services. In order to conduct these validations, use existing tools and test scripts. It is important to comply to the [AWS penetration testing customer support policy](https://aws.amazon.com/security/penetration-testing/) when carrying out these assessments.
+ **AWS** **security best practice validation** - Validate whether your AWS implementation complies to the AWS Well Architected Framework and other selected benchmarks, such as the Center for Internet Security (CIS). For this validation, you can use tools and services such as [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html), [Prowler](https://github.com/prowler-cloud/prowler/#requirements-and-installation) (GitHub), [AWS Service Screener](https://github.com/aws-samples/service-screener-v2) (GitHub), or [AWS Self-Service Security Assessment](https://github.com/awslabs/aws-security-assessment-solution) (GitHub).

It is important to document and communicate all security and compliance findings to the security team and leaders. Standardize reporting templates and use them to facilitate the communication to the respective security stakeholder. Document all exceptions made during finding remediation and make sure that the respective security stakeholders sign off.
