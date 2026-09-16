---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_UpdateIngressPoint.html
---

# UpdateIngressPoint
<a name="API_UpdateIngressPoint"></a>

Update attributes of a provisioned ingress endpoint resource.

## Request Syntax
<a name="API_UpdateIngressPoint_RequestSyntax"></a>

```
{
   "IngressPointConfiguration": { ... },
   "IngressPointId": "{{string}}",
   "IngressPointName": "{{string}}",
   "RuleSetId": "{{string}}",
   "StatusToUpdate": "{{string}}",
   "TlsPolicy": "{{string}}",
   "TrafficPolicyId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateIngressPoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IngressPointConfiguration](#API_UpdateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-UpdateIngressPoint-request-IngressPointConfiguration"></a>
If you choose an Authenticated ingress endpoint, you must configure either an SMTP password or a secret ARN.
Type: [IngressPointConfiguration](API_IngressPointConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [IngressPointId](#API_UpdateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-UpdateIngressPoint-request-IngressPointId"></a>
The identifier for the ingress endpoint you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [IngressPointName](#API_UpdateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-UpdateIngressPoint-request-IngressPointName"></a>
A user friendly name for the ingress endpoint resource.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[A-Za-z0-9_\-]+`
Required: No

 ** [RuleSetId](#API_UpdateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-UpdateIngressPoint-request-RuleSetId"></a>
The identifier of an existing rule set that you attach to an ingress endpoint resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [StatusToUpdate](#API_UpdateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-UpdateIngressPoint-request-StatusToUpdate"></a>
The update status of an ingress endpoint.
Type: String
Valid Values: `ACTIVE | CLOSED`
Required: No

 ** [TlsPolicy](#API_UpdateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-UpdateIngressPoint-request-TlsPolicy"></a>
The Transport Layer Security (TLS) policy for the ingress point. Valid values are REQUIRED, OPTIONAL. Only ingress endpoints using REQUIRED or OPTIONAL as TlsPolicy can be updated.
Type: String
Valid Values: `REQUIRED | OPTIONAL | FIPS`
Required: No

 ** [TrafficPolicyId](#API_UpdateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-UpdateIngressPoint-request-TrafficPolicyId"></a>
The identifier of an existing traffic policy that you attach to an ingress endpoint resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Elements
<a name="API_UpdateIngressPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateIngressPoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_UpdateIngressPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/UpdateIngressPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/UpdateIngressPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/UpdateIngressPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/UpdateIngressPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/UpdateIngressPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/UpdateIngressPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/UpdateIngressPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/UpdateIngressPoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/UpdateIngressPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/UpdateIngressPoint)
