---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ChainedInvokeDetails.html
---

# ChainedInvokeDetails
<a name="API_ChainedInvokeDetails"></a>

Contains details about a chained function invocation in a durable execution, including the target function and invocation parameters.

## Contents
<a name="API_ChainedInvokeDetails_Contents"></a>

 ** Error **   <a name="lambda-Type-ChainedInvokeDetails-Error"></a>
Details about the chained invocation failure.
Type: [ErrorObject](API_ErrorObject.md) object
Required: No

 ** Result **   <a name="lambda-Type-ChainedInvokeDetails-Result"></a>
The response payload from the chained invocation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 6291456.
Required: No

## See Also
<a name="API_ChainedInvokeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ChainedInvokeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ChainedInvokeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ChainedInvokeDetails)
