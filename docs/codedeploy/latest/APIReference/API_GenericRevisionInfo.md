---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GenericRevisionInfo.html
---

# GenericRevisionInfo
<a name="API_GenericRevisionInfo"></a>

Information about an application revision.

## Contents
<a name="API_GenericRevisionInfo_Contents"></a>

 ** deploymentGroups **   <a name="CodeDeploy-Type-GenericRevisionInfo-deploymentGroups"></a>
The deployment groups for which this is the current target revision.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9+=,.@_-]*`
Required: No

 ** description **   <a name="CodeDeploy-Type-GenericRevisionInfo-description"></a>
A comment about the revision.
Type: String
Required: No

 ** firstUsedTime **   <a name="CodeDeploy-Type-GenericRevisionInfo-firstUsedTime"></a>
When the revision was first used by AWS CodeDeploy.
Type: Timestamp
Required: No

 ** lastUsedTime **   <a name="CodeDeploy-Type-GenericRevisionInfo-lastUsedTime"></a>
When the revision was last used by AWS CodeDeploy.
Type: Timestamp
Required: No

 ** registerTime **   <a name="CodeDeploy-Type-GenericRevisionInfo-registerTime"></a>
When the revision was registered with AWS CodeDeploy.
Type: Timestamp
Required: No

## See Also
<a name="API_GenericRevisionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/GenericRevisionInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/GenericRevisionInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/GenericRevisionInfo)
