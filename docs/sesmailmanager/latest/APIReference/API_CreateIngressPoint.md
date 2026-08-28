---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateIngressPoint.html
---

# CreateIngressPoint
<a name="API_CreateIngressPoint"></a>

Provision a new ingress endpoint resource.

## Request Syntax
<a name="API_CreateIngressPoint_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "IngressPointConfiguration": { ... },
   "IngressPointName": "{{string}}",
   "NetworkConfiguration": { ... },
   "RuleSetId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TlsPolicy": "{{string}}",
   "TrafficPolicyId": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateIngressPoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-CreateIngressPoint-request-ClientToken"></a>
A unique token that Amazon SES uses to recognize subsequent retries of the same request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [IngressPointConfiguration](#API_CreateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-CreateIngressPoint-request-IngressPointConfiguration"></a>
If you choose an Authenticated ingress endpoint, you must configure either an SMTP password or a secret ARN.
Type: [IngressPointConfiguration](API_IngressPointConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [IngressPointName](#API_CreateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-CreateIngressPoint-request-IngressPointName"></a>
A user friendly name for an ingress endpoint resource.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[A-Za-z0-9_\-]+`
Required: Yes

 ** [NetworkConfiguration](#API_CreateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-CreateIngressPoint-request-NetworkConfiguration"></a>
Specifies the network configuration for the ingress point. This allows you to create an IPv4-only, Dual-Stack, or PrivateLink type of ingress point. If not specified, the default network type is IPv4-only.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [RuleSetId](#API_CreateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-CreateIngressPoint-request-RuleSetId"></a>
The identifier of an existing rule set that you attach to an ingress endpoint resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [Tags](#API_CreateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-CreateIngressPoint-request-Tags"></a>
The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [TlsPolicy](#API_CreateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-CreateIngressPoint-request-TlsPolicy"></a>
The Transport Layer Security (TLS) policy for the ingress point. The FIPS value is only valid in US and Canada regions.
Type: String
Valid Values: `REQUIRED | OPTIONAL | FIPS`
Required: No

 ** [TrafficPolicyId](#API_CreateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-CreateIngressPoint-request-TrafficPolicyId"></a>
The identifier of an existing traffic policy that you attach to an ingress endpoint resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [Type](#API_CreateIngressPoint_RequestSyntax) **   <a name="sesmailmanager-CreateIngressPoint-request-Type"></a>
The type of the ingress endpoint to create.
Type: String
Valid Values: `OPEN | AUTH | MTLS`
Required: Yes

## Response Syntax
<a name="API_CreateIngressPoint_ResponseSyntax"></a>

```
{
   "IngressPointId": "string"
}
```

## Response Elements
<a name="API_CreateIngressPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IngressPointId](#API_CreateIngressPoint_ResponseSyntax) **   <a name="sesmailmanager-CreateIngressPoint-response-IngressPointId"></a>
The unique identifier for a previously created ingress endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

## Errors
<a name="API_CreateIngressPoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Occurs when an operation exceeds a predefined service quota or limit.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateIngressPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/CreateIngressPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/CreateIngressPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/CreateIngressPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/CreateIngressPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/CreateIngressPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/CreateIngressPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/CreateIngressPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/CreateIngressPoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/CreateIngressPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/CreateIngressPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
