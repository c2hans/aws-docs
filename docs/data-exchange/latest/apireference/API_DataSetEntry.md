---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DataSetEntry.html
---

# DataSetEntry
<a name="API_DataSetEntry"></a>

A data set is an AWS resource with one or more revisions.

## Contents
<a name="API_DataSetEntry_Contents"></a>

 ** Arn **   <a name="dataexchange-Type-DataSetEntry-Arn"></a>
The ARN for the data set.
Type: String
Required: Yes

 ** AssetType **   <a name="dataexchange-Type-DataSetEntry-AssetType"></a>
The type of asset that is added to a data set.
Type: String
Valid Values: `S3_SNAPSHOT | REDSHIFT_DATA_SHARE | API_GATEWAY_API | S3_DATA_ACCESS | LAKE_FORMATION_DATA_PERMISSION`
Required: Yes

 ** CreatedAt **   <a name="dataexchange-Type-DataSetEntry-CreatedAt"></a>
The date and time that the data set was created, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** Description **   <a name="dataexchange-Type-DataSetEntry-Description"></a>
The description for the data set.
Type: String
Required: Yes

 ** Id **   <a name="dataexchange-Type-DataSetEntry-Id"></a>
The unique identifier for the data set.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** Name **   <a name="dataexchange-Type-DataSetEntry-Name"></a>
The name of the data set.
Type: String
Required: Yes

 ** Origin **   <a name="dataexchange-Type-DataSetEntry-Origin"></a>
A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).
Type: String
Valid Values: `OWNED | ENTITLED`
Required: Yes

 ** UpdatedAt **   <a name="dataexchange-Type-DataSetEntry-UpdatedAt"></a>
The date and time that the data set was last updated, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** OriginDetails **   <a name="dataexchange-Type-DataSetEntry-OriginDetails"></a>
If the origin of this data set is ENTITLED, includes the details for the product on AWS Marketplace.
Type: [OriginDetails](API_OriginDetails.md) object
Required: No

 ** SourceId **   <a name="dataexchange-Type-DataSetEntry-SourceId"></a>
The data set ID of the owned data set corresponding to the entitled data set being viewed. This parameter is returned when a data set owner is viewing the entitled copy of its owned data set.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: No

## See Also
<a name="API_DataSetEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/DataSetEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/DataSetEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/DataSetEntry)
