---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetsFromLakeFormationTagPolicyResponseDetails.html
---

# ImportAssetsFromLakeFormationTagPolicyResponseDetails
<a name="API_ImportAssetsFromLakeFormationTagPolicyResponseDetails"></a>

Details from an import AWS Lake Formation tag policy job response.

## Contents
<a name="API_ImportAssetsFromLakeFormationTagPolicyResponseDetails_Contents"></a>

 ** CatalogId **   <a name="dataexchange-Type-ImportAssetsFromLakeFormationTagPolicyResponseDetails-CatalogId"></a>
The identifier for the AWS Glue Data Catalog.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*/^[\d]{12}$/.*`
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-ImportAssetsFromLakeFormationTagPolicyResponseDetails-DataSetId"></a>
The unique identifier for the data set associated with this import job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-ImportAssetsFromLakeFormationTagPolicyResponseDetails-RevisionId"></a>
The unique identifier for the revision associated with this import job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** RoleArn **   <a name="dataexchange-Type-ImportAssetsFromLakeFormationTagPolicyResponseDetails-RoleArn"></a>
The IAM role's ARN that allows AWS Data Exchange to assume the role and grant and revoke permissions to AWS Lake Formation data permissions.
Type: String
Pattern: `arn:aws:iam::(\d{12}):role\/.+`
Required: Yes

 ** Database **   <a name="dataexchange-Type-ImportAssetsFromLakeFormationTagPolicyResponseDetails-Database"></a>
A structure for the database object.
Type: [DatabaseLFTagPolicyAndPermissions](API_DatabaseLFTagPolicyAndPermissions.md) object
Required: No

 ** Table **   <a name="dataexchange-Type-ImportAssetsFromLakeFormationTagPolicyResponseDetails-Table"></a>
A structure for the table object.
Type: [TableLFTagPolicyAndPermissions](API_TableLFTagPolicyAndPermissions.md) object
Required: No

## See Also
<a name="API_ImportAssetsFromLakeFormationTagPolicyResponseDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ImportAssetsFromLakeFormationTagPolicyResponseDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ImportAssetsFromLakeFormationTagPolicyResponseDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ImportAssetsFromLakeFormationTagPolicyResponseDetails)
