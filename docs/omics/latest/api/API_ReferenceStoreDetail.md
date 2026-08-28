---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ReferenceStoreDetail.html
---

# ReferenceStoreDetail
<a name="API_ReferenceStoreDetail"></a>

Details about a reference store.

## Contents
<a name="API_ReferenceStoreDetail_Contents"></a>

 ** arn **   <a name="omics-Type-ReferenceStoreDetail-arn"></a>
The store's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`
Required: Yes

 ** creationTime **   <a name="omics-Type-ReferenceStoreDetail-creationTime"></a>
When the store was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="omics-Type-ReferenceStoreDetail-id"></a>
The store's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** description **   <a name="omics-Type-ReferenceStoreDetail-description"></a>
The store's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** name **   <a name="omics-Type-ReferenceStoreDetail-name"></a>
The store's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** sseConfig **   <a name="omics-Type-ReferenceStoreDetail-sseConfig"></a>
The store's server-side encryption (SSE) settings.
Type: [SseConfig](API_SseConfig.md) object
Required: No

## See Also
<a name="API_ReferenceStoreDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ReferenceStoreDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ReferenceStoreDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ReferenceStoreDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
