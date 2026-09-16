---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeNotebookInstance.html
---

# DescribeNotebookInstance
<a name="API_DescribeNotebookInstance"></a>

Returns information about a notebook instance.

## Request Syntax
<a name="API_DescribeNotebookInstance_RequestSyntax"></a>

```
{
   "NotebookInstanceName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeNotebookInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NotebookInstanceName](#API_DescribeNotebookInstance_RequestSyntax) **   <a name="sagemaker-DescribeNotebookInstance-request-NotebookInstanceName"></a>
The name of the notebook instance that you want information about.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

## Response Syntax
<a name="API_DescribeNotebookInstance_ResponseSyntax"></a>

```
{
   "AcceleratorTypes": [ "string" ],
   "AdditionalCodeRepositories": [ "string" ],
   "CreationTime": number,
   "DefaultCodeRepository": "string",
   "DirectInternetAccess": "string",
   "FailureReason": "string",
   "InstanceMetadataServiceConfiguration": {
      "MinimumInstanceMetadataServiceVersion": "string"
   },
   "InstanceType": "string",
   "IpAddressType": "string",
   "KmsKeyId": "string",
   "LastModifiedTime": number,
   "NetworkInterfaceId": "string",
   "NotebookInstanceArn": "string",
   "NotebookInstanceLifecycleConfigName": "string",
   "NotebookInstanceName": "string",
   "NotebookInstanceStatus": "string",
   "PlatformIdentifier": "string",
   "RoleArn": "string",
   "RootAccess": "string",
   "SecurityGroups": [ "string" ],
   "SubnetId": "string",
   "Url": "string",
   "VolumeSizeInGB": number
}
```

## Response Elements
<a name="API_DescribeNotebookInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AcceleratorTypes](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-AcceleratorTypes"></a>
This parameter is no longer supported. Elastic Inference (EI) is no longer available.
This parameter was used to specify a list of the EI instance types associated with this notebook instance.
Type: Array of strings
Valid Values: `ml.eia1.medium | ml.eia1.large | ml.eia1.xlarge | ml.eia2.medium | ml.eia2.large | ml.eia2.xlarge`

 ** [AdditionalCodeRepositories](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-AdditionalCodeRepositories"></a>
An array of up to three Git repositories associated with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see [Associating Git Repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `https://([^/]+)/?(.*)$|^[a-zA-Z0-9](-*[a-zA-Z0-9])*`

 ** [CreationTime](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-CreationTime"></a>
A timestamp. Use this parameter to return the time when the notebook instance was created
Type: Timestamp

 ** [DefaultCodeRepository](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-DefaultCodeRepository"></a>
The Git repository associated with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see [Associating Git Repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `https://([^/]+)/?(.*)$|^[a-zA-Z0-9](-*[a-zA-Z0-9])*`

 ** [DirectInternetAccess](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-DirectInternetAccess"></a>
Describes whether SageMaker AI provides internet access to the notebook instance. If this value is set to *Disabled*, the notebook instance does not have internet access, and cannot connect to SageMaker AI training and endpoint services.
For more information, see [Notebook Instances Are Internet-Enabled by Default](https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-additional-considerations.html#appendix-notebook-and-internet-access).
Type: String
Valid Values: `Enabled | Disabled`

 ** [FailureReason](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-FailureReason"></a>
If status is `Failed`, the reason it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [InstanceMetadataServiceConfiguration](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-InstanceMetadataServiceConfiguration"></a>
Information on the IMDS configuration of the notebook instance
Type: [InstanceMetadataServiceConfiguration](API_InstanceMetadataServiceConfiguration.md) object

 ** [InstanceType](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-InstanceType"></a>
The type of ML compute instance running on the notebook instance.
Type: String
Valid Values: `ml.t2.medium | ml.t2.large | ml.t2.xlarge | ml.t2.2xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.m5d.large | ml.m5d.xlarge | ml.m5d.2xlarge | ml.m5d.4xlarge | ml.m5d.8xlarge | ml.m5d.12xlarge | ml.m5d.16xlarge | ml.m5d.24xlarge | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.c5d.xlarge | ml.c5d.2xlarge | ml.c5d.4xlarge | ml.c5d.9xlarge | ml.c5d.18xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.p3dn.24xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.8xlarge | ml.r5.12xlarge | ml.r5.16xlarge | ml.r5.24xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.16xlarge | ml.g5.12xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.inf1.xlarge | ml.inf1.2xlarge | ml.inf1.6xlarge | ml.inf1.24xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.inf2.xlarge | ml.inf2.8xlarge | ml.inf2.24xlarge | ml.inf2.48xlarge | ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p6-b200.48xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.m6id.large | ml.m6id.xlarge | ml.m6id.2xlarge | ml.m6id.4xlarge | ml.m6id.8xlarge | ml.m6id.12xlarge | ml.m6id.16xlarge | ml.m6id.24xlarge | ml.m6id.32xlarge | ml.c6id.large | ml.c6id.xlarge | ml.c6id.2xlarge | ml.c6id.4xlarge | ml.c6id.8xlarge | ml.c6id.12xlarge | ml.c6id.16xlarge | ml.c6id.24xlarge | ml.c6id.32xlarge | ml.r6id.large | ml.r6id.xlarge | ml.r6id.2xlarge | ml.r6id.4xlarge | ml.r6id.8xlarge | ml.r6id.12xlarge | ml.r6id.16xlarge | ml.r6id.24xlarge | ml.r6id.32xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.p5.4xlarge | ml.p5en.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge`

 ** [IpAddressType](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-IpAddressType"></a>
The IP address type configured for the notebook instance. Returns `ipv4` for IPv4-only connectivity or `dualstack` for both IPv4 and IPv6 connectivity.
Type: String
Valid Values: `ipv4 | dualstack`

 ** [KmsKeyId](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-KmsKeyId"></a>
The AWS KMS key ID SageMaker AI uses to encrypt data when storing it on the ML storage volume attached to the instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`

 ** [LastModifiedTime](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-LastModifiedTime"></a>
A timestamp. Use this parameter to retrieve the time when the notebook instance was last modified.
Type: Timestamp

 ** [NetworkInterfaceId](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-NetworkInterfaceId"></a>
The network interface IDs that SageMaker AI created at the time of creating the instance.
Type: String

 ** [NotebookInstanceArn](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-NotebookInstanceArn"></a>
The Amazon Resource Name (ARN) of the notebook instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [NotebookInstanceLifecycleConfigName](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-NotebookInstanceLifecycleConfigName"></a>
Returns the name of a notebook instance lifecycle configuration.
For information about notebook instance lifestyle configurations, see [Step 2.1: (Optional) Customize a Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`

 ** [NotebookInstanceName](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-NotebookInstanceName"></a>
The name of the SageMaker AI notebook instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`

 ** [NotebookInstanceStatus](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-NotebookInstanceStatus"></a>
The status of the notebook instance.
Type: String
Valid Values: `Pending | InService | Stopping | Stopped | Failed | Deleting | Updating | PendingMaintenance | InMaintenance`

 ** [PlatformIdentifier](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-PlatformIdentifier"></a>
The platform identifier of the notebook instance runtime environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.
Pattern: `(notebook-al1-v1|notebook-al2-v1|notebook-al2-v2|notebook-al2-v3|notebook-al2023-v1)`

 ** [RoleArn](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the instance.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [RootAccess](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-RootAccess"></a>
Whether root access is enabled or disabled for users of the notebook instance.
Lifecycle configurations need root access to be able to set up a notebook instance. Because of this, lifecycle configurations associated with a notebook instance always run with root access even if you disable root access for users.
Type: String
Valid Values: `Enabled | Disabled`

 ** [SecurityGroups](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-SecurityGroups"></a>
The IDs of the VPC security groups.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`

 ** [SubnetId](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-SubnetId"></a>
The ID of the VPC subnet.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`

 ** [Url](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-Url"></a>
The URL that you use to connect to the Jupyter notebook that is running in your notebook instance.
Type: String

 ** [VolumeSizeInGB](#API_DescribeNotebookInstance_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstance-response-VolumeSizeInGB"></a>
The size, in GB, of the ML storage volume attached to the notebook instance.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 16384.

## Errors
<a name="API_DescribeNotebookInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeNotebookInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeNotebookInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeNotebookInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeNotebookInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeNotebookInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeNotebookInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeNotebookInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeNotebookInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeNotebookInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeNotebookInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeNotebookInstance)
