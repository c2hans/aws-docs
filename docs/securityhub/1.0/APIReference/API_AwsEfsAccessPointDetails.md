---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEfsAccessPointDetails.html
---

# AwsEfsAccessPointDetails
<a name="API_AwsEfsAccessPointDetails"></a>

Provides information about an Amazon EFS access point.

## Contents
<a name="API_AwsEfsAccessPointDetails_Contents"></a>

 ** AccessPointId **   <a name="securityhub-Type-AwsEfsAccessPointDetails-AccessPointId"></a>
The ID of the Amazon EFS access point.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Arn **   <a name="securityhub-Type-AwsEfsAccessPointDetails-Arn"></a>
The Amazon Resource Name (ARN) of the Amazon EFS access point.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClientToken **   <a name="securityhub-Type-AwsEfsAccessPointDetails-ClientToken"></a>
The opaque string specified in the request to ensure idempotent creation.
Type: String
Pattern: `.*\S.*`
Required: No

 ** FileSystemId **   <a name="securityhub-Type-AwsEfsAccessPointDetails-FileSystemId"></a>
The ID of the Amazon EFS file system that the access point applies to.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PosixUser **   <a name="securityhub-Type-AwsEfsAccessPointDetails-PosixUser"></a>
The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point, that is used for all file operations by NFS clients using the access point.
Type: [AwsEfsAccessPointPosixUserDetails](API_AwsEfsAccessPointPosixUserDetails.md) object
Required: No

 ** RootDirectory **   <a name="securityhub-Type-AwsEfsAccessPointDetails-RootDirectory"></a>
The directory on the Amazon EFS file system that the access point exposes as the root directory to NFS clients using the access point.
Type: [AwsEfsAccessPointRootDirectoryDetails](API_AwsEfsAccessPointRootDirectoryDetails.md) object
Required: No

## See Also
<a name="API_AwsEfsAccessPointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEfsAccessPointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEfsAccessPointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEfsAccessPointDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
