---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetTrafficPolicyInstance.html
---

# GetTrafficPolicyInstance
<a name="API_GetTrafficPolicyInstance"></a>

Gets information about a specified traffic policy instance.

**Note**
 Use `GetTrafficPolicyInstance` with the `id` of new traffic policy instance to confirm that the `CreateTrafficPolicyInstance` or an `UpdateTrafficPolicyInstance` request completed successfully. For more information, see the `State` response element.

**Note**
In the Route 53 console, traffic policy instances are known as policy records.

## Request Syntax
<a name="API_GetTrafficPolicyInstance_RequestSyntax"></a>

```
GET /2013-04-01/trafficpolicyinstance/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTrafficPolicyInstance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetTrafficPolicyInstance_RequestSyntax) **   <a name="Route53-GetTrafficPolicyInstance-request-uri-Id"></a>
The ID of the traffic policy instance that you want to get information about.
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

## Request Body
<a name="API_GetTrafficPolicyInstance_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTrafficPolicyInstance_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetTrafficPolicyInstanceResponse>
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
</GetTrafficPolicyInstanceResponse>
```

## Response Elements
<a name="API_GetTrafficPolicyInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetTrafficPolicyInstanceResponse](#API_GetTrafficPolicyInstance_ResponseSyntax) **   <a name="Route53-GetTrafficPolicyInstance-response-GetTrafficPolicyInstanceResponse"></a>
Root level tag for the GetTrafficPolicyInstanceResponse parameters.
Required: Yes

 ** [TrafficPolicyInstance](#API_GetTrafficPolicyInstance_ResponseSyntax) **   <a name="Route53-GetTrafficPolicyInstance-response-TrafficPolicyInstance"></a>
A complex type that contains settings for the traffic policy instance.
Type: [TrafficPolicyInstance](API_TrafficPolicyInstance.md) object

## Errors
<a name="API_GetTrafficPolicyInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchTrafficPolicyInstance **
No traffic policy instance exists with the specified ID.
 ** message **

HTTP Status Code: 404

## Examples
<a name="API_GetTrafficPolicyInstance_Examples"></a>

### Example Request
<a name="API_GetTrafficPolicyInstance_Example_1"></a>

This example illustrates one usage of GetTrafficPolicyInstance.

```
GET /2013-04-01/trafficpolicyinstance/12131415-abac-5432-caba-6f5e4d3c2b1a
```

### Example Response
<a name="API_GetTrafficPolicyInstance_Example_2"></a>

This example illustrates one usage of GetTrafficPolicyInstance.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<GetTrafficPolicyInstanceResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
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
</GetTrafficPolicyInstanceResponse>
```

## See Also
<a name="API_GetTrafficPolicyInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetTrafficPolicyInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetTrafficPolicyInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetTrafficPolicyInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetTrafficPolicyInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetTrafficPolicyInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetTrafficPolicyInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetTrafficPolicyInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetTrafficPolicyInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetTrafficPolicyInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetTrafficPolicyInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
