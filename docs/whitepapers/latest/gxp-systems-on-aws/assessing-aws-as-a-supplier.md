---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/assessing-aws-as-a-supplier.html
---

# Assessing AWS as a supplier
<a name="assessing-aws-as-a-supplier"></a>

 This section of the whitepaper provides information and insights into AWS to assist with a supplier assessment.

## About AWS
<a name="about-aws"></a>

 In 2006, AWS began offering on-demand IT infrastructure services to businesses in the form of web services with pay-as-you-go pricing. Today, AWS provides highly reliable, scalable, low-cost cloud that powers hundreds of thousands of businesses in countries around the world. Using AWS, businesses no longer need to plan for and procure servers and other IT infrastructure weeks or months in advance. Instead, they can instantly spin up hundreds or thousands of servers in minutes and deliver results faster. Offering over 200 fully featured services from data centers globally, AWS gives you the ability to take advantage of a broad set of global cloud-based products including compute, storage, databases, networking, security, analytics, machine learning, generative AI, mobile, developer tools, management tools, Internet of Things (IoT), media services, and enterprise applications. The rapid pace of innovation by AWS allows you to focus on what's most important to you and your end users without the undifferentiated heavy lifting.

## AWS Healthcare and Life Sciences
<a name="aws-healthcare-and-life-sciences"></a>

 AWS started its dedicated Healthcare and Life Sciences (HCLS) Practice in 2014 in response to the growing demand for an experienced and reliable life sciences cloud industry leader. Today, the AWS Healthcare and Life Sciences Practice team consists of members that have been in the industry on average for over 20 years and had previous titles such as Chief Medical Officer, Chief Digital Officer, Physician, Radiologist, and Researcher among many others. The AWS Healthcare and Life Sciences practice serves a large ecosystem of HCLS customers, including pharmaceutical, biotechnology, medical device, genomics, health tech, start-ups, university and government institutions, in addition to healthcare payers and providers. A full list of customer case studies can be found at [Healthcare & Life Sciences Case Studies](https://aws.amazon.com/health/case-studies/).

 In addition to the resources available within the HCLS practice at AWS, you can also work with AWS Life Sciences Competency Partners to drive innovation and improve efficiency across the life sciences value chain including cost-effective storage and compute capabilities, advanced analytics, and patient personalization mechanisms. AWS Life Sciences Competency Partners have demonstrated technical expertise and customer success in building life science solutions on AWS. A full list of AWS Life Sciences Competency Partners can be found at [AWS Life Sciences Competency Partners](https://aws.amazon.com/health/life-sciences/partner-solutions/).

## AWS services
<a name="aws-services"></a>

 AWS delivers a scalable cloud computing platform with high availability and dependability, providing the tools that enable you to run a wide range of applications. Helping to protect the confidentiality, integrity, and availability of our customers' systems and data is of the utmost importance to AWS, as is maintaining customer trust and confidence.

 Similar to other general-purpose IT products such as operating systems and database engines, AWS offers commercial off-the-shelf (COTS) IT services according to IT quality and security standards such as ISO, NIST, SOC, and many others. For the purposes of this paper, we will use the definition of COTS in accordance with the definition established by FedRAMP, a United States government-wide program for procurement and security assessment. FedRAMP references the US Federal Acquisition Regulation (FAR) for its definition of COTS, which outlines COTS items as:
+ Products or services that are offered and sold competitively in substantial quantities in the commercial marketplace based on an established catalog.
+ Offered without modification or customization.
+ Offered under standard commercial terms and conditions.

 Under GAMP guidelines (such as GAMP 5: A Risk-Based Approach to Compliant GxP Computerized Systems), organizations implementing GxP-compliant environments will need to categorize AWS services using respective GAMP software and hardware categories (for example, Software Category 1 for infrastructure software, including operating systems, database managers, and security software or Category 5 for custom or bespoke software). Most often, organizations using AWS services for validated applications will categorize them under Software Category 1.

 AWS offers products falling into several categories. The following is a subset of those AWS offerings spanning Compute, Storage, Database, Networking and Content Delivery, Security and Compliance, and Machine Learning. A later section of this whitepaper, AWS Products in GxP Systems, will provide information to assist you in using AWS services to implement your GxP-compliant environments.

**Subset of AWS offerings by group**

| Group | AWS products |
| --- | --- |
| Compute | [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/), [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/), [Amazon Elastic Container Registry (Amazon ECR)](https://aws.amazon.com/ecr/), [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/), [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/), [Amazon Lightsail](https://aws.amazon.com/lightsail/), [AWS Billing and Cost Management](https://aws.amazon.com/batch/), [https://aws.amazon.com/elasticbeanstalk/](https://aws.amazon.com/elasticbeanstalk/), [https://aws.amazon.com/fargate/](https://aws.amazon.com/fargate/), [Lambda](https://aws.amazon.com/lambda/), [https://aws.amazon.com/outposts/](https://aws.amazon.com/outposts/), [AWS Serverless Application Model (AWS SAM)](https://aws.amazon.com/sam/), [AWS Wavelength](https://aws.amazon.com/wavelength/), [AWS App Runner](https://aws.amazon.com/apprunner/) |
| Storage | [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/), [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/), [Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/), [https://aws.amazon.com/fsx/lustre/](https://aws.amazon.com/fsx/lustre/), [Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/), [https://aws.amazon.com/s3/storage-classes/glacier/](https://aws.amazon.com/s3/storage-classes/glacier/), [AWS Backup](https://aws.amazon.com/backup/), [AWS Snow Family](https://aws.amazon.com/snowball/), [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/), [AWS Storage Gateway](https://aws.amazon.com/storagegateway/), [CloudEndure Disaster Recovery](https://aws.amazon.com/cloudendure-disaster-recovery/) |
| Database | [Amazon Aurora](https://aws.amazon.com/rds/aurora/), [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), [Amazon DocumentDB (with MongoDB compatibility)](https://aws.amazon.com/documentdb/), [Porting Assistant for .NET](https://aws.amazon.com/elasticache/), [Amazon Keyspaces](https://aws.amazon.com/keyspaces/), [https://aws.amazon.com/neptune/](https://aws.amazon.com/neptune/), [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/), [Amazon Redshift](https://aws.amazon.com/redshift/), [Amazon Timestream](https://aws.amazon.com/timestream/), [AWS Database Migration Service (AWS DMS)](https://aws.amazon.com/dms/) |
| Networking and Content Delivery | [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/), [https://aws.amazon.com/api-gateway/](https://aws.amazon.com/api-gateway/), [Amazon CloudFront](https://aws.amazon.com/cloudfront/), [Amazon Route 53](https://aws.amazon.com/route53/), [AWS PrivateLink](https://aws.amazon.com/privatelink/), [AWS App Mesh](https://aws.amazon.com/app-mesh/), [AWS Cloud Map](https://aws.amazon.com/cloud-map/), [https://aws.amazon.com/directconnect/](https://aws.amazon.com/directconnect/), [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/), [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/), [Elastic Load Balancing](https://aws.amazon.com/elb/), [AWS Private 5G](https://aws.amazon.com/private5g/) |
| [Security, Identity, and Compliance](https://aws.amazon.com/architecture/security-identity-compliance/) | [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/), [Amazon Cognito](https://aws.amazon.com/cognito/), [Amazon Detective](https://aws.amazon.com/detective/), [https://aws.amazon.com/guardduty/](https://aws.amazon.com/guardduty/), [Amazon Inspector](https://aws.amazon.com/inspector/), [Amazon Macie](https://aws.amazon.com/macie/), [AWS Artifact](https://aws.amazon.com/artifact/), [AWS Certificate Manager (ACM)](https://aws.amazon.com/certificate-manager/), [AWS CloudHSM](https://aws.amazon.com/cloudhsm/), [Amazon DynamoDB Streams](https://aws.amazon.com/directoryservice/), [AWS Firewall Manager](https://aws.amazon.com/firewall-manager/), [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/), [AWS Resource Access Manager (AWS RAM)](https://aws.amazon.com/ram/), [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), [https://aws.amazon.com/security-hub/](https://aws.amazon.com/security-hub/), [AWS Shield](https://aws.amazon.com/shield/), (IAM), [AWS WAF](https://aws.amazon.com/waf/), [Amazon Verified Permissions](https://aws.amazon.com/verified-permissions/), [Amazon Security Lake](https://aws.amazon.com/security-lake/) |
| Machine Learning | [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/), [Amazon Augmented AI](https://aws.amazon.com/augmented-ai/), [Amazon CodeGuru](https://aws.amazon.com/codeguru/profiler/), [Amazon Comprehend](https://aws.amazon.com/comprehend/), [Amazon Personalize](https://aws.amazon.com/personalize/), [Amazon Rekognition](https://aws.amazon.com/rekognition/), [Amazon Transcribe](https://aws.amazon.com/transcribe/), [Amazon Kendra](https://aws.amazon.com/kendra/), [Amazon Lex](https://aws.amazon.com/lex/), [Amazon Bedrock](https://aws.amazon.com/bedrock/), [Amazon Q](https://aws.amazon.com/q/) |

 In addition to these offerings, AWS also empowers the HCLS industry by providing purpose-built health services and solutions. Some of the AWS healthcare and life sciences services are listed in the following table.

**AWS health and life sciences services**

| AWS product | Brief description |
| --- | --- |
| [AWS HealthLake](https://console.aws.amazon.com/healthlake/home/) | Provide a complete view of individual or patient population health data using the [HealthLake console](https://console.aws.amazon.com/healthlake/home/) |
| [AWS HealthImaging](https://aws.amazon.com/healthimaging/) | Store, transform, and analyze medical images in the cloud at petabyte scale. |
| [AWS HealthOmics](https://aws.amazon.com/omics/) | Transform genomic, transcriptomic, and other omics data into insights. |
| [Amazon Transcribe Medical](https://aws.amazon.com/transcribe/medical/) | Automatically convert medical speech to text. |
| [Amazon Comprehend Medical](https://aws.amazon.com/comprehend/medical/) | Extract information from unstructured medical text accurately and quickly. |

**Note**
Details and specifications for the full portfolio of AWS products are [available online](https://aws.amazon.com/).

## AWS Cloud Security
<a name="aws-cloud-security"></a>

 AWS infrastructure has been architected to be one of the most flexible and secure cloud computing environments available today. It's designed to provide an extremely scalable, highly reliable platform that enables customers to deploy applications and data quickly and securely. This infrastructure is built and managed not only according to security best practices and standards, but also with the unique needs of the cloud in mind. AWS uses redundant and layered controls, continuous validation and testing, and a substantial amount of automation to ensure that the underlying infrastructure is continuously monitored and protected.

 We have many [customer testimonials](https://aws.amazon.com/solutions/case-studies/) that highlight the security benefits of using the AWS cloud, in that the security capabilities provided by AWS far exceed the customer's own on-premises capabilities.

*"We had heard urban legends about 'security issues in the cloud,' but the more we looked into AWS, the more it was obvious to us that AWS is a secure environment and we would be able to use it with peace of mind."*

– Yoshihiro Moriya, Certified Information System Auditor at Hoya

*"There was no way we could achieve the security certification levels that AWS has. We have great confidence in the logical separation of customers in the AWS Cloud, particularly through Amazon VPC, which allows us to customize our virtual networking environment to meet our specific requirements."*

– Michael Lockhart, IT Infrastructure Manager at The GPT Group

*"When you're in telehealth and you touch protected health information, security is paramount. AWS is absolutely critical to do what we do today. Security and compliance are table stakes. If you don't have those, the rest doesn't matter."*

– Cory Costley, Chief Product Officer, Avizia

 Many more customer testimonials, including those from health and life science companies, can be found in [Customer Success Stories](https://aws.amazon.com/solutions/case-studies/).

 IT security is often not the core business of our customers. IT departments operate on limited budgets and do a good job of securing their data centers and software given limited resources. In the case of AWS, security is foundational to our core business and so significant resources are applied to ensuring the security of the cloud and helping our customers ensure security in the cloud, as described further in the following section.

## Shared Responsibility Model
<a name="shared-security-responsibility-model"></a>

 Security and Compliance is a shared responsibility between AWS and the customer. This shared model can help relieve your operational burden because AWS operates, manages and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. Customers assume responsibility and management of the guest operating system (including updates and security patches), other associated application software, and the configuration of the AWS-provided security group firewall. You should carefully consider the services you choose because your responsibilities vary depending on the services used, the integration of those services into your IT environment, and applicable laws and regulations.

 The following figure provides an overview of the [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/). This differentiation of responsibility is commonly referred to as Security of the Cloud compared to Security in the Cloud, which will be explained in more detail in the following paragraphs.

![Diagram showing the AWS Shared Responsibility Model](https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/images/shared-responsibility-model.png)

 AWS is responsible for the security and compliance of the cloud, the infrastructure that runs all the services offered in the AWS Cloud. Cloud security at AWS is the highest priority. AWS customers benefit from a data center and network architecture that are built to meet the requirements of the most security-sensitive organizations. This infrastructure consists of the hardware, software, networking, and facilities that run AWS cloud services.

 Customers are responsible for the security and compliance in the cloud, which consists of customer-configured systems and services provisioned on AWS. Responsibility within the AWS Cloud is determined by the AWS cloud services that you select and ultimately the amount of configuration work you must perform as part of your security responsibilities. For example, a service such as Amazon Elastic Compute Cloud (Amazon EC2) is categorized as infrastructure as a service (IaaS) and, as such, requires you to perform all the necessary security configuration and management tasks. Customers that deploy an Amazon EC2 instance are responsible for management of the guest operating system (including updates and security patches), any application software or utilities installed by you on the instances, and the configuration of the AWS-provided firewall (called a security group) on each instance. For abstracted services, such as Amazon Simple Storage Service (Amazon S3) and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system, and platforms, while customers access the endpoints to store and retrieve data. You're responsible for managing your data and component configuration (including encryption options), classifying your assets, and using AWS Identity and Access Management (IAM) tools to apply the appropriate permissions.

 The customer and AWS Shared Responsibility model also extends to IT controls. The same as the responsibility to operate the IT environment is shared between you and AWS, so is the management, operation, and verification of IT controls shared. AWS can help relieve your burden of operating controls by managing those controls associated with the physical infrastructure deployed in the AWS environment that might previously have been managed by you. Because every customer is deployed differently in AWS, you can take advantage of shifting management of certain IT controls to AWS which results in a (new) distributed control environment. You can then use the AWS control and compliance documentation available to you, in addition to techniques discussed later in this whitepaper, to perform your control evaluation and verification procedures as required. The following are examples of controls that are managed by AWS, AWS customers, or both.

**Inherited controls** – Controls that you fully inherit from AWS.
+ Physical and environmental controls

**Shared controls** – Controls that apply to both the infrastructure layer and customer layers, but in completely separate contexts or perspectives. In a shared control, AWS provides the requirements for the infrastructure and you must provide your own control implementation within your use of AWS services. Examples include:
+ **Patch management** – AWS is responsible for patching and fixing flaws within the infrastructure, but you are responsible for patching your guest OS and applications.
+ **Configuration management** – AWS maintains the configuration of its infrastructure devices, but you are responsible for configuring your own guest operating systems, databases, and applications.
+ **Awareness and training** – AWS trains AWS employees, but you must train your own employees.

**Customer specific controls** – Controls that are ultimately your responsibility based on the application you're deploying within AWS services. Examples include:
+ **Data management** – For instance, placement of data on Amazon S3 where you activate encryption.

 While certain controls are customer specific, AWS strives to provide you with the tools and resources to make implementation easier.

 For further information about AWS physical and operational security processes for the network and server infrastructure under the management of AWS see [AWS Cloud Security](https://aws.amazon.com/security/).

 For customers who are designing the security infrastructure and configuration for applications running in AWS, see the [Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/).

## AWS certifications and attestations
<a name="aws-certifications-and-attestations"></a>

 The AWS global infrastructure is designed and managed according to security best practices in addition to a variety of security compliance standards. With AWS, you can be assured that you're building web architectures on top of some of the most secure computing infrastructure in the world. The IT infrastructure that AWS provides is designed and managed in alignment with security best practices and a variety of IT security standards including the following that life science customers might find most relevant:
+ [SOC 1, 2, 3](https://aws.amazon.com/compliance/soc-faqs/)
+ ISO [9001](https://aws.amazon.com/compliance/iso-9001-faqs/) / ISO [27001](https://aws.amazon.com/compliance/iso-27001-faqs/) / ISO [27017](https://aws.amazon.com/compliance/iso-27017-faqs/) / ISO [27018](https://aws.amazon.com/compliance/iso-27018-faqs/)
+ [HITRUST](https://aws.amazon.com/compliance/hitrust/)
+ [FedRAMP](https://aws.amazon.com/compliance/fedramp/)
+ [CSA Security, Trust & Assurance Registry (STAR)](https://aws.amazon.com/compliance/csa/)
+ [National Institute of Standards and Technology (NIST)](https://aws.amazon.com/compliance/nist/)

 There are no specific certifications for GxP compliance for cloud services to date, however the controls and guidance described in this whitepaper, in conjunction with additional resources supplied by AWS, provide information on AWS services GxP-compatibility, which will assist you in designing and building your own GxP-compliant solutions.

 AWS provides on-demand access to security and compliance reports and select online agreements through [AWS Artifact](https://aws.amazon.com/artifact/), with reports accessible through AWS customer accounts under NDA. AWS Artifact is a central resource for compliance related information and is where you can find additional information on the AWS compliance programs described in this section.

### SOC 1, 2, and 3
<a name="soc-1-2-3"></a>

 AWS System and Organization Controls (SOC) Reports are independent third-party examination reports that demonstrate how AWS achieves key compliance controls and objectives. The purpose of these reports is to help you and your auditors understand the AWS controls established to support operations and compliance.

 The SOC 1 reports are designed to focus on controls in a service organization that are likely to be relevant to an audit of a user entity's financial statements. The AWS SOC 1 report is designed to cover specific key controls that are likely to be required during a financial audit, in addition to covering a broad range of IT general controls to accommodate a wide range of usage and audit scenarios. The AWS SOC1 control objectives include security organization, employee user access, logical security, secure data handling, physical security and environmental protection, change management, data integrity, availability and redundancy, and incident handling.

 The SOC 2 report is an attestation report that expands the evaluation of controls to the criteria set forth by the American Institute of Certified Public Accountants (AICPA) Trust Services Principles. These principles define leading practice controls relevant to security, availability, processing integrity, confidentiality, and privacy applicable to service organizations such as AWS. The AWS SOC 2 is an evaluation of the design and operating effectiveness of controls that meet the criteria for the security and availability principles set forth in the AICPA's Trust Services Principles criteria. This report provides additional transparency into AWS security and availability based on a pre-defined industry standard of leading practices and further demonstrates the commitment of AWS to protecting customer data. The SOC2 report includes outlining AWS controls, a description of AWS services relevant to security, availability, and confidentiality, and test results against controls. You will probably find the SOC 2 report to be the most detailed and relevant SOC report as it relates to GxP compliance.

 AWS also publishes a SOC 3 report. The SOC 3 report is a publicly available summary of the AWS SOC 2 report. The report includes the external auditor's assessment of the operation of controls (based on the AICPA's Security Trust Principles included in the SOC 2 report), the assertion from AWS management regarding the effectiveness of controls, and an overview of AWS infrastructure and services.

### FedRAMP
<a name="fedramp"></a>

 The Federal Risk and Authorization Management Program (FedRAMP) is a US government-wide program that delivers a standard approach to security assessment, authorization, and continuous monitoring for cloud products and services. FedRAMP uses the NIST Special Publication 800 series and requires cloud service providers to receive an independent security assessment conducted by a third-party assessment organization (3PAO) to ensure that authorizations are compliant with the Federal Information Security Management Act (FISMA).

 For AWS services in scope for FedRAMP assessment and authorization, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).

### ISO 9001
<a name="iso-9001"></a>

 ISO 9001:2015 outlines a process-oriented approach to documenting and reviewing the structure, responsibilities, and procedures required to achieve effective quality management within an organization. Specific sections of the standard contain information on topics such as:
+ Requirements for a quality management system (QMS), including quality documentation, document control, and determining process interactions
+ Responsibilities of management
+ Management of resources, including human resources and an organization's work environment
+ Service development, including the steps from design to delivery
+ Customer satisfaction
+ Measurement, analysis, and improvement of the QMS through activities like internal audits and corrective and preventive actions

 The AWS ISO 9001:2015 certification directly supports customers who develop, migrate and operate their quality-controlled IT systems in the AWS Cloud. You can use AWS compliance reports as evidence for your own ISO 9001:2015 programs and industry-specific quality programs, such as GxP in life sciences and ISO 13485 in medical devices.

### ISO/IEC 27001
<a name="isoiec-27001"></a>

 ISO/IEC 27001:2013 is a widely adopted global security standard that sets out requirements and best practices for a systematic approach to managing company and customer information that's based on periodic risk assessments appropriate to ever-changing threat scenarios. To achieve the certification, a company must show it has a systematic and ongoing approach to managing information security risks that affect the confidentiality, integrity, and availability of company and customer information.

 This widely recognized international security standard specifies that AWS does the following:
+ We systematically evaluate AWS information security risks, considering the impact of threats and vulnerabilities.
+ We design and implement a comprehensive suite of information security controls and other forms of risk management to address customer and architecture security risks.
+ We have an overarching management process to ensure that the information security controls meet our needs on an ongoing basis.

 AWS has achieved ISO 27001 certification of the Information Security Management System (ISMS) covering AWS infrastructure, data centers, and services.

### ISO/IEC 27017
<a name="isoiec-27017"></a>

 ISO/IEC 27017:2015 provides guidance on the information security aspects of cloud computing, recommending the implementation of cloud-specific information security controls that supplement the guidance of the ISO/IEC 27002 and ISO/IEC 27001 standards. This code of practice provides additional information security controls implementation guidance specific to cloud service providers.

 The AWS attestation to the ISO/IEC 27017:2015 standard not only demonstrates an ongoing commitment to align with globally recognized best practices but also verifies that AWS has a system of highly precise controls in place that are specific to cloud services.

### ISO/IEC 27018
<a name="isoiec-27018"></a>

 ISO 27018 is the first international code of practice that focuses on protection of personal data in the cloud. It's based on ISO information security standard 27002 and provides implementation guidance on ISO 27002 controls applicable to public cloud personally identifiable information (PII). It also provides a set of additional controls and associated guidance intended to address public cloud PII protection requirements not addressed by the existing ISO 27002 control set.

 AWS has achieved ISO 27018 certification, an internationally recognized code of practice, which demonstrates the commitment of AWS to the privacy and protection of your content.

### HITRUST
<a name="hitrust"></a>

 The Health Information Trust Alliance Common Security Framework (HITRUST CSF) uses nationally and internationally accepted standards and regulations such as GDPR, ISO, NIST, PCI, and HIPAA to create a comprehensive set of baseline security and privacy controls.

 HITRUST has developed the HITRUST CSF Assurance Program, which incorporates the common requirements, methodology, and tools that enable an organization and its business partners to take a consistent and incremental approach to managing compliance. Further, it allows business partners and vendors to assess and report against multiple sets of requirements.

 Certain AWS services have been assessed under the HITRUST CSF Assurance Program by an approved HITRUST CSF Assessor as meeting the HITRUST CSF Certification Criteria. The certification is valid for 2 years, describes the AWS services that have been validated, and can be accessed at [Health Information Trust Alliance Common Security Framework](https://aws.amazon.com/compliance/hitrust/). You might consider using the AWS HITRUST CSF certification of AWS services to support your own HITRUST CSF certification, to complement your GxP compliance programs.

### CSA Security, Trust & Assurance Registry
<a name="csa-security-trust-assurance-registry-star"></a>

 In 2011, the Cloud Security Alliance (CSA) launched the [Security, Trust & Assurance Registry (STAR)](https://cloudsecurityalliance.org/press-releases/2011/08/04/csa-announces-star/), an initiative to encourage transparency of security practices within cloud providers. STAR is a free, publicly accessible registry that documents the security controls provided by various cloud computing offerings, thereby helping users assess the security of cloud providers they currently use or are considering.

 AWS participates in the voluntary STAR self-assessment to document AWS compliance with CSA-published best practices. AWS publishes the completed [CSA Consensus Assessments Initiative Questionnaire (CAIQ)](https://d1.awsstatic.com/whitepapers/compliance/CSA_Consensus_Assessments_Initiative_Questionnaire.pdf) on the AWS website.

### National Institute of Standards and Technology
<a name="nist"></a>

 The [National Institute of Standards and Technology (NIST)](https://www.nist.gov/) 800-53 security controls are generally applicable to US Federal Information Systems. Federal Information Systems typically must go through a formal assessment and authorization process to ensure sufficient protection of confidentiality, integrity, and availability of information and information systems.

 AWS cloud infrastructure and services have been validated by third-party testing performed against the NIST 800-53 Revision 4 controls and additional FedRAMP requirements. AWS has received FedRAMP Authorizations to Operate (ATO) from multiple authorizing agencies for the AWS GovCloud (US) and the AWS US East and AWS US West Regions.

## Infrastructure controls
<a name="infrastructure-description-and-controls"></a>

### Cloud models (nature of the cloud)
<a name="cloud-models-nature-of-the-cloud"></a>

 Cloud computing is the on-demand delivery of compute power, database storage, applications, and other IT resources through a cloud services platform through the internet with pay-as-you-go pricing. As cloud computing has grown in popularity, several different models and deployment strategies have emerged to help meet specific needs of different users. Each type of cloud service and deployment method provides you with different levels of control, flexibility, and management.

#### Cloud computing models
<a name="cloud-computing-models"></a>

![Figure 2 – Comparing shared responsibility of traditional IT, IaaS, PaaS, and SaaS](https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/images/image3.png)

 In a traditional on-premises model, the organization is responsible for every layer of the technology stack including the physical network, servers, applications, and data. As organizations move from IaaS to platform as a service (PaaS) to software as a service (SaaS), more responsibility shifts to the supplier. IaaS transfers physical infrastructure and virtualization. PaaS additionally transfers the operating system, middleware, and runtime. SaaS transfers responsibility for the application itself, while the organization retains responsibility for the data and how it is used.

 The preceding diagram is an adaptation of existing models which took the same layers depicted for Traditional IT and applied them to the cloud. However, this gives the impression that all server, storage, and network management is handled by the cloud service provider. Although this is true for the physical infrastructure, a regulated company will still have a virtual network, use storage services and need to manage a fleet of virtual servers. This means control domains, such as patch management, still apply to the regulated company. For that reason, the Virtual Network, Storage, and Server layers have been added.

 The following diagram applies the preceding model to AWS services:

![Figure 3 – Shared responsibility spectrum across AWS services](https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/images/image4.png)

 Different AWS services provide different customer responsibility boundaries. For most AWS services, AWS operates, manages, and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. The customer assumes responsibility and management of the guest operating system (including updates and security patches), other associated application software, and the configuration of the AWS-provided security group firewall. Core infrastructure services like Amazon EC2 offer more customization but require more customer responsibility, while managed services like Amazon S3 shift more responsibility to AWS with security best practices built in by default. Container services provide a balance between customization and customer responsibility. The customer always retains responsibility for their data and client-side encryption, while AWS manages progressively more of the underlying infrastructure, services, and network controls. Because the boundary between customer and AWS responsibilities differs by AWS service, it's recommended that customers assess where the shared responsibility boundary falls for each service to implement proper controls and configurations.

**Infrastructure as a service**

 Infrastructure as a service (IaaS) contains the basic building blocks for cloud IT and typically provides access to networking features, computers (virtual or on dedicated hardware), and data storage space. IaaS provides you with the highest level of flexibility and management control over your IT resources and is most similar to the existing IT resources that many IT departments and developers are familiar with today (for example, Amazon EC2).

 While cloud providers maintain the physical hardware infrastructure, organizations using IaaS retain substantial control over their operating systems, storage configurations, networking components, security protocols, and application deployment. The specific balance of management responsibilities between the service provider and the customer organization varies according to the chosen service offering.

**Platform as a service**

 Platform as a service (PaaS) removes the need for organizations to manage the underlying infrastructure (usually hardware and operating systems) and so you can focus on the deployment and management of your applications (for example, ). This helps you be more efficient because you don't need to worry about resource procurement, capacity planning, software maintenance, patching, or any of the other undifferentiated heavy lifting involved in running your application.

**Software as a service**

 Software as a service (SaaS) provides you with a completed product that is run and managed by the service provider. In most cases, people referring to Software as a Service are referring to end-user applications (for example, Amazon Connect). With a SaaS offering, you don't have to think about how the service is maintained or how the underlying infrastructure is managed; you only need to think about how you will use that particular piece of software. A common example of a SaaS application is web-based email, which can be used to send and receive email without having to manage feature additions to the email product or maintain the servers and operating systems on which the email program is running.

#### Cloud computing deployment models
<a name="cloud-computing-deployment-models"></a>

**Cloud**

 A cloud-based application is fully deployed in the cloud and all parts of the application run in the cloud. Applications in the cloud have either been created in the cloud or have been migrated from an existing infrastructure to take advantage of the benefits of cloud computing (see [What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/)). Cloud-based applications can be built on low-level infrastructure pieces or can use higher level services that provide abstraction from the management, architecting, and scaling requirements of core infrastructure.

**Hybrid**

 A hybrid deployment is a way to connect infrastructure and applications between cloud-based resources and existing resources that aren't located in the cloud. The most common method of hybrid deployment is between the cloud and existing on-premises infrastructure to extend—and grow—an organization's infrastructure into the cloud while connecting cloud resources to the internal system. For more information about how AWS can help you with hybrid deployment, see [Hybrid Cloud with AWS](https://aws.amazon.com/hybrid/).

**On-premises**

 The deployment of resources on-premises, using virtualization and resource management tools, is sometimes sought for its ability to provide dedicated resources. In most cases this deployment model is the same as legacy IT infrastructure while using application management and virtualization technologies to try and increase resource use. For more information, see [Hybrid Cloud with AWS](https://aws.amazon.com/hybrid/).

### Security
<a name="security"></a>

#### Physical security
<a name="physical-security"></a>

 Amazon has many years of experience in designing, constructing, and operating large-scale data centers. This experience has been applied to the AWS platform and infrastructure. AWS data centers are housed in facilities that aren't branded as AWS facilities. Physical access is strictly controlled both at the perimeter and at building ingress points by professional security staff using video surveillance, intrusion detection systems, and other electronic means. Authorized staff must pass two-factor authentication a minimum of two times to access data center floors. All visitors are required to present identification and are signed in and continually escorted by authorized staff. AWS only provides data center access and information to employees and contractors who have a legitimate business need for such privileges. When an employee no longer has a business need for these privileges, his or her access is immediately revoked, even if they continue to be an employee of Amazon or AWS. All physical access to data centers by AWS employees is logged and audited routinely.

 For more information about infrastructure security, see [AWS Data Center Controls](https://aws.amazon.com/compliance/data-center/controls/).

**Single- or multi-tenant environments**

 As cloud technology has rapidly evolved over the past decade, one fundamental technique used to maximize physical resources and lower customer costs has been to offer multi-tenant services to cloud customers. To facilitate this architecture, AWS has developed and implemented powerful and flexible logical security controls to create strong isolation boundaries between customers. At AWS, Security is our top priority, and you will find a rich history of AWS steadily enhancing its features and controls to help customers achieve their security posture requirements such as GxP. Coming from operating an on-premises environment, you will often find that Cloud Service Providers like AWS enable you to effectively optimize your security configurations in the cloud compared to your on-premises solutions.

 The AWS logical security capabilities and security controls address the concerns driving physical separation to protect your data. The provided isolation combined with the added automation and flexibility offers a security posture that matches or bests the security controls seen in traditional, physically separated environments.

 Additional detailed information on logical separation on AWS can be found in the [Logical Separation on AWS](https://d1.awsstatic.com/whitepapers/compliance/AWS_Logical_Separation_Handbook.pdf) whitepaper.

### Global infrastructure
<a name="cloud-infrastructure-qualification-activities"></a>

#### Geography
<a name="geography"></a>

 AWS serves over a million active customers in more than 200 countries. As customers grow their businesses, AWS will continue to provide infrastructure that meets their global requirements.

 The AWS Cloud is built around AWS Regions and Availability Zones. An AWS Region is a physical location in the world and has multiple AZs. Availability Zones consist of one or more discrete data centers, each with redundant power, networking, and connectivity, housed in separate facilities. These AZs offer you the ability to operate production applications and databases that are more highly available, fault tolerant, and scalable than would be possible from a single data center. The AWS Cloud operates in over 70 AZs in over 20 geographic Regions around the world, with announced plans for more AZs and Regions. For more information about AWS AZs and Regions, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

 Each AWS Region is designed to be completely isolated from the other Regions. This achieves the greatest possible fault tolerance and stability. Each Availability Zone is isolated, but the AZs in a Region are connected through low-latency links. AWS provides customers with the flexibility to place instances and store data within multiple geographic regions and across multiple AZs within each AWS Region. Each AZ is designed as an independent failure zone. This means that AZs are physically separated within a typical metropolitan region and are located in lower risk flood plains (specific flood zone categorization varies by AWS Region). In addition to discrete uninterruptable power supplies (UPS) and onsite backup generation facilities, they are each fed through different grids from independent utilities to further reduce single points of failure. Availability Zones are all redundantly connected to multiple tier-1 transit providers.

#### Data locations
<a name="data-locations"></a>

 Where geographic limitations apply, unlike other cloud providers, who often define a region as a single data center, the multiple Availability Zone (AZ) design of every AWS Region offers you advantages. If you're focused on high availability, you can design your applications to run in multiple AZs to achieve even greater fault-tolerance. AWS Regions meet the highest levels of security, compliance, and data protection. If you have data residency requirements, you can [choose the AWS Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) that is in close proximity to your desired location. You retain complete control and ownership over the Region in which your data is physically located, making it straightforward to meet regional compliance and data residency requirements.

 In addition, for moving on-premises data to AWS for migrations or ongoing workflows, [AWS Cloud Data Migration](https://aws.amazon.com/cloud-data-migration/) describes the various tools and services that you can use to ensure data onshoring compliance, including:
+ Hybrid cloud storage (AWS Storage Gateway, )
+ Online data transfer (AWS DataSync, AWS Transfer Family, Amazon S3 Transfer Acceleration, AWS Snowcone, Amazon Data Firehose, and APN Partner Products)
+ Offline data transfer (AWS Snowcone, AWS Snowball Edge, and AWS Snowmobile)

#### Capacity
<a name="capacity"></a>

 When it comes to capacity planning, AWS examines capacity at both a service and rack usage level. The AWS capacity planning process also automatically triggers the procurement process for approval so that AWS doesn't have additional lag time to account for, and AWS relies on capacity planning models—which are informed in part by customer demand—to trigger new data center builds. AWS enables you to reserve instances so that space is guaranteed in the AWS Regions of your choice. AWS uses the number of reserved instances to inform planning for FOOB (future out of bound).

#### Uptime and change management
<a name="uptime"></a>

 To ensure accountability, AWS maintains documented service level agreements (SLAs) for each service, with core services guaranteed at minimum 99.9% availability. Regular SLA performance reporting, service credits for any breaches, and transparent incident reporting with root cause analysis demonstrate the commitment of AWS to service reliability. A full list of AWS SLAs can be found at [AWS Service Level Agreements](https://aws.amazon.com/legal/service-level-agreements/).

 AWS actively manages service uptime through a comprehensive system of monitoring and change management. AWS also maintains continuous real-time service health monitoring through the [AWS Service Health Dashboard](https://health.aws.amazon.com/health/status), employing automated detection and response mechanisms for potential availability issues while strategically scheduling proactive maintenance to minimize customer impact.

 Change management follows a sophisticated approach where service updates are deployed through controlled rollout waves and blue/green deployments to ensure zero-downtime updates. AWS communicates these changes through advance notifications on the AWS Health Dashboard and implements a regional deployment strategy to contain any potential impact of changes.

 Supporting these technical measures, AWS provides extensive guidance to customers on architecting for high availability, offering technical documentation for resilient design patterns and supporting business continuity planning through the Well-Architected Framework. This comprehensive approach ensures service reliability while enabling continuous improvement and feature deployment, all while maintaining transparent communication with customers about service health and changes.
