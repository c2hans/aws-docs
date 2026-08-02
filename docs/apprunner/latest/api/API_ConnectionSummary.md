---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_ConnectionSummary.html
---

# ConnectionSummary
<a name="API_ConnectionSummary"></a>

Provides summary information about an AWS App Runner connection resource.

## Contents
<a name="API_ConnectionSummary_Contents"></a>

 ** ConnectionArn **   <a name="apprunner-Type-ConnectionSummary-ConnectionArn"></a>
The Amazon Resource Name (ARN) of this connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

 ** ConnectionName **   <a name="apprunner-Type-ConnectionSummary-ConnectionName"></a>
The customer-provided connection name.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 32.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{3,31}`
Required: No

 ** CreatedAt **   <a name="apprunner-Type-ConnectionSummary-CreatedAt"></a>
The App Runner connection creation time, expressed as a Unix time stamp.
Type: Timestamp
Required: No

 ** ProviderType **   <a name="apprunner-Type-ConnectionSummary-ProviderType"></a>
The source repository provider.
Type: String
Valid Values: `GITHUB | BITBUCKET`
Required: No

 ** Status **   <a name="apprunner-Type-ConnectionSummary-Status"></a>
The current state of the App Runner connection. When the state is `AVAILABLE`, you can use the connection to create an App Runner service.
Type: String
Valid Values: `PENDING_HANDSHAKE | AVAILABLE | ERROR | DELETED`
Required: No

## See Also
<a name="API_ConnectionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/ConnectionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/ConnectionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/ConnectionSummary)
