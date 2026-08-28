---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_JobMetrics.html
---

# JobMetrics
<a name="API_JobMetrics"></a>

An object containing `inputRecords`, `totalRecordsProcessed`, `matchIDs`, and `recordsNotProcessed`.

## Contents
<a name="API_JobMetrics_Contents"></a>

 ** deleteRecordsProcessed **   <a name="API-Type-JobMetrics-deleteRecordsProcessed"></a>
The number of records processed that were marked for deletion (`DELETE` = True) in the input file. This metric tracks records flagged for removal during the job execution.
Type: Integer
Required: No

 ** inputRecords **   <a name="API-Type-JobMetrics-inputRecords"></a>
The total number of input records.
Type: Integer
Required: No

 ** matchIDs **   <a name="API-Type-JobMetrics-matchIDs"></a>
The total number of `matchID`s generated.
Type: Integer
Required: No

 ** recordsNotProcessed **   <a name="API-Type-JobMetrics-recordsNotProcessed"></a>
The total number of records that did not get processed.
Type: Integer
Required: No

 ** totalRecordsProcessed **   <a name="API-Type-JobMetrics-totalRecordsProcessed"></a>
The total number of records processed.
Type: Integer
Required: No

## See Also
<a name="API_JobMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/JobMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/JobMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/JobMetrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
