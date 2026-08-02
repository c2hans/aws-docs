---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ApprovalRuleOverriddenEventMetadata.html
---

# ApprovalRuleOverriddenEventMetadata
<a name="API_ApprovalRuleOverriddenEventMetadata"></a>

Returns information about an override event for approval rules for a pull request.

## Contents
<a name="API_ApprovalRuleOverriddenEventMetadata_Contents"></a>

 ** overrideStatus **   <a name="CodeCommit-Type-ApprovalRuleOverriddenEventMetadata-overrideStatus"></a>
The status of the override event.
Type: String
Valid Values: `OVERRIDE | REVOKE`
Required: No

 ** revisionId **   <a name="CodeCommit-Type-ApprovalRuleOverriddenEventMetadata-revisionId"></a>
The revision ID of the pull request when the override event occurred.
Type: String
Required: No

## See Also
<a name="API_ApprovalRuleOverriddenEventMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ApprovalRuleOverriddenEventMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ApprovalRuleOverriddenEventMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ApprovalRuleOverriddenEventMetadata)
