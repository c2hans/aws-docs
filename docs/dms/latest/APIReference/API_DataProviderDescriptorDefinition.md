---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DataProviderDescriptorDefinition.html
---

# DataProviderDescriptorDefinition
<a name="API_DataProviderDescriptorDefinition"></a>

Information about a data provider.

## Contents
<a name="API_DataProviderDescriptorDefinition_Contents"></a>

 ** DataProviderIdentifier **   <a name="DMS-Type-DataProviderDescriptorDefinition-DataProviderIdentifier"></a>
The name or Amazon Resource Name (ARN) of the data provider.
Type: String
Required: Yes

 ** SecretsManagerAccessRoleArn **   <a name="DMS-Type-DataProviderDescriptorDefinition-SecretsManagerAccessRoleArn"></a>
The ARN of the role used to access AWS Secrets Manager.
Type: String
Required: No

 ** SecretsManagerSecretId **   <a name="DMS-Type-DataProviderDescriptorDefinition-SecretsManagerSecretId"></a>
The identifier of the AWS Secrets Manager Secret used to store access credentials for the data provider.
Type: String
Required: No

## See Also
<a name="API_DataProviderDescriptorDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DataProviderDescriptorDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DataProviderDescriptorDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DataProviderDescriptorDefinition)
