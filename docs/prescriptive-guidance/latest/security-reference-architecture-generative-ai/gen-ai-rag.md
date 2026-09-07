---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-rag.html
---

# Capability 2. Providing secure access, usage, and implementation for generative AI model customization
<a name="gen-ai-rag"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

The scope of this scenario is to secure model customization. This use case focuses on securing the resources and training environment for a model customization job as well as securing the invocation of a custom model. The following diagram illustrates the AWS services recommended for the Generative AI account for this capability.

![Services recommended for model customization.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/images/guide-img/a349f18f-a9fd-43a3-9a48-27534bf6412a/images/b1ca6b72-d43b-43fe-adfa-82e57b14ffe8.png)

The Generative AI account includes services required for customizing a model along with a suite of required security services to implement security guardrails and centralized security governance. To allow for private model customization, you should create Amazon S3 gateway endpoints for the training data and evaluation Amazon S3 buckets that a private VPC environment is configured to access.

## Rationale
<a name="rag-rationale"></a>

[Model customization](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) improves foundation model (FM) performance for specific use cases by providing training data. Amazon Bedrock offers two customization methods:
+ Continued pre-training with unlabeled data to enhance domain knowledge
+ Fine-tuning with labeled data to optimize task-specific performance

Customized models require [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) for inference.

This capability addresses the following scenarios from the [Generative AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/):
+ **Scope 4 - Model customization** – You customize an FM (from [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) or [Amazon SageMaker Jumpstart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)) with your data to improve performance for specific tasks or domains. You control the application, customer data, training data, and customized model. The FM provider controls the pre-trained model and its training data.
+ **Scope 5 - Model training from scratch** – You train a model from scratch using datasets you provide. You control the training data, model algorithm, training infrastructure, application, customer data, and related infrastructure.

Beyond customizing models within Amazon Bedrock, you can use the [Custom Model Import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html) feature to import models customized in other environments, such as Amazon SageMaker AI. Use [Safetensors](https://huggingface.co/docs/safetensors/en/index) for the imported model serialization format. Unlike `pickle`, Safetensors stores only tensor data, not arbitrary Python objects. This approach eliminates vulnerabilities from unpickling untrusted data because Safetensors can't execute code.

To detect potential training data leakage, introduce canaries into your training data. Canaries are unique, identifiable strings that should never appear in model outputs. Configure prompt logging to alert when these canaries are detected, indicating the model may be memorizing and reproducing training data inappropriately.

### Amazon Bedrock model customization
<a name="9999999999999999br--model-customization.a1f374a2-9ae4-5183-8c67-8fb7f5c53c7f"></a>

You can privately and securely customize FMs with your own data in Amazon Bedrock to build applications specific to your domain, organization, and use case. Fine-tuning increases model accuracy by providing your own task-specific, labeled training dataset to further specialize FMs. Continued pre-training trains models using your own unlabeled data in a secure and managed environment with customer managed keys. For more information, see [Customize your model to improve its performance for your use case](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) in the Amazon Bedrock documentation.

### Model training or fine-tuning with SageMaker AI
<a name="model-training-or-fine-tuning-with-9999999999999999sm-.c2099cf6-e2f6-5e7e-8df7-300677b6699c"></a>

You can train new models or fine-tune existing models by using [Amazon SageMaker AI training jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html). This solution creates models customized for your business needs while maintaining control of all resources, including Amazon Elastic Compute Cloud (Amazon EC2) instances, training code, and training infrastructure.

## Security considerations
<a name="rag-security"></a>

Model customization creates artifacts, including the model and its weights, that are used in production workloads. This stage faces the following threats:
+ **Data and model poisoning** – A threat actor injects malicious data to alter model behavior, introducing bias and causing unintended outputs.
+ **Sensitive information disclosure** – A model trained on datasets containing personally identifiable information (PII) leaks sensitive information during inference.

SageMaker AI and Amazon Bedrock provide features that mitigate these risks, including data protection, access control, network security, logging, and monitoring.

## Remediations
<a name="rag-remediations"></a>

This section reviews the AWS services and features that address the risks that are specific to this capability.

### Data protection
<a name="data-protection.c4c4cad4-74bd-53ed-b249-585f649199cc"></a>

Encrypt the model customization job, output files (training and validation metrics), and resulting custom model. For this encryption, use an AWS Key Management Service (AWS KMS) [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) that you create, own, and manage.

When you use Amazon Bedrock to run a model customization job, you store the input files (training and validation data) in your Amazon S3 bucket. When the job is completed, Amazon Bedrock stores the output metrics files in the S3 bucket that you specified when you created the job. Amazon Bedrock stores the resulting custom model artifacts in an S3 bucket controlled by AWS. By default, input and output files are encrypted with [Amazon S3 SSE-S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html) server-side encryption using an AWS managed key. You can choose to [encrypt these files](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-custom-job.html) with a customer managed key.

### Identity and access management
<a name="identity-and-access-management.a6b9f328-3e14-5785-b409-05dc0642643b"></a>

Create a custom AWS Identity and Access Management (IAM) service role for model customization or model import that follows the [principle of least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege).

To create a service role for model customization, follow the [instructions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-iam-role.html) in the Amazon Bedrock documentation.

To create a service role for importing pre-trained models, follow the [instructions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-import-iam-role.html) in the Amazon Bedrock documentation.

### Network security
<a name="network-security.cca3c83f-da21-576a-83e8-702573e1ab15"></a>

[Use a VPC](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-job-access-security.html#vpc-model-customization:~:text=Protect%20your%20model%20customization%20jobs%20using%20a%20VPC) with Amazon Virtual Private Cloud (Amazon VPC) to control access to your data. When you create your VPC, use the default DNS settings for your endpoint route table so that standard Amazon S3 URLs resolve.

If you configure your VPC with no internet access, create an [Amazon S3 VPC endpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html). Use this VPC endpoint to allow your model customization jobs to access the S3 buckets that store your training and validation data and model artifacts.

For SageMaker AI, configure the training job with a [VPC configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html), including private subnets and security groups that restrict both inbound and outbound traffic. This approach helps to ensure that Amazon EC2 instances can only access the resources that you define. Combined with Amazon S3 VPC endpoints, this approach helps to ensure that EC2 instances only access specified S3 buckets.

After you set up your VPC and endpoint, attach permissions to your [model customization IAM role](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-job-access-security.html). After you configure the VPC and required roles and permissions, you can create a [model customization job](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-job-access-security.html#:~:text=Protect%20your%20model%20customization%20jobs%20using%20a%20VPC) that uses this VPC. By creating a VPC with no internet access and an associated Amazon S3 VPC endpoint for training data, you can run your model customization job with private connectivity without internet exposure.

## Recommended AWS services
<a name="rag-services"></a>

This section discusses the AWS services that are recommended to build this capability securely. In addition to the services in this section, use Amazon OpenSearch Service and Amazon Comprehend as discussed in Capability 3.

### Amazon S3
<a name="9999999999999999s3-.246fc299-a1f7-5bf7-9c87-ec448bb88155"></a>

When you run a model customization job, the job accesses your Amazon S3 bucket to download input data and upload job metrics. You can choose fine-tuning or continued pre-training as the model type when you submit your [model customization job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-submit.html) on the Amazon Bedrock console or API. After a model customization job completes, [analyze the training process results](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-analyze.html). To do this, you can view the files in the output S3 bucket that you specified when you submitted the job or view details about the model.

[Encrypt](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) both buckets with a customer managed key. Use Amazon S3 Object Lock or versioning to ensure data integrity. For additional network security hardening, create a [gateway endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) for the S3 buckets that the VPC environment accesses. [Log and monitor](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html) all access. Use [resource-based policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) to control access to your Amazon S3 files.

### Amazon Macie
<a name="9999999999999999mcelong-.169b8bd7-3346-59df-981c-835033cb87f1"></a>

[Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover and help protect your sensitive data in AWS. You need to identify the type and classification of data that your workload is processing to ensure that appropriate controls are enforced. Macie can help identify sensitive data in your prompt store and model invocation logs stored in S3 buckets.

You can use Macie to automate discovery, logging, and reporting of sensitive data in Amazon S3. You can do this in two ways: Configure Macie to perform automated sensitive data discovery, or create and run sensitive data discovery jobs. For more information, see [Discovering sensitive data with Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/data-classification.html) in the Macie documentation.

### Amazon EventBridge
<a name="9999999999999999evlong-.9f541b93-4c49-52a6-916c-a7a02a8e48c8"></a>

Use [EventBridge](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-eventbridge.html) to configure SageMaker to respond automatically to model customization job status changes in Amazon Bedrock. Events from Amazon Bedrock are delivered to EventBridge in near real time. You can write simple [rules](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-eventbridge.html#monitoring-eventbridge-create-rule) to automate actions when an event matches a rule.

### AWS KMS
<a name="9999999999999999kms-.58922528-8bb3-50f0-aa97-cdf019684eba"></a>

Use a customer managed key to encrypt the model customization job, output files (training and validation metrics), resulting custom model, and [Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) that host the training, validation, and output data. For more information, see [Encryption of custom models](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-custom-job.html) in the Amazon Bedrock documentation.

A [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) is a resource policy for an AWS KMS key. Key policies are the primary way to control access to KMS keys. You can also use IAM policies and grants to control access to KMS keys, but every KMS key must have a key policy. Use a [key policy to provide permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-custom-job.html#encryption-key-policy) to a role to access the custom model encrypted with the customer managed key. This approach allows specified roles to use a custom model for inference.

### Amazon CloudWatch
<a name="9999999999999999cwlong-.5a68946f-b525-5dad-b7a6-39d2a00c3609"></a>

Use [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to monitor training job metrics in SageMaker and fine-tuning metrics in Amazon Bedrock. [Create alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) to receive notifications when a job fails or when a metric deviates from baseline.

### AWS CloudTrail
<a name="9999999999999999ctlong-.7936da81-8f15-53df-8b36-fe7bf97d2269"></a>

Use [CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) to log all events on your AWS resources. Create a trail filtered on your training resources, including datasets on Amazon S3. This trail enables you to act on suspicious activity surrounding your resources.
