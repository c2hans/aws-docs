---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_KerberosAuthenticationSettings.html
---

# KerberosAuthenticationSettings
<a name="API_KerberosAuthenticationSettings"></a>

Specifies the settings required for kerberos authentication when creating the replication instance.

## Contents
<a name="API_KerberosAuthenticationSettings_Contents"></a>

 ** KeyCacheSecretIamArn **   <a name="DMS-Type-KerberosAuthenticationSettings-KeyCacheSecretIamArn"></a>
Specifies the Amazon Resource Name (ARN) of the IAM role that grants AWS DMS access to the secret containing key cache file for the kerberos authentication.
Type: String
Required: No

 ** KeyCacheSecretId **   <a name="DMS-Type-KerberosAuthenticationSettings-KeyCacheSecretId"></a>
Specifies the ID of the secret that stores the key cache file required for kerberos authentication.
Type: String
Required: No

 ** Krb5FileContents **   <a name="DMS-Type-KerberosAuthenticationSettings-Krb5FileContents"></a>
Specifies the contents of krb5 configuration file required for kerberos authentication.
Type: String
Required: No

## See Also
<a name="API_KerberosAuthenticationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/KerberosAuthenticationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/KerberosAuthenticationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/KerberosAuthenticationSettings)
