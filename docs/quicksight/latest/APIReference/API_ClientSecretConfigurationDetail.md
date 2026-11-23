---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ClientSecretConfigurationDetail.html
---

# ClientSecretConfigurationDetail

The details of an IdP-provided client secret. Required when `ClientSecretSourceType` is `IDP_PROVIDED`.

## Contents
<a name="API_ClientSecretConfigurationDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Idp **   <a name="QS-Type-ClientSecretConfigurationDetail-Idp"></a>
An IdP-provided client secret, with the AWS Secrets Manager secret ARN for each Region.
Type: [IdpClientSecretInput](API_IdpClientSecretInput.md) object
Required: No

## See Also
<a name="API_ClientSecretConfigurationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ClientSecretConfigurationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ClientSecretConfigurationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ClientSecretConfigurationDetail)
