---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_XksProxyConfigurationType.html
---

# XksProxyConfigurationType
<a name="API_XksProxyConfigurationType"></a>

Detailed information about the external key store proxy (XKS proxy). Your external key store proxy translates AWS KMS requests into a format that your external key manager can understand. These fields appear in a [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) response only when the `CustomKeyStoreType` is `EXTERNAL_KEY_STORE`.

## Contents
<a name="API_XksProxyConfigurationType_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccessKeyId **   <a name="KMS-Type-XksProxyConfigurationType-AccessKeyId"></a>
The part of the external key store [proxy authentication credential](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateCustomKeyStore.html#KMS-CreateCustomKeyStore-request-XksProxyAuthenticationCredential) that uniquely identifies the secret access key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 30.
Pattern: `^[A-Z2-7]+$`
Required: No

 ** Connectivity **   <a name="KMS-Type-XksProxyConfigurationType-Connectivity"></a>
Indicates whether the external key store proxy uses a public endpoint or an Amazon VPC endpoint service to communicate with AWS KMS.
Type: String
Valid Values: `PUBLIC_ENDPOINT | VPC_ENDPOINT_SERVICE`
Required: No

 ** UriEndpoint **   <a name="KMS-Type-XksProxyConfigurationType-UriEndpoint"></a>
The URI endpoint for the external key store proxy.
If the external key store proxy has a public endpoint, it is displayed here.
If the external key store proxy uses an Amazon VPC endpoint service name, this field displays the private DNS name associated with the VPC endpoint service.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 128.
Pattern: `^https://[a-zA-Z0-9.-]+$`
Required: No

 ** UriPath **   <a name="KMS-Type-XksProxyConfigurationType-UriPath"></a>
The path to the external key store proxy APIs.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 128.
Pattern: `^(/[a-zA-Z0-9\/_-]+/kms/xks/v\d{1,2})$|^(/kms/xks/v\d{1,2})$`
Required: No

 ** VpcEndpointServiceName **   <a name="KMS-Type-XksProxyConfigurationType-VpcEndpointServiceName"></a>
The Amazon VPC endpoint service used to communicate with the external key store proxy. This field appears only when the external key store proxy uses an Amazon VPC endpoint service to communicate with AWS KMS.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `^(com|eu)\.amazonaws\.vpce\.([a-z]+-){2,3}\d+\.vpce-svc-[0-9a-z]+$`
Required: No

 ** VpcEndpointServiceOwner **   <a name="KMS-Type-XksProxyConfigurationType-VpcEndpointServiceOwner"></a>
The AWS account ID that owns the Amazon VPC endpoint service used to communicate with the external key store proxy (XKS). This field appears only when the XKS uses an VPC endpoint service to communicate with AWS KMS.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

## See Also
<a name="API_XksProxyConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/XksProxyConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/XksProxyConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/XksProxyConfigurationType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
