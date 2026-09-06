---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_OracleParameters.html
---

# OracleParameters
<a name="API_OracleParameters"></a>

The parameters for Oracle.

## Contents
<a name="API_OracleParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Database **   <a name="QS-Type-OracleParameters-Database"></a>
The database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Host **   <a name="QS-Type-OracleParameters-Host"></a>
An Oracle host.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** Port **   <a name="QS-Type-OracleParameters-Port"></a>
The port.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

 ** UseServiceName **   <a name="QS-Type-OracleParameters-UseServiceName"></a>
A Boolean value that indicates whether the `Database` uses a service name or an SID. If this value is left blank, the default value is `SID`. If this value is set to `false`, the value is `SID`.
Type: Boolean
Required: No

## See Also
<a name="API_OracleParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/OracleParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/OracleParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/OracleParameters)
