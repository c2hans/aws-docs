---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_RevisionEntry.html
---

# RevisionEntry
<a name="API_RevisionEntry"></a>

A revision is a container for one or more assets.

## Contents
<a name="API_RevisionEntry_Contents"></a>

 ** Arn **   <a name="dataexchange-Type-RevisionEntry-Arn"></a>
The ARN for the revision.
Type: String
Required: Yes

 ** CreatedAt **   <a name="dataexchange-Type-RevisionEntry-CreatedAt"></a>
The date and time that the revision was created, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-RevisionEntry-DataSetId"></a>
The unique identifier for the data set associated with the data set revision.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** Id **   <a name="dataexchange-Type-RevisionEntry-Id"></a>
The unique identifier for the revision.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** UpdatedAt **   <a name="dataexchange-Type-RevisionEntry-UpdatedAt"></a>
The date and time that the revision was last updated, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** Comment **   <a name="dataexchange-Type-RevisionEntry-Comment"></a>
An optional comment about the revision.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** Finalized **   <a name="dataexchange-Type-RevisionEntry-Finalized"></a>
To publish a revision to a data set in a product, the revision must first be finalized. Finalizing a revision tells AWS Data Exchange that your changes to the assets in the revision are complete. After it's in this read-only state, you can publish the revision to your products. Finalized revisions can be published through the AWS Data Exchange console or the AWS Marketplace Catalog API, using the StartChangeSet AWS Marketplace Catalog API action. When using the API, revisions are uniquely identified by their ARN.
Type: Boolean
Required: No

 ** RevocationComment **   <a name="dataexchange-Type-RevisionEntry-RevocationComment"></a>
A required comment to inform subscribers of the reason their access to the revision was revoked.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 512.
Required: No

 ** Revoked **   <a name="dataexchange-Type-RevisionEntry-Revoked"></a>
A status indicating that subscribers' access to the revision was revoked.
Type: Boolean
Required: No

 ** RevokedAt **   <a name="dataexchange-Type-RevisionEntry-RevokedAt"></a>
The date and time that the revision was revoked, in ISO 8601 format.
Type: Timestamp
Required: No

 ** SourceId **   <a name="dataexchange-Type-RevisionEntry-SourceId"></a>
The revision ID of the owned revision corresponding to the entitled revision being viewed. This parameter is returned when a revision owner is viewing the entitled copy of its owned revision.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: No

## See Also
<a name="API_RevisionEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/RevisionEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/RevisionEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/RevisionEntry)
