---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_Instance.html
---

# Instance
<a name="API_Instance"></a>

The details of the instance.

## Contents
<a name="API_Instance_Contents"></a>

 ** awsAccountId **   <a name="supplychain-Type-Instance-awsAccountId"></a>
The AWS account ID that owns the instance.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** instanceId **   <a name="supplychain-Type-Instance-instanceId"></a>
The AWS Supply Chain instance identifier.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** state **   <a name="supplychain-Type-Instance-state"></a>
The state of the instance.
Type: String
Valid Values: `Initializing | Active | CreateFailed | DeleteFailed | Deleting | Deleted`
Required: Yes

 ** createdTime **   <a name="supplychain-Type-Instance-createdTime"></a>
The instance creation timestamp.
Type: Timestamp
Required: No

 ** errorMessage **   <a name="supplychain-Type-Instance-errorMessage"></a>
The AWS Supply Chain instance error message. If the instance results in an unhealthy state, customers need to check the error message, delete the current instance, and recreate a new one based on the mitigation from the error message.
Type: String
Required: No

 ** instanceDescription **   <a name="supplychain-Type-Instance-instanceDescription"></a>
The AWS Supply Chain instance description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 501.
Pattern: `([a-zA-Z0-9., _ʼ'%-]){0,500}`
Required: No

 ** instanceName **   <a name="supplychain-Type-Instance-instanceName"></a>
The AWS Supply Chain instance name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `(?![ _ʼ'%-])[a-zA-Z0-9 _ʼ'%-]{0,62}[a-zA-Z0-9]`
Required: No

 ** kmsKeyArn **   <a name="supplychain-Type-Instance-kmsKeyArn"></a>
The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you optionally provided for encryption. If you did not provide anything here, AWS Supply Chain uses the AWS owned KMS key and nothing is returned.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:[a-z0-9][-.a-z0-9]{0,62}:kms:([a-z0-9][-.a-z0-9]{0,62})?:([a-z0-9][-.a-z0-9]{0,62})?:key/.{0,1019}`
Required: No

 ** lastModifiedTime **   <a name="supplychain-Type-Instance-lastModifiedTime"></a>
The instance last modified timestamp.
Type: Timestamp
Required: No

 ** versionNumber **   <a name="supplychain-Type-Instance-versionNumber"></a>
The version number of the instance.
Type: Double
Required: No

 ** webAppDnsDomain **   <a name="supplychain-Type-Instance-webAppDnsDomain"></a>
The WebApp DNS domain name of the instance.
Type: String
Pattern: `(?![-])[a-zA-Z0-9-]{1,62}[a-zA-Z0-9]`
Required: No

## See Also
<a name="API_Instance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/Instance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/Instance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/Instance)
