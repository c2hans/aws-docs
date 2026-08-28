---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_VariantStoreItem.html
---

# VariantStoreItem
<a name="API_VariantStoreItem"></a>

A variant store.

## Contents
<a name="API_VariantStoreItem_Contents"></a>

 ** creationTime **   <a name="omics-Type-VariantStoreItem-creationTime"></a>
When the store was created.
Type: Timestamp
Required: Yes

 ** description **   <a name="omics-Type-VariantStoreItem-description"></a>
The store's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: Yes

 ** id **   <a name="omics-Type-VariantStoreItem-id"></a>
The store's ID.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** name **   <a name="omics-Type-VariantStoreItem-name"></a>
The store's name.
Type: String
Required: Yes

 ** reference **   <a name="omics-Type-VariantStoreItem-reference"></a>
The store's genome reference.
Type: [ReferenceItem](API_ReferenceItem.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** sseConfig **   <a name="omics-Type-VariantStoreItem-sseConfig"></a>
The store's server-side encryption (SSE) settings.
Type: [SseConfig](API_SseConfig.md) object
Required: Yes

 ** status **   <a name="omics-Type-VariantStoreItem-status"></a>
The store's status.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED`
Required: Yes

 ** statusMessage **   <a name="omics-Type-VariantStoreItem-statusMessage"></a>
The store's status message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** storeArn **   <a name="omics-Type-VariantStoreItem-storeArn"></a>
The store's ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:([^: ]*):([^: ]*):([^: ]*):([0-9]{12}):([^: ]*)`
Required: Yes

 ** storeSizeBytes **   <a name="omics-Type-VariantStoreItem-storeSizeBytes"></a>
The store's size in bytes.
Type: Long
Required: Yes

 ** updateTime **   <a name="omics-Type-VariantStoreItem-updateTime"></a>
When the store was updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_VariantStoreItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/VariantStoreItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/VariantStoreItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/VariantStoreItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
