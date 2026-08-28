---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_AssetEntry.html
---

# AssetEntry
<a name="API_AssetEntry"></a>

An asset in AWS Data Exchange is a piece of data (Amazon S3 object) or a means of fulfilling data (Amazon Redshift datashare or Amazon API Gateway API, AWS Lake Formation data permission, or Amazon S3 data access). The asset can be a structured data file, an image file, or some other data file that can be stored as an Amazon S3 object, an Amazon API Gateway API, or an Amazon Redshift datashare, an AWS Lake Formation data permission, or an Amazon S3 data access. When you create an import job for your files, API Gateway APIs, Amazon Redshift datashares, AWS Lake Formation data permission, or Amazon S3 data access, you create an asset in AWS Data Exchange.

## Contents
<a name="API_AssetEntry_Contents"></a>

 ** Arn **   <a name="dataexchange-Type-AssetEntry-Arn"></a>
The ARN for the asset.
Type: String
Required: Yes

 ** AssetDetails **   <a name="dataexchange-Type-AssetEntry-AssetDetails"></a>
Details about the asset.
Type: [AssetDetails](API_AssetDetails.md) object
Required: Yes

 ** AssetType **   <a name="dataexchange-Type-AssetEntry-AssetType"></a>
The type of asset that is added to a data set.
Type: String
Valid Values: `S3_SNAPSHOT | REDSHIFT_DATA_SHARE | API_GATEWAY_API | S3_DATA_ACCESS | LAKE_FORMATION_DATA_PERMISSION`
Required: Yes

 ** CreatedAt **   <a name="dataexchange-Type-AssetEntry-CreatedAt"></a>
The date and time that the asset was created, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-AssetEntry-DataSetId"></a>
The unique identifier for the data set associated with this asset.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** Id **   <a name="dataexchange-Type-AssetEntry-Id"></a>
The unique identifier for the asset.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** Name **   <a name="dataexchange-Type-AssetEntry-Name"></a>
The name of the asset. When importing from Amazon S3, the Amazon S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target Amazon S3 object key. When importing from Amazon API Gateway API, the API name is used as the asset name. When importing from Amazon Redshift, the datashare name is used as the asset name. When importing from AWS Lake Formation, the static values of "Database(s) included in LF-tag policy" or "Table(s) included in LF-tag policy" are used as the asset name.
Type: String
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-AssetEntry-RevisionId"></a>
The unique identifier for the revision associated with this asset.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** UpdatedAt **   <a name="dataexchange-Type-AssetEntry-UpdatedAt"></a>
The date and time that the asset was last updated, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** SourceId **   <a name="dataexchange-Type-AssetEntry-SourceId"></a>
The asset ID of the owned asset corresponding to the entitled asset being viewed. This parameter is returned when an asset owner is viewing the entitled copy of its owned asset.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: No

## See Also
<a name="API_AssetEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/AssetEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/AssetEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/AssetEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
