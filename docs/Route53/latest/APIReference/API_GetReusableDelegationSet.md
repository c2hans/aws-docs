---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetReusableDelegationSet.html
---

# GetReusableDelegationSet
<a name="API_GetReusableDelegationSet"></a>

Retrieves information about a specified reusable delegation set, including the four name servers that are assigned to the delegation set.

## Request Syntax
<a name="API_GetReusableDelegationSet_RequestSyntax"></a>

```
GET /2013-04-01/delegationset/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetReusableDelegationSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetReusableDelegationSet_RequestSyntax) **   <a name="Route53-GetReusableDelegationSet-request-uri-Id"></a>
The ID of the reusable delegation set that you want to get a list of name servers for.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_GetReusableDelegationSet_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetReusableDelegationSet_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetReusableDelegationSetResponse>
   <DelegationSet>
      <CallerReference>string</CallerReference>
      <Id>string</Id>
      <NameServers>
         <NameServer>string</NameServer>
      </NameServers>
   </DelegationSet>
</GetReusableDelegationSetResponse>
```

## Response Elements
<a name="API_GetReusableDelegationSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetReusableDelegationSetResponse](#API_GetReusableDelegationSet_ResponseSyntax) **   <a name="Route53-GetReusableDelegationSet-response-GetReusableDelegationSetResponse"></a>
Root level tag for the GetReusableDelegationSetResponse parameters.
Required: Yes

 ** [DelegationSet](#API_GetReusableDelegationSet_ResponseSyntax) **   <a name="Route53-GetReusableDelegationSet-response-DelegationSet"></a>
A complex type that contains information about the reusable delegation set.
Type: [DelegationSet](API_DelegationSet.md) object

## Errors
<a name="API_GetReusableDelegationSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DelegationSetNotReusable **
A reusable delegation set with the specified ID does not exist.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchDelegationSet **
A reusable delegation set with the specified ID does not exist.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_GetReusableDelegationSet_Examples"></a>

### Example Request
<a name="API_GetReusableDelegationSet_Example_1"></a>

This example illustrates one usage of GetReusableDelegationSet.

```
GET /2013-04-01/delegationset/N1PA6795SAMPLE
```

### Example Response
<a name="API_GetReusableDelegationSet_Example_2"></a>

This example illustrates one usage of GetReusableDelegationSet.

```
<?xml version="1.0" encoding="UTF-8"?>
<GetReusableDelegationSetResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <DelegationSet>
      <Id>/delegationset/N1PA6795SAMPLE</Id>
      <CallerReference>2014-10-13T16:30:01Z</CallerReference>
      <NameServers>
         <NameServer>ns-2048.awsdns-64.com</NameServer>
         <NameServer>ns-2049.awsdns-65.net</NameServer>
         <NameServer>ns-2050.awsdns-66.org</NameServer>
         <NameServer>ns-2051.awsdns-67.co.uk</NameServer>
      </NameServers>
   </DelegationSet>
</GetReusableDelegationSetResponse>
```

## See Also
<a name="API_GetReusableDelegationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetReusableDelegationSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetReusableDelegationSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetReusableDelegationSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetReusableDelegationSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetReusableDelegationSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetReusableDelegationSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetReusableDelegationSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetReusableDelegationSet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetReusableDelegationSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetReusableDelegationSet)
