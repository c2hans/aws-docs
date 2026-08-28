---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEfsAccessPointPosixUserDetails.html
---

# AwsEfsAccessPointPosixUserDetails
<a name="API_AwsEfsAccessPointPosixUserDetails"></a>

Provides details for all file system operations using this Amazon EFS access point.

## Contents
<a name="API_AwsEfsAccessPointPosixUserDetails_Contents"></a>

 ** Gid **   <a name="securityhub-Type-AwsEfsAccessPointPosixUserDetails-Gid"></a>
The POSIX group ID used for all file system operations using this access point.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SecondaryGids **   <a name="securityhub-Type-AwsEfsAccessPointPosixUserDetails-SecondaryGids"></a>
Secondary POSIX group IDs used for all file system operations using this access point.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Uid **   <a name="securityhub-Type-AwsEfsAccessPointPosixUserDetails-Uid"></a>
The POSIX user ID used for all file system operations using this access point.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEfsAccessPointPosixUserDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEfsAccessPointPosixUserDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEfsAccessPointPosixUserDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEfsAccessPointPosixUserDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
