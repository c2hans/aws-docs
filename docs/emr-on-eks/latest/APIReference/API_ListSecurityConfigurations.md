---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListSecurityConfigurations.html
---

# ListSecurityConfigurations
<a name="API_ListSecurityConfigurations"></a>

Lists security configurations based on a set of parameters. Security configurations in Amazon EMR on EKS are templates for different security setups. You can use security configurations to configure the AWS Lake Formation integration setup. You can also create a security configuration to re-use a security setup each time you create a virtual cluster.

## Request Syntax
<a name="API_ListSecurityConfigurations_RequestSyntax"></a>

```
GET /securityconfigurations?createdAfter={{createdAfter}}&createdBefore={{createdBefore}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSecurityConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [createdAfter](#API_ListSecurityConfigurations_RequestSyntax) **   <a name="emroneks-ListSecurityConfigurations-request-uri-createdAfter"></a>
The date and time after which the security configuration was created.

 ** [createdBefore](#API_ListSecurityConfigurations_RequestSyntax) **   <a name="emroneks-ListSecurityConfigurations-request-uri-createdBefore"></a>
The date and time before which the security configuration was created.

 ** [maxResults](#API_ListSecurityConfigurations_RequestSyntax) **   <a name="emroneks-ListSecurityConfigurations-request-uri-maxResults"></a>
The maximum number of security configurations the operation can list.

 ** [nextToken](#API_ListSecurityConfigurations_RequestSyntax) **   <a name="emroneks-ListSecurityConfigurations-request-uri-nextToken"></a>
The token for the next set of security configurations to return.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

## Request Body
<a name="API_ListSecurityConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSecurityConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "securityConfigurations": [
      {
         "arn": "string",
         "createdAt": "string",
         "createdBy": "string",
         "id": "string",
         "name": "string",
         "securityConfigurationData": {
            "authenticationConfiguration": {
               "iamConfiguration": {
                  "systemRole": "string"
               },
               "identityCenterConfiguration": {
                  "emrIdentityCenterApplicationARN": "string",
                  "enableIdentityCenter": boolean,
                  "identityCenterApplicationAssignmentRequired": boolean,
                  "identityCenterInstanceARN": "string"
               }
            },
            "authorizationConfiguration": {
               "encryptionConfiguration": {
                  "inTransitEncryptionConfiguration": {
                     "tlsCertificateConfiguration": {
                        "certificateProviderType": "string",
                        "privateCertificateSecretArn": "string",
                        "publicCertificateSecretArn": "string"
                     }
                  }
               },
               "lakeFormationConfiguration": {
                  "authorizedSessionTagValue": "string",
                  "queryEngineRoleArn": "string",
                  "secureNamespaceInfo": {
                     "clusterId": "string",
                     "namespace": "string"
                  }
               }
            }
         },
         "tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListSecurityConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSecurityConfigurations_ResponseSyntax) **   <a name="emroneks-ListSecurityConfigurations-response-nextToken"></a>
The token for the next set of security configurations to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [securityConfigurations](#API_ListSecurityConfigurations_ResponseSyntax) **   <a name="emroneks-ListSecurityConfigurations-response-securityConfigurations"></a>
The list of returned security configurations.
Type: Array of [SecurityConfiguration](API_SecurityConfiguration.md) objects

## Errors
<a name="API_ListSecurityConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This is an internal server exception.
HTTP Status Code: 500

 ** ValidationException **
There are invalid parameters in the client request.
HTTP Status Code: 400

## See Also
<a name="API_ListSecurityConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/ListSecurityConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/ListSecurityConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/ListSecurityConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/ListSecurityConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/ListSecurityConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/ListSecurityConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/ListSecurityConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/ListSecurityConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/ListSecurityConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/ListSecurityConfigurations)
