---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateTrafficPolicy.html
---

# CreateTrafficPolicy
<a name="API_CreateTrafficPolicy"></a>

Creates a traffic policy, which you use to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com).

## Request Syntax
<a name="API_CreateTrafficPolicy_RequestSyntax"></a>

```
POST /2013-04-01/trafficpolicy HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateTrafficPolicyRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Comment>{{string}}</Comment>
   <Document>{{string}}</Document>
   <Name>{{string}}</Name>
</CreateTrafficPolicyRequest>
```

## URI Request Parameters
<a name="API_CreateTrafficPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTrafficPolicy_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateTrafficPolicyRequest](#API_CreateTrafficPolicy_RequestSyntax) **   <a name="Route53-CreateTrafficPolicy-request-CreateTrafficPolicyRequest"></a>
Root level tag for the CreateTrafficPolicyRequest parameters.
Required: Yes

 ** [Comment](#API_CreateTrafficPolicy_RequestSyntax) **   <a name="Route53-CreateTrafficPolicy-request-Comment"></a>
(Optional) Any comments that you want to include about the traffic policy.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [Document](#API_CreateTrafficPolicy_RequestSyntax) **   <a name="Route53-CreateTrafficPolicy-request-Document"></a>
The definition of this traffic policy in JSON format. For more information, see [Traffic Policy Document Format](https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html).
Type: String
Length Constraints: Maximum length of 102400.
Required: Yes

 ** [Name](#API_CreateTrafficPolicy_RequestSyntax) **   <a name="Route53-CreateTrafficPolicy-request-Name"></a>
The name of the traffic policy.
Type: String
Length Constraints: Maximum length of 512.
Required: Yes

## Response Syntax
<a name="API_CreateTrafficPolicy_ResponseSyntax"></a>

```
HTTP/1.1 201
Location: {{Location}}
<?xml version="1.0" encoding="UTF-8"?>
<CreateTrafficPolicyResponse>
   <TrafficPolicy>
      <Comment>string</Comment>
      <Document>string</Document>
      <Id>string</Id>
      <Name>string</Name>
      <Type>string</Type>
      <Version>integer</Version>
   </TrafficPolicy>
</CreateTrafficPolicyResponse>
```

## Response Elements
<a name="API_CreateTrafficPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The response returns the following HTTP headers.

 ** [Location](#API_CreateTrafficPolicy_ResponseSyntax) **   <a name="Route53-CreateTrafficPolicy-response-Location"></a>
A unique URL that represents a new traffic policy.
Length Constraints: Maximum length of 1024.

The following data is returned in XML format by the service.

 ** [CreateTrafficPolicyResponse](#API_CreateTrafficPolicy_ResponseSyntax) **   <a name="Route53-CreateTrafficPolicy-response-CreateTrafficPolicyResponse"></a>
Root level tag for the CreateTrafficPolicyResponse parameters.
Required: Yes

 ** [TrafficPolicy](#API_CreateTrafficPolicy_ResponseSyntax) **   <a name="Route53-CreateTrafficPolicy-response-TrafficPolicy"></a>
A complex type that contains settings for the new traffic policy.
Type: [TrafficPolicy](API_TrafficPolicy.md) object

## Errors
<a name="API_CreateTrafficPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidTrafficPolicyDocument **
The format of the traffic policy document that you specified in the `Document` element is not valid.
 ** message **

HTTP Status Code: 400

 ** TooManyTrafficPolicies **
This traffic policy can't be created because the current account has reached the limit on the number of traffic policies.
For information about default limits, see [Limits](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html) in the *Amazon Route 53 Developer Guide*.
To get the current limit for an account, see [GetAccountLimit](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetAccountLimit.html).
To request a higher limit, [create a case](http://aws.amazon.com/route53-request) with the AWS Support Center.
 ** message **

HTTP Status Code: 400

 ** TrafficPolicyAlreadyExists **
A traffic policy that has the same value for `Name` already exists.
 ** message **

HTTP Status Code: 409

## Examples
<a name="API_CreateTrafficPolicy_Examples"></a>

### Example Request
<a name="API_CreateTrafficPolicy_Example_1"></a>

This example illustrates one usage of CreateTrafficPolicy.

```
POST /2013-04-01/trafficpolicy HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateTrafficPolicyRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Name>MyTrafficPolicy</Name>
   <Document>traffic policy definition in JSON format</Document>
   <Comment>First traffic policy</Comment>
</CreateTrafficPolicyRequest>
```

### Example Response
<a name="API_CreateTrafficPolicy_Example_2"></a>

This example illustrates one usage of CreateTrafficPolicy.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<CreateTrafficPolicyResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <TrafficPolicy>
      <Id>12345</Id>
      <Version>1</Version>
      <Name>MyTrafficPolicy</Name>
      <Type>A</Type>
      <Document>traffic policy definition in JSON format</Document>
      <Comment>First traffic policy</Comment>
   </TrafficPolicy>
</CreateTrafficPolicyResponse>
```

## See Also
<a name="API_CreateTrafficPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/CreateTrafficPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/CreateTrafficPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CreateTrafficPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/CreateTrafficPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CreateTrafficPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/CreateTrafficPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/CreateTrafficPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/CreateTrafficPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/CreateTrafficPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CreateTrafficPolicy)
