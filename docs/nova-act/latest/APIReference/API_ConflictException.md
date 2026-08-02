---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ConflictException.html
---

# ConflictException
<a name="API_ConflictException"></a>

The request could not be completed due to a conflict with the current state of the resource.

HTTP Status Code returned: 409

## Contents
<a name="API_ConflictException_Contents"></a>

 ** message **   <a name="novaact-Type-ConflictException-message"></a>
The requested operation conflicts with the current state of the resource.
Type: String
Pattern: `[\s\S]+`
Required: Yes

 ** resourceId **   <a name="novaact-Type-ConflictException-resourceId"></a>
The identifier of the resource that caused the conflict.
Type: String
Pattern: `[\s\S]+`
Required: Yes

 ** resourceType **   <a name="novaact-Type-ConflictException-resourceType"></a>
The type of resource that caused the conflict.
Type: String
Pattern: `[\s\S]+`
Required: Yes

## See Also
<a name="API_ConflictException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/ConflictException)
