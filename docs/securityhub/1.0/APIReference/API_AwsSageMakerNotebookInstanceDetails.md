---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSageMakerNotebookInstanceDetails.html
---

# AwsSageMakerNotebookInstanceDetails
<a name="API_AwsSageMakerNotebookInstanceDetails"></a>

 Provides details about an Amazon SageMaker AI notebook instance.

## Contents
<a name="API_AwsSageMakerNotebookInstanceDetails_Contents"></a>

 ** AcceleratorTypes **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-AcceleratorTypes"></a>
 A list of Amazon Elastic Inference instance types to associate with the notebook instance. Currently, only one instance type can be associated with a notebook instance.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** AdditionalCodeRepositories **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-AdditionalCodeRepositories"></a>
 An array of up to three Git repositories associated with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see [Associating Git repositories with SageMaker AI notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html) in the *Amazon SageMaker AI Developer Guide*.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** DefaultCodeRepository **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-DefaultCodeRepository"></a>
 The Git repository associated with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see [Associating Git repositories with SageMaker AI notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html) in the *Amazon SageMaker AI Developer Guide*.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DirectInternetAccess **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-DirectInternetAccess"></a>
 Sets whether SageMaker AI provides internet access to the notebook instance. If you set this to `Disabled`, this notebook instance is able to access resources only in your VPC, and is not be able to connect to SageMaker AI training and endpoint services unless you configure a Network Address Translation (NAT) Gateway in your VPC.
Type: String
Pattern: `.*\S.*`
Required: No

 ** FailureReason **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-FailureReason"></a>
 If status of the instance is `Failed`, the reason it failed.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceMetadataServiceConfiguration **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-InstanceMetadataServiceConfiguration"></a>
 Information on the IMDS configuration of the notebook instance.
Type: [AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails](API_AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails.md) object
Required: No

 ** InstanceType **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-InstanceType"></a>
 The type of machine learning (ML) compute instance to launch for the notebook instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KmsKeyId **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-KmsKeyId"></a>
 The Amazon Resource Name (ARN) of an AWS Key Management Service (AWS KMS) key that SageMaker AI uses to encrypt data on the storage volume attached to your notebook instance. The KMS key you provide must be enabled. For information, see [Enabling and disabling keys](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) in the * AWS Key Management Service Developer Guide*.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NetworkInterfaceId **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-NetworkInterfaceId"></a>
 The network interface ID that SageMaker AI created when the instance was created.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NotebookInstanceArn **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-NotebookInstanceArn"></a>
 The Amazon Resource Name (ARN) of the notebook instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NotebookInstanceLifecycleConfigName **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-NotebookInstanceLifecycleConfigName"></a>
 The name of a notebook instance lifecycle configuration.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NotebookInstanceName **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-NotebookInstanceName"></a>
 The name of the new notebook instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NotebookInstanceStatus **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-NotebookInstanceStatus"></a>
 The status of the notebook instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PlatformIdentifier **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-PlatformIdentifier"></a>
 The platform identifier of the notebook instance runtime environment.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RoleArn **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-RoleArn"></a>
 The Amazon Resource Name (ARN) of the IAM role associated with the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RootAccess **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-RootAccess"></a>
 Whether root access is enabled or disabled for users of the notebook instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SecurityGroups **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-SecurityGroups"></a>
 The VPC security group IDs.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SubnetId **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-SubnetId"></a>
 The ID of the VPC subnet to which you have a connectivity from your ML compute instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Url **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-Url"></a>
 The URL that you use to connect to the Jupyter notebook that is running in your notebook instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VolumeSizeInGB **   <a name="securityhub-Type-AwsSageMakerNotebookInstanceDetails-VolumeSizeInGB"></a>
 The size, in GB, of the ML storage volume to attach to the notebook instance.
Type: Integer
Required: No

## See Also
<a name="API_AwsSageMakerNotebookInstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsSageMakerNotebookInstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsSageMakerNotebookInstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsSageMakerNotebookInstanceDetails)
