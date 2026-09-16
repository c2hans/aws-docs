---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html
---

# CreateResolverEndpoint
<a name="API_route53resolver_CreateResolverEndpoint"></a>

Creates a Resolver endpoint. There are two types of Resolver endpoints, inbound and outbound:
+ An *inbound Resolver endpoint* forwards DNS queries to the DNS service for a VPC from your network.
+ An *outbound Resolver endpoint* forwards DNS queries from the DNS service for a VPC to your network.

## Request Syntax
<a name="API_route53resolver_CreateResolverEndpoint_RequestSyntax"></a>

```
{
   "CreatorRequestId": "{{string}}",
   "Direction": "{{string}}",
   "Dns64Enabled": {{boolean}},
   "IpAddresses": [
      {
         "Ip": "{{string}}",
         "Ipv6": "{{string}}",
         "SubnetId": "{{string}}"
      }
   ],
   "Ipv6InternetAccessEnabled": {{boolean}},
   "Name": "{{string}}",
   "OutpostArn": "{{string}}",
   "PreferredInstanceType": "{{string}}",
   "Protocols": [ "{{string}}" ],
   "ResolverEndpointType": "{{string}}",
   "RniEnhancedMetricsEnabled": {{boolean}},
   "SecurityGroupIds": [ "{{string}}" ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TargetNameServerMetricsEnabled": {{boolean}}
}
```

## Request Parameters
<a name="API_route53resolver_CreateResolverEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreatorRequestId](#API_route53resolver_CreateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-request-CreatorRequestId"></a>
A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. `CreatorRequestId` can be any unique string, for example, a date/time stamp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Direction](#API_route53resolver_CreateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-request-Direction"></a>
Specify the applicable value:
+  `INBOUND`: Resolver forwards DNS queries to the DNS service for a VPC from your network.
+  `OUTBOUND`: Resolver forwards DNS queries from the DNS service for a VPC to your network.
+  `INBOUND_DELEGATION`: Resolver delegates queries to Route 53 private hosted zones from your network.
Type: String
Valid Values: `INBOUND | OUTBOUND | INBOUND_DELEGATION`
Required: Yes

 ** [Dns64Enabled](#API_route53resolver_CreateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-request-Dns64Enabled"></a>
Specifies whether DNS64 is enabled for the inbound Resolver endpoint. When set to `true`, Route 53 Resolver synthesizes AAAA (IPv6) records for IPv4-only services by prepending the `64:ff9b::/96` prefix to the IPv4 address. This enables IPv6-only clients that send queries through the inbound endpoint to reach IPv4-only services. DNS64 works with NAT64 to provide complete IPv6-to-IPv4 translation. Default is false.
Type: Boolean
Required: No

 ** [IpAddresses](#API_route53resolver_CreateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-request-IpAddresses"></a>
The subnets and IP addresses in your VPC that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints). The subnet ID uniquely identifies a VPC.
Even though the minimum is 1, Route 53 requires that you create at least two.
We recommend using [VPC Resolver on AWS Outposts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-getting-started.html) to create endpoints on AWS Outposts Racks.
Outposts subnets with [Local Network Interface (LNI)](https://docs.aws.amazon.com/outposts/latest/server-userguide/local-network-interface.html) enabled are not compatible with Route 53 Resolver endpoints. If you enable LNI on a subnet that contains Route 53 Resolver endpoint elastic network interfaces (ENIs), those ENIs will stop functioning. For more information, see [Subnet compatibility for Resolver endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver.html#best-practices-resolver-subnet-compatibility) in the *Amazon Route 53 Developer Guide*.
Type: Array of [IpAddressRequest](API_route53resolver_IpAddressRequest.md) objects
Array Members: Minimum number of 2 items. Maximum number of 20 items.
Required: Yes

 ** [Ipv6InternetAccessEnabled](#API_route53resolver_CreateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-request-Ipv6InternetAccessEnabled"></a>
Specifies whether IPv6 internet access is enabled for the outbound Resolver endpoint. When set to `true`, the endpoint elastic network interfaces (ENIs) can forward DNS queries to public IPv6 targets through an internet gateway. Default is false.
When you enable IPv6 internet access, use network controls like security groups, NACLs, or egress-only internet gateways to protect the endpoint ENIs from unsolicited ingress traffic. Be aware that some network controls can affect DNS query throughput due to connection tracking. For more information, see [Amazon EC2 security group connection tracking](https://docs.aws.amazon.com/ec2/latest/userguide/security-group-connection-tracking.html) and [Resolver endpoint scaling](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoint-scaling.html).
Type: Boolean
Required: No

 ** [Name](#API_route53resolver_CreateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-request-Name"></a>
A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** [OutpostArn](#API_route53resolver_CreateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-request-OutpostArn"></a>
The Amazon Resource Name (ARN) of the Outpost. If you specify this, you must also specify a value for the `PreferredInstanceType`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
Required: No

 ** [PreferredInstanceType](#API_route53resolver_CreateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-request-PreferredInstanceType"></a>
The instance type. If you specify this, you must also specify a value for the `OutpostArn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [Protocols](#API_route53resolver_CreateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-request-Protocols"></a>
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
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `DoH | Do53 | DoH-FIPS`
Required: No

 ** [ResolverEndpointType](#API_route53resolver_CreateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-request-ResolverEndpointType"></a>
 For the endpoint type you can choose either IPv4, IPv6, or dual-stack. A dual-stack endpoint means that it will resolve via both IPv4 and IPv6. This endpoint type is applied to all IP addresses.
Type: String
Valid Values: `IPV6 | IPV4 | DUALSTACK`
Required: No

 ** [RniEnhancedMetricsEnabled](#API_route53resolver_CreateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-request-RniEnhancedMetricsEnabled"></a>
Specifies whether RNI enhanced metrics are enabled for the Resolver endpoints. When set to true, one-minute granular metrics are published in CloudWatch for each RNI associated with this endpoint. When set to false, metrics are not published. Default is false.
Standard CloudWatch pricing and charges are applied for using the Route 53 Resolver endpoint RNI enhanced metrics. For more information, see [Detailed metrics](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html).
Type: Boolean
Required: No

 ** [SecurityGroupIds](#API_route53resolver_CreateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-request-SecurityGroupIds"></a>
The ID of one or more security groups that you want to use to control access to this VPC. The security group that you specify must include one or more inbound rules (for inbound Resolver endpoints) or outbound rules (for outbound Resolver endpoints). Inbound and outbound rules must allow TCP and UDP access. For inbound access, open port 53. For outbound access, open the port that you're using for DNS queries on your network.
Some security group rules will cause your connection to be tracked. For outbound resolver endpoint, it can potentially impact the maximum queries per second from outbound endpoint to your target name server. For inbound resolver endpoint, it can bring down the overall maximum queries per second per IP address to as low as 1500. To avoid connection tracking caused by security group, see [Untracked connections](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#untracked-connectionsl).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [Tags](#API_route53resolver_CreateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-request-Tags"></a>
A list of the tag keys and values that you want to associate with the endpoint.
Type: Array of [Tag](API_route53resolver_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** [TargetNameServerMetricsEnabled](#API_route53resolver_CreateResolverEndpoint_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-request-TargetNameServerMetricsEnabled"></a>
Specifies whether target name server metrics are enabled for the outbound Resolver endpoints. When set to true, one-minute granular metrics are published in CloudWatch for each target name server associated with this endpoint. When set to false, metrics are not published. Default is false. This is not supported for inbound Resolver endpoints.
Standard CloudWatch pricing and charges are applied for using the Route 53 Resolver endpoint target name server metrics. For more information, see [Detailed metrics](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html).
Type: Boolean
Required: No

## Response Syntax
<a name="API_route53resolver_CreateResolverEndpoint_ResponseSyntax"></a>

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
<a name="API_route53resolver_CreateResolverEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResolverEndpoint](#API_route53resolver_CreateResolverEndpoint_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverEndpoint-response-ResolverEndpoint"></a>
Information about the `CreateResolverEndpoint` request, including the status of the request.
Type: [ResolverEndpoint](API_route53resolver_ResolverEndpoint.md) object

## Errors
<a name="API_route53resolver_CreateResolverEndpoint_Errors"></a>

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

 ** LimitExceededException **
The request caused one or more limits to be exceeded.
 ** ResourceType **
For a `LimitExceededException` error, the type of resource that exceeded the current limit.
HTTP Status Code: 400

 ** ResourceExistsException **
The resource that you tried to create already exists.
 ** ResourceType **
For a `ResourceExistsException` error, the type of resource that the error applies to.
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
<a name="API_route53resolver_CreateResolverEndpoint_Examples"></a>

### CreateResolverEndpoint Example
<a name="API_route53resolver_CreateResolverEndpoint_Example_1"></a>

This example illustrates one usage of CreateResolverEndpoint.

#### Sample Request
<a name="API_route53resolver_CreateResolverEndpoint_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 283
X-Amz-Target: Route53Resolver.CreateResolverEndpoint
X-Amz-Date: 20181101T191344Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "Direction": "OUTBOUND",
    "Name": "MyOutbound",
    "Tags": [
        {
            "Key": "LineOfBusiness",
            "Value": "Engineering"
        }
    ],
    "CreatorRequestId": "5678",
    "SecurityGroupIds": [
        "sg-071b99f42example"
    ],
    "IpAddresses": [
        {
            "SubnetId": "subnet-0bca4d363dexample"
        },
        {
            "SubnetId": "subnet-0bca4d363dexample"
        }
    ],
    "RniEnhancedMetricsEnabled": false,
    "TargetNameServerMetricsEnabled": true
}
```

#### Sample Response
<a name="API_route53resolver_CreateResolverEndpoint_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 19:13:44 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 531
x-amzn-RequestId: 08afd081-9d67-4281-a277-b3880example
Connection: keep-alive

{
    "ResolverEndpoint": {
        "Arn": "arn:aws:route53resolver:us-east-2:123456789012:resolver-endpoint/rslvr-out-fdc049932dexample",
        "CreationTime": "2018-11-01T19:13:44.830Z",
        "CreatorRequestId": "5678",
        "Direction": "OUTBOUND",
        "HostVPCId": "vpc-0dd415a0edexample",
        "Id": "rslvr-out-fdc049932dexample",
        "IpAddressCount": 2,
        "ModificationTime": "2018-11-01T19:13:44.830Z",
        "Name": "MyOutbound",
        "Protocols": [
            "DoH"
        ],
        "ResolverEndpointType": "IPV4",
        "Ipv6InternetAccessEnabled": false,
        "RniEnhancedMetricsEnabled": false,
        "SecurityGroupIds": [
            "sg-071b99f42example"
        ],
        "Status": "CREATING",
        "StatusMessage": "[Trace id: 1-5bdb5068-e0bdc4d232b1a3fe9c344c10] Creating the Resolver Endpoint",
        "TargetNameServerMetricsEnabled": true
    }
}
```

## See Also
<a name="API_route53resolver_CreateResolverEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/CreateResolverEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/CreateResolverEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/CreateResolverEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/CreateResolverEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/CreateResolverEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/CreateResolverEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/CreateResolverEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/CreateResolverEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/CreateResolverEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/CreateResolverEndpoint)
