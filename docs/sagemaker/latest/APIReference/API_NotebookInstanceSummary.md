---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_NotebookInstanceSummary.html
---

# NotebookInstanceSummary
<a name="API_NotebookInstanceSummary"></a>

Provides summary information for an SageMaker AI notebook instance.

## Contents
<a name="API_NotebookInstanceSummary_Contents"></a>

 ** NotebookInstanceArn **   <a name="sagemaker-Type-NotebookInstanceSummary-NotebookInstanceArn"></a>
The Amazon Resource Name (ARN) of the notebook instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** NotebookInstanceName **   <a name="sagemaker-Type-NotebookInstanceSummary-NotebookInstanceName"></a>
The name of the notebook instance that you want a summary for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** AdditionalCodeRepositories **   <a name="sagemaker-Type-NotebookInstanceSummary-AdditionalCodeRepositories"></a>
An array of up to three Git repositories associated with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see [Associating Git Repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `https://([^/]+)/?(.*)$|^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** CreationTime **   <a name="sagemaker-Type-NotebookInstanceSummary-CreationTime"></a>
A timestamp that shows when the notebook instance was created.
Type: Timestamp
Required: No

 ** DefaultCodeRepository **   <a name="sagemaker-Type-NotebookInstanceSummary-DefaultCodeRepository"></a>
The Git repository associated with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see [Associating Git Repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `https://([^/]+)/?(.*)$|^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** InstanceType **   <a name="sagemaker-Type-NotebookInstanceSummary-InstanceType"></a>
The type of ML compute instance that the notebook instance is running on.
Type: String
Valid Values: `ml.t2.medium | ml.t2.large | ml.t2.xlarge | ml.t2.2xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.m5d.large | ml.m5d.xlarge | ml.m5d.2xlarge | ml.m5d.4xlarge | ml.m5d.8xlarge | ml.m5d.12xlarge | ml.m5d.16xlarge | ml.m5d.24xlarge | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.c5d.xlarge | ml.c5d.2xlarge | ml.c5d.4xlarge | ml.c5d.9xlarge | ml.c5d.18xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.p3dn.24xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.8xlarge | ml.r5.12xlarge | ml.r5.16xlarge | ml.r5.24xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.16xlarge | ml.g5.12xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.inf1.xlarge | ml.inf1.2xlarge | ml.inf1.6xlarge | ml.inf1.24xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.inf2.xlarge | ml.inf2.8xlarge | ml.inf2.24xlarge | ml.inf2.48xlarge | ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p6-b200.48xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.m6id.large | ml.m6id.xlarge | ml.m6id.2xlarge | ml.m6id.4xlarge | ml.m6id.8xlarge | ml.m6id.12xlarge | ml.m6id.16xlarge | ml.m6id.24xlarge | ml.m6id.32xlarge | ml.c6id.large | ml.c6id.xlarge | ml.c6id.2xlarge | ml.c6id.4xlarge | ml.c6id.8xlarge | ml.c6id.12xlarge | ml.c6id.16xlarge | ml.c6id.24xlarge | ml.c6id.32xlarge | ml.r6id.large | ml.r6id.xlarge | ml.r6id.2xlarge | ml.r6id.4xlarge | ml.r6id.8xlarge | ml.r6id.12xlarge | ml.r6id.16xlarge | ml.r6id.24xlarge | ml.r6id.32xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.p5.4xlarge | ml.p5en.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge`
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-NotebookInstanceSummary-LastModifiedTime"></a>
A timestamp that shows when the notebook instance was last modified.
Type: Timestamp
Required: No

 ** NotebookInstanceLifecycleConfigName **   <a name="sagemaker-Type-NotebookInstanceSummary-NotebookInstanceLifecycleConfigName"></a>
The name of a notebook instance lifecycle configuration associated with this notebook instance.
For information about notebook instance lifestyle configurations, see [Step 2.1: (Optional) Customize a Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** NotebookInstanceStatus **   <a name="sagemaker-Type-NotebookInstanceSummary-NotebookInstanceStatus"></a>
The status of the notebook instance.
Type: String
Valid Values: `Pending | InService | Stopping | Stopped | Failed | Deleting | Updating`
Required: No

 ** Url **   <a name="sagemaker-Type-NotebookInstanceSummary-Url"></a>
The URL that you use to connect to the Jupyter notebook running in your notebook instance.
Type: String
Required: No

## See Also
<a name="API_NotebookInstanceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/NotebookInstanceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/NotebookInstanceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/NotebookInstanceSummary)
