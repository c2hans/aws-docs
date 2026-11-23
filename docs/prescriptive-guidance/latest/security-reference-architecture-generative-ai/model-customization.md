---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/model-customization.html
---

# Model customization

Model customization adapts a model using training data. It introduces datasets, training jobs, evaluation results, and model artifacts that need protection before the model enters production. The security design follows those resources from data approval through training and release.

This page covers [Amazon Bedrock customization](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-job-access-security.html) and [Amazon SageMaker AI training](https://docs.aws.amazon.com/sagemaker/latest/dg/mkt-algo-model-internet-free.html), with shared data and release controls for both. When the resulting model serves an application, the model inference controls also apply. If your application only invokes a pretrained model or retrieves content from a knowledge base, follow the inference and retrieval guidance.

## Security considerations
<a name="security-considerations"></a>

Training and customization introduce these risks:
+ Training jobs or notebooks expose protected datasets outside their approved environment.
+ Untrusted datasets, model weights, or dependencies compromise the training or serving workflow.
+ A training identity approves and deploys its own model without independent review.
+ Model weights or retained checkpoints reveal information learned from sensitive training data.

## Infrastructure security
<a name="infrastructure-security"></a>

Protect training data and model artifacts, and limit each job to its approved dependencies. These controls help protect sensitive datasets and the integrity of models released for inference.

### Amazon Bedrock: isolate managed customization jobs
<a name="amazon-bedrock-isolate-managed-customization-jobs"></a>

An Amazon Bedrock customization job needs access to its input data and a destination for its output. Configure [Amazon VPC access for the job](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-job-access-security.html#vpc-config) with private subnets and an [Amazon S3 gateway endpoint](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-s3.html). [Restrict the Amazon S3 endpoint policy](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#edit-vpc-endpoint-policy-s3) to the job's input and output buckets. Also use the [job role and bucket policies](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-job-access-security.html) to restrict data access.

Review each job subnet's route table and [remove routes that provide internet egress](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html), including routes to NAT gateways. Keep these route tables associated with the Amazon S3 gateway endpoint so approved job data remains reachable. Test that the job can read approved inputs and write outputs while unrelated datasets remain inaccessible.

### Amazon SageMaker AI: isolate training environments
<a name="amazon-sagemaker-ai-isolate-training-environments"></a>

Configure training jobs with private subnets and security groups restricted to their dependencies. Enable [network isolation](https://docs.aws.amazon.com/sagemaker/latest/dg/mkt-algo-model-internet-free.html) in Amazon SageMaker AI for compatible training code that does not need outbound calls. SageMaker AI handles the transfer of training data and artifacts outside the isolated container. When training code needs access to other services, use VPC endpoints for AWS dependencies and restrict other outbound destinations. For routed egress requiring inspection, use [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) and restrict external package sources.

Apply the [DNS filtering baseline](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/#filter-outbound-dns-requests) to training VPCs that permit outbound calls.

Govern the training images and code you supply. Use approved [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) images and [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-ecr.html) scanning to identify image vulnerabilities. Preserve code, dependency versions, and image identity for each approved run. For training on compute you operate, use [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) to patch your managed nodes, and test updates before sensitive jobs.

### Shared account and release boundaries
<a name="shared-account-and-release-boundaries"></a>

In this architecture, the optional [AI training account](https://dp8l2mfblnx2f.cloudfront.net/architecture/#map-account-roles-to-your-services) contains sensitive datasets and production model development workloads. Treat it as part of the [production security boundary](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-model-inference.html) from the start of training. Use separate roles and network controls for training and inference, and restrict promotion of reviewed artifacts to the release workflow. Host production SageMaker AI endpoints in the inference account to limit the effect of training administration on the serving workload.

## Identity and data security
<a name="identity-and-data-security"></a>

### Shared dataset governance
<a name="shared-dataset-governance"></a>

Data owners approve the source, permitted use, and retention of training datasets. The training team preserves that information as data is prepared and used, with evaluation data kept separate from training inputs. Store training, validation, and output data in S3 with [Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) enabled and permissions separated by purpose. Use [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) to preserve dataset history and [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) when the data owner's retention requirements call for it.

Apply the shared sensitive-data checks before admitting data to training. Detection results inform the data owner's review; permission to train on a record still requires approval for that use. Check approved inputs for [poisoned or irrelevant content](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec06-bp01.html) before training, and log filtering decisions against the dataset version. Cover intermediate files, checkpoints, and final artifacts in retention decisions.

Separate authority across the following roles. Apply the shared identity and data controls to their policies, keys, and credentials.

|
|
| **Role** | **Permitted responsibilities** | **Restricted responsibilities** |
| --- |--- |--- |
| Dataset administrator | Approve dataset access, versions, and retention | Model approval and production deployment |
| Job execution role | Read approved inputs and write job outputs | Unrelated datasets, approval changes, and production deployment |
| Model approver | Review evaluations and approve a specific model version | Modifying the evaluated dataset, code, or artifact |
| Deployment role | Deploy the approved version through the release workflow | Approving that version or replacing the reviewed artifact |

### Amazon Bedrock: protect job data and custom models
<a name="amazon-bedrock-protect-job-data-and-custom-models"></a>

Configure [Bedrock customization encryption](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-custom-job.html) with a customer managed [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) key for the custom model when the organization needs control over key administration. Encrypt input and output S3 buckets separately and scope the job role's bucket and key permissions to its datasets and artifacts. Keep customization, import, and production invocation permissions separate.

For [Amazon Bedrock Custom Model Import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html#model-customization-import-model-source), supply model weights in Safetensors format with the required Hugging Face configuration and tokenizer files. Check the supported architecture and artifact requirements before import.

### Amazon SageMaker AI: protect and approve model versions
<a name="amazon-sagemaker-ai-protect-and-approve-model-versions"></a>

[Amazon SageMaker Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) records model versions and their approval status. Use the `sagemaker:ModelApprovalStatus`[ condition key](https://docs.aws.amazon.com/service-authorization/latest/reference/list_sagemaker.html) with both `CreateModelPackage` and `UpdateModelPackage` to restrict who can submit an `Approved` status. Cover both actions so the training role cannot create an already-approved package or approve it later.

Amazon SageMaker AI requires [versioned model packages to be ](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackage.html)`Approved`[ for deployment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackage.html) via the [ModelApprovalStatus](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackage.html#API_CreateModelPackage_RequestSyntax) parameter. Require the release workflow to check the exact package version and restrict production model and endpoint changes to the release role. The ModelApprovalStatus parameter controls approval-status requests; it does not replace deployment permissions. Test that the training role cannot approve a package or deploy artifacts outside the release workflow. Apply the same review to imported models, including their origin, dependencies, and evaluation evidence.

Where compatible with the framework, prefer [Safetensors for tensor weights](https://aws.amazon.com/blogs/security/enhancing-cloud-security-in-ai-ml-the-little-pickle-story/) over pickle-based formats, which can run code during loading. Verify artifact sources and integrity before loading, and review serving code and dependencies separately. A safer weights format does not establish that the complete model package is safe.

Use customer managed AWS KMS keys for training S3 buckets and [training storage volumes that accept them](https://docs.aws.amazon.com/sagemaker/latest/dg/key-management.html). Some instance types based on the AWS Nitro System use hardware-encrypted local storage and do not accept an AWS KMS key for those volumes. For distributed training, enable [inter-container traffic encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/train-encrypt.html) to help protect communication between training instances. This setting has no effect on a single-instance job and can increase training time.

## AI application security
<a name="ai-application-security"></a>

### Amazon Bedrock: evaluate before enabling inference
<a name="amazon-bedrock-evaluate-before-enabling-inference"></a>

Define release criteria before evaluation. Restrict reviewer access to the prompt and response data approved for the evaluation, including sensitive content in generated responses.

Evaluate customized models for leakage, poisoning effects, harmful output, and task quality using applicable [Amazon Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html) workflows. Add human review when automated measures do not adequately assess quality or safety. [Amazon Bedrock human evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-create-human.html) can evaluate a supported Bedrock model or supplied inference responses. Use representative prompts, clear rating instructions, and reviewers familiar with the intended use.

Record evidence against the exact model version and intended use. Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) [customization events](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-eventbridge.html) to trigger review workflows. Job completion is a starting point for evaluation, not release approval.

Apply [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) when the model serves requests, following the [inference guidance](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/#amazon-bedrock-configure-and-test-inference-guardrails). Guardrails assess inference content; they do not remove sensitive information already learned by model weights.

### Amazon SageMaker AI: evaluate behavior and retain lineage
<a name="amazon-sagemaker-ai-evaluate-behavior-and-retain-lineage"></a>

Define comparison groups and acceptance criteria when bias analysis applies to the model and its intended use. Existing customers can use [Amazon SageMaker Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-detect-post-training-bias.html); Clarify is [no longer available to new customers](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-availability-change.html). For predictive models, [compute standardized bias metrics with pandas and scikit-learn and use SHAP for feature attribution](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-availability-change.html#clarify-configuring-replacements). For language models hosted on SageMaker AI, use the [fmeval library](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-auto-lib.html) or [evaluate saved model responses with Amazon Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-built-in-metrics.html). Prompt-and-response evaluation does not replace predictive model bias and explainability analysis.

Before approval, run [adversarial security tests](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec05-bp01.html) for the model's intended use and record pass criteria. For a generative model, run these checks in an isolated test workflow:
+ Leakage: use synthetic sensitive markers and prompts intended to elicit training examples; check responses for disclosure.
+ Poisoning: submit deliberately modified training data to the validation stage and verify that integrity and provenance checks reject it.
+ Unsafe output: submit disallowed-use and evasion prompts, and review responses against the organization's safety criteria.

Use [Amazon SageMaker ML Lineage Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking-manual-creation.html) to associate code, datasets, and model artifacts with the evaluation. Preserve dataset versions or checksums with the results: [automatic S3 lineage records](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking-auto-creation.html) track the supplied URI, not each file's hash. Keep approval independent of the training job.

Repeat evaluation after changes to the model or serving stack. If your inference application uses Amazon Bedrock Guardrails with SageMaker AI, implement the [explicit ApplyGuardrail integration](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/#amazon-sagemaker-ai-integrate-input-and-output-checks). The ApplyGuardrail integration does not act as a training-data or model-approval control.

### Shared monitoring and rollback evidence
<a name="shared-monitoring-and-rollback-evidence"></a>

Record job failures, approval decisions, and artifact promotion. Use [Amazon CloudWatch metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html) and [AWS CloudTrail](https://docs.aws.amazon.com/sagemaker/latest/dg/logging-using-cloudtrail.html) for applicable operational and API evidence. Configure relevant S3 data events for dataset access. Apply the [shared threat detection](https://dp8l2mfblnx2f.cloudfront.net/architecture/#detect-threats-in-ai-workloads) and [configuration checks](https://dp8l2mfblnx2f.cloudfront.net/architecture/#keep-required-settings-enabled) to the training environment. Correlate findings with the affected dataset, job, and model version.

## Design considerations
<a name="design-considerations"></a>

Customization can incorporate sensitive information into model weights. Before approving that use, review retention, deletion, and possible retraining requirements with the data owner. Keep a previously approved model available for rollback and verify that it can still be deployed under current hosting and residency requirements. Configuration checks, dataset approval, and model evaluation each contribute separate evidence to the release decision.
