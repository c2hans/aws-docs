---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Predecessor.html
---

# Predecessor
<a name="API_Predecessor"></a>

A job run that was used in the predicate of a conditional trigger that triggered this job run.

## Contents
<a name="API_Predecessor_Contents"></a>

 ** JobName **   <a name="Glue-Type-Predecessor-JobName"></a>
The name of the job definition used by the predecessor job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** RunId **   <a name="Glue-Type-Predecessor-RunId"></a>
The job-run ID of the predecessor job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_Predecessor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Predecessor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Predecessor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Predecessor)
