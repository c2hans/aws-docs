---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverEndpointIpAddress.html
---

# AssociateResolverEndpointIpAddress
<a name="API_route53resolver_AssociateResolverEndpointIpAddress"></a>

Adds IP addresses to an inbound or an outbound Resolver endpoint. If you want to add more than one IP address, submit one `AssociateResolverEndpointIpAddress` request for each IP address.

To remove an IP address from an endpoint, see [DisassociateResolverEndpointIpAddress](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverEndpointIpAddress.html).

## Request Syntax
<a name="API_route53resolver_AssociateResolverEndpointIpAddress_RequestSyntax"></a>

```
{
   "IpAddress": {
      "Ip": "{{string}}",
      "IpId": "{{string}}",
      "Ipv6": "{{string}}",
      "SubnetId": "{{string}}"
   },
   "ResolverEndpointId": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_AssociateResolverEndpointIpAddress_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IpAddress](#API_route53resolver_AssociateResolverEndpointIpAddress_RequestSyntax) **   <a name="Route53Resolver-route53resolver_AssociateResolverEndpointIpAddress-request-IpAddress"></a>
Either the IPv4 address that you want to add to a Resolver endpoint or a subnet ID. If you specify a subnet ID, Resolver chooses an IP address for you from the available IPs in the specified subnet.
Type: [IpAddressUpdate](API_route53resolver_IpAddressUpdate.md) object
Required: Yes

 ** [ResolverEndpointId](#API_route53resolver_AssociateResolverEndpointIpAddress_RequestSyntax) **   <a name="Route53Resolver-route53resolver_AssociateResolverEndpointIpAddress-request-ResolverEndpointId"></a>
The ID of the Resolver endpoint that you want to associate IP addresses with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_route53resolver_AssociateResolverEndpointIpAddress_ResponseSyntax"></a>

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
<a name="API_route53resolver_AssociateResolverEndpointIpAddress_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResolverEndpoint](#API_route53resolver_AssociateResolverEndpointIpAddress_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_AssociateResolverEndpointIpAddress-response-ResolverEndpoint"></a>
The response to an `AssociateResolverEndpointIpAddress` request.
Type: [ResolverEndpoint](API_route53resolver_ResolverEndpoint.md) object

## Errors
<a name="API_route53resolver_AssociateResolverEndpointIpAddress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_route53resolver_AssociateResolverEndpointIpAddress_Examples"></a>

### AssociateResolverEndpointIpAddress Example
<a name="API_route53resolver_AssociateResolverEndpointIpAddress_Example_1"></a>

This example illustrates one usage of AssociateResolverEndpointIpAddress.

#### Sample Request
<a name="API_route53resolver_AssociateResolverEndpointIpAddress_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 107
X-Amz-Target: Route53Resolver.AssociateResolverEndpointIpAddress
X-Amz-Date: 20181101T185222Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "IpAddress": {
        "SubnetId": "subnet-02f91e0e98example"
    },
    "ResolverEndpointId": "rslvr-in-60b9fd8fdbexample"
}
```

#### Sample Response
<a name="API_route53resolver_AssociateResolverEndpointIpAddress_Example_1_Response"></a>

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
<a name="API_route53resolver_AssociateResolverEndpointIpAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/AssociateResolverEndpointIpAddress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/AssociateResolverEndpointIpAddress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/AssociateResolverEndpointIpAddress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/AssociateResolverEndpointIpAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/AssociateResolverEndpointIpAddress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/AssociateResolverEndpointIpAddress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/AssociateResolverEndpointIpAddress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/AssociateResolverEndpointIpAddress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/AssociateResolverEndpointIpAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/AssociateResolverEndpointIpAddress)
