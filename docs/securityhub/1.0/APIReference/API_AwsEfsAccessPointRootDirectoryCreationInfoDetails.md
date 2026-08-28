---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEfsAccessPointRootDirectoryCreationInfoDetails.html
---

# AwsEfsAccessPointRootDirectoryCreationInfoDetails
<a name="API_AwsEfsAccessPointRootDirectoryCreationInfoDetails"></a>

Provides information about the settings that Amazon EFS uses to create the root directory when a client connects to an access point.

## Contents
<a name="API_AwsEfsAccessPointRootDirectoryCreationInfoDetails_Contents"></a>

 ** OwnerGid **   <a name="securityhub-Type-AwsEfsAccessPointRootDirectoryCreationInfoDetails-OwnerGid"></a>
Specifies the POSIX group ID to apply to the root directory.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OwnerUid **   <a name="securityhub-Type-AwsEfsAccessPointRootDirectoryCreationInfoDetails-OwnerUid"></a>
Specifies the POSIX user ID to apply to the root directory.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Permissions **   <a name="securityhub-Type-AwsEfsAccessPointRootDirectoryCreationInfoDetails-Permissions"></a>
Specifies the POSIX permissions to apply to the root directory, in the format of an octal number representing the file's mode bits.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEfsAccessPointRootDirectoryCreationInfoDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEfsAccessPointRootDirectoryCreationInfoDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEfsAccessPointRootDirectoryCreationInfoDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEfsAccessPointRootDirectoryCreationInfoDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
