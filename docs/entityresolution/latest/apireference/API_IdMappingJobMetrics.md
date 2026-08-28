---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingJobMetrics.html
---

# IdMappingJobMetrics
<a name="API_IdMappingJobMetrics"></a>

An object that contains metrics about an ID mapping job, including counts of input records, processed records, and mapped records between source and target identifiers.

## Contents
<a name="API_IdMappingJobMetrics_Contents"></a>

 ** deleteRecordsProcessed **   <a name="API-Type-IdMappingJobMetrics-deleteRecordsProcessed"></a>
The number of records processed that were marked for deletion in the input file using the DELETE schema mapping field. These are the records to be removed from the ID mapping table.
Type: Integer
Required: No

 ** inputRecords **   <a name="API-Type-IdMappingJobMetrics-inputRecords"></a>
The total number of records that were input for processing.
Type: Integer
Required: No

 ** mappedRecordsRemoved **   <a name="API-Type-IdMappingJobMetrics-mappedRecordsRemoved"></a>
 The number of mapped records removed.
Type: Integer
Required: No

 ** mappedSourceRecordsRemoved **   <a name="API-Type-IdMappingJobMetrics-mappedSourceRecordsRemoved"></a>
 The number of source records removed due to ID mapping.
Type: Integer
Required: No

 ** mappedTargetRecordsRemoved **   <a name="API-Type-IdMappingJobMetrics-mappedTargetRecordsRemoved"></a>
 The number of mapped target records removed.
Type: Integer
Required: No

 ** newMappedRecords **   <a name="API-Type-IdMappingJobMetrics-newMappedRecords"></a>
 The number of new mapped records.
Type: Integer
Required: No

 ** newMappedSourceRecords **   <a name="API-Type-IdMappingJobMetrics-newMappedSourceRecords"></a>
 The number of new source records mapped.
Type: Integer
Required: No

 ** newMappedTargetRecords **   <a name="API-Type-IdMappingJobMetrics-newMappedTargetRecords"></a>
 The number of new mapped target records.
Type: Integer
Required: No

 ** newUniqueRecordsLoaded **   <a name="API-Type-IdMappingJobMetrics-newUniqueRecordsLoaded"></a>
The number of new unique records processed in the current job run, after removing duplicates. This metric excludes deletion-related records. Duplicates are determined by the field marked as UNIQUE\_ID in your schema mapping. Records sharing the same value in this field are considered duplicates. For example, if your current run processes five new records with the same UNIQUE\_ID value, they would count as one new unique record in this metric.
Type: Integer
Required: No

 ** recordsNotProcessed **   <a name="API-Type-IdMappingJobMetrics-recordsNotProcessed"></a>
The total number of records that did not get processed.
Type: Integer
Required: No

 ** totalMappedRecords **   <a name="API-Type-IdMappingJobMetrics-totalMappedRecords"></a>
 The total number of records that were mapped.
Type: Integer
Required: No

 ** totalMappedSourceRecords **   <a name="API-Type-IdMappingJobMetrics-totalMappedSourceRecords"></a>
 The total number of mapped source records.
Type: Integer
Required: No

 ** totalMappedTargetRecords **   <a name="API-Type-IdMappingJobMetrics-totalMappedTargetRecords"></a>
 The total number of distinct mapped target records.
Type: Integer
Required: No

 ** totalRecordsProcessed **   <a name="API-Type-IdMappingJobMetrics-totalRecordsProcessed"></a>
The total number of records that were processed.
Type: Integer
Required: No

 ** uniqueRecordsLoaded **   <a name="API-Type-IdMappingJobMetrics-uniqueRecordsLoaded"></a>
The number of de-duplicated processed records across all runs, excluding deletion-related records. Duplicates are determined by the field marked as UNIQUE\_ID in your schema mapping. Records sharing the same value in this field are considered duplicates. For example, if you specified "customer\_id" as a UNIQUE\_ID field and had three records with the same customer\_id value, they would count as one unique record in this metric.
Type: Integer
Required: No

## See Also
<a name="API_IdMappingJobMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/IdMappingJobMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/IdMappingJobMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/IdMappingJobMetrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
