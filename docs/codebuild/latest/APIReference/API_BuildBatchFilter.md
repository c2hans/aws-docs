---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatchFilter.html
---

# BuildBatchFilter
<a name="API_BuildBatchFilter"></a>

Specifies filters when retrieving batch builds.

## Contents
<a name="API_BuildBatchFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** status **   <a name="CodeBuild-Type-BuildBatchFilter-status"></a>
The status of the batch builds to retrieve. Only batch builds that have this status will be retrieved.
Type: String
Valid Values: `SUCCEEDED | FAILED | FAULT | TIMED_OUT | IN_PROGRESS | STOPPED`
Required: No

## See Also
<a name="API_BuildBatchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BuildBatchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BuildBatchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BuildBatchFilter)
