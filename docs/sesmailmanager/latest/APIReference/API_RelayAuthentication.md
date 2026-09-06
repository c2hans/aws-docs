---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RelayAuthentication.html
---

# RelayAuthentication
<a name="API_RelayAuthentication"></a>

Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored, or specify an empty NoAuthentication structure if the relay destination server does not require SMTP credential authentication.

## Contents
<a name="API_RelayAuthentication_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** NoAuthentication **   <a name="sesmailmanager-Type-RelayAuthentication-NoAuthentication"></a>
Keep an empty structure if the relay destination server does not require SMTP credential authentication.
Type: [NoAuthentication](API_NoAuthentication.md) object
Required: No

 ** SecretArn **   <a name="sesmailmanager-Type-RelayAuthentication-SecretArn"></a>
The ARN of the secret created in secrets manager where the relay server's SMTP credentials are stored.
Type: String
Pattern: `arn:(aws|aws-cn|aws-us-gov|aws-eusc):secretsmanager:[a-z0-9-]+:\d{12}:secret:[a-zA-Z0-9/_+=,.@-]+`
Required: No

## See Also
<a name="API_RelayAuthentication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RelayAuthentication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RelayAuthentication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RelayAuthentication)
