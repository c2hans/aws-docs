---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_NodeInputPort.html
---

# NodeInputPort
<a name="API_NodeInputPort"></a>

A node input port.

## Contents
<a name="API_NodeInputPort_Contents"></a>

 ** DefaultValue **   <a name="panorama-Type-NodeInputPort-DefaultValue"></a>
The input port's default value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Description **   <a name="panorama-Type-NodeInputPort-Description"></a>
The input port's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** MaxConnections **   <a name="panorama-Type-NodeInputPort-MaxConnections"></a>
The input port's max connections.
Type: Integer
Required: No

 ** Name **   <a name="panorama-Type-NodeInputPort-Name"></a>
The input port's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9\_]+`
Required: No

 ** Type **   <a name="panorama-Type-NodeInputPort-Type"></a>
The input port's type.
Type: String
Valid Values: `BOOLEAN | STRING | INT32 | FLOAT32 | MEDIA`
Required: No

## See Also
<a name="API_NodeInputPort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/NodeInputPort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/NodeInputPort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/NodeInputPort)
