---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ResourceIdentifier.html
---

# ResourceIdentifier
<a name="API_ResourceIdentifier"></a>

Information that identifies the noncompliant resource.

## Contents
<a name="API_ResourceIdentifier_Contents"></a>

 ** account **   <a name="iot-Type-ResourceIdentifier-account"></a>
The account with which the resource is associated.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

 ** caCertificateId **   <a name="iot-Type-ResourceIdentifier-caCertificateId"></a>
The ID of the CA certificate used to authorize the certificate.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`
Required: No

 ** clientId **   <a name="iot-Type-ResourceIdentifier-clientId"></a>
The client ID.
Type: String
Required: No

 ** cognitoIdentityPoolId **   <a name="iot-Type-ResourceIdentifier-cognitoIdentityPoolId"></a>
The ID of the Amazon Cognito identity pool.
Type: String
Required: No

 ** deviceCertificateArn **   <a name="iot-Type-ResourceIdentifier-deviceCertificateArn"></a>
The ARN of the identified device certificate.
Type: String
Required: No

 ** deviceCertificateId **   <a name="iot-Type-ResourceIdentifier-deviceCertificateId"></a>
The ID of the certificate attached to the resource.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`
Required: No

 ** iamRoleArn **   <a name="iot-Type-ResourceIdentifier-iamRoleArn"></a>
The ARN of the IAM role that has overly permissive actions.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** issuerCertificateIdentifier **   <a name="iot-Type-ResourceIdentifier-issuerCertificateIdentifier"></a>
The issuer certificate identifier.
Type: [IssuerCertificateIdentifier](API_IssuerCertificateIdentifier.md) object
Required: No

 ** policyVersionIdentifier **   <a name="iot-Type-ResourceIdentifier-policyVersionIdentifier"></a>
The version of the policy associated with the resource.
Type: [PolicyVersionIdentifier](API_PolicyVersionIdentifier.md) object
Required: No

 ** roleAliasArn **   <a name="iot-Type-ResourceIdentifier-roleAliasArn"></a>
The ARN of the role alias that has overly permissive actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_ResourceIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ResourceIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ResourceIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ResourceIdentifier)
