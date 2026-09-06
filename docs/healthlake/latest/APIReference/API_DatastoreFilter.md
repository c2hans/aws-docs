---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DatastoreFilter.html
---

# DatastoreFilter
<a name="API_DatastoreFilter"></a>

The filters applied to a data store query.

## Contents
<a name="API_DatastoreFilter_Contents"></a>

 ** CreatedAfter **   <a name="HealthLake-Type-DatastoreFilter-CreatedAfter"></a>
Filter to set cutoff dates for records. All data stores created after the specified date are included in the results.
Type: Timestamp
Required: No

 ** CreatedBefore **   <a name="HealthLake-Type-DatastoreFilter-CreatedBefore"></a>
Filter to set cutoff dates for records. All data stores created before the specified date are included in the results.
Type: Timestamp
Required: No

 ** DatastoreName **   <a name="HealthLake-Type-DatastoreFilter-DatastoreName"></a>
Filter data store results by name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: No

 ** DatastoreStatus **   <a name="HealthLake-Type-DatastoreFilter-DatastoreStatus"></a>
Filter data store results by status.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | DELETED | CREATE_FAILED | UPDATING | UPDATE_FAILED`
Required: No

## See Also
<a name="API_DatastoreFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/DatastoreFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/DatastoreFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/DatastoreFilter)
