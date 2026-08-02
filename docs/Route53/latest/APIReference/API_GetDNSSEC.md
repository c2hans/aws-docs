---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetDNSSEC.html
---

# GetDNSSEC
<a name="API_GetDNSSEC"></a>

Returns information about DNSSEC for a specific hosted zone, including the key-signing keys (KSKs) in the hosted zone.

## Request Syntax
<a name="API_GetDNSSEC_RequestSyntax"></a>

```
GET /2013-04-01/hostedzone/{{Id}}/dnssec HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDNSSEC_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetDNSSEC_RequestSyntax) **   <a name="Route53-GetDNSSEC-request-uri-HostedZoneId"></a>
A unique string used to identify a hosted zone.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_GetDNSSEC_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDNSSEC_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetDNSSECResponse>
   <KeySigningKeys>
      <KeySigningKey>
         <CreatedDate>timestamp</CreatedDate>
         <DigestAlgorithmMnemonic>string</DigestAlgorithmMnemonic>
         <DigestAlgorithmType>integer</DigestAlgorithmType>
         <DigestValue>string</DigestValue>
         <DNSKEYRecord>string</DNSKEYRecord>
         <DSRecord>string</DSRecord>
         <Flag>integer</Flag>
         <KeyTag>integer</KeyTag>
         <KmsArn>string</KmsArn>
         <LastModifiedDate>timestamp</LastModifiedDate>
         <Name>string</Name>
         <PublicKey>string</PublicKey>
         <SigningAlgorithmMnemonic>string</SigningAlgorithmMnemonic>
         <SigningAlgorithmType>integer</SigningAlgorithmType>
         <Status>string</Status>
         <StatusMessage>string</StatusMessage>
      </KeySigningKey>
   </KeySigningKeys>
   <Status>
      <ServeSignature>string</ServeSignature>
      <StatusMessage>string</StatusMessage>
   </Status>
</GetDNSSECResponse>
```

## Response Elements
<a name="API_GetDNSSEC_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetDNSSECResponse](#API_GetDNSSEC_ResponseSyntax) **   <a name="Route53-GetDNSSEC-response-GetDNSSECResponse"></a>
Root level tag for the GetDNSSECResponse parameters.
Required: Yes

 ** [KeySigningKeys](#API_GetDNSSEC_ResponseSyntax) **   <a name="Route53-GetDNSSEC-response-KeySigningKeys"></a>
The key-signing keys (KSKs) in your account.
Type: Array of [KeySigningKey](API_KeySigningKey.md) objects

 ** [Status](#API_GetDNSSEC_ResponseSyntax) **   <a name="Route53-GetDNSSEC-response-Status"></a>
A string representing the status of DNSSEC.
Type: [DNSSECStatus](API_DNSSECStatus.md) object

## Errors
<a name="API_GetDNSSEC_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgument **
Parameter name is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

## See Also
<a name="API_GetDNSSEC_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetDNSSEC)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetDNSSEC)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetDNSSEC)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetDNSSEC)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetDNSSEC)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetDNSSEC)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetDNSSEC)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetDNSSEC)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetDNSSEC)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetDNSSEC)
