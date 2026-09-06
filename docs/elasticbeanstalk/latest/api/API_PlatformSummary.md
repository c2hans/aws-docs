---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_PlatformSummary.html
---

# PlatformSummary
<a name="API_PlatformSummary"></a>

Summary information about a platform version.

## Contents
<a name="API_PlatformSummary_Contents"></a>

 ** OperatingSystemName **
The operating system used by the platform version.
Type: String
Required: No

 ** OperatingSystemVersion **
The version of the operating system used by the platform version.
Type: String
Required: No

 ** PlatformArn **
The ARN of the platform version.
Type: String
Required: No

 ** PlatformBranchLifecycleState **
The state of the platform version's branch in its lifecycle.
Possible values: `beta` \| `supported` \| `deprecated` \| `retired`
Type: String
Required: No

 ** PlatformBranchName **
The platform branch to which the platform version belongs.
Type: String
Required: No

 ** PlatformCategory **
The category of platform version.
Type: String
Required: No

 ** PlatformLifecycleState **
The state of the platform version in its lifecycle.
Possible values: `recommended` \| empty
If an empty value is returned, the platform version is supported but isn't the recommended one for its branch.
Type: String
Required: No

 ** PlatformOwner **
The AWS account ID of the person who created the platform version.
Type: String
Required: No

 ** PlatformStatus **
The status of the platform version. You can create an environment from the platform version once it is ready.
Type: String
Valid Values: `Creating | Failed | Ready | Deleting | Deleted`
Required: No

 ** PlatformVersion **
The version string of the platform version.
Type: String
Required: No

 ** SupportedAddonList.member.N **
The additions associated with the platform version.
Type: Array of strings
Required: No

 ** SupportedTierList.member.N **
The tiers in which the platform version runs.
Type: Array of strings
Required: No

## See Also
<a name="API_PlatformSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/PlatformSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/PlatformSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/PlatformSummary)
