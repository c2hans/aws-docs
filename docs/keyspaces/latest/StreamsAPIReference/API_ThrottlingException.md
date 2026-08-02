---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_ThrottlingException.html
---

# ThrottlingException
<a name="API_ThrottlingException"></a>

The request rate is too high and exceeds the service's throughput limits.

This exception occurs when you send too many requests in a short period of time. Implement exponential backoff in your retry strategy to handle this exception. Reducing your request frequency or distributing requests more evenly can help avoid throughput exceptions.

This exception can also occur when more than two processes are reading from the same stream shard at the same time. Ensure that only one process reads from a stream shard at the same time.

HTTP Status Code returned: 400

## Contents
<a name="API_ThrottlingException_Contents"></a>

 ** message **   <a name="keyspaces-Type-ThrottlingException-message"></a>
The request was denied due to request throttling. Reduce the frequency of requests and try again.
Type: String
Required: No

## See Also
<a name="API_ThrottlingException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/ThrottlingException)
