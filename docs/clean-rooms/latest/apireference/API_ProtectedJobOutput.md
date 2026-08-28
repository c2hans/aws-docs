---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedJobOutput.html
---

# ProtectedJobOutput
<a name="API_ProtectedJobOutput"></a>

Contains details about the protected job output.

## Contents
<a name="API_ProtectedJobOutput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** memberList **   <a name="API-Type-ProtectedJobOutput-memberList"></a>
The list of member AWS account(s) that received the results of the job.
Type: Array of [ProtectedJobSingleMemberOutput](API_ProtectedJobSingleMemberOutput.md) objects
Required: No

 ** s3 **   <a name="API-Type-ProtectedJobOutput-s3"></a>
If present, the output for a protected job with an `S3` output type.
Type: [ProtectedJobS3Output](API_ProtectedJobS3Output.md) object
Required: No

## See Also
<a name="API_ProtectedJobOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedJobOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedJobOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedJobOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
