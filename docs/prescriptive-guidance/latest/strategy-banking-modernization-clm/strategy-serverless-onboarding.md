---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-banking-modernization-clm/strategy-serverless-onboarding.html
---

# Serverless onboarding
<a name="strategy-serverless-onboarding"></a>

This section focuses on the client onboarding use case. It serves as an example of how to reuse serverless patterns to modernize a key customer journey.

## An onboarding solution
<a name="onboarding-solution"></a>

An onboarding solution usually does not come in isolation, but is part of a larger landscape. The components and services required for integration include the following:

1. Lead generation (CRM systems)

1. Due diligence (AML, risk and compliance)

1. Central client data file (core banking systems)

1. Digital signature management (using a third-party tool like DocuSign)

1. Biometrics verification

1. Digital contract management lifecycle

1. Process and operating model automation

**Note**
The integration of these components with external applications is beyond the scope of this strategy.

The following diagram illustrates a serverless architecture for interacting with customers through chatbots in the AWS Cloud:

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-banking-modernization-clm/images/guide-img/3dd14f64-3f68-43c4-8bd5-d6738253ef4f/images/0b45dff3-6316-47db-9f96-0d963f3a9f6f.png)

**Note**
The architecture is based on the QnA Bot on AWS solution and the updates to Amazon Rekognition. For more information, see [QnA Bot on AWS](https://aws.amazon.com/solutions/implementations/aws-qnabot/) in the AWS Solutions Library and [Amazon Rekognition announces updates to its face detection, analysis, and recognition capabilities](https://aws.amazon.com/blogs/machine-learning/amazon-rekognition-announces-updates-to-its-face-detection-analysis-and-recognition-capabilities/) in the AWS Machine Learning Blog.

The diagram shows the following workflow:

1. Customers access the front-end components to interact with the bot. In this case, the front-end library can be included in existing assets in various ways. For example, you can integrate these components into the corporate website or link them to a major chatting app. These components are delivered in JavaScript and served through static asset management by using Amazon Simple Storage Service (Amazon S3) and Amazon CloudFront.

1. The front-end components embed connections to the back-end components to validate credentials through Amazon Cognito. Once authorized, the client service can communicate with the onboarding solution's service.

1. Customers interact with the service by using an Amazon Lex bot. A predefined scenario for onboarding is run by using AWS Step Functions to call the necessary services to complete the process. You can tailor this scenario to fit the needs of the banking system (for example, to meet photography requirements, translation in multiple languages, and natural language processing to match customer intent). You can use AWS Lambda functions to fulfill the actions of the Amazon Lex bot with the customer and call services depending on the onboarding stage.

1. The output of Step Functions is sent in a batch to the bank internal system through Amazon EventBridge, which uses your preferred method to connect to the Bank Internal System. You can handle this communication either by peering to another AWS account or network peering through a virtual private network (VPN) to the banking system.

1. The entire architecture is designed for security and compliance by using AWS Config, Amazon Macie, AWS Artifact, and AWS Security Hub.

## Security and compliance considerations
<a name="security-compliance-considerations"></a>

Maintaining security and handling sensitive information is at the heart of the serverless onboarding approach. Serverless onboarding is designed to be stateless and doesn't store any PII or critical business data. To ensure continuous security and compliance, you must put the following services in place and configure them correctly:
+ AWS Config ensures the integrity and confidentiality of the services through rules tailored for compliance. Controls in place will validate overall compliance and prevent drifts in configuration.
+ Macie detects and tags any PII throughout the process.
+ Security Hub ensures that all services are defined and used within the security scope.
+ AWS Artifact provides audit evidence for the compliance of AWS services.

Transactions and non-repudiation evidence can be stored and encrypted by using [customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) or a dedicated hardware security module (HSM) that's sealed for audit purposes. You can also seal data at low cost while ensuring integrity and security by using [Amazon S3 Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-vaults.html).

Only the operational team should be permitted to access the environment. Any development activities should be streamlined through automatic continuous delivery to prevent any human access to the production environment. For auditing purposes, an additional role should be provisioned to access artifacts and compliance reports on the platform.

AWS can help ensure that you meet regulatory and compliance standards. For more information, see [FINMA ISAE 3000 Type 2 Report](https://aws.amazon.com/compliance/finma/?nc1=h_ls) in the AWS documentation. You can also download relevant banking artifacts directly from [AWS Artifact](https://aws.amazon.com/artifact/), including FINMA Circular 2008/21, FINMA ISAE 3000 Type 2, FINMA Circular 2018/03, and Global Financial Services Regulatory Principles.
