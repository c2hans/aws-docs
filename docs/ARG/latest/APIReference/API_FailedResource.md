---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_FailedResource.html
---

# FailedResource
<a name="API_FailedResource"></a>

A resource that failed to be added to or removed from a group.

## Contents
<a name="API_FailedResource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ErrorCode **   <a name="ARG-Type-FailedResource-ErrorCode"></a>
The error code associated with the failure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** ErrorMessage **   <a name="ARG-Type-FailedResource-ErrorMessage"></a>
The error message text associated with the failure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ResourceArn **   <a name="ARG-Type-FailedResource-ResourceArn"></a>
The Amazon resource name (ARN) of the resource that failed to be added or removed.
Type: String
Pattern: `arn:aws(-[a-z]+)*:[a-z0-9\-]*:([a-z]{2}(-[a-z]+)+-\d{1})?:([0-9]{12})?:.+`
Required: No

## See Also
<a name="API_FailedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/FailedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/FailedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/FailedResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
