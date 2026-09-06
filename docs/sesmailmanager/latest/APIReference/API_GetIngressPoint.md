---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetIngressPoint.html
---

# GetIngressPoint
<a name="API_GetIngressPoint"></a>

Fetch ingress endpoint resource attributes.

## Request Syntax
<a name="API_GetIngressPoint_RequestSyntax"></a>

```
{
   "IncludeTrustStoreContents": "{{string}}",
   "IngressPointId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetIngressPoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IncludeTrustStoreContents](#API_GetIngressPoint_RequestSyntax) **   <a name="sesmailmanager-GetIngressPoint-request-IncludeTrustStoreContents"></a>
Whether to include the trust store contents in the response. Use INCLUDE to retrieve trust store certificate and CRL contents.
Type: String
Valid Values: `EXCLUDE | INCLUDE`
Required: No

 ** [IngressPointId](#API_GetIngressPoint_RequestSyntax) **   <a name="sesmailmanager-GetIngressPoint-request-IngressPointId"></a>
The identifier of an ingress endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_GetIngressPoint_ResponseSyntax"></a>

```
{
   "ARecord": "string",
   "CreatedTimestamp": number,
   "IngressPointArn": "string",
   "IngressPointAuthConfiguration": {
      "IngressPointPasswordConfiguration": {
         "PreviousSmtpPasswordExpiryTimestamp": number,
         "PreviousSmtpPasswordVersion": "string",
         "SmtpPasswordVersion": "string"
      },
      "SecretArn": "string",
      "TlsAuthConfiguration": {
         "TrustStore": {
            "CAContent": "string",
            "CrlContent": "string",
            "KmsKeyArn": "string"
         }
      }
   },
   "IngressPointId": "string",
   "IngressPointName": "string",
   "LastUpdatedTimestamp": number,
   "NetworkConfiguration": { ... },
   "RuleSetId": "string",
   "Status": "string",
   "TlsPolicy": "string",
   "TrafficPolicyId": "string",
   "Type": "string"
}
```

## Response Elements
<a name="API_GetIngressPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARecord](#API_GetIngressPoint_ResponseSyntax) **   <a name="sesmailmanager-GetIngressPoint-response-ARecord"></a>
 The DNS A Record that identifies your ingress endpoint. Configure your DNS Mail Exchange (MX) record with this value to route emails to Mail Manager.
Type: String

 ** [CreatedTimestamp](#API_GetIngressPoint_ResponseSyntax) **   <a name="sesmailmanager-GetIngressPoint-response-CreatedTimestamp"></a>
The timestamp of when the ingress endpoint was created.
Type: Timestamp

 ** [IngressPointArn](#API_GetIngressPoint_ResponseSyntax) **   <a name="sesmailmanager-GetIngressPoint-response-IngressPointArn"></a>
The Amazon Resource Name (ARN) of the ingress endpoint resource.
Type: String

 ** [IngressPointAuthConfiguration](#API_GetIngressPoint_ResponseSyntax) **   <a name="sesmailmanager-GetIngressPoint-response-IngressPointAuthConfiguration"></a>
The authentication configuration of the ingress endpoint resource.
Type: [IngressPointAuthConfiguration](API_IngressPointAuthConfiguration.md) object

 ** [IngressPointId](#API_GetIngressPoint_ResponseSyntax) **   <a name="sesmailmanager-GetIngressPoint-response-IngressPointId"></a>
The identifier of an ingress endpoint resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [IngressPointName](#API_GetIngressPoint_ResponseSyntax) **   <a name="sesmailmanager-GetIngressPoint-response-IngressPointName"></a>
A user friendly name for the ingress endpoint.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[A-Za-z0-9_\-]+`

 ** [LastUpdatedTimestamp](#API_GetIngressPoint_ResponseSyntax) **   <a name="sesmailmanager-GetIngressPoint-response-LastUpdatedTimestamp"></a>
The timestamp of when the ingress endpoint was last updated.
Type: Timestamp

 ** [NetworkConfiguration](#API_GetIngressPoint_ResponseSyntax) **   <a name="sesmailmanager-GetIngressPoint-response-NetworkConfiguration"></a>
The network configuration for the ingress point.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [RuleSetId](#API_GetIngressPoint_ResponseSyntax) **   <a name="sesmailmanager-GetIngressPoint-response-RuleSetId"></a>
The identifier of a rule set resource associated with the ingress endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [Status](#API_GetIngressPoint_ResponseSyntax) **   <a name="sesmailmanager-GetIngressPoint-response-Status"></a>
The status of the ingress endpoint resource.
Type: String
Valid Values: `PROVISIONING | DEPROVISIONING | UPDATING | ACTIVE | CLOSED | FAILED | ASSOCIATED_VPC_ENDPOINT_DOES_NOT_EXIST`

 ** [TlsPolicy](#API_GetIngressPoint_ResponseSyntax) **   <a name="sesmailmanager-GetIngressPoint-response-TlsPolicy"></a>
The selected Transport Layer Security (TLS) policy of the ingress point.
Type: String
Valid Values: `REQUIRED | OPTIONAL | FIPS`

 ** [TrafficPolicyId](#API_GetIngressPoint_ResponseSyntax) **   <a name="sesmailmanager-GetIngressPoint-response-TrafficPolicyId"></a>
The identifier of the traffic policy resource associated with the ingress endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [Type](#API_GetIngressPoint_ResponseSyntax) **   <a name="sesmailmanager-GetIngressPoint-response-Type"></a>
The type of ingress endpoint.
Type: String
Valid Values: `OPEN | AUTH | MTLS`

## Errors
<a name="API_GetIngressPoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_GetIngressPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/GetIngressPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/GetIngressPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/GetIngressPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/GetIngressPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/GetIngressPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/GetIngressPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/GetIngressPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/GetIngressPoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/GetIngressPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/GetIngressPoint)
