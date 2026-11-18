---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SpaceSummary.html
---

# SpaceSummary
<a name="API_SpaceSummary"></a>

A summary of a space, as returned by `ListSpaces`.

## Contents
<a name="API_SpaceSummary_Contents"></a>

 ** arn **   <a name="opensearchmemory-Type-SpaceSummary-arn"></a>
The Amazon Resource Name (ARN) of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws:osm:[a-z0-9-]+:[0-9]{12}:space/sp-[a-f0-9]{12}`
Required: Yes

 ** createdAt **   <a name="opensearchmemory-Type-SpaceSummary-createdAt"></a>
When the space was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="opensearchmemory-Type-SpaceSummary-name"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][a-zA-Z0-9 _-]*`
Required: Yes

 ** spaceId **   <a name="opensearchmemory-Type-SpaceSummary-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

 ** status **   <a name="opensearchmemory-Type-SpaceSummary-status"></a>
The status of the space.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | DELETED | FAILED`
Required: Yes

## See Also
<a name="API_SpaceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/SpaceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/SpaceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/SpaceSummary)
