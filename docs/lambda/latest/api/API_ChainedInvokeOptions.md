---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ChainedInvokeOptions.html
---

# ChainedInvokeOptions
<a name="API_ChainedInvokeOptions"></a>

Configuration options for chained function invocations in durable executions, including retry settings and timeout configuration.

## Contents
<a name="API_ChainedInvokeOptions_Contents"></a>

 ** FunctionName **   <a name="lambda-Type-ChainedInvokeOptions-FunctionName"></a>
The name or ARN of the Lambda function to invoke.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** TenantId **   <a name="lambda-Type-ChainedInvokeOptions-TenantId"></a>
The tenant identifier for the chained invocation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\._:\/=+\-@ ]+`
Required: No

 ** XAmznTraceId **   <a name="lambda-Type-ChainedInvokeOptions-XAmznTraceId"></a>
The AWS X-Ray trace header to use when starting the chained invocation. This parameter is optional. If you omit this value, the child invocation inherits the parent durable execution's trace header.
Specify this value on the `START` update for the chained invocation operation. For more information about the header format, see [Tracing header](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-tracingheader) in the * AWS X-Ray Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

## See Also
<a name="API_ChainedInvokeOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ChainedInvokeOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ChainedInvokeOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ChainedInvokeOptions)
