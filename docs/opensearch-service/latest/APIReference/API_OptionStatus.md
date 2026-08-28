---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_OptionStatus.html
---

# OptionStatus
<a name="API_OptionStatus"></a>

Provides the current status of an entity.

## Contents
<a name="API_OptionStatus_Contents"></a>

 ** CreationDate **   <a name="opensearchservice-Type-OptionStatus-CreationDate"></a>
The timestamp when the entity was created.
Type: Timestamp
Required: Yes

 ** State **   <a name="opensearchservice-Type-OptionStatus-State"></a>
The state of the entity.
Type: String
Valid Values: `RequiresIndexDocuments | Processing | Active`
Required: Yes

 ** UpdateDate **   <a name="opensearchservice-Type-OptionStatus-UpdateDate"></a>
The timestamp of the last time the entity was updated.
Type: Timestamp
Required: Yes

 ** PendingDeletion **   <a name="opensearchservice-Type-OptionStatus-PendingDeletion"></a>
Indicates whether the entity is being deleted.
Type: Boolean
Required: No

 ** UpdateVersion **   <a name="opensearchservice-Type-OptionStatus-UpdateVersion"></a>
The latest version of the entity.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_OptionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/OptionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/OptionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/OptionStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
