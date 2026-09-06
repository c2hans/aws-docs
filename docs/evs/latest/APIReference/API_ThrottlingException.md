---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_ThrottlingException.html
---

# ThrottlingException
<a name="API_ThrottlingException"></a>

The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.

HTTP Status Code returned: 400

## Contents
<a name="API_ThrottlingException_Contents"></a>

 ** message **   <a name="evs-Type-ThrottlingException-message"></a>
Describes the error encountered.
Type: String
Required: Yes

 ** retryAfterSeconds **   <a name="evs-Type-ThrottlingException-retryAfterSeconds"></a>
The seconds to wait to retry.
Type: Integer
Required: No

## See Also
<a name="API_ThrottlingException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/ThrottlingException)
