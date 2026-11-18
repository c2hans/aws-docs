---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_BatchGetEventError.html
---

# BatchGetEventError
<a name="API_BatchGetEventError"></a>

A requested event that the call didn't return, and the reason.

## Contents
<a name="API_BatchGetEventError_Contents"></a>

 ** errorCode **   <a name="opensearchmemory-Type-BatchGetEventError-errorCode"></a>
The reason that the call didn't return the event.
Type: String
Valid Values: `RESOURCE_NOT_FOUND | THROTTLING | ACCESS_DENIED | INTERNAL_SERVER`
Required: Yes

 ** eventId **   <a name="opensearchmemory-Type-BatchGetEventError-eventId"></a>
The ID of the requested event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** message **   <a name="opensearchmemory-Type-BatchGetEventError-message"></a>
A human-readable description.
Type: String
Required: Yes

## See Also
<a name="API_BatchGetEventError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/BatchGetEventError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/BatchGetEventError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/BatchGetEventError)
