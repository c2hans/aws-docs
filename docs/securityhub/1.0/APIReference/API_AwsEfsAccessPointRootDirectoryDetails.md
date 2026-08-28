---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEfsAccessPointRootDirectoryDetails.html
---

# AwsEfsAccessPointRootDirectoryDetails
<a name="API_AwsEfsAccessPointRootDirectoryDetails"></a>

Provides information about the directory on the Amazon EFS file system that the access point exposes as the root directory to NFS clients using the access point.

## Contents
<a name="API_AwsEfsAccessPointRootDirectoryDetails_Contents"></a>

 ** CreationInfo **   <a name="securityhub-Type-AwsEfsAccessPointRootDirectoryDetails-CreationInfo"></a>
Specifies the POSIX IDs and permissions to apply to the access point's root directory.
Type: [AwsEfsAccessPointRootDirectoryCreationInfoDetails](API_AwsEfsAccessPointRootDirectoryCreationInfoDetails.md) object
Required: No

 ** Path **   <a name="securityhub-Type-AwsEfsAccessPointRootDirectoryDetails-Path"></a>
Specifies the path on the Amazon EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide `CreationInfo`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEfsAccessPointRootDirectoryDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEfsAccessPointRootDirectoryDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEfsAccessPointRootDirectoryDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEfsAccessPointRootDirectoryDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
