---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_MembershipProtectedJobResultConfiguration.html
---

# MembershipProtectedJobResultConfiguration
<a name="API_MembershipProtectedJobResultConfiguration"></a>

Contains configurations for protected job results.

## Contents
<a name="API_MembershipProtectedJobResultConfiguration_Contents"></a>

 ** outputConfiguration **   <a name="API-Type-MembershipProtectedJobResultConfiguration-outputConfiguration"></a>
 The output configuration for a protected job result.
Type: [MembershipProtectedJobOutputConfiguration](API_MembershipProtectedJobOutputConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** roleArn **   <a name="API-Type-MembershipProtectedJobResultConfiguration-roleArn"></a>
The unique ARN for an IAM role that is used by AWS Clean Rooms to write protected job results to the result location, given by the member who can receive results.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 512.
Pattern: `arn:aws:iam::[\w]+:role/[\w+=./@-]+`
Required: Yes

## See Also
<a name="API_MembershipProtectedJobResultConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/MembershipProtectedJobResultConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/MembershipProtectedJobResultConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/MembershipProtectedJobResultConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
