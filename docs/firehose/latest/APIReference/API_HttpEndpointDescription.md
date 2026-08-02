---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_HttpEndpointDescription.html
---

# HttpEndpointDescription
<a name="API_HttpEndpointDescription"></a>

Describes the HTTP endpoint selected as the destination.

## Contents
<a name="API_HttpEndpointDescription_Contents"></a>

 ** Name **   <a name="Firehose-Type-HttpEndpointDescription-Name"></a>
The name of the HTTP endpoint selected as the destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^(?!\s*$).+`
Required: No

 ** Url **   <a name="Firehose-Type-HttpEndpointDescription-Url"></a>
The URL of the HTTP endpoint selected as the destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `https://.*`
Required: No

## See Also
<a name="API_HttpEndpointDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/HttpEndpointDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/HttpEndpointDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/HttpEndpointDescription)
