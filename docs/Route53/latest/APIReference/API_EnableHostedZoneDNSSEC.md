---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_EnableHostedZoneDNSSEC.html
---

# EnableHostedZoneDNSSEC
<a name="API_EnableHostedZoneDNSSEC"></a>

Enables DNSSEC signing in a specific hosted zone.

## Request Syntax
<a name="API_EnableHostedZoneDNSSEC_RequestSyntax"></a>

```
POST /2013-04-01/hostedzone/{{Id}}/enable-dnssec HTTP/1.1
```

## URI Request Parameters
<a name="API_EnableHostedZoneDNSSEC_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_EnableHostedZoneDNSSEC_RequestSyntax) **   <a name="Route53-EnableHostedZoneDNSSEC-request-uri-HostedZoneId"></a>
A unique string used to identify a hosted zone.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_EnableHostedZoneDNSSEC_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_EnableHostedZoneDNSSEC_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<EnableHostedZoneDNSSECResponse>
   <ChangeInfo>
      <Comment>string</Comment>
      <Id>string</Id>
      <Status>string</Status>
      <SubmittedAt>timestamp</SubmittedAt>
   </ChangeInfo>
</EnableHostedZoneDNSSECResponse>
```

## Response Elements
<a name="API_EnableHostedZoneDNSSEC_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [EnableHostedZoneDNSSECResponse](#API_EnableHostedZoneDNSSEC_ResponseSyntax) **   <a name="Route53-EnableHostedZoneDNSSEC-response-EnableHostedZoneDNSSECResponse"></a>
Root level tag for the EnableHostedZoneDNSSECResponse parameters.
Required: Yes

 ** [ChangeInfo](#API_EnableHostedZoneDNSSEC_ResponseSyntax) **   <a name="Route53-EnableHostedZoneDNSSEC-response-ChangeInfo"></a>
A complex type that describes change information about changes made to your hosted zone.
Type: [ChangeInfo](API_ChangeInfo.md) object

## Errors
<a name="API_EnableHostedZoneDNSSEC_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request.
 ** message **

HTTP Status Code: 400

 ** DNSSECNotFound **
The hosted zone doesn't have any DNSSEC resources.
HTTP Status Code: 400

 ** HostedZonePartiallyDelegated **
The hosted zone nameservers don't match the parent nameservers. The hosted zone and parent must have the same nameservers.
HTTP Status Code: 400

 ** InvalidArgument **
Parameter name is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidKeySigningKeyStatus **
The key-signing key (KSK) status isn't valid or another KSK has the status `INTERNAL_FAILURE`.
HTTP Status Code: 400

 ** InvalidKMSArn **
The KeyManagementServiceArn that you specified isn't valid to use with DNSSEC signing.
HTTP Status Code: 400

 ** KeySigningKeyWithActiveStatusNotFound **
A key-signing key (KSK) with `ACTIVE` status wasn't found.
HTTP Status Code: 400

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

## See Also
<a name="API_EnableHostedZoneDNSSEC_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/EnableHostedZoneDNSSEC)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/EnableHostedZoneDNSSEC)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/EnableHostedZoneDNSSEC)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/EnableHostedZoneDNSSEC)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/EnableHostedZoneDNSSEC)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/EnableHostedZoneDNSSEC)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/EnableHostedZoneDNSSEC)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/EnableHostedZoneDNSSEC)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/EnableHostedZoneDNSSEC)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/EnableHostedZoneDNSSEC)
