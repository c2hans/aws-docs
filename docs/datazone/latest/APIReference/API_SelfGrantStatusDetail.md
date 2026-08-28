---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SelfGrantStatusDetail.html
---

# SelfGrantStatusDetail
<a name="API_SelfGrantStatusDetail"></a>

The details for the self granting status.

## Contents
<a name="API_SelfGrantStatusDetail_Contents"></a>

 ** databaseName **   <a name="datazone-Type-SelfGrantStatusDetail-databaseName"></a>
The name of the database used for the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** status **   <a name="datazone-Type-SelfGrantStatusDetail-status"></a>
The self granting status of the data source.
Type: String
Valid Values: `GRANT_PENDING | REVOKE_PENDING | GRANT_IN_PROGRESS | REVOKE_IN_PROGRESS | GRANTED | GRANT_FAILED | REVOKE_FAILED`
Required: Yes

 ** failureCause **   <a name="datazone-Type-SelfGrantStatusDetail-failureCause"></a>
The reason for why the operation failed.
Type: String
Required: No

 ** schemaName **   <a name="datazone-Type-SelfGrantStatusDetail-schemaName"></a>
The name of the schema used in the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_SelfGrantStatusDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SelfGrantStatusDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SelfGrantStatusDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SelfGrantStatusDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
