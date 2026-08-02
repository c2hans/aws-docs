---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_DestinationConfig.html
---

# DestinationConfig
<a name="API_DestinationConfig"></a>

A configuration object that specifies the destination of an event after Lambda processes it. For more information, see [Adding a destination](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html#invocation-async-destinations).

## Contents
<a name="API_DestinationConfig_Contents"></a>

 ** OnFailure **   <a name="lambda-Type-DestinationConfig-OnFailure"></a>
The destination configuration for failed invocations.
Type: [OnFailure](API_OnFailure.md) object
Required: No

 ** OnSuccess **   <a name="lambda-Type-DestinationConfig-OnSuccess"></a>
The destination configuration for successful invocations. Not supported in `CreateEventSourceMapping` or `UpdateEventSourceMapping`.
Type: [OnSuccess](API_OnSuccess.md) object
Required: No

## See Also
<a name="API_DestinationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/DestinationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/DestinationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/DestinationConfig)
