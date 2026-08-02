---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_HttpEndpointCommonAttribute.html
---

# HttpEndpointCommonAttribute
<a name="API_HttpEndpointCommonAttribute"></a>

Describes the metadata that's delivered to the specified HTTP endpoint destination.

## Contents
<a name="API_HttpEndpointCommonAttribute_Contents"></a>

 ** AttributeName **   <a name="Firehose-Type-HttpEndpointCommonAttribute-AttributeName"></a>
The name of the HTTP endpoint common attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^(?!\s*$).+`
Required: Yes

 ** AttributeValue **   <a name="Firehose-Type-HttpEndpointCommonAttribute-AttributeValue"></a>
The value of the HTTP endpoint common attribute.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_HttpEndpointCommonAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/HttpEndpointCommonAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/HttpEndpointCommonAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/HttpEndpointCommonAttribute)
