---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DataSourceSummary.html
---

# DataSourceSummary
<a name="API_DataSourceSummary"></a>

The details of the data source.

## Contents
<a name="API_DataSourceSummary_Contents"></a>

 ** dataSourceId **   <a name="datazone-Type-DataSourceSummary-dataSourceId"></a>
The ID of the data source.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** domainId **   <a name="datazone-Type-DataSourceSummary-domainId"></a>
The ID of the Amazon DataZone domain in which the data source exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-DataSourceSummary-name"></a>
The name of the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** status **   <a name="datazone-Type-DataSourceSummary-status"></a>
The status of the data source.
Type: String
Valid Values: `CREATING | FAILED_CREATION | READY | UPDATING | FAILED_UPDATE | RUNNING | DELETING | FAILED_DELETION`
Required: Yes

 ** type **   <a name="datazone-Type-DataSourceSummary-type"></a>
The type of the data source.
Type: String
Required: Yes

 ** connectionId **   <a name="datazone-Type-DataSourceSummary-connectionId"></a>
The connection ID that's part of the data source summary.
Type: String
Required: No

 ** createdAt **   <a name="datazone-Type-DataSourceSummary-createdAt"></a>
The timestamp of when the data source was created.
Type: Timestamp
Required: No

 ** description **   <a name="datazone-Type-DataSourceSummary-description"></a>
The data source description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** enableSetting **   <a name="datazone-Type-DataSourceSummary-enableSetting"></a>
Specifies whether the data source is enabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** environmentId **   <a name="datazone-Type-DataSourceSummary-environmentId"></a>
The ID of the environment in which the data source exists.
Type: String
Required: No

 ** lastRunAssetCount **   <a name="datazone-Type-DataSourceSummary-lastRunAssetCount"></a>
The count of the assets created during the last data source run.
Type: Integer
Required: No

 ** lastRunAt **   <a name="datazone-Type-DataSourceSummary-lastRunAt"></a>
The timestamp of when the data source run was last performed.
Type: Timestamp
Required: No

 ** lastRunErrorMessage **   <a name="datazone-Type-DataSourceSummary-lastRunErrorMessage"></a>
The details of the error message that is returned if the operation cannot be successfully completed.
Type: [DataSourceErrorMessage](API_DataSourceErrorMessage.md) object
Required: No

 ** lastRunStatus **   <a name="datazone-Type-DataSourceSummary-lastRunStatus"></a>
The status of the last data source run.
Type: String
Valid Values: `REQUESTED | RUNNING | FAILED | PARTIALLY_SUCCEEDED | SUCCESS`
Required: No

 ** schedule **   <a name="datazone-Type-DataSourceSummary-schedule"></a>
The details of the schedule of the data source runs.
Type: [ScheduleConfiguration](API_ScheduleConfiguration.md) object
Required: No

 ** updatedAt **   <a name="datazone-Type-DataSourceSummary-updatedAt"></a>
The timestamp of when the data source was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DataSourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DataSourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DataSourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DataSourceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
