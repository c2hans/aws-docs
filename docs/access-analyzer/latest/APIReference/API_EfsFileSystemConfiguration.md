---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_EfsFileSystemConfiguration.html
---

# EfsFileSystemConfiguration
<a name="API_EfsFileSystemConfiguration"></a>

The proposed access control configuration for an Amazon EFS file system. You can propose a configuration for a new Amazon EFS file system or an existing Amazon EFS file system that you own by specifying the Amazon EFS policy. For more information, see [Using file systems in Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/using-fs.html).
+ If the configuration is for an existing Amazon EFS file system and you do not specify the Amazon EFS policy, then the access preview uses the existing Amazon EFS policy for the file system.
+ If the access preview is for a new resource and you do not specify the policy, then the access preview assumes an Amazon EFS file system without a policy.
+ To propose deletion of an existing Amazon EFS file system policy, you can specify an empty string for the Amazon EFS policy.

## Contents
<a name="API_EfsFileSystemConfiguration_Contents"></a>

 ** fileSystemPolicy **   <a name="accessanalyzer-Type-EfsFileSystemConfiguration-fileSystemPolicy"></a>
The JSON policy definition to apply to the Amazon EFS file system. For more information on the elements that make up a file system policy, see [Amazon EFS Resource-based policies](https://docs.aws.amazon.com/efs/latest/ug/access-control-overview.html#access-control-manage-access-intro-resource-policies).
Type: String
Required: No

## See Also
<a name="API_EfsFileSystemConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/EfsFileSystemConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/EfsFileSystemConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/EfsFileSystemConfiguration)
