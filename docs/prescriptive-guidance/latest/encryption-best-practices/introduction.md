---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/introduction.html
---

# Encryption best practices and features for AWS services
<a name="introduction"></a>

*Kurt Kumar and Ken Beer, Amazon Web Services*

Encryption is a fundamental cybersecurity tool for protecting sensitive data in the digital age. As organizations increasingly rely on data to drive their operations, including generative AI deployments, safeguarding this valuable information through robust encryption practices is an essential component of a comprehensive data protection strategy. This guide can help you understand encryption principles and the encryption capabilities that AWS offers.

Modern cybersecurity threats include the risk of a *data breach*, which is when unauthorized access to your information assets results in the loss of data. Data is a business asset that is unique to each organization. It can include customer information, business plans, design documents, or code. Protecting the business means protecting its data.

Data encryption can help protect your business data even after a breach occurs. It provides a layer of defense against unintended disclosure. To access encrypted data in the AWS Cloud, users need permissions to use the key to decrypt and need permissions to use the service where the data resides. Without both of these permissions, users are unable to decrypt and view the data.

Generally, there are three types of data that you can encrypt. *Data in transit* is data that is actively moving through your network, such as between network resources. *Data at rest* is data that is stationary and dormant, such as data that is in storage. Examples include block storage, object storage, databases, archives, and Internet of Things (IoT) devices. *Data in use* refers to data that applications or services are actively processing or using. By securing data at the point of use, organizations can help mitigate the risks of unintended disclosure.

This guide discusses considerations and best practices for encrypting data in transit and data at rest. It also reviews the encryption features and controls that are available in many AWS services. You can implement these encryption recommendations at the service level in your AWS Cloud environments.

## Intended audience
<a name="intended-audience"></a>

This guide can be used by small, medium, and large organizations in both public and private sectors. Whether your organization is in the initial stages of assessing and implementing a data protection strategy or aiming to enhance existing security controls, the recommendations outlined in this guide are best suited for the following audiences:
+ Executive officers who formulate policies for their enterprise, such as chief executive officers (CEOs), chief technology officers (CTOs), chief information officers (CIOs), and chief information security officers (CISOs)
+ Technology officers who are responsible for setting up technical standards, such as technical vice presidents and directors
+ Business stakeholders and application owners who are responsible for:
  + Assessing risk posture, data classification, and protection requirements
  + Monitoring compliance with established organizational standards
+ Compliance, internal audit, and governance officers who are in charge of monitoring adherence to compliance policies, including statutory and voluntary compliance regimes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
