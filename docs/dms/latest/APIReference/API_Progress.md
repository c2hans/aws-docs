---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_Progress.html
---

# Progress
<a name="API_Progress"></a>

Provides information about the progress of the schema conversion operation.

## Contents
<a name="API_Progress_Contents"></a>

 ** ProcessedObject **   <a name="DMS-Type-Progress-ProcessedObject"></a>
The name of the database object that the schema conversion operation currently uses.
Type: [ProcessedObject](API_ProcessedObject.md) object
Required: No

 ** ProgressPercent **   <a name="DMS-Type-Progress-ProgressPercent"></a>
The percent complete for the current step of the schema conversion operation.
Type: Double
Required: No

 ** ProgressStep **   <a name="DMS-Type-Progress-ProgressStep"></a>
The step of the schema conversion operation. This parameter can store one of the following values:
+  `IN_PROGRESS` – The operation is running.
+  `LOADING_METADATA` – Loads metadata from the source database.
+  `COUNTING_OBJECTS` – Determines the number of objects involved in the operation.
+  `ANALYZING` – Analyzes the source database objects.
+  `CONVERTING` – Converts the source database objects to a format compatible with the target database.
+  `APPLYING` – Applies the converted code to the target database.
+  `FINISHED` – The operation completed successfully.
Type: String
Required: No

 ** TotalObjects **   <a name="DMS-Type-Progress-TotalObjects"></a>
The number of objects in this schema conversion operation.
Type: Long
Required: No

## See Also
<a name="API_Progress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/Progress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/Progress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/Progress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
