---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_MockErrorOutput.html
---

# MockErrorOutput
<a name="API_MockErrorOutput"></a>

A JSON object that contains a mocked error.

## Contents
<a name="API_MockErrorOutput_Contents"></a>

 ** cause **   <a name="StepFunctions-Type-MockErrorOutput-cause"></a>
A string containing the cause of the exception thrown when executing the state's logic.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.
Required: No

 ** error **   <a name="StepFunctions-Type-MockErrorOutput-error"></a>
A string denoting the error code of the exception thrown when invoking the tested state. This field is required if `mock.errorOutput` is specified.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_MockErrorOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/MockErrorOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/MockErrorOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/MockErrorOutput)
