---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ExecutionContext.html
---

# ExecutionContext
<a name="API_ExecutionContext"></a>

Contains contextual information about the execution of a pentest job, such as errors, warnings, or informational messages.

## Contents
<a name="API_ExecutionContext_Contents"></a>

 ** context **   <a name="securityagent-Type-ExecutionContext-context"></a>
The context message.
Type: String
Required: No

 ** contextType **   <a name="securityagent-Type-ExecutionContext-contextType"></a>
The type of context. Valid values include ERROR, CLIENT\_ERROR, WARNING, and INFO.
Type: String
Valid Values: `ERROR | CLIENT_ERROR | WARNING | INFO`
Required: No

 ** timestamp **   <a name="securityagent-Type-ExecutionContext-timestamp"></a>
The date and time the context was recorded, in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_ExecutionContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ExecutionContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ExecutionContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ExecutionContext)
