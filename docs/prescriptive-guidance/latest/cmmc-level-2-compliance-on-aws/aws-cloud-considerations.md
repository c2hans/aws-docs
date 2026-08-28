---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/aws-cloud-considerations.html
---

# AWS cloud considerations
<a name="aws-cloud-considerations"></a>

## Shared responsibility model
<a name="shared-responsibility-model.e2f4d3dd-145b-5c19-b8dc-95a8f4619f0e"></a>

Security and compliance are shared responsibilities between AWS and you. Under the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/), AWS is responsible for the security of the cloud infrastructure, and you are responsible for security in the cloud, including meeting CMMC requirements for your workloads. AWS maintains its own compliance certifications, including FedRAMP High authorization for AWS GovCloud (US) and FedRAMP Moderate authorization for US East/West commercial Regions. Through [AWS Artifact](https://aws.amazon.com/artifact/), you can access the AWS CMMC Customer Package, which documents the controls AWS implements on your behalf, helping reduce the number of controls you need to fully implement and evidence yourself.

### Control inheritance mode
<a name="control-inheritance-mode"></a>

The AWS CMMC CRM categorizes all 110 NIST SP 800-171 Rev. 2 requirements into three inheritance types:

|
|
| Inheritance type | Count | Description |
| --- |--- |--- |
| Inheritable | 21 | AWS satisfies the requirement entirely if implemented correctly. You must still document the inheritance in your SSP via the CRM. |
| Partial | 79 | Shared responsibility. AWS provides infrastructure-level controls; you must configure, operate, and evidence your portion. |
| Customer Only | 10 | No AWS service coverage. Requires your organizational policies, procedures, or non-AWS technology. |

The 21 inheritable controls include all 6 Physical Protection (PE) practices, 8 of 9 Media Protection (MP) practices, 5 Maintenance (MA) practices, and 2 Access Control (AC) practices. When you deploy on AWS these controls are inherited under the right conditions under the shared responsibility model. AWS maintains FedRAMP-authorized controls for these areas. You document this inheritance in your SSP and provide your assessor with the AWS CMMC Customer Package from AWS Artifact as evidence.

The 10 customer-only controls cannot be solved through AWS configuration alone:

|
|
| Control | Requirement | What you must implement |
| --- |--- |--- |
| AC.L2-3.1.8 | Unsuccessful logon attempts | Account lockout policy and mechanism |
| AC.L2-3.1.18 | Mobile device connection | Mobile device management policy |
| AC.L2-3.1.19 | Encrypt CUI on mobile devices | Mobile encryption enforcement |
| AC.L2-3.1.21 | Portable storage use | Removable media policy |
| IA.L2-3.5.7 | Password complexity | Password policy (may configure in IAM) |
| IA.L2-3.5.8 | Password reuse prohibition | Password history policy (may configure in IAM) |
| IA.L2-3.5.9 | Temporary password use | Temporary credential procedures |
| SC.L2-3.13.7 | Split tunneling prevention | VPN/network configuration |
| SC.L2-3.13.12 | Collaborative device control | Policy for cameras, microphones, displays |
| SC.L2-3.13.14 | Voice/video protection | Encryption for communications |

For the 79 partially inheritable controls, the CRM specifies what AWS provides and what you must implement. When building your SSP control narratives, reference the CRM "AWS Implementation Details" and "Customer Implementation Expectations" columns to accurately delineate responsibilities.

### Automation
<a name="automation"></a>

With automation, you can implement infrastructure and application changes without manual intervention. You should also automate the security and compliance controls to the greatest extent possible so that evidence collection and monitoring operate continuously alongside your workloads. Automation also helps detect when controls drift from their intended configuration so that you can implement remediation steps in near real time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
