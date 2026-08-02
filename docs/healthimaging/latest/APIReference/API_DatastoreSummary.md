---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DatastoreSummary.html
---

# DatastoreSummary
<a name="API_DatastoreSummary"></a>

List of summaries of data stores.

## Contents
<a name="API_DatastoreSummary_Contents"></a>

 ** datastoreId **   <a name="healthimaging-Type-DatastoreSummary-datastoreId"></a>
The data store identifier.
Type: String
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** datastoreName **   <a name="healthimaging-Type-DatastoreSummary-datastoreName"></a>
The data store name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9._/#-]+`
Required: Yes

 ** datastoreStatus **   <a name="healthimaging-Type-DatastoreSummary-datastoreStatus"></a>
The data store status.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | DELETING | DELETED`
Required: Yes

 ** createdAt **   <a name="healthimaging-Type-DatastoreSummary-createdAt"></a>
The timestamp when the data store was created.
Type: Timestamp
Required: No

 ** datastoreArn **   <a name="healthimaging-Type-DatastoreSummary-datastoreArn"></a>
The Amazon Resource Name (ARN) for the data store.
Type: String
Pattern: `arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:medical-imaging:[a-z0-9-]+:[0-9]{12}:datastore/[0-9a-z]{32}(/imageset/[0-9a-z]{32})?`
Required: No

 ** updatedAt **   <a name="healthimaging-Type-DatastoreSummary-updatedAt"></a>
The timestamp when the data store was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DatastoreSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/DatastoreSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/DatastoreSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/DatastoreSummary)
