---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_TestDNSAnswer.html
---

# TestDNSAnswer
<a name="API_TestDNSAnswer"></a>

Gets the value that Amazon Route 53 returns in response to a DNS request for a specified record name and type. You can optionally specify the IP address of a DNS resolver, an EDNS0 client subnet IP address, and a subnet mask.

This call only supports querying public hosted zones.

**Note**
The `TestDnsAnswer ` returns information similar to what you would expect from the answer section of the `dig` command. Therefore, if you query for the name servers of a subdomain that point to the parent name servers, those will not be returned.

## Request Syntax
<a name="API_TestDNSAnswer_RequestSyntax"></a>

```
GET /2013-04-01/testdnsanswer?edns0clientsubnetip={{EDNS0ClientSubnetIP}}&edns0clientsubnetmask={{EDNS0ClientSubnetMask}}&hostedzoneid={{HostedZoneId}}&recordname={{RecordName}}&recordtype={{RecordType}}&resolverip={{ResolverIP}} HTTP/1.1
```

## URI Request Parameters
<a name="API_TestDNSAnswer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [edns0clientsubnetip](#API_TestDNSAnswer_RequestSyntax) **   <a name="Route53-TestDNSAnswer-request-uri-EDNS0ClientSubnetIP"></a>
If the resolver that you specified for resolverip supports EDNS0, specify the IPv4 or IPv6 address of a client in the applicable location, for example, `192.0.2.44` or `2001:db8:85a3::8a2e:370:7334`.
Length Constraints: Maximum length of 45.
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`

 ** [edns0clientsubnetmask](#API_TestDNSAnswer_RequestSyntax) **   <a name="Route53-TestDNSAnswer-request-uri-EDNS0ClientSubnetMask"></a>
If you specify an IP address for `edns0clientsubnetip`, you can optionally specify the number of bits of the IP address that you want the checking tool to include in the DNS query. For example, if you specify `192.0.2.44` for `edns0clientsubnetip` and `24` for `edns0clientsubnetmask`, the checking tool will simulate a request from 192.0.2.0/24. The default value is 24 bits for IPv4 addresses and 64 bits for IPv6 addresses.
The range of valid values depends on whether `edns0clientsubnetip` is an IPv4 or an IPv6 address:
+  **IPv4**: Specify a value between 0 and 32
+  **IPv6**: Specify a value between 0 and 128
Length Constraints: Minimum length of 0. Maximum length of 3.

 ** [hostedzoneid](#API_TestDNSAnswer_RequestSyntax) **   <a name="Route53-TestDNSAnswer-request-uri-HostedZoneId"></a>
The ID of the hosted zone that you want Amazon Route 53 to simulate a query for.
Length Constraints: Maximum length of 32.
Required: Yes

 ** [recordname](#API_TestDNSAnswer_RequestSyntax) **   <a name="Route53-TestDNSAnswer-request-uri-RecordName"></a>
The name of the resource record set that you want Amazon Route 53 to simulate a query for.
Length Constraints: Maximum length of 1024.
Required: Yes

 ** [recordtype](#API_TestDNSAnswer_RequestSyntax) **   <a name="Route53-TestDNSAnswer-request-uri-RecordType"></a>
The type of the resource record set.
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`
Required: Yes

 ** [resolverip](#API_TestDNSAnswer_RequestSyntax) **   <a name="Route53-TestDNSAnswer-request-uri-ResolverIP"></a>
If you want to simulate a request from a specific DNS resolver, specify the IP address for that resolver. If you omit this value, `TestDnsAnswer` uses the IP address of a DNS resolver in the AWS US East (N. Virginia) Region (`us-east-1`).
Length Constraints: Maximum length of 45.
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`

## Request Body
<a name="API_TestDNSAnswer_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_TestDNSAnswer_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<TestDNSAnswerResponse>
   <Nameserver>string</Nameserver>
   <Protocol>string</Protocol>
   <RecordData>
      <RecordDataEntry>string</RecordDataEntry>
   </RecordData>
   <RecordName>string</RecordName>
   <RecordType>string</RecordType>
   <ResponseCode>string</ResponseCode>
</TestDNSAnswerResponse>
```

## Response Elements
<a name="API_TestDNSAnswer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [TestDNSAnswerResponse](#API_TestDNSAnswer_ResponseSyntax) **   <a name="Route53-TestDNSAnswer-response-TestDNSAnswerResponse"></a>
Root level tag for the TestDNSAnswerResponse parameters.
Required: Yes

 ** [Nameserver](#API_TestDNSAnswer_ResponseSyntax) **   <a name="Route53-TestDNSAnswer-response-Nameserver"></a>
The Amazon Route 53 name server used to respond to the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [Protocol](#API_TestDNSAnswer_ResponseSyntax) **   <a name="Route53-TestDNSAnswer-response-Protocol"></a>
The protocol that Amazon Route 53 used to respond to the request, either `UDP` or `TCP`.
Type: String

 ** [RecordData](#API_TestDNSAnswer_ResponseSyntax) **   <a name="Route53-TestDNSAnswer-response-RecordData"></a>
A list that contains values that Amazon Route 53 returned for this resource record set.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 512.

 ** [RecordName](#API_TestDNSAnswer_ResponseSyntax) **   <a name="Route53-TestDNSAnswer-response-RecordName"></a>
The name of the resource record set that you submitted a request for.
Type: String
Length Constraints: Maximum length of 1024.

 ** [RecordType](#API_TestDNSAnswer_ResponseSyntax) **   <a name="Route53-TestDNSAnswer-response-RecordType"></a>
The type of the resource record set that you submitted a request for.
Type: String
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`

 ** [ResponseCode](#API_TestDNSAnswer_ResponseSyntax) **   <a name="Route53-TestDNSAnswer-response-ResponseCode"></a>
A code that indicates whether the request is valid or not. The most common response code is `NOERROR`, meaning that the request is valid. If the response is not valid, Amazon Route 53 returns a response code that describes the error. For a list of possible response codes, see [DNS RCODES](http://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6) on the IANA website.
Type: String

## Errors
<a name="API_TestDNSAnswer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

## Examples
<a name="API_TestDNSAnswer_Examples"></a>

### Example Request
<a name="API_TestDNSAnswer_Example_1"></a>

This example illustrates one usage of TestDNSAnswer.

```
GET /2013-04-01/testdnsanswer?hostedzoneid=Z111111QQQQQQQ&recordname=www.example.com&recordtype=A&resolverip=192.0.2.44
```

### Example Response
<a name="API_TestDNSAnswer_Example_2"></a>

This example illustrates one usage of TestDNSAnswer.

```
<?xml version="1.0" encoding="UTF-8"?>
<TestDnsAnswerResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Nameserver>ns-2048.awsdns-64.com</Nameserver>
   <RecordName>www.example.com</RecordName>
   <RecordType>A</RecordType>
   <RecordData>
      <RecordDataEntry>198.51.100.222</RecordDataEntry>
   </RecordData>
   <ResponseCode>NOERROR</ResponseCode>
   <Protocol>UDP</Protocol>
</TestDnsAnswerResponse>
```

## See Also
<a name="API_TestDNSAnswer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/TestDNSAnswer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/TestDNSAnswer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/TestDNSAnswer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/TestDNSAnswer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/TestDNSAnswer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/TestDNSAnswer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/TestDNSAnswer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/TestDNSAnswer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/TestDNSAnswer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/TestDNSAnswer)
