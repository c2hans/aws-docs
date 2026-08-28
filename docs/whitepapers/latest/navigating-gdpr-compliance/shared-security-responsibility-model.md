---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/shared-security-responsibility-model.html
---

# Shared Security Responsibility Model
<a name="shared-security-responsibility-model"></a>

AWS follows a shared responsibility model for security and compliance. Under this model, AWS is responsible for the "Security OF the Cloud". This includes protecting the infrastructure that runs AWS services, such as data centers, networks, hardware, and the foundational software that supports services like [Amazon Simple Storage Service (Amazon S3](https://aws.amazon.com/s3/)) and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/).

Customers are responsible for "Security IN the Cloud". This means configuring and managing the security of the AWS services they use. Responsibilities include managing user access, encrypting data, setting up monitoring, and implementing technical and organizational measures to meet their own compliance needs, including under the GDPR.

Under the GDPR, this model remains unchanged. AWS acts as a processor or sub-processor for customer data, while customers act as controllers or processors and retain full control over how personal data is collected, used, and secured within their AWS environment. Understanding this distinction is essential for customers to assess their compliance needs, especially when conducting data protection impact assessments or evaluating international data transfers.

For more information, see the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).

## **AWS and Law Enforcement Information Requests**
<a name="aws-and-law-enforcement-information-requests"></a>

In line with its commitments under the [Supplementary Addendum](https://d1.awsstatic.com/Supplementary_Addendum_to_the_AWS_GDPR_DPA.pdf) to the [AWS DPA](https://d1.awsstatic.com/legal/aws-dpa/aws-dpa.pdf), If AWS receives a legally valid and binding request for customer data, AWS reviews the request to confirm its legal sufficiency and appropriateness. Wherever possible, AWS will redirect the requesting authority to contact the customer directly.

If AWS is legally compelled to disclose customer data, it will notify the customer before providing any data, unless legally prohibited from doing so. AWS challenges requests that are overly broad, inappropriate, or conflict with applicable law. AWS will disclose only the minimum amount of data necessary to comply with the request.

These commitments are part of AWS's broader approach to privacy and customer control. AWS publishes regular [Information Request Reports](https://aws.amazon.com/compliance/data-privacy-faq/) (e.g., [January – June 2025](https://d1.awsstatic.com/Security/pdfs/Amazon_AWS_Information_Request_Report_H1_2025.pdf)) summarizing the number and type of requests received. The full policy and process for Law Enforcement is available in the AWS [Law Enforcement Guidelines](https://d1.awsstatic.com/certifications/Amazon_LawEnforcement_Guidelines.pdf).

Customers can rely on these commitments as part of their own compliance assessments, including for international data transfers and risk-based evaluations under the GDPR.

## **Data Protection Impact Assessments (DPIA) Support**
<a name="data-protection-impact-assessments-dpia-support"></a>

AWS customers, as controllers, are responsible for determining when a Data Protection Impact Assessment (DPIA) is required under Article 35 of the GDPR and for conducting such DPIA. AWS supports customers by providing tools and documentation to help identify and mitigate risks, including:
+ [Amazon Macie](https://aws.amazon.com/macie) for sensitive data discovery and classification;
+ [AWS CloudTrail](https://aws.amazon.com/cloudtrail) for comprehensive logs of activity;
+ [AWS Security Hub](https://aws.amazon.com/security-hub/) for centralized security and compliance insights;
+ [AWS Artifact](https://aws.amazon.com/artifact/) for on-demand compliance reports; and
+ [AWS Organizations](https://aws.amazon.com/organizations/) for multi-account management capabilities.
+ In line with the shared responsibility model, AWS secures the infrastructure and necessary tooling, while customers are responsible for determining when a DPIA is necessary and conducting the assessment in accordance with GDPR requirements.

## **Data Transfer Impact Assessment (DTIA) Support**
<a name="data-transfer-impact-assessment-dtia-support"></a>

Customers, as controllers, must conduct their own Data Transfer Impact Assessments (DTIAs) for international data transfers. In line with the shared responsibility model, AWS supports customers by providing the necessary tools and resources for such transfers, but does not conduct the assessments.

Customers can use AWS services with confidence that their data remains in the AWS Region they select. Only a small number of AWS services involve the transfer of customer data, for example, to develop and improve those services, where you can opt-out of the transfer, or because the transfer is an essential part of the service (such as a content delivery service). AWS's systems are designed to prevent remote access by AWS personnel to customer data unless specifically requested by the customer or required by law. More information is available on the "[Privacy Features of AWS Services](https://aws.amazon.com/compliance/privacy-features/)" webpage.

[AWS Control Tower](https://aws.amazon.com/controltower/) and [regional](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/?nc1=h_ls) services enable customers to implement strict data residency controls. Supplementary measures include strong encryption controls through [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/) and [AWS CloudHSM](https://aws.amazon.com/cloudhsm/), robust access controls through [AWS Identity and Access Management (AWS IAM)](https://aws.amazon.com/iam/) and comprehensive logging through [AWS CloudTrail](https://aws.amazon.com/cloudtrail).

To facilitate international data transfers, AWS also provides the appropriate data transfer mechanisms, such as the SCCs, which are part of the AWS Service Terms and incorporated by reference into the AWS DPA to validate data transfers from the EEA to countries not recognized by the European Commission as providing an adequate level of protection for personal data subject to GDPR. AWS has also certified to the EU-US Data Privacy Framework (DPF) and adheres to the DPF Principles, providing another relevant transfer mechanism. You can view the AWS DPF certification [here](https://www.dataprivacyframework.gov/list). Please note that to locate the certification, search for “Amazon” in the search bar as AWS is one of the covered entities under the Amazon.com, Inc. certification. For more detailed guidance on international data transfers, please see the Annex “AWS Customer EU Data Transfer Assessment Guide” below.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
