---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_CallbackOptions.html
---

# CallbackOptions
<a name="API_CallbackOptions"></a>

Configuration options for callback operations in durable executions, including timeout settings and retry behavior.

## Contents
<a name="API_CallbackOptions_Contents"></a>

 ** HeartbeatTimeoutSeconds **   <a name="lambda-Type-CallbackOptions-HeartbeatTimeoutSeconds"></a>
The heartbeat timeout for the callback operation, in seconds. If not specified or set to 0, heartbeat timeout is disabled.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 99999999.
Required: No

 ** TimeoutSeconds **   <a name="lambda-Type-CallbackOptions-TimeoutSeconds"></a>
The timeout for the callback operation in seconds. If not specified or set to 0, the callback has no timeout.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 99999999.
Required: No

## See Also
<a name="API_CallbackOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/CallbackOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/CallbackOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/CallbackOptions)
