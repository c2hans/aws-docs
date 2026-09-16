---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateNotebookInstance.html
---

# UpdateNotebookInstance
<a name="API_UpdateNotebookInstance"></a>

Updates a notebook instance. NotebookInstance updates include upgrading or downgrading the ML compute instance used for your notebook instance to accommodate changes in your workload requirements.

**Note**
This API can attach lifecycle configurations to notebook instances. Lifecycle configuration scripts execute with root access and the notebook instance's IAM execution role privileges. Principals with this permission and access to lifecycle configurations can execute code with the execution role's credentials. See [Customize a Notebook Instance Using a Lifecycle Configuration Script](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html) for security best practices.

## Request Syntax
<a name="API_UpdateNotebookInstance_RequestSyntax"></a>

```
{
   "AcceleratorTypes": [ "{{string}}" ],
   "AdditionalCodeRepositories": [ "{{string}}" ],
   "DefaultCodeRepository": "{{string}}",
   "DisassociateAcceleratorTypes": {{boolean}},
   "DisassociateAdditionalCodeRepositories": {{boolean}},
   "DisassociateDefaultCodeRepository": {{boolean}},
   "DisassociateLifecycleConfig": {{boolean}},
   "InstanceMetadataServiceConfiguration": {
      "MinimumInstanceMetadataServiceVersion": "{{string}}"
   },
   "InstanceType": "{{string}}",
   "IpAddressType": "{{string}}",
   "LifecycleConfigName": "{{string}}",
   "NotebookInstanceName": "{{string}}",
   "PlatformIdentifier": "{{string}}",
   "RoleArn": "{{string}}",
   "RootAccess": "{{string}}",
   "VolumeSizeInGB": {{number}}
}
```

## Request Parameters
<a name="API_UpdateNotebookInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AcceleratorTypes](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-AcceleratorTypes"></a>
This parameter is no longer supported. Elastic Inference (EI) is no longer available.
This parameter was used to specify a list of the EI instance types to associate with this notebook instance.
Type: Array of strings
Valid Values: `ml.eia1.medium | ml.eia1.large | ml.eia1.xlarge | ml.eia2.medium | ml.eia2.large | ml.eia2.xlarge`
Required: No

 ** [AdditionalCodeRepositories](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-AdditionalCodeRepositories"></a>
An array of up to three Git repositories to associate with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see [Associating Git Repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `https://([^/]+)/?(.*)$|^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** [DefaultCodeRepository](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-DefaultCodeRepository"></a>
The Git repository to associate with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see [Associating Git Repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `https://([^/]+)/?(.*)$|^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** [DisassociateAcceleratorTypes](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-DisassociateAcceleratorTypes"></a>
This parameter is no longer supported. Elastic Inference (EI) is no longer available.
This parameter was used to specify a list of the EI instance types to remove from this notebook instance.
Type: Boolean
Required: No

 ** [DisassociateAdditionalCodeRepositories](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-DisassociateAdditionalCodeRepositories"></a>
A list of names or URLs of the default Git repositories to remove from this notebook instance. This operation is idempotent. If you specify a Git repository that is not associated with the notebook instance when you call this method, it does not throw an error.
Type: Boolean
Required: No

 ** [DisassociateDefaultCodeRepository](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-DisassociateDefaultCodeRepository"></a>
The name or URL of the default Git repository to remove from this notebook instance. This operation is idempotent. If you specify a Git repository that is not associated with the notebook instance when you call this method, it does not throw an error.
Type: Boolean
Required: No

 ** [DisassociateLifecycleConfig](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-DisassociateLifecycleConfig"></a>
Set to `true` to remove the notebook instance lifecycle configuration currently associated with the notebook instance. This operation is idempotent. If you specify a lifecycle configuration that is not associated with the notebook instance when you call this method, it does not throw an error.
Type: Boolean
Required: No

 ** [InstanceMetadataServiceConfiguration](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-InstanceMetadataServiceConfiguration"></a>
Information on the IMDS configuration of the notebook instance
Type: [InstanceMetadataServiceConfiguration](API_InstanceMetadataServiceConfiguration.md) object
Required: No

 ** [InstanceType](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-InstanceType"></a>
The Amazon ML compute instance type.
Type: String
Valid Values: `ml.t2.medium | ml.t2.large | ml.t2.xlarge | ml.t2.2xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.m5d.large | ml.m5d.xlarge | ml.m5d.2xlarge | ml.m5d.4xlarge | ml.m5d.8xlarge | ml.m5d.12xlarge | ml.m5d.16xlarge | ml.m5d.24xlarge | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.c5d.xlarge | ml.c5d.2xlarge | ml.c5d.4xlarge | ml.c5d.9xlarge | ml.c5d.18xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.p3dn.24xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.8xlarge | ml.r5.12xlarge | ml.r5.16xlarge | ml.r5.24xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.16xlarge | ml.g5.12xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.inf1.xlarge | ml.inf1.2xlarge | ml.inf1.6xlarge | ml.inf1.24xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.inf2.xlarge | ml.inf2.8xlarge | ml.inf2.24xlarge | ml.inf2.48xlarge | ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p6-b200.48xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.m6id.large | ml.m6id.xlarge | ml.m6id.2xlarge | ml.m6id.4xlarge | ml.m6id.8xlarge | ml.m6id.12xlarge | ml.m6id.16xlarge | ml.m6id.24xlarge | ml.m6id.32xlarge | ml.c6id.large | ml.c6id.xlarge | ml.c6id.2xlarge | ml.c6id.4xlarge | ml.c6id.8xlarge | ml.c6id.12xlarge | ml.c6id.16xlarge | ml.c6id.24xlarge | ml.c6id.32xlarge | ml.r6id.large | ml.r6id.xlarge | ml.r6id.2xlarge | ml.r6id.4xlarge | ml.r6id.8xlarge | ml.r6id.12xlarge | ml.r6id.16xlarge | ml.r6id.24xlarge | ml.r6id.32xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.p5.4xlarge | ml.p5en.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge`
Required: No

 ** [IpAddressType](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-IpAddressType"></a>
The IP address type for the notebook instance. Specify `ipv4` for IPv4-only connectivity or `dualstack` for both IPv4 and IPv6 connectivity. The notebook instance must be stopped before updating this setting. When you specify `dualstack`, the subnet must support IPv6 addressing.
Type: String
Valid Values: `ipv4 | dualstack`
Required: No

 ** [LifecycleConfigName](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-LifecycleConfigName"></a>
The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see [Step 2.1: (Optional) Customize a Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** [NotebookInstanceName](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-NotebookInstanceName"></a>
The name of the notebook instance to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** [PlatformIdentifier](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-PlatformIdentifier"></a>
The platform identifier of the notebook instance runtime environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.
Pattern: `(notebook-al1-v1|notebook-al2-v1|notebook-al2-v2|notebook-al2-v3|notebook-al2023-v1)`
Required: No

 ** [RoleArn](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that SageMaker AI can assume to access the notebook instance. For more information, see [SageMaker AI Roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html).
To be able to pass this role to SageMaker AI, the caller of this API must have the `iam:PassRole` permission.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** [RootAccess](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-RootAccess"></a>
Whether root access is enabled or disabled for users of the notebook instance. The default value is `Enabled`.
If you set this to `Disabled`, users don't have root access on the notebook instance, but lifecycle configuration scripts still run with root permissions.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** [VolumeSizeInGB](#API_UpdateNotebookInstance_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstance-request-VolumeSizeInGB"></a>
The size, in GB, of the ML storage volume to attach to the notebook instance. The default value is 5 GB. ML storage volumes are encrypted, so SageMaker AI can't determine the amount of available free space on the volume. Because of this, you can increase the volume size when you update a notebook instance, but you can't decrease the volume size. If you want to decrease the size of the ML storage volume in use, create a new notebook instance with the desired size.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 16384.
Required: No

## Response Elements
<a name="API_UpdateNotebookInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateNotebookInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_UpdateNotebookInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateNotebookInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateNotebookInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateNotebookInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateNotebookInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateNotebookInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateNotebookInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateNotebookInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateNotebookInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateNotebookInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateNotebookInstance)
