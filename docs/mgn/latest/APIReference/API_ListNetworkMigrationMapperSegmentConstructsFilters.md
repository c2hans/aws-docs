---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationMapperSegmentConstructsFilters.html
---

# ListNetworkMigrationMapperSegmentConstructsFilters
<a name="API_ListNetworkMigrationMapperSegmentConstructsFilters"></a>

Filters for listing mapper segment constructs.

## Contents
<a name="API_ListNetworkMigrationMapperSegmentConstructsFilters_Contents"></a>

 ** constructIDs **   <a name="mgn-Type-ListNetworkMigrationMapperSegmentConstructsFilters-constructIDs"></a>
A list of construct IDs to filter by.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** constructTypes **   <a name="mgn-Type-ListNetworkMigrationMapperSegmentConstructsFilters-constructTypes"></a>
A list of construct types to filter by.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 24.
Pattern: `AWS::([A-Z\d]){2,10}::[a-zA-Z\d]{2,30}`
Required: No

## See Also
<a name="API_ListNetworkMigrationMapperSegmentConstructsFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListNetworkMigrationMapperSegmentConstructsFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListNetworkMigrationMapperSegmentConstructsFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListNetworkMigrationMapperSegmentConstructsFilters)
