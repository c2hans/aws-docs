---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_DomainSummary.html
---

# DomainSummary
<a name="API_DomainSummary"></a>

Summary information about a Domain.

## Contents
<a name="API_DomainSummary_Contents"></a>

 ** arn **   <a name="connecthealth-Type-DomainSummary-arn"></a>

Type: String
Pattern: `arn:aws:health-agent:[a-z0-9-]+:[0-9]{12}:domain/(hai-|dom-)[a-z0-9]+`
Required: Yes

 ** createdAt **   <a name="connecthealth-Type-DomainSummary-createdAt"></a>
The timestamp when the Domain was created.
Type: Timestamp
Required: Yes

 ** domainId **   <a name="connecthealth-Type-DomainSummary-domainId"></a>
The unique identifier of the Domain.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

 ** name **   <a name="connecthealth-Type-DomainSummary-name"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** status **   <a name="connecthealth-Type-DomainSummary-status"></a>

Type: String
Valid Values: `ACTIVE | DELETING | DELETED`
Required: Yes

## See Also
<a name="API_DomainSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/DomainSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/DomainSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/DomainSummary)
