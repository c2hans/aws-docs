---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetTrafficPolicy.html
---

# GetTrafficPolicy
<a name="API_GetTrafficPolicy"></a>

Gets information about a specific traffic policy version.

For information about how of deleting a traffic policy affects the response from `GetTrafficPolicy`, see [DeleteTrafficPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicy.html).

## Request Syntax
<a name="API_GetTrafficPolicy_RequestSyntax"></a>

```
GET /2013-04-01/trafficpolicy/{{Id}}/{{Version}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTrafficPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetTrafficPolicy_RequestSyntax) **   <a name="Route53-GetTrafficPolicy-request-uri-Id"></a>
The ID of the traffic policy that you want to get information about.
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** [Version](#API_GetTrafficPolicy_RequestSyntax) **   <a name="Route53-GetTrafficPolicy-request-uri-Version"></a>
The version number of the traffic policy that you want to get information about.
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

## Request Body
<a name="API_GetTrafficPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTrafficPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetTrafficPolicyResponse>
   <TrafficPolicy>
      <Comment>string</Comment>
      <Document>string</Document>
      <Id>string</Id>
      <Name>string</Name>
      <Type>string</Type>
      <Version>integer</Version>
   </TrafficPolicy>
</GetTrafficPolicyResponse>
```

## Response Elements
<a name="API_GetTrafficPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetTrafficPolicyResponse](#API_GetTrafficPolicy_ResponseSyntax) **   <a name="Route53-GetTrafficPolicy-response-GetTrafficPolicyResponse"></a>
Root level tag for the GetTrafficPolicyResponse parameters.
Required: Yes

 ** [TrafficPolicy](#API_GetTrafficPolicy_ResponseSyntax) **   <a name="Route53-GetTrafficPolicy-response-TrafficPolicy"></a>
A complex type that contains settings for the specified traffic policy.
Type: [TrafficPolicy](API_TrafficPolicy.md) object

## Errors
<a name="API_GetTrafficPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchTrafficPolicy **
No traffic policy exists with the specified ID.
 ** message **

HTTP Status Code: 404

## Examples
<a name="API_GetTrafficPolicy_Examples"></a>

### Example Request
<a name="API_GetTrafficPolicy_Example_1"></a>

This example illustrates one usage of GetTrafficPolicy.

```
GET /2013-04-01/trafficpolicy/12345678-abcd-9876-fedc-1a2b3c4de5f6/2
```

### Example Response
<a name="API_GetTrafficPolicy_Example_2"></a>

This example illustrates one usage of GetTrafficPolicy.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<GetTrafficPolicyResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <TrafficPolicy>
      <Id>12345678-abcd-9876-fedc-1a2b3c4de5f6</Id>
      <Version>2</Version>
      <Name>MyTrafficPolicy</Name>
      <Type>A</Type>
      <Document>traffic policy definition in JSON format</Document>
      <Comment>New traffic policy version</Comment>
   </TrafficPolicy>
</GetTrafficPolicyResponse>
```

## See Also
<a name="API_GetTrafficPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetTrafficPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetTrafficPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetTrafficPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetTrafficPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetTrafficPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetTrafficPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetTrafficPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetTrafficPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetTrafficPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetTrafficPolicy)
