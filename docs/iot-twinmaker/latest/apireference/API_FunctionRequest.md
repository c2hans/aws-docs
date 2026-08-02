---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_FunctionRequest.html
---

# FunctionRequest
<a name="API_FunctionRequest"></a>

The function request body.

## Contents
<a name="API_FunctionRequest_Contents"></a>

 ** implementedBy **   <a name="tm-Type-FunctionRequest-implementedBy"></a>
The data connector.
Type: [DataConnector](API_DataConnector.md) object
Required: No

 ** requiredProperties **   <a name="tm-Type-FunctionRequest-requiredProperties"></a>
The required properties of the function.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** scope **   <a name="tm-Type-FunctionRequest-scope"></a>
The scope of the function.
Type: String
Valid Values: `ENTITY | WORKSPACE`
Required: No

## See Also
<a name="API_FunctionRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/FunctionRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/FunctionRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/FunctionRequest)
