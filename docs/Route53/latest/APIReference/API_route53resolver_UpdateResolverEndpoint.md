---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverEndpoint.html
---

# UpdateResolverEndpoint
<a name="API_route53resolver_UpdateResolverEndpoint"></a>

Updates the name, or endpoint type for an inbound or an outbound Resolver endpoint. You can only update between IPV4 and DUALSTACK, IPV6 endpoint type can't be updated to other type.

## Request Syntax
<a name="API_route53resolver_UpdateResolverEndpoint_RequestSyntax"></a>

```
{
   "Dns64Enabled": {{boolean}},
   "Ipv6InternetAccessEnabled": {{boolean}},
   "Name": "{{string}}",
   "Protocols": [ "{{string}}" ],
   "ResolverEndpointId": "{{string}}",
   "ResolverEndpointType": "{{string}}",
   "RniEnhancedMetricsEnabled": {{boolean}},
   "TargetNameServerMetricsEnabled": {{boolean}},
   "UpdateIpAddresses": [
      {
         "IpId": "{{string}}",
         "Ipv6": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_route53resolver_UpdateResolverEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Dns64Enabled](#API_route53resolver_UpdateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverEndpoint-request-Dns64Enabled"></a>
Specifies whether DNS64 is enabled for the inbound Resolver endpoint. When set to `true`, Route 53 Resolver synthesizes AAAA (IPv6) records for IPv4-only services by prepending the `64:ff9b::/96` prefix to the IPv4 address. This enables IPv6-only clients that send queries through the inbound endpoint to reach IPv4-only services. DNS64 works with NAT64 to provide complete IPv6-to-IPv4 translation.
Type: Boolean
Required: No

 ** [Ipv6InternetAccessEnabled](#API_route53resolver_UpdateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverEndpoint-request-Ipv6InternetAccessEnabled"></a>
Specifies whether IPv6 internet access is enabled for the outbound Resolver endpoint. When set to `true`, the endpoint elastic network interfaces (ENIs) can forward DNS queries to public IPv6 targets through an internet gateway.
When you enable IPv6 internet access, use network controls like security groups, NACLs, or egress-only internet gateways to protect the endpoint ENIs from unsolicited ingress traffic. Be aware that some network controls can affect DNS query throughput due to connection tracking. For more information, see [Amazon EC2 security group connection tracking](https://docs.aws.amazon.com/ec2/latest/userguide/security-group-connection-tracking.html) and [Resolver endpoint scaling](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoint-scaling.html).
Type: Boolean
Required: No

 ** [Name](#API_route53resolver_UpdateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverEndpoint-request-Name"></a>
The name of the Resolver endpoint that you want to update.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** [Protocols](#API_route53resolver_UpdateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverEndpoint-request-Protocols"></a>
 The protocols you want to use for the endpoint. DoH-FIPS is applicable for default inbound endpoints only.
For a default inbound endpoint you can apply the protocols as follows:
+  Do53 and DoH in combination.
+ Do53 and DoH-FIPS in combination.
+ Do53 alone.
+ DoH alone.
+ DoH-FIPS alone.
+ None, which is treated as Do53.
For a delegation inbound endpoint you can use Do53 only.
For an outbound endpoint you can apply the protocols as follows:
+  Do53 and DoH in combination.
+ Do53 alone.
+ DoH alone.
+ None, which is treated as Do53.
 You can't change the protocol of an inbound endpoint directly from only Do53 to only DoH, or DoH-FIPS. This is to prevent a sudden disruption to incoming traffic that relies on Do53. To change the protocol from Do53 to DoH, or DoH-FIPS, you must first enable both Do53 and DoH, or Do53 and DoH-FIPS, to make sure that all incoming traffic has transferred to using the DoH protocol, or DoH-FIPS, and then remove the Do53.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `DoH | Do53 | DoH-FIPS`
Required: No

 ** [ResolverEndpointId](#API_route53resolver_UpdateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverEndpoint-request-ResolverEndpointId"></a>
The ID of the Resolver endpoint that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ResolverEndpointType](#API_route53resolver_UpdateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverEndpoint-request-ResolverEndpointType"></a>
 Specifies the endpoint type for what type of IP address the endpoint uses to forward DNS queries.
Updating to `IPV6` type isn't currently supported.
Type: String
Valid Values: `IPV6 | IPV4 | DUALSTACK`
Required: No

 ** [RniEnhancedMetricsEnabled](#API_route53resolver_UpdateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverEndpoint-request-RniEnhancedMetricsEnabled"></a>
Updates whether RNI enhanced metrics are enabled for the Resolver endpoints. When set to true, one-minute granular metrics are published in CloudWatch for each RNI associated with this endpoint. When set to false, metrics are not published.
Standard CloudWatch pricing and charges are applied for using the Route 53 Resolver endpoint RNI enhanced metrics. For more information, see [Detailed metrics](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html).
Type: Boolean
Required: No

 ** [TargetNameServerMetricsEnabled](#API_route53resolver_UpdateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverEndpoint-request-TargetNameServerMetricsEnabled"></a>
Updates whether target name server metrics are enabled for the outbound Resolver endpoints. When set to true, one-minute granular metrics are published in CloudWatch for each target name server associated with this endpoint. When set to false, metrics are not published. This setting is not supported for inbound Resolver endpoints.
Standard CloudWatch pricing and charges are applied for using the Route 53 Resolver endpoint target name server metrics. For more information, see [Detailed metrics](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html).
Type: Boolean
Required: No

 ** [UpdateIpAddresses](#API_route53resolver_UpdateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverEndpoint-request-UpdateIpAddresses"></a>
 Specifies the IPv6 address when you update the Resolver endpoint from IPv4 to dual-stack. If you don't specify an IPv6 address, one will be automatically chosen from your subnet.
Type: Array of [UpdateIpAddress](API_route53resolver_UpdateIpAddress.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_route53resolver_UpdateResolverEndpoint_ResponseSyntax"></a>

```
{
   "ResolverEndpoint": {
      "Arn": "string",
      "CreationTime": "string",
      "CreatorRequestId": "string",
      "Direction": "string",
      "Dns64Enabled": boolean,
      "HostVPCId": "string",
      "Id": "string",
      "IpAddressCount": number,
      "Ipv6InternetAccessEnabled": boolean,
      "ModificationTime": "string",
      "Name": "string",
      "OutpostArn": "string",
      "PreferredInstanceType": "string",
      "Protocols": [ "string" ],
      "ResolverEndpointType": "string",
      "RniEnhancedMetricsEnabled": boolean,
      "SecurityGroupIds": [ "string" ],
      "Status": "string",
      "StatusMessage": "string",
      "TargetNameServerMetricsEnabled": boolean
   }
}
```

## Response Elements
<a name="API_route53resolver_UpdateResolverEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResolverEndpoint](#API_route53resolver_UpdateResolverEndpoint_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverEndpoint-response-ResolverEndpoint"></a>
The response to an `UpdateResolverEndpoint` request.
Type: [ResolverEndpoint](API_route53resolver_ResolverEndpoint.md) object

## Errors
<a name="API_route53resolver_UpdateResolverEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The current account doesn't have the IAM permissions required to perform the specified Resolver operation.
This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.
HTTP Status Code: 400

 ** InternalServiceErrorException **
We encountered an unknown error. Try again in a few minutes.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters in this request are not valid.
 ** FieldName **
For an `InvalidParameterException` error, the name of the parameter that's invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceType **
For a `ResourceNotFoundException` error, the type of resource that doesn't exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

## Examples
<a name="API_route53resolver_UpdateResolverEndpoint_Examples"></a>

### UpdateResolverEndpoint Example
<a name="API_route53resolver_UpdateResolverEndpoint_Example_1"></a>

This example illustrates one usage of UpdateResolverEndpoint.

#### Sample Request
<a name="API_route53resolver_UpdateResolverEndpoint_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: Route53Resolver.UpdateResolverEndpoint
X-Amz-Date: 20181101T192600Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "Name":"MyInbound",
    "ResolverEndpointId": "rslvr-in-60b9fd8fdbexample"
}
```

#### Sample Response
<a name="API_route53resolver_UpdateResolverEndpoint_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 18:52:22 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 479
x-amzn-RequestId: bda80f7b-0f2c-41d1-9043-f36d3example
Connection: keep-alive

{
    "ResolverEndpoint":{
        "Arn":"arn:aws:route53resolver:us-east-2:0123456789012:resolver-endpoint/rslvr-in-60b9fd8fdbexample",
        "CreationTime":"2018-11-01T18:44:50.372Z",
        "CreatorRequestId":"1234",
        "Direction":"INBOUND",
        "HostVPCId":"vpc-03cf94c75cexample",
        "Id":"rslvr-in-60b9fd8fdbexample",
        "IpAddressCount":3,
        "ModificationTime":"2018-11-01T18:44:50.372Z",
        "Name":"MyInbound",
        "Protocols": [
            "DoH"
        ],
        "ResolverEndpointType": "IPV4",
        "Dns64Enabled": false,
        "RniEnhancedMetricsEnabled": false,
        "SecurityGroupIds":[
            "sg-020a3554aexample"
        ],
        "Status":"UPDATING",
        "StatusMessage":"Updating the Resolver Endpoint"
    }
}
```

## See Also
<a name="API_route53resolver_UpdateResolverEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/UpdateResolverEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/UpdateResolverEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/UpdateResolverEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/UpdateResolverEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/UpdateResolverEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/UpdateResolverEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/UpdateResolverEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/UpdateResolverEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/UpdateResolverEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/UpdateResolverEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
