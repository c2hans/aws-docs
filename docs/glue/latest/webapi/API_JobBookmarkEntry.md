---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_JobBookmarkEntry.html
---

# JobBookmarkEntry
<a name="API_JobBookmarkEntry"></a>

Defines a point that a job can resume processing.

## Contents
<a name="API_JobBookmarkEntry_Contents"></a>

 ** Attempt **   <a name="Glue-Type-JobBookmarkEntry-Attempt"></a>
The attempt ID number.
Type: Integer
Required: No

 ** JobBookmark **   <a name="Glue-Type-JobBookmarkEntry-JobBookmark"></a>
The bookmark itself.
Type: String
Required: No

 ** JobName **   <a name="Glue-Type-JobBookmarkEntry-JobName"></a>
The name of the job in question.
Type: String
Required: No

 ** PreviousRunId **   <a name="Glue-Type-JobBookmarkEntry-PreviousRunId"></a>
The unique run identifier associated with the previous job run.
Type: String
Required: No

 ** Run **   <a name="Glue-Type-JobBookmarkEntry-Run"></a>
The run ID number.
Type: Integer
Required: No

 ** RunId **   <a name="Glue-Type-JobBookmarkEntry-RunId"></a>
The run ID number.
Type: String
Required: No

 ** Version **   <a name="Glue-Type-JobBookmarkEntry-Version"></a>
The version of the job.
Type: Integer
Required: No

## See Also
<a name="API_JobBookmarkEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/JobBookmarkEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/JobBookmarkEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/JobBookmarkEntry)
