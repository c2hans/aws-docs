---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_PlatformDescription.html
---

# PlatformDescription
<a name="API_PlatformDescription"></a>

Detailed information about a platform version.

## Contents
<a name="API_PlatformDescription_Contents"></a>

 ** CustomAmiList.member.N **
The custom AMIs supported by the platform version.
Type: Array of [CustomAmi](API_CustomAmi.md) objects
Required: No

 ** DateCreated **
The date when the platform version was created.
Type: Timestamp
Required: No

 ** DateUpdated **
The date when the platform version was last updated.
Type: Timestamp
Required: No

 ** Description **
The description of the platform version.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 ** Frameworks.member.N **
The frameworks supported by the platform version.
Type: Array of [PlatformFramework](API_PlatformFramework.md) objects
Required: No

 ** Maintainer **
Information about the maintainer of the platform version.
Type: String
Required: No

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
Possible values: `Beta` \| `Supported` \| `Deprecated` \| `Retired`
Type: String
Required: No

 ** PlatformBranchName **
The platform branch to which the platform version belongs.
Type: String
Required: No

 ** PlatformCategory **
The category of the platform version.
Type: String
Required: No

 ** PlatformLifecycleState **
The state of the platform version in its lifecycle.
Possible values: `Recommended` \| `null`
If a null value is returned, the platform version isn't the recommended one for its branch. Each platform branch has a single recommended platform version, typically the most recent one.
Type: String
Required: No

 ** PlatformName **
The name of the platform version.
Type: String
Required: No

 ** PlatformOwner **
The AWS account ID of the person who created the platform version.
Type: String
Required: No

 ** PlatformStatus **
The status of the platform version.
Type: String
Valid Values: `Creating | Failed | Ready | Deleting | Deleted`
Required: No

 ** PlatformVersion **
The version of the platform version.
Type: String
Required: No

 ** ProgrammingLanguages.member.N **
The programming languages supported by the platform version.
Type: Array of [PlatformProgrammingLanguage](API_PlatformProgrammingLanguage.md) objects
Required: No

 ** SolutionStackName **
The name of the solution stack used by the platform version.
Type: String
Required: No

 ** SupportedAddonList.member.N **
The additions supported by the platform version.
Type: Array of strings
Required: No

 ** SupportedTierList.member.N **
The tiers supported by the platform version.
Type: Array of strings
Required: No

## See Also
<a name="API_PlatformDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/PlatformDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/PlatformDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/PlatformDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
