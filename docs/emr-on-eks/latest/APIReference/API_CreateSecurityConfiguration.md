---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateSecurityConfiguration.html
---

# CreateSecurityConfiguration
<a name="API_CreateSecurityConfiguration"></a>

Creates a security configuration. Security configurations in Amazon EMR on EKS are templates for different security setups. You can use security configurations to configure the AWS Lake Formation integration setup. You can also create a security configuration to re-use a security setup each time you create a virtual cluster.

## Request Syntax
<a name="API_CreateSecurityConfiguration_RequestSyntax"></a>

```
POST /securityconfigurations HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "containerProvider": {
      "id": "{{string}}",
      "info": { ... },
      "type": "{{string}}"
   },
   "name": "{{string}}",
   "securityConfigurationData": {
      "authorizationConfiguration": {
         "encryptionConfiguration": {
            "inTransitEncryptionConfiguration": {
               "tlsCertificateConfiguration": {
                  "certificateProviderType": "{{string}}",
                  "privateCertificateSecretArn": "{{string}}",
                  "publicCertificateSecretArn": "{{string}}"
               }
            }
         },
         "lakeFormationConfiguration": {
            "authorizedSessionTagValue": "{{string}}",
            "queryEngineRoleArn": "{{string}}",
            "secureNamespaceInfo": {
               "clusterId": "{{string}}",
               "namespace": "{{string}}"
            }
         }
      }
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSecurityConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSecurityConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateSecurityConfiguration_RequestSyntax) **   <a name="emroneks-CreateSecurityConfiguration-request-clientToken"></a>
The client idempotency token to use when creating the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: Yes

 ** [containerProvider](#API_CreateSecurityConfiguration_RequestSyntax) **   <a name="emroneks-CreateSecurityConfiguration-request-containerProvider"></a>
The container provider associated with the security configuration.
Type: [ContainerProvider](API_ContainerProvider.md) object
Required: No

 ** [name](#API_CreateSecurityConfiguration_RequestSyntax) **   <a name="emroneks-CreateSecurityConfiguration-request-name"></a>
The name of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: Yes

 ** [securityConfigurationData](#API_CreateSecurityConfiguration_RequestSyntax) **   <a name="emroneks-CreateSecurityConfiguration-request-securityConfigurationData"></a>
Security configuration input for the request.
Type: [SecurityConfigurationData](API_SecurityConfigurationData.md) object
Required: Yes

 ** [tags](#API_CreateSecurityConfiguration_RequestSyntax) **   <a name="emroneks-CreateSecurityConfiguration-request-tags"></a>
The tags to add to the security configuration.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_CreateSecurityConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_CreateSecurityConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateSecurityConfiguration_ResponseSyntax) **   <a name="emroneks-CreateSecurityConfiguration-response-arn"></a>
The ARN (Amazon Resource Name) of the security configuration.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):\/securityconfigurations\/[0-9a-zA-Z]+$`

 ** [id](#API_CreateSecurityConfiguration_ResponseSyntax) **   <a name="emroneks-CreateSecurityConfiguration-response-id"></a>
The ID of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

 ** [name](#API_CreateSecurityConfiguration_ResponseSyntax) **   <a name="emroneks-CreateSecurityConfiguration-response-name"></a>
The name of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`

## Errors
<a name="API_CreateSecurityConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This is an internal server exception.
HTTP Status Code: 500

 ** ValidationException **
There are invalid parameters in the client request.
HTTP Status Code: 400

## See Also
<a name="API_CreateSecurityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/CreateSecurityConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/CreateSecurityConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/CreateSecurityConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/CreateSecurityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/CreateSecurityConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/CreateSecurityConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/CreateSecurityConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/CreateSecurityConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/CreateSecurityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/CreateSecurityConfiguration)
