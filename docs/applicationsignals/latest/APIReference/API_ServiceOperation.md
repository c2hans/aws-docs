---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceOperation.html
---

# ServiceOperation
<a name="API_ServiceOperation"></a>

This structure contains information about an operation discovered by Application Signals. An operation is a specific function performed by a service that was discovered by Application Signals, and is often an API that is called by an upstream dependent.

## Contents
<a name="API_ServiceOperation_Contents"></a>

 ** MetricReferences **   <a name="applicationsignals-Type-ServiceOperation-MetricReferences"></a>
An array of structures that each contain information about one metric associated with this service operation that was discovered by Application Signals.
Type: Array of [MetricReference](API_MetricReference.md) objects
Required: Yes

 ** Name **   <a name="applicationsignals-Type-ServiceOperation-Name"></a>
The name of the operation, discovered by Application Signals.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_ServiceOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ServiceOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ServiceOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ServiceOperation)
