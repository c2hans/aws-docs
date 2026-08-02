---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDataviewListEntry.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxDataviewListEntry
<a name="API_KxDataviewListEntry"></a>

 A collection of kdb dataview entries.

## Contents
<a name="API_KxDataviewListEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** activeVersions **   <a name="finspace-Type-KxDataviewListEntry-activeVersions"></a>
 The active changeset versions for the given dataview entry.
Type: Array of [KxDataviewActiveVersion](API_KxDataviewActiveVersion.md) objects
Required: No

 ** autoUpdate **   <a name="finspace-Type-KxDataviewListEntry-autoUpdate"></a>
 The option to specify whether you want to apply all the future additions and corrections automatically to the dataview when you ingest new changesets. The default value is false.
Type: Boolean
Required: No

 ** availabilityZoneId **   <a name="finspace-Type-KxDataviewListEntry-availabilityZoneId"></a>
 The identifier of the availability zones.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** azMode **   <a name="finspace-Type-KxDataviewListEntry-azMode"></a>
The number of availability zones you want to assign per volume. Currently, FinSpace only supports `SINGLE` for volumes. This places dataview in a single AZ.
Type: String
Valid Values: `SINGLE | MULTI`
Required: No

 ** changesetId **   <a name="finspace-Type-KxDataviewListEntry-changesetId"></a>
A unique identifier for the changeset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** createdTimestamp **   <a name="finspace-Type-KxDataviewListEntry-createdTimestamp"></a>
 The timestamp at which the dataview list entry was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

 ** databaseName **   <a name="finspace-Type-KxDataviewListEntry-databaseName"></a>
 A unique identifier of the database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: No

 ** dataviewName **   <a name="finspace-Type-KxDataviewListEntry-dataviewName"></a>
 A unique identifier of the dataview.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: No

 ** description **   <a name="finspace-Type-KxDataviewListEntry-description"></a>
 A description for the dataview list entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`
Required: No

 ** environmentId **   <a name="finspace-Type-KxDataviewListEntry-environmentId"></a>
A unique identifier for the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*\S.*`
Required: No

 ** lastModifiedTimestamp **   <a name="finspace-Type-KxDataviewListEntry-lastModifiedTimestamp"></a>
The last time that the dataview list was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

 ** readWrite **   <a name="finspace-Type-KxDataviewListEntry-readWrite"></a>
 Returns True if the dataview is created as writeable and False otherwise.
Type: Boolean
Required: No

 ** segmentConfigurations **   <a name="finspace-Type-KxDataviewListEntry-segmentConfigurations"></a>
 The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment.
Type: Array of [KxDataviewSegmentConfiguration](API_KxDataviewSegmentConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** status **   <a name="finspace-Type-KxDataviewListEntry-status"></a>
 The status of a given dataview entry.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | FAILED | DELETING`
Required: No

 ** statusReason **   <a name="finspace-Type-KxDataviewListEntry-statusReason"></a>
 The error message when a failed state occurs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^[a-zA-Z0-9\_\-\.\s]+$`
Required: No

## See Also
<a name="API_KxDataviewListEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxDataviewListEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxDataviewListEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxDataviewListEntry)
