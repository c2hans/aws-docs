---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UnprocessedSecurityControl.html
---

# UnprocessedSecurityControl
<a name="API_UnprocessedSecurityControl"></a>

 Provides details about a security control for which a response couldn't be returned.

## Contents
<a name="API_UnprocessedSecurityControl_Contents"></a>

 ** ErrorCode **   <a name="securityhub-Type-UnprocessedSecurityControl-ErrorCode"></a>
 The error code for the unprocessed security control. The `NOT_FOUND` value has been deprecated and replaced by the `RESOURCE_NOT_FOUND` value.
Type: String
Valid Values: `INVALID_INPUT | ACCESS_DENIED | NOT_FOUND | RESOURCE_NOT_FOUND | LIMIT_EXCEEDED`
Required: Yes

 ** SecurityControlId **   <a name="securityhub-Type-UnprocessedSecurityControl-SecurityControlId"></a>
 The control (identified with `SecurityControlId`, `SecurityControlArn`, or a mix of both parameters) for which a response couldn't be returned.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ErrorReason **   <a name="securityhub-Type-UnprocessedSecurityControl-ErrorReason"></a>
 The reason why the security control was unprocessed.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_UnprocessedSecurityControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UnprocessedSecurityControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UnprocessedSecurityControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UnprocessedSecurityControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
