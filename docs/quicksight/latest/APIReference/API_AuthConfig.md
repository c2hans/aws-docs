---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AuthConfig.html
---

# AuthConfig
<a name="API_AuthConfig"></a>

Authentication configuration for connecting to external services.

## Contents
<a name="API_AuthConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AuthenticationMetadata **   <a name="QS-Type-AuthConfig-AuthenticationMetadata"></a>
The authentication metadata containing the specific configuration for the chosen authentication type.
Type: [AuthenticationMetadata](API_AuthenticationMetadata.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** AuthenticationType **   <a name="QS-Type-AuthConfig-AuthenticationType"></a>
The type of authentication method.
Type: String
Valid Values: `BASIC | API_KEY | OAUTH2_CLIENT_CREDENTIALS | NONE | IAM | OAUTH2_AUTHORIZATION_CODE`
Required: Yes

## See Also
<a name="API_AuthConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AuthConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AuthConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AuthConfig)
