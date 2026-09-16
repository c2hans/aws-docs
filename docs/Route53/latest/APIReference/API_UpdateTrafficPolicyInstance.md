---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateTrafficPolicyInstance.html
---

# UpdateTrafficPolicyInstance
<a name="API_UpdateTrafficPolicyInstance"></a>

**Note**
After you submit a `UpdateTrafficPolicyInstance` request, there's a brief delay while Route 53 creates the resource record sets that are specified in the traffic policy definition. Use `GetTrafficPolicyInstance` with the `id` of updated traffic policy instance confirm that the `UpdateTrafficPolicyInstance` request completed successfully. For more information, see the `State` response element.

Updates the resource record sets in a specified hosted zone that were created based on the settings in a specified traffic policy version.

When you update a traffic policy instance, Amazon Route 53 continues to respond to DNS queries for the root resource record set name (such as example.com) while it replaces one group of resource record sets with another. Route 53 performs the following operations:

1. Route 53 creates a new group of resource record sets based on the specified traffic policy. This is true regardless of how significant the differences are between the existing resource record sets and the new resource record sets.

1. When all of the new resource record sets have been created, Route 53 starts to respond to DNS queries for the root resource record set name (such as example.com) by using the new resource record sets.

1. Route 53 deletes the old group of resource record sets that are associated with the root resource record set name.

## Request Syntax
<a name="API_UpdateTrafficPolicyInstance_RequestSyntax"></a>

```
POST /2013-04-01/trafficpolicyinstance/{{Id}} HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<UpdateTrafficPolicyInstanceRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <TrafficPolicyId>{{string}}</TrafficPolicyId>
   <TrafficPolicyVersion>{{integer}}</TrafficPolicyVersion>
   <TTL>{{long}}</TTL>
</UpdateTrafficPolicyInstanceRequest>
```

## URI Request Parameters
<a name="API_UpdateTrafficPolicyInstance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateTrafficPolicyInstance_RequestSyntax) **   <a name="Route53-UpdateTrafficPolicyInstance-request-uri-Id"></a>
The ID of the traffic policy instance that you want to update.
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

## Request Body
<a name="API_UpdateTrafficPolicyInstance_RequestBody"></a>

The request accepts the following data in XML format.

 ** [UpdateTrafficPolicyInstanceRequest](#API_UpdateTrafficPolicyInstance_RequestSyntax) **   <a name="Route53-UpdateTrafficPolicyInstance-request-UpdateTrafficPolicyInstanceRequest"></a>
Root level tag for the UpdateTrafficPolicyInstanceRequest parameters.
Required: Yes

 ** [TrafficPolicyId](#API_UpdateTrafficPolicyInstance_RequestSyntax) **   <a name="Route53-UpdateTrafficPolicyInstance-request-TrafficPolicyId"></a>
The ID of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** [TrafficPolicyVersion](#API_UpdateTrafficPolicyInstance_RequestSyntax) **   <a name="Route53-UpdateTrafficPolicyInstance-request-TrafficPolicyVersion"></a>
The version of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

 ** [TTL](#API_UpdateTrafficPolicyInstance_RequestSyntax) **   <a name="Route53-UpdateTrafficPolicyInstance-request-TTL"></a>
The TTL that you want Amazon Route 53 to assign to all of the updated resource record sets.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

## Response Syntax
<a name="API_UpdateTrafficPolicyInstance_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<UpdateTrafficPolicyInstanceResponse>
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
</UpdateTrafficPolicyInstanceResponse>
```

## Response Elements
<a name="API_UpdateTrafficPolicyInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [UpdateTrafficPolicyInstanceResponse](#API_UpdateTrafficPolicyInstance_ResponseSyntax) **   <a name="Route53-UpdateTrafficPolicyInstance-response-UpdateTrafficPolicyInstanceResponse"></a>
Root level tag for the UpdateTrafficPolicyInstanceResponse parameters.
Required: Yes

 ** [TrafficPolicyInstance](#API_UpdateTrafficPolicyInstance_ResponseSyntax) **   <a name="Route53-UpdateTrafficPolicyInstance-response-TrafficPolicyInstance"></a>
A complex type that contains settings for the updated traffic policy instance.
Type: [TrafficPolicyInstance](API_TrafficPolicyInstance.md) object

## Errors
<a name="API_UpdateTrafficPolicyInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictingTypes **
You tried to update a traffic policy instance by using a traffic policy version that has a different DNS type than the current type for the instance. You specified the type in the JSON document in the `CreateTrafficPolicy` or `CreateTrafficPolicyVersion`request.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchTrafficPolicy **
No traffic policy exists with the specified ID.
 ** message **

HTTP Status Code: 404

 ** NoSuchTrafficPolicyInstance **
No traffic policy instance exists with the specified ID.
 ** message **

HTTP Status Code: 404

 ** PriorRequestNotComplete **
If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an `HTTP 400 error` (`Bad request`). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.
HTTP Status Code: 400

## Examples
<a name="API_UpdateTrafficPolicyInstance_Examples"></a>

### Example Request
<a name="API_UpdateTrafficPolicyInstance_Example_1"></a>

This example illustrates one usage of UpdateTrafficPolicyInstance.

```
POST /2013-04-01/trafficpolicyinstance/12131415-abac-5432-caba-6f5e4d3c2b1a HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<UpdateTrafficPolicyInstanceRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <TTL>300</TTL>
   <TrafficPolicyId>12345678-abcd-9876-fedc-1a2b3c4de5f6</TrafficPolicyId>
   <VersionNumber>7</VersionNumber>
</UpdateTrafficPolicyInstanceRequest>
```

### Example Response
<a name="API_UpdateTrafficPolicyInstance_Example_2"></a>

This example illustrates one usage of UpdateTrafficPolicyInstance.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<UpdateTrafficPolicyInstanceResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <TrafficPolicyInstance>
      <Id>12131415-abac-5432-caba-6f5e4d3c2b1a</Id>
      <HostedZoneId>Z1D633PJN98FT9</HostedZoneId>
      <Name>www.example.com</Name>
      <TTL>300</TTL>
      <State>Applied</State>
      <Message/>
      <TrafficPolicyId>12345678-abcd-9876-fedc-1a2b3c4de5f6</TrafficPolicyId>
      <TrafficPolicyVersion>7</TrafficPolicyVersion>
      <TrafficPolicyType>A</TrafficPolicyType>
   </TrafficPolicyInstance>
</UpdateTrafficPolicyInstanceResponse>
```

## See Also
<a name="API_UpdateTrafficPolicyInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/UpdateTrafficPolicyInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/UpdateTrafficPolicyInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/UpdateTrafficPolicyInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/UpdateTrafficPolicyInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/UpdateTrafficPolicyInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/UpdateTrafficPolicyInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/UpdateTrafficPolicyInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/UpdateTrafficPolicyInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/UpdateTrafficPolicyInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/UpdateTrafficPolicyInstance)
