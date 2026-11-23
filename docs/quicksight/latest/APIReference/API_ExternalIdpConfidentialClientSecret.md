---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ExternalIdpConfidentialClientSecret.html
---

# ExternalIdpConfidentialClientSecret

A client secret of a confidential external IdP client. Secret values are never included.

## Contents
<a name="API_ExternalIdpConfidentialClientSecret_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClientSecretId **   <a name="QS-Type-ExternalIdpConfidentialClientSecret-ClientSecretId"></a>
The ID of the client secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** CreatedAt **   <a name="QS-Type-ExternalIdpConfidentialClientSecret-CreatedAt"></a>
The time when the client secret was created.
Type: Timestamp
Required: Yes

 ** Description **   <a name="QS-Type-ExternalIdpConfidentialClientSecret-Description"></a>
The description of the client secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9 _.,!?\-]*`
Required: No

 ** RegionalSecretManagerArns **   <a name="QS-Type-ExternalIdpConfidentialClientSecret-RegionalSecretManagerArns"></a>
The ARN of the AWS Secrets Manager secret that holds the client secret, for each Region.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 5. Maximum length of 30.
Key Pattern: `[a-z]{2}(-[a-z]+)+-[0-9]+`
Value Length Constraints: Minimum length of 20. Maximum length of 2048.
Value Pattern: `arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:.+`
Required: No

 ** UpdatedAt **   <a name="QS-Type-ExternalIdpConfidentialClientSecret-UpdatedAt"></a>
The time when the secret's Region ARNs were last updated. This value is present only after you call `UpdateAccessControlApplicationSecret`.
Type: Timestamp
Required: No

## See Also
<a name="API_ExternalIdpConfidentialClientSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ExternalIdpConfidentialClientSecret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ExternalIdpConfidentialClientSecret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ExternalIdpConfidentialClientSecret)
