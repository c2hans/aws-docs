---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateVpcConfiguration.html
---

# CreateVpcConfiguration
<a name="API_agent_CreateVpcConfiguration"></a>

Creates a VPC configuration that lets a knowledge base connect to a resource in your private VPC. This operation is asynchronous: it returns a `vpcConfigurationId` with status `CREATING`. Poll `GetVpcConfiguration` until the status becomes `CREATED` or `CREATE_FAILED`.

## Request Syntax
<a name="API_agent_CreateVpcConfiguration_RequestSyntax"></a>

```
POST /knowledgebases/{{knowledgeBaseId}}/vpcconfigurations/ HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "hostHeader": "{{string}}",
   "name": "{{string}}",
   "port": {{number}},
   "protocol": "{{string}}",
   "resolutionMode": "{{string}}",
   "resourceTarget": "{{string}}",
   "subnetIds": [ "{{string}}" ],
   "tlsServerName": "{{string}}",
   "vpcId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent_CreateVpcConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_agent_CreateVpcConfiguration_RequestSyntax) **   <a name="bedrock-agent_CreateVpcConfiguration-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base to associate this VPC configuration with.
Pattern: `[0-9a-zA-Z]{10}`
Required: Yes

## Request Body
<a name="API_agent_CreateVpcConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_agent_CreateVpcConfiguration_RequestSyntax) **   <a name="bedrock-agent_CreateVpcConfiguration-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.
Type: String
Length Constraints: Minimum length of 33. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`
Required: No

 ** [description](#API_agent_CreateVpcConfiguration_RequestSyntax) **   <a name="bedrock-agent_CreateVpcConfiguration-request-description"></a>
An optional description of the VPC configuration. If you don't specify a description, the VPC configuration has no description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[^\p{C}]*`
Required: No

 ** [hostHeader](#API_agent_CreateVpcConfiguration_RequestSyntax) **   <a name="bedrock-agent_CreateVpcConfiguration-request-hostHeader"></a>
An optional HTTP `Host` header value to send when invoking the resource. Set this only if your resource (or an upstream router or ingress) routes by the `Host` header and that host differs from the target. This setting is independent of `tlsServerName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9._:\[\]-]{1,255}`
Required: No

 ** [name](#API_agent_CreateVpcConfiguration_RequestSyntax) **   <a name="bedrock-agent_CreateVpcConfiguration-request-name"></a>
An optional human-readable name for the VPC configuration. If you don't specify a name, the VPC configuration has no name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9 _-]*[a-zA-Z0-9])?`
Required: No

 ** [port](#API_agent_CreateVpcConfiguration_RequestSyntax) **   <a name="bedrock-agent_CreateVpcConfiguration-request-port"></a>
The port on which to reach the resource.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

 ** [protocol](#API_agent_CreateVpcConfiguration_RequestSyntax) **   <a name="bedrock-agent_CreateVpcConfiguration-request-protocol"></a>
The protocol used to connect to the resource. Specify `HTTP` for plaintext or `HTTPS` for TLS. When you specify `HTTPS`, you must also provide `tlsServerName`.
Type: String
Valid Values: `HTTP | HTTPS`
Required: Yes

 ** [resolutionMode](#API_agent_CreateVpcConfiguration_RequestSyntax) **   <a name="bedrock-agent_CreateVpcConfiguration-request-resolutionMode"></a>
Controls how a domain-name `resourceTarget` is resolved. This applies only when the target is a domain name; it has no effect for IP-address targets, which have no name to resolve. In all cases the resolved address must be reachable from inside your VPC. Valid values:
+  `IN_VPC` (default, recommended) – The target domain name is resolved privately, using the DNS resolvers of the VPC, such as private Route 53 hosted zones or on-premises DNS reachable from the VPC. Use this for targets that are private to your VPC, such as internal load balancers, private hosted-zone names, or on-premises hosts.
+  `PUBLIC` – The target domain name is resolved against public DNS resolvers. Select this only when the target's domain name must be resolved through public DNS and the resulting address is still reachable from the VPC, an uncommon split-horizon configuration. If you are unsure, use `IN_VPC`.
Type: String
Valid Values: `PUBLIC | IN_VPC`
Required: Yes

 ** [resourceTarget](#API_agent_CreateVpcConfiguration_RequestSyntax) **   <a name="bedrock-agent_CreateVpcConfiguration-request-resourceTarget"></a>
The private IPv4 address or DNS name of the resource you want the knowledge base to reach. The target must be privately reachable from inside your VPC, such as an internal load balancer or a private IP. The following are not supported:
+ Internet-facing endpoints
+ Loopback addresses
+ Link-local addresses
+ Wildcard addresses
+ Multicast addresses
+ IPv6 literals
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [subnetIds](#API_agent_CreateVpcConfiguration_RequestSyntax) **   <a name="bedrock-agent_CreateVpcConfiguration-request-subnetIds"></a>
The subnets, in the VPC identified by `vpcId`, that the knowledge base uses to connect to the resource.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `subnet-[a-zA-Z0-9]+`
Required: Yes

 ** [tlsServerName](#API_agent_CreateVpcConfiguration_RequestSyntax) **   <a name="bedrock-agent_CreateVpcConfiguration-request-tlsServerName"></a>
The expected TLS server name. The service matches this value against the Subject Alternative Names on your resource's TLS certificate during invocation. This field is required when `protocol` is `HTTPS`. Set it to a hostname on your certificate, such as `app.internal.example.com`. You can use a single leftmost wildcard, such as `*.example.com`. The value must be a hostname without a port.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(\*\.)?([A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)*[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?`
Required: No

 ** [vpcId](#API_agent_CreateVpcConfiguration_RequestSyntax) **   <a name="bedrock-agent_CreateVpcConfiguration-request-vpcId"></a>
The identifier of the VPC that the knowledge base connects through to reach the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `vpc-[a-zA-Z0-9]+`
Required: Yes

## Response Syntax
<a name="API_agent_CreateVpcConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "status": "string",
   "vpcConfigurationId": "string"
}
```

## Response Elements
<a name="API_agent_CreateVpcConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [status](#API_agent_CreateVpcConfiguration_ResponseSyntax) **   <a name="bedrock-agent_CreateVpcConfiguration-response-status"></a>
The current status of the VPC configuration. Immediately after creation this is `CREATING`.
Type: String
Valid Values: `CREATING | CREATED | DELETING | CREATE_FAILED | DELETE_FAILED`

 ** [vpcConfigurationId](#API_agent_CreateVpcConfiguration_ResponseSyntax) **   <a name="bedrock-agent_CreateVpcConfiguration-response-vpcConfigurationId"></a>
The unique identifier of the VPC configuration that was created.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-z0-9](?:[a-z0-9-]{30}[a-z0-9])`

## Errors
<a name="API_agent_CreateVpcConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because of missing access permissions.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict performing an operation.
HTTP Status Code: 409

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The number of requests exceeds the service quota. Resubmit your request later.
HTTP Status Code: 402

 ** ThrottlingException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 429

 ** ValidationException **
Input validation failed. Check your request parameters and retry the request.
 ** fieldList **
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_CreateVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/CreateVpcConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/CreateVpcConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CreateVpcConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/CreateVpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CreateVpcConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/CreateVpcConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/CreateVpcConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/CreateVpcConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/CreateVpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CreateVpcConfiguration)
