---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_PosixUser.html
---

# PosixUser
<a name="API_S3Files_PosixUser"></a>

Specifies the POSIX identity with uid, gid, and secondary group IDs for user enforcement.

## Contents
<a name="API_S3Files_PosixUser_Contents"></a>

 ** gid **   <a name="AmazonS3-Type-S3Files_PosixUser-gid"></a>
The POSIX group ID.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** uid **   <a name="AmazonS3-Type-S3Files_PosixUser-uid"></a>
The POSIX user ID.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** secondaryGids **   <a name="AmazonS3-Type-S3Files_PosixUser-secondaryGids"></a>
An array of secondary POSIX group IDs.
Type: Array of longs
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

## See Also
<a name="API_S3Files_PosixUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/PosixUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/PosixUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/PosixUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
