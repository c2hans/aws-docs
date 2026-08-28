---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/data-protection.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data protection
<a name="data-protection"></a>

 Before architecting an ML workload, the foundational practices that influence security should be in place. For example, [data classification](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-classification.html) provides a way to categorize data based on levels of sensitivity, and encryption protects data by rendering it unintelligible to unauthorized access. These methods are important, because they support objectives such as preventing mishandling or complying with regulatory obligations.

 SageMaker AI Studio provides several features for protecting data at rest and in-transit. However, as described in the [AWS Shared Responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), customers are responsible for maintaining control over the content that is hosted on AWS Global infrastructure. In this section, we describe how customers can use those features to protect their data.

## Protect data at rest
<a name="protect-data-at-rest"></a>

 To protect your SageMaker AI Studio notebooks along with your model-building data and model artifacts, SageMaker AI encrypts the notebooks, as well as the output from training and batch transform jobs. SageMaker AI encrypts these by default, using the [AWS Managed Key for Amazon S3](https://docs.aws.amazon.com/kms/latest/developerguide/services-s3.html). This AWS Managed Key for Amazon S3 cannot be shared for cross-account access. For cross-account access, specify your customer-managed key while creating SageMaker AI resources so it can be shared for cross-account access.

 With SageMaker AI Studio, data can be stored in the following locations:
+  **S3 bucket** – When a shareable notebook is enabled, SageMaker AI Studio shares notebook snapshots and metadata in an S3 bucket.
+  **EFS volume** – SageMaker AI Studio attaches an EFS volume to your domain for storing notebooks and data files. This EFS volume persists even after the domain is deleted.
+  **EBS volume** – EBS is attached to the instance that the notebook runs on. This volume persists for the duration of the instance.

### Encryption at rest with AWS KMS
<a name="encryption-at-rest-with-aws-kms"></a>
+  You can pass your [AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys) to encrypt an EBS volume attached to notebooks, training, tuning, batch transform jobs, and endpoints.
+  If you don't specify a KMS key, SageMaker AI encrypts both operating system (OS) volumes and ML data volumes with a system-managed KMS key.
+  Sensitive data that needs to be encrypted with a KMS key for compliance reasons should be stored in the ML storage volume or in Amazon S3, both of which can be encrypted using a KMS key you specify.

## Protect data in transit
<a name="protect-data-in-transit"></a>

 SageMaker AI Studio ensures that ML model artifacts and other system artifacts are encrypted in transit and at rest. Requests to the SageMaker AI API and console are made over a secure (SSL) connection. Some intra-network data in-transit (inside the service platform) is unencrypted. This includes:
+  Command and control communications between the service control plane and training job instances (not customer data).
+  Communications between nodes in distributed processing and training jobs (intra-network).

 However, you can choose to encrypt communication between nodes in a training cluster. Enabling inter-container traffic encryption can increase training time, especially if you are using distributed deep learning algorithms.

 By default, Amazon SageMaker AI runs training jobs in an Amazon VPC to help keep your data secure. You can add another level of security to protect your training containers and data by configuring a private VPC. Furthermore, you can configure your SageMaker AI Studio domain to run in VPC only mode, and set up VPC endpoints to route traffic over a private network without egressing traffic over the internet.

## Data protection guardrails
<a name="data-protection-guardrails"></a>

### Encrypt SageMaker AI hosting volumes at rest
<a name="encrypt-sagemaker-hosting-volumes-at-rest"></a>

 Use the following policy to enforce encryption during hosting a SageMaker AI endpoint for online inference:

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement": [
     {
         "Sid": "Encryption",
         "Effect": "Allow",
         "Action": [
             "sagemaker:CreateEndpointConfig"
         ],
         "Resource": "*",
         "Condition": {
             "Null": {
                 "sagemaker:VolumeKmsKey": "false"
             }
         }
     }
   ]
 }
```

------

### Encrypt S3 buckets used during Model Monitoring
<a name="encrypt-s3-buckets-used-during-model-monitoring"></a>

 [Model Monitoring](https://www.dominodatalab.com/data-science-dictionary/model-monitoring) captures data sent to your SageMaker AI endpoint and stores it in an S3 bucket. When you set up the Data Capture Config, you need to encrypt the S3 bucket. Currently there is no compensating control for this.

 In addition to capturing endpoint outputs, the Model Monitoring service checks for drift against a pre-specified baseline. You need to encrypt the outputs and the intermediate storage volumes used to monitor the drift.

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement": [
     {
         "Sid": "Encryption",
         "Effect": "Allow",
         "Action": [
             "sagemaker:CreateMonitoringSchedule",
             "sagemaker:UpdateMonitoringSchedule"
         ],
         "Resource": "*",
         "Condition": {
             "Null": {
                 "sagemaker:VolumeKmsKey": "false",
                 "sagemaker:OutputKmsKey": "false"
             }
         }
     }
   ]
 }
```

------

### Encrypt a SageMaker AI Studio domain storage volume
<a name="encrypt-a-sagemaker-studio-domain-storage-volume"></a>

 Enforce encryption to storage volume attached to Studio domain. This policy requires a user to provide a CMK to encrypt the storage volumes attached to studio domains.

------
#### [ JSON ]

****

```
{
     "Version":"2012-10-17",
     "Statement": [
         {
             "Sid": "EncryptDomainStorage",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:CreateDomain"
             ],
             "Resource": "*",
             "Condition": {
                 "Null": {
                     "sagemaker:VolumeKmsKey": "false"
                 }
             }
         }
     ]
 }
```

------

### Encrypt data stored in S3 that is used to share notebooks
<a name="encrypt-data-stored-in-s3-that-is-used-to-share-notebooks"></a>

 This is the policy to encrypt any data stored in the bucket that is used to share notebooks between users in a SageMaker AI Studio domain:

------
#### [ JSON ]

****

```
{
     "Version":"2012-10-17",
     "Statement": [
         {
             "Sid": "EncryptDomainSharingS3Bucket",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:CreateDomain",
                 "sagemaker:UpdateDomain"
             ],
             "Resource": "*",
             "Condition": {
                 "Null": {
                     "sagemaker:DomainSharingOutputKmsKey": "false"
                 }
             }
         }
     ]
 }
```

------

## Limitations
<a name="limitations-1"></a>
+  Once a domain is created, you cannot update the attached EFS volume storage with a custom AWS KMS key.
+  You cannot update training/processing jobs or endpoint configurations with KMS keys once they have been created.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
