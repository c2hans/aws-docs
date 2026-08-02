---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RedshiftCredentials.html
---

# RedshiftCredentials
<a name="API_RedshiftCredentials"></a>

Amazon Redshift credentials of a connection.

## Contents
<a name="API_RedshiftCredentials_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** secretArn **   <a name="datazone-Type-RedshiftCredentials-secretArn"></a>
The secret ARN of the Amazon Redshift credentials of a connection.
Type: String
Pattern: `arn:aws[^:]*:secretsmanager:[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]:\d{12}:secret:.*`
Required: No

 ** usernamePassword **   <a name="datazone-Type-RedshiftCredentials-usernamePassword"></a>
The username and password of the Amazon Redshift credentials of a connection.
Type: [UsernamePassword](API_UsernamePassword.md) object
Required: No

## See Also
<a name="API_RedshiftCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RedshiftCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RedshiftCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RedshiftCredentials)
