---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_QuickAuthenticationConfig.html
---

# QuickAuthenticationConfig

The Quick Sight authentication configuration of an access control application.

## Contents
<a name="API_QuickAuthenticationConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** QuickAuthenticationType **   <a name="QS-Type-QuickAuthenticationConfig-QuickAuthenticationType"></a>
How the external client authenticates to Quick Sight.
Type: String
Valid Values: `QUICK_MANAGED_PUBLIC_AUTH_CODE`
Required: Yes

 ** QuickAuthenticationConfigurationDetail **   <a name="QS-Type-QuickAuthenticationConfig-QuickAuthenticationConfigurationDetail"></a>
The details of the Quick Sight authentication configuration.
Type: [QuickAuthenticationConfigurationDetail](API_QuickAuthenticationConfigurationDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_QuickAuthenticationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/QuickAuthenticationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/QuickAuthenticationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/QuickAuthenticationConfig)
