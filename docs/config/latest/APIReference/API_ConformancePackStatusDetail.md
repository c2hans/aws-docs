---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConformancePackStatusDetail.html
---

# ConformancePackStatusDetail
<a name="API_ConformancePackStatusDetail"></a>

Status details of a conformance pack.

## Contents
<a name="API_ConformancePackStatusDetail_Contents"></a>

 ** ConformancePackArn **   <a name="config-Type-ConformancePackStatusDetail-ConformancePackArn"></a>
Amazon Resource Name (ARN) of comformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** ConformancePackId **   <a name="config-Type-ConformancePackStatusDetail-ConformancePackId"></a>
ID of the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** ConformancePackName **   <a name="config-Type-ConformancePackStatusDetail-ConformancePackName"></a>
Name of the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: Yes

 ** ConformancePackState **   <a name="config-Type-ConformancePackStatusDetail-ConformancePackState"></a>
Indicates deployment status of conformance pack.
 AWS Config sets the state of the conformance pack to:
+ CREATE\_IN\_PROGRESS when a conformance pack creation is in progress for an account.
+ CREATE\_COMPLETE when a conformance pack has been successfully created in your account.
+ CREATE\_FAILED when a conformance pack creation failed in your account.
+ DELETE\_IN\_PROGRESS when a conformance pack deletion is in progress.
+ DELETE\_FAILED when a conformance pack deletion failed in your account.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_COMPLETE | CREATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`
Required: Yes

 ** LastUpdateRequestedTime **   <a name="config-Type-ConformancePackStatusDetail-LastUpdateRequestedTime"></a>
Last time when conformation pack creation and update was requested.
Type: Timestamp
Required: Yes

 ** StackArn **   <a name="config-Type-ConformancePackStatusDetail-StackArn"></a>
Amazon Resource Name (ARN) of AWS CloudFormation stack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** ConformancePackStatusReason **   <a name="config-Type-ConformancePackStatusDetail-ConformancePackStatusReason"></a>
The reason of conformance pack creation failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** LastUpdateCompletedTime **   <a name="config-Type-ConformancePackStatusDetail-LastUpdateCompletedTime"></a>
Last time when conformation pack creation and update was successful.
Type: Timestamp
Required: No

## See Also
<a name="API_ConformancePackStatusDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConformancePackStatusDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConformancePackStatusDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConformancePackStatusDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
