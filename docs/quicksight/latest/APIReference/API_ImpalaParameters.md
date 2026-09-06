---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ImpalaParameters.html
---

# ImpalaParameters
<a name="API_ImpalaParameters"></a>

The parameters that are required to connect to a Impala data source.

## Contents
<a name="API_ImpalaParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Host **   <a name="QS-Type-ImpalaParameters-Host"></a>
The host name of the Impala data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** Port **   <a name="QS-Type-ImpalaParameters-Port"></a>
The port of the Impala data source.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

 ** SqlEndpointPath **   <a name="QS-Type-ImpalaParameters-SqlEndpointPath"></a>
The HTTP path of the Impala data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** Database **   <a name="QS-Type-ImpalaParameters-Database"></a>
The database of the Impala data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ImpalaParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ImpalaParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ImpalaParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ImpalaParameters)
