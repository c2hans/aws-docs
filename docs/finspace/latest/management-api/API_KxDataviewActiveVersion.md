---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDataviewActiveVersion.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxDataviewActiveVersion
<a name="API_KxDataviewActiveVersion"></a>

 The active version of the dataview that is currently in use by this cluster.

## Contents
<a name="API_KxDataviewActiveVersion_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** attachedClusters **   <a name="finspace-Type-KxDataviewActiveVersion-attachedClusters"></a>
 The list of clusters that are currently using this dataview.
Type: Array of strings
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: No

 ** changesetId **   <a name="finspace-Type-KxDataviewActiveVersion-changesetId"></a>
A unique identifier for the changeset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** createdTimestamp **   <a name="finspace-Type-KxDataviewActiveVersion-createdTimestamp"></a>
 The timestamp at which the dataview version was active. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

 ** segmentConfigurations **   <a name="finspace-Type-KxDataviewActiveVersion-segmentConfigurations"></a>
 The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment.
Type: Array of [KxDataviewSegmentConfiguration](API_KxDataviewSegmentConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** versionId **   <a name="finspace-Type-KxDataviewActiveVersion-versionId"></a>
 A unique identifier of the active version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: No

## See Also
<a name="API_KxDataviewActiveVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxDataviewActiveVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxDataviewActiveVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxDataviewActiveVersion)
