---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_InsightEntity.html
---

# InsightEntity
<a name="API_InsightEntity"></a>

Specifies the entity for which to retrieve insights. An entity can be an Amazon OpenSearch Service domain or an Amazon Web Services account.

## Contents
<a name="API_InsightEntity_Contents"></a>

 ** Type **   <a name="opensearchservice-Type-InsightEntity-Type"></a>
The type of the entity. Possible values are `Account` and `DomainName`.
Type: String
Valid Values: `Account | DomainName`
Required: Yes

 ** Value **   <a name="opensearchservice-Type-InsightEntity-Value"></a>
The value of the entity. For `DomainName`, this is the domain name. For `Account`, this is the Amazon Web Services account ID.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `([a-z][a-z0-9\-]+|\d{12})`
Required: No

## See Also
<a name="API_InsightEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/InsightEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/InsightEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/InsightEntity)
