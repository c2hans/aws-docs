---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateTrafficPolicyInstance.html
---

# CreateTrafficPolicyInstance
<a name="API_CreateTrafficPolicyInstance"></a>

Creates resource record sets in a specified hosted zone based on the settings in a specified traffic policy version. In addition, `CreateTrafficPolicyInstance` associates the resource record sets with a specified domain name (such as example.com) or subdomain name (such as www.example.com). Amazon Route 53 responds to DNS queries for the domain or subdomain name by using the resource record sets that `CreateTrafficPolicyInstance` created.

**Note**
After you submit an `CreateTrafficPolicyInstance` request, there's a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. Use `GetTrafficPolicyInstance` with the `id` of new traffic policy instance to confirm that the `CreateTrafficPolicyInstance` request completed successfully. For more information, see the `State` response element.

## Request Syntax
<a name="API_CreateTrafficPolicyInstance_RequestSyntax"></a>

```
POST /2013-04-01/trafficpolicyinstance HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateTrafficPolicyInstanceRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HostedZoneId>{{string}}</HostedZoneId>
   <Name>{{string}}</Name>
   <TrafficPolicyId>{{string}}</TrafficPolicyId>
   <TrafficPolicyVersion>{{integer}}</TrafficPolicyVersion>
   <TTL>{{long}}</TTL>
</CreateTrafficPolicyInstanceRequest>
```

## URI Request Parameters
<a name="API_CreateTrafficPolicyInstance_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTrafficPolicyInstance_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateTrafficPolicyInstanceRequest](#API_CreateTrafficPolicyInstance_RequestSyntax) **   <a name="Route53-CreateTrafficPolicyInstance-request-CreateTrafficPolicyInstanceRequest"></a>
Root level tag for the CreateTrafficPolicyInstanceRequest parameters.
Required: Yes

 ** [HostedZoneId](#API_CreateTrafficPolicyInstance_RequestSyntax) **   <a name="Route53-CreateTrafficPolicyInstance-request-HostedZoneId"></a>
The ID of the hosted zone that you want Amazon Route 53 to create resource record sets in by using the configuration in a traffic policy.
Type: String
Length Constraints: Maximum length of 32.
Required: Yes

 ** [Name](#API_CreateTrafficPolicyInstance_RequestSyntax) **   <a name="Route53-CreateTrafficPolicyInstance-request-Name"></a>
The domain name (such as example.com) or subdomain name (such as www.example.com) for which Amazon Route 53 responds to DNS queries by using the resource record sets that Route 53 creates for this traffic policy instance.
Type: String
Length Constraints: Maximum length of 1024.
Required: Yes

 ** [TrafficPolicyId](#API_CreateTrafficPolicyInstance_RequestSyntax) **   <a name="Route53-CreateTrafficPolicyInstance-request-TrafficPolicyId"></a>
The ID of the traffic policy that you want to use to create resource record sets in the specified hosted zone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** [TrafficPolicyVersion](#API_CreateTrafficPolicyInstance_RequestSyntax) **   <a name="Route53-CreateTrafficPolicyInstance-request-TrafficPolicyVersion"></a>
The version of the traffic policy that you want to use to create resource record sets in the specified hosted zone.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

 ** [TTL](#API_CreateTrafficPolicyInstance_RequestSyntax) **   <a name="Route53-CreateTrafficPolicyInstance-request-TTL"></a>
(Optional) The TTL that you want Amazon Route 53 to assign to all of the resource record sets that it creates in the specified hosted zone.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

## Response Syntax
<a name="API_CreateTrafficPolicyInstance_ResponseSyntax"></a>

```
HTTP/1.1 201
Location: {{Location}}
<?xml version="1.0" encoding="UTF-8"?>
<CreateTrafficPolicyInstanceResponse>
   <TrafficPolicyInstance>
      <HostedZoneId>string</HostedZoneId>
      <Id>string</Id>
      <Message>string</Message>
      <Name>string</Name>
      <State>string</State>
      <TrafficPolicyId>string</TrafficPolicyId>
      <TrafficPolicyType>string</TrafficPolicyType>
      <TrafficPolicyVersion>integer</TrafficPolicyVersion>
      <TTL>long</TTL>
   </TrafficPolicyInstance>
</CreateTrafficPolicyInstanceResponse>
```

## Response Elements
<a name="API_CreateTrafficPolicyInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The response returns the following HTTP headers.

 ** [Location](#API_CreateTrafficPolicyInstance_ResponseSyntax) **   <a name="Route53-CreateTrafficPolicyInstance-response-Location"></a>
A unique URL that represents a new traffic policy instance.
Length Constraints: Maximum length of 1024.

The following data is returned in XML format by the service.

 ** [CreateTrafficPolicyInstanceResponse](#API_CreateTrafficPolicyInstance_ResponseSyntax) **   <a name="Route53-CreateTrafficPolicyInstance-response-CreateTrafficPolicyInstanceResponse"></a>
Root level tag for the CreateTrafficPolicyInstanceResponse parameters.
Required: Yes

 ** [TrafficPolicyInstance](#API_CreateTrafficPolicyInstance_ResponseSyntax) **   <a name="Route53-CreateTrafficPolicyInstance-response-TrafficPolicyInstance"></a>
A complex type that contains settings for the new traffic policy instance.
Type: [TrafficPolicyInstance](API_TrafficPolicyInstance.md) object

## Errors
<a name="API_CreateTrafficPolicyInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

 ** NoSuchTrafficPolicy **
No traffic policy exists with the specified ID.
 ** message **

HTTP Status Code: 404

 ** TooManyTrafficPolicyInstances **
This traffic policy instance can't be created because the current account has reached the limit on the number of traffic policy instances.
For information about default limits, see [Limits](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html) in the *Amazon Route 53 Developer Guide*.
For information about how to get the current limit for an account, see [GetAccountLimit](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetAccountLimit.html).
To request a higher limit, [create a case](http://aws.amazon.com/route53-request) with the AWS Support Center.
 ** message **

HTTP Status Code: 400

 ** TrafficPolicyInstanceAlreadyExists **
There is already a traffic policy instance with the specified ID.
 ** message **

HTTP Status Code: 409

## Examples
<a name="API_CreateTrafficPolicyInstance_Examples"></a>

### Example Request
<a name="API_CreateTrafficPolicyInstance_Example_1"></a>

This example illustrates one usage of CreateTrafficPolicyInstance.

```
POST /2013-04-01/trafficpolicyinstance HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateTrafficPolicyInstanceRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HostedZoneId>Z1D633PJN98FT9</HostedZoneId>
   <Name>www.example.com</Name>
   <TTL>300</TTL>
   <TrafficPolicyId>12345678-abcd-9876-fedc-1a2b3c4de5f6</TrafficPolicyId>
   <TrafficPolicyVersion>3</TrafficPolicyVersion>
</CreateTrafficPolicyInstanceRequest>
```

### Example Response
<a name="API_CreateTrafficPolicyInstance_Example_2"></a>

This example illustrates one usage of CreateTrafficPolicyInstance.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<CreateTrafficPolicyInstanceResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <TrafficPolicyInstance>
      <Id>12131415-abac-5432-caba-6f5e4d3c2b1a</Id>
      <HostedZoneId>Z1D633PJN98FT9</HostedZoneId>
      <Name>www.example.com</Name>
      <TTL>300</TTL>
      <State>Applied</State>
      <Message/>
      <TrafficPolicyId>12345678-abcd-9876-fedc-1a2b3c4de5f6</TrafficPolicyId>
      <TrafficPolicyVersion>3</TrafficPolicyVersion>
      <TrafficPolicyType>A</TrafficPolicyType>
   </TrafficPolicyInstance>
</CreateTrafficPolicyInstanceResponse>
```

## See Also
<a name="API_CreateTrafficPolicyInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/CreateTrafficPolicyInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/CreateTrafficPolicyInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CreateTrafficPolicyInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/CreateTrafficPolicyInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CreateTrafficPolicyInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/CreateTrafficPolicyInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/CreateTrafficPolicyInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/CreateTrafficPolicyInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/CreateTrafficPolicyInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CreateTrafficPolicyInstance)
