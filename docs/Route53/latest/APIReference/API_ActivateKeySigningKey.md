---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ActivateKeySigningKey.html
---

# ActivateKeySigningKey
<a name="API_ActivateKeySigningKey"></a>

Activates a key-signing key (KSK) so that it can be used for signing by DNSSEC. This operation changes the KSK status to `ACTIVE`.

## Request Syntax
<a name="API_ActivateKeySigningKey_RequestSyntax"></a>

```
POST /2013-04-01/keysigningkey/{{HostedZoneId}}/{{Name}}/activate HTTP/1.1
```

## URI Request Parameters
<a name="API_ActivateKeySigningKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HostedZoneId](#API_ActivateKeySigningKey_RequestSyntax) **   <a name="Route53-ActivateKeySigningKey-request-uri-HostedZoneId"></a>
A unique string used to identify a hosted zone.
Length Constraints: Maximum length of 32.
Required: Yes

 ** [Name](#API_ActivateKeySigningKey_RequestSyntax) **   <a name="Route53-ActivateKeySigningKey-request-uri-Name"></a>
A string used to identify a key-signing key (KSK). `Name` can include numbers, letters, and underscores (\_). `Name` must be unique for each key-signing key in the same hosted zone.
Length Constraints: Minimum length of 3. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_ActivateKeySigningKey_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ActivateKeySigningKey_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ActivateKeySigningKeyResponse>
   <ChangeInfo>
      <Comment>string</Comment>
      <Id>string</Id>
      <Status>string</Status>
      <SubmittedAt>timestamp</SubmittedAt>
   </ChangeInfo>
</ActivateKeySigningKeyResponse>
```

## Response Elements
<a name="API_ActivateKeySigningKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ActivateKeySigningKeyResponse](#API_ActivateKeySigningKey_ResponseSyntax) **   <a name="Route53-ActivateKeySigningKey-response-ActivateKeySigningKeyResponse"></a>
Root level tag for the ActivateKeySigningKeyResponse parameters.
Required: Yes

 ** [ChangeInfo](#API_ActivateKeySigningKey_ResponseSyntax) **   <a name="Route53-ActivateKeySigningKey-response-ChangeInfo"></a>
A complex type that describes change information about changes made to your hosted zone.
Type: [ChangeInfo](API_ChangeInfo.md) object

## Errors
<a name="API_ActivateKeySigningKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request.
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

 ** InvalidSigningStatus **
Your hosted zone status isn't valid for this operation. In the hosted zone, change the status to enable `DNSSEC` or disable `DNSSEC`.
HTTP Status Code: 400

 ** NoSuchKeySigningKey **
The specified key-signing key (KSK) doesn't exist.
HTTP Status Code: 404

## See Also
<a name="API_ActivateKeySigningKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ActivateKeySigningKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ActivateKeySigningKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ActivateKeySigningKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ActivateKeySigningKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ActivateKeySigningKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ActivateKeySigningKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ActivateKeySigningKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ActivateKeySigningKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ActivateKeySigningKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ActivateKeySigningKey)
