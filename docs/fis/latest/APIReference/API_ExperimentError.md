---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentError.html
---

# ExperimentError
<a name="API_ExperimentError"></a>

Describes the error when an experiment has `failed`.

## Contents
<a name="API_ExperimentError_Contents"></a>

 ** accountId **   <a name="fis-Type-ExperimentError-accountId"></a>
The AWS Account ID where the experiment failure occurred.
Type: String
Required: No

 ** code **   <a name="fis-Type-ExperimentError-code"></a>
The error code for the failed experiment.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\S]+`
Required: No

 ** location **   <a name="fis-Type-ExperimentError-location"></a>
Context for the section of the experiment template that failed.
Type: String
Required: No

## See Also
<a name="API_ExperimentError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentError)
