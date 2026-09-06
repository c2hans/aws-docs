---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DataProductRevision.html
---

# DataProductRevision
<a name="API_DataProductRevision"></a>

The data product revision.

## Contents
<a name="API_DataProductRevision_Contents"></a>

 ** createdAt **   <a name="datazone-Type-DataProductRevision-createdAt"></a>
The timestamp at which the data product revision was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-DataProductRevision-createdBy"></a>
The user who created the data product revision.
Type: String
Required: No

 ** domainId **   <a name="datazone-Type-DataProductRevision-domainId"></a>
The ID of the domain where the data product revision lives.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: No

 ** id **   <a name="datazone-Type-DataProductRevision-id"></a>
The ID of the data product revision.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** revision **   <a name="datazone-Type-DataProductRevision-revision"></a>
The data product revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_DataProductRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DataProductRevision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DataProductRevision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DataProductRevision)
