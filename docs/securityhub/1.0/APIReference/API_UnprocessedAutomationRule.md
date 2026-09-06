---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UnprocessedAutomationRule.html
---

# UnprocessedAutomationRule
<a name="API_UnprocessedAutomationRule"></a>

 A list of objects containing `RuleArn`, `ErrorCode`, and `ErrorMessage`. This parameter tells you which automation rules the request didn't process and why.

## Contents
<a name="API_UnprocessedAutomationRule_Contents"></a>

 ** ErrorCode **   <a name="securityhub-Type-UnprocessedAutomationRule-ErrorCode"></a>
 The error code associated with the unprocessed automation rule.
Type: Integer
Required: No

 ** ErrorMessage **   <a name="securityhub-Type-UnprocessedAutomationRule-ErrorMessage"></a>
 An error message describing why a request didn't process a specific rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleArn **   <a name="securityhub-Type-UnprocessedAutomationRule-RuleArn"></a>
 The Amazon Resource Name (ARN) for the unprocessed automation rule.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_UnprocessedAutomationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UnprocessedAutomationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UnprocessedAutomationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UnprocessedAutomationRule)
