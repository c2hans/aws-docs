---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_PlatformBranchSummary.html
---

# PlatformBranchSummary
<a name="API_PlatformBranchSummary"></a>

Summary information about a platform branch.

## Contents
<a name="API_PlatformBranchSummary_Contents"></a>

 ** BranchName **
The name of the platform branch.
Type: String
Required: No

 ** BranchOrder **
An ordinal number that designates the order in which platform branches have been added to a platform. This can be helpful, for example, if your code calls the `ListPlatformBranches` action and then displays a list of platform branches.
A larger `BranchOrder` value designates a newer platform branch within the platform.
Type: Integer
Required: No

 ** LifecycleState **
The support life cycle state of the platform branch.
Possible values: `beta` \| `supported` \| `deprecated` \| `retired`
Type: String
Required: No

 ** PlatformName **
The name of the platform to which this platform branch belongs.
Type: String
Required: No

 ** SupportedTierList.member.N **
The environment tiers that platform versions in this branch support.
Possible values: `WebServer/Standard` \| `Worker/SQS/HTTP`
Type: Array of strings
Required: No

## See Also
<a name="API_PlatformBranchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/PlatformBranchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/PlatformBranchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/PlatformBranchSummary)
