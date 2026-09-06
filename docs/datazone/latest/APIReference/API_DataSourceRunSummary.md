---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DataSourceRunSummary.html
---

# DataSourceRunSummary
<a name="API_DataSourceRunSummary"></a>

The details of a data source run.

## Contents
<a name="API_DataSourceRunSummary_Contents"></a>

 ** createdAt **   <a name="datazone-Type-DataSourceRunSummary-createdAt"></a>
The timestamp of when a data source run was created.
Type: Timestamp
Required: Yes

 ** dataSourceId **   <a name="datazone-Type-DataSourceRunSummary-dataSourceId"></a>
The identifier of the data source of the data source run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-DataSourceRunSummary-id"></a>
The identifier of the data source run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** projectId **   <a name="datazone-Type-DataSourceRunSummary-projectId"></a>
The project ID of the data source run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** status **   <a name="datazone-Type-DataSourceRunSummary-status"></a>
The status of the data source run.
Type: String
Valid Values: `REQUESTED | RUNNING | FAILED | PARTIALLY_SUCCEEDED | SUCCESS`
Required: Yes

 ** type **   <a name="datazone-Type-DataSourceRunSummary-type"></a>
The type of the data source run.
Type: String
Valid Values: `PRIORITIZED | SCHEDULED`
Required: Yes

 ** updatedAt **   <a name="datazone-Type-DataSourceRunSummary-updatedAt"></a>
The timestamp of when a data source run was updated.
Type: Timestamp
Required: Yes

 ** errorMessage **   <a name="datazone-Type-DataSourceRunSummary-errorMessage"></a>
The details of the error message that is returned if the operation cannot be successfully completed.
Type: [DataSourceErrorMessage](API_DataSourceErrorMessage.md) object
Required: No

 ** lineageSummary **   <a name="datazone-Type-DataSourceRunSummary-lineageSummary"></a>
The run lineage summary of a data source.
Type: [DataSourceRunLineageSummary](API_DataSourceRunLineageSummary.md) object
Required: No

 ** runStatisticsForAssets **   <a name="datazone-Type-DataSourceRunSummary-runStatisticsForAssets"></a>
The asset statistics from the data source run.
Type: [RunStatisticsForAssets](API_RunStatisticsForAssets.md) object
Required: No

 ** startedAt **   <a name="datazone-Type-DataSourceRunSummary-startedAt"></a>
The timestamp of when a data source run was started.
Type: Timestamp
Required: No

 ** stoppedAt **   <a name="datazone-Type-DataSourceRunSummary-stoppedAt"></a>
The timestamp of when a data source run was stopped.
Type: Timestamp
Required: No

## See Also
<a name="API_DataSourceRunSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DataSourceRunSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DataSourceRunSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DataSourceRunSummary)
