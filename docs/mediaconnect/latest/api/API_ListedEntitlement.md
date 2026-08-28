---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListedEntitlement.html
---

# ListedEntitlement
<a name="API_ListedEntitlement"></a>

 An entitlement that has been granted to you from other AWS accounts.

## Contents
<a name="API_ListedEntitlement_Contents"></a>

 ** entitlementArn **   <a name="mediaconnect-Type-ListedEntitlement-entitlementArn"></a>
 The ARN of the entitlement.
Type: String
Required: Yes

 ** entitlementName **   <a name="mediaconnect-Type-ListedEntitlement-entitlementName"></a>
 The name of the entitlement.
Type: String
Required: Yes

 ** dataTransferSubscriberFeePercent **   <a name="mediaconnect-Type-ListedEntitlement-dataTransferSubscriberFeePercent"></a>
 Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Type: Integer
Required: No

## See Also
<a name="API_ListedEntitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ListedEntitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ListedEntitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ListedEntitlement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
