---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteKeySigningKey.html
---

# DeleteKeySigningKey
<a name="API_DeleteKeySigningKey"></a>

Deletes a key-signing key (KSK). Before you can delete a KSK, you must deactivate it. The KSK must be deactivated before you can delete it regardless of whether the hosted zone is enabled for DNSSEC signing.

You can use [DeactivateKeySigningKey](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeactivateKeySigningKey.html) to deactivate the key before you delete it.

Use [GetDNSSEC](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetDNSSEC.html) to verify that the KSK is in an `INACTIVE` status.

## Request Syntax
<a name="API_DeleteKeySigningKey_RequestSyntax"></a>

```
DELETE /2013-04-01/keysigningkey/{{HostedZoneId}}/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteKeySigningKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HostedZoneId](#API_DeleteKeySigningKey_RequestSyntax) **   <a name="Route53-DeleteKeySigningKey-request-uri-HostedZoneId"></a>
A unique string used to identify a hosted zone.
Length Constraints: Maximum length of 32.
Required: Yes

 ** [Name](#API_DeleteKeySigningKey_RequestSyntax) **   <a name="Route53-DeleteKeySigningKey-request-uri-Name"></a>
A string used to identify a key-signing key (KSK).
Length Constraints: Minimum length of 3. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_DeleteKeySigningKey_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteKeySigningKey_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<DeleteKeySigningKeyResponse>
   <ChangeInfo>
      <Comment>string</Comment>
      <Id>string</Id>
      <Status>string</Status>
      <SubmittedAt>timestamp</SubmittedAt>
   </ChangeInfo>
</DeleteKeySigningKeyResponse>
```

## Response Elements
<a name="API_DeleteKeySigningKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [DeleteKeySigningKeyResponse](#API_DeleteKeySigningKey_ResponseSyntax) **   <a name="Route53-DeleteKeySigningKey-response-DeleteKeySigningKeyResponse"></a>
Root level tag for the DeleteKeySigningKeyResponse parameters.
Required: Yes

 ** [ChangeInfo](#API_DeleteKeySigningKey_ResponseSyntax) **   <a name="Route53-DeleteKeySigningKey-response-ChangeInfo"></a>
A complex type that describes change information about changes made to your hosted zone.
Type: [ChangeInfo](API_ChangeInfo.md) object

## Errors
<a name="API_DeleteKeySigningKey_Errors"></a>

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
<a name="API_DeleteKeySigningKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/DeleteKeySigningKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/DeleteKeySigningKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/DeleteKeySigningKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/DeleteKeySigningKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/DeleteKeySigningKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/DeleteKeySigningKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/DeleteKeySigningKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/DeleteKeySigningKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/DeleteKeySigningKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/DeleteKeySigningKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
