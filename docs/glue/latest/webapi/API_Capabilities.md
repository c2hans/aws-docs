---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Capabilities.html
---

# Capabilities
<a name="API_Capabilities"></a>

Specifies the supported authentication types returned by the `DescribeConnectionType` API.

## Contents
<a name="API_Capabilities_Contents"></a>

 ** SupportedAuthenticationTypes **   <a name="Glue-Type-Capabilities-SupportedAuthenticationTypes"></a>
A list of supported authentication types.
Type: Array of strings
Valid Values: `BASIC | OAUTH2 | CUSTOM | IAM`
Required: Yes

 ** SupportedComputeEnvironments **   <a name="Glue-Type-Capabilities-SupportedComputeEnvironments"></a>
A list of supported compute environments.
Type: Array of strings
Valid Values: `SPARK | ATHENA | PYTHON`
Required: Yes

 ** SupportedDataOperations **   <a name="Glue-Type-Capabilities-SupportedDataOperations"></a>
A list of supported data operations.
Type: Array of strings
Valid Values: `READ | WRITE`
Required: Yes

## See Also
<a name="API_Capabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Capabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Capabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Capabilities)
