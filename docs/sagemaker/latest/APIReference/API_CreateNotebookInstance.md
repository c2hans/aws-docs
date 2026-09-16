---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateNotebookInstance.html
---

# CreateNotebookInstance
<a name="API_CreateNotebookInstance"></a>

Creates an SageMaker AI notebook instance. A notebook instance is a machine learning (ML) compute instance running on a Jupyter notebook.

In a `CreateNotebookInstance` request, specify the type of ML compute instance that you want to run. SageMaker AI launches the instance, installs common libraries that you can use to explore datasets for model training, and attaches an ML storage volume to the notebook instance.

SageMaker AI also provides a set of example notebooks. Each notebook demonstrates how to use SageMaker AI with a specific algorithm or with a machine learning framework.

After receiving the request, SageMaker AI does the following:

1. Creates a network interface in the SageMaker AI VPC.

1. (Option) If you specified `SubnetId`, SageMaker AI creates a network interface in your own VPC, which is inferred from the subnet ID that you provide in the input. When creating this network interface, SageMaker AI attaches the security group that you specified in the request to the network interface that it creates in your VPC.

1. Launches an EC2 instance of the type specified in the request in the SageMaker AI VPC. If you specified `SubnetId` of your VPC, SageMaker AI specifies both network interfaces when launching this instance. This enables inbound traffic from your own VPC to the notebook instance, assuming that the security groups allow it.

After creating the notebook instance, SageMaker AI returns its Amazon Resource Name (ARN). You can't change the name of a notebook instance after you create it.

After SageMaker AI creates the notebook instance, you can connect to the Jupyter server and work in Jupyter notebooks. For example, you can write code to explore a dataset that you can use for model training, train a model, host models by creating SageMaker AI endpoints, and validate hosted models.

For more information, see [How It Works](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html).

## Request Syntax
<a name="API_CreateNotebookInstance_RequestSyntax"></a>

```
{
   "AcceleratorTypes": [ "{{string}}" ],
   "AdditionalCodeRepositories": [ "{{string}}" ],
   "DefaultCodeRepository": "{{string}}",
   "DirectInternetAccess": "{{string}}",
   "InstanceMetadataServiceConfiguration": {
      "MinimumInstanceMetadataServiceVersion": "{{string}}"
   },
   "InstanceType": "{{string}}",
   "IpAddressType": "{{string}}",
   "KmsKeyId": "{{string}}",
   "LifecycleConfigName": "{{string}}",
   "NotebookInstanceName": "{{string}}",
   "PlatformIdentifier": "{{string}}",
   "RoleArn": "{{string}}",
   "RootAccess": "{{string}}",
   "SecurityGroupIds": [ "{{string}}" ],
   "SubnetId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VolumeSizeInGB": {{number}}
}
```

## Request Parameters
<a name="API_CreateNotebookInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AcceleratorTypes](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-AcceleratorTypes"></a>
This parameter is no longer supported. Elastic Inference (EI) is no longer available.
This parameter was used to specify a list of EI instance types to associate with this notebook instance.
Type: Array of strings
Valid Values: `ml.eia1.medium | ml.eia1.large | ml.eia1.xlarge | ml.eia2.medium | ml.eia2.large | ml.eia2.xlarge`
Required: No

 ** [AdditionalCodeRepositories](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-AdditionalCodeRepositories"></a>
An array of up to three Git repositories to associate with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see [Associating Git Repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `https://([^/]+)/?(.*)$|^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** [DefaultCodeRepository](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-DefaultCodeRepository"></a>
A Git repository to associate with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see [Associating Git Repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `https://([^/]+)/?(.*)$|^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** [DirectInternetAccess](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-DirectInternetAccess"></a>
Sets whether SageMaker AI provides internet access to the notebook instance. If you set this to `Disabled` this notebook instance is able to access resources only in your VPC, and is not be able to connect to SageMaker AI training and endpoint services unless you configure a NAT Gateway in your VPC.
For more information, see [Notebook Instances Are Internet-Enabled by Default](https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-additional-considerations.html#appendix-notebook-and-internet-access). You can set the value of this parameter to `Disabled` only if you set a value for the `SubnetId` parameter.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** [InstanceMetadataServiceConfiguration](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-InstanceMetadataServiceConfiguration"></a>
Information on the IMDS configuration of the notebook instance
Type: [InstanceMetadataServiceConfiguration](API_InstanceMetadataServiceConfiguration.md) object
Required: No

 ** [InstanceType](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-InstanceType"></a>
The type of ML compute instance to launch for the notebook instance.
Type: String
Valid Values: `ml.t2.medium | ml.t2.large | ml.t2.xlarge | ml.t2.2xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.m5d.large | ml.m5d.xlarge | ml.m5d.2xlarge | ml.m5d.4xlarge | ml.m5d.8xlarge | ml.m5d.12xlarge | ml.m5d.16xlarge | ml.m5d.24xlarge | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.c5d.xlarge | ml.c5d.2xlarge | ml.c5d.4xlarge | ml.c5d.9xlarge | ml.c5d.18xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.p3dn.24xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.8xlarge | ml.r5.12xlarge | ml.r5.16xlarge | ml.r5.24xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.16xlarge | ml.g5.12xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.inf1.xlarge | ml.inf1.2xlarge | ml.inf1.6xlarge | ml.inf1.24xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.inf2.xlarge | ml.inf2.8xlarge | ml.inf2.24xlarge | ml.inf2.48xlarge | ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p6-b200.48xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.m6id.large | ml.m6id.xlarge | ml.m6id.2xlarge | ml.m6id.4xlarge | ml.m6id.8xlarge | ml.m6id.12xlarge | ml.m6id.16xlarge | ml.m6id.24xlarge | ml.m6id.32xlarge | ml.c6id.large | ml.c6id.xlarge | ml.c6id.2xlarge | ml.c6id.4xlarge | ml.c6id.8xlarge | ml.c6id.12xlarge | ml.c6id.16xlarge | ml.c6id.24xlarge | ml.c6id.32xlarge | ml.r6id.large | ml.r6id.xlarge | ml.r6id.2xlarge | ml.r6id.4xlarge | ml.r6id.8xlarge | ml.r6id.12xlarge | ml.r6id.16xlarge | ml.r6id.24xlarge | ml.r6id.32xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.p5.4xlarge | ml.p5en.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge`
Required: Yes

 ** [IpAddressType](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-IpAddressType"></a>
The IP address type for the notebook instance. Specify `ipv4` for IPv4-only connectivity or `dualstack` for both IPv4 and IPv6 connectivity. When you specify `dualstack`, the subnet must support IPv6 CIDR blocks. If not specified, defaults to `ipv4`.
Type: String
Valid Values: `ipv4 | dualstack`
Required: No

 ** [KmsKeyId](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-KmsKeyId"></a>
The Amazon Resource Name (ARN) of a AWS Key Management Service key that SageMaker AI uses to encrypt data on the storage volume attached to your notebook instance. The KMS key you provide must be enabled. For information, see [Enabling and Disabling Keys](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** [LifecycleConfigName](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-LifecycleConfigName"></a>
The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see [Step 2.1: (Optional) Customize a Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** [NotebookInstanceName](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-NotebookInstanceName"></a>
The name of the new notebook instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** [PlatformIdentifier](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-PlatformIdentifier"></a>
The platform identifier of the notebook instance runtime environment. The default value is `notebook-al2023-v1`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.
Pattern: `(notebook-al1-v1|notebook-al2-v1|notebook-al2-v2|notebook-al2-v3|notebook-al2023-v1)`
Required: No

 ** [RoleArn](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-RoleArn"></a>
 When you send any requests to AWS resources from the notebook instance, SageMaker AI assumes this role to perform tasks on your behalf. You must grant this role necessary permissions so SageMaker AI can perform these tasks. The policy must allow the SageMaker AI service principal (sagemaker.amazonaws.com) permissions to assume this role. For more information, see [SageMaker AI Roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html).
To be able to pass this role to SageMaker AI, the caller of this API must have the `iam:PassRole` permission.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [RootAccess](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-RootAccess"></a>
Whether root access is enabled or disabled for users of the notebook instance. The default value is `Enabled`.
Lifecycle configurations need root access to be able to set up a notebook instance. Because of this, lifecycle configurations associated with a notebook instance always run with root access even if you disable root access for users.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** [SecurityGroupIds](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-SecurityGroupIds"></a>
The VPC security group IDs, in the form sg-xxxxxxxx. The security groups must be for the same VPC as specified in the subnet.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: No

 ** [SubnetId](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-SubnetId"></a>
The ID of the subnet in a VPC to which you would like to have a connectivity from your ML compute instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: No

 ** [Tags](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [VolumeSizeInGB](#API_CreateNotebookInstance_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstance-request-VolumeSizeInGB"></a>
The size, in GB, of the ML storage volume to attach to the notebook instance. The default value is 5 GB.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 16384.
Required: No

## Response Syntax
<a name="API_CreateNotebookInstance_ResponseSyntax"></a>

```
{
   "NotebookInstanceArn": "string"
}
```

## Response Elements
<a name="API_CreateNotebookInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NotebookInstanceArn](#API_CreateNotebookInstance_ResponseSyntax) **   <a name="sagemaker-CreateNotebookInstance-response-NotebookInstanceArn"></a>
The Amazon Resource Name (ARN) of the notebook instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateNotebookInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateNotebookInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateNotebookInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateNotebookInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateNotebookInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateNotebookInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateNotebookInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateNotebookInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateNotebookInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateNotebookInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateNotebookInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateNotebookInstance)
