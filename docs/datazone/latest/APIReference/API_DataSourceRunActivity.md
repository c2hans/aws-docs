---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DataSourceRunActivity.html
---

# DataSourceRunActivity
<a name="API_DataSourceRunActivity"></a>

The activity details of the data source run.

## Contents
<a name="API_DataSourceRunActivity_Contents"></a>

 ** createdAt **   <a name="datazone-Type-DataSourceRunActivity-createdAt"></a>
The timestamp of when data source run activity was created.
Type: Timestamp
Required: Yes

 ** dataAssetStatus **   <a name="datazone-Type-DataSourceRunActivity-dataAssetStatus"></a>
The status of the asset included in the data source run activity.
Type: String
Valid Values: `FAILED | PUBLISHING_FAILED | SUCCEEDED_CREATED | SUCCEEDED_UPDATED | SKIPPED_ALREADY_IMPORTED | SKIPPED_ARCHIVED | SKIPPED_NO_ACCESS | UNCHANGED`
Required: Yes

 ** database **   <a name="datazone-Type-DataSourceRunActivity-database"></a>
The database included in the data source run activity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** dataSourceRunId **   <a name="datazone-Type-DataSourceRunActivity-dataSourceRunId"></a>
The identifier of the data source for the data source run activity.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** projectId **   <a name="datazone-Type-DataSourceRunActivity-projectId"></a>
The project ID included in the data source run activity.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** technicalName **   <a name="datazone-Type-DataSourceRunActivity-technicalName"></a>
The technical name included in the data source run activity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** updatedAt **   <a name="datazone-Type-DataSourceRunActivity-updatedAt"></a>
The timestamp of when data source run activity was updated.
Type: Timestamp
Required: Yes

 ** dataAssetId **   <a name="datazone-Type-DataSourceRunActivity-dataAssetId"></a>
The identifier of the asset included in the data source run activity.
Type: String
Required: No

 ** errorMessage **   <a name="datazone-Type-DataSourceRunActivity-errorMessage"></a>
The details of the error message that is returned if the operation cannot be successfully completed.
Type: [DataSourceErrorMessage](API_DataSourceErrorMessage.md) object
Required: No

 ** lineageSummary **   <a name="datazone-Type-DataSourceRunActivity-lineageSummary"></a>
The data lineage summary.
Type: [LineageInfo](API_LineageInfo.md) object
Required: No

 ** technicalDescription **   <a name="datazone-Type-DataSourceRunActivity-technicalDescription"></a>
The technical description included in the data source run activity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_DataSourceRunActivity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DataSourceRunActivity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DataSourceRunActivity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DataSourceRunActivity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
