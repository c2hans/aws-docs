---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetsFromLakeFormationTagPolicyRequestDetails.html
---

# ImportAssetsFromLakeFormationTagPolicyRequestDetails
<a name="API_ImportAssetsFromLakeFormationTagPolicyRequestDetails"></a>

Details about the assets imported from an AWS Lake Formation tag policy request.

## Contents
<a name="API_ImportAssetsFromLakeFormationTagPolicyRequestDetails_Contents"></a>

 ** CatalogId **   <a name="dataexchange-Type-ImportAssetsFromLakeFormationTagPolicyRequestDetails-CatalogId"></a>
The identifier for the AWS Glue Data Catalog.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*/^[\d]{12}$/.*`
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-ImportAssetsFromLakeFormationTagPolicyRequestDetails-DataSetId"></a>
The unique identifier for the data set associated with this import job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-ImportAssetsFromLakeFormationTagPolicyRequestDetails-RevisionId"></a>
The unique identifier for the revision associated with this import job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** RoleArn **   <a name="dataexchange-Type-ImportAssetsFromLakeFormationTagPolicyRequestDetails-RoleArn"></a>
The IAM role's ARN that allows AWS Data Exchange to assume the role and grant and revoke permissions of subscribers to AWS Lake Formation data permissions.
Type: String
Pattern: `arn:aws:iam::(\d{12}):role\/.+`
Required: Yes

 ** Database **   <a name="dataexchange-Type-ImportAssetsFromLakeFormationTagPolicyRequestDetails-Database"></a>
A structure for the database object.
Type: [DatabaseLFTagPolicyAndPermissions](API_DatabaseLFTagPolicyAndPermissions.md) object
Required: No

 ** Table **   <a name="dataexchange-Type-ImportAssetsFromLakeFormationTagPolicyRequestDetails-Table"></a>
A structure for the table object.
Type: [TableLFTagPolicyAndPermissions](API_TableLFTagPolicyAndPermissions.md) object
Required: No

## See Also
<a name="API_ImportAssetsFromLakeFormationTagPolicyRequestDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ImportAssetsFromLakeFormationTagPolicyRequestDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ImportAssetsFromLakeFormationTagPolicyRequestDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ImportAssetsFromLakeFormationTagPolicyRequestDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
