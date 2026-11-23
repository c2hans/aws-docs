---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHostedZoneFeatures.html
---

# UpdateHostedZoneFeatures

Updates the features configuration for a hosted zone. This operation allows you to enable or disable specific features for your hosted zone, such as accelerated recovery and public DNS fallback.

Accelerated recovery enables you to update DNS records in your public hosted zone even when the us-east-1 region is unavailable.

Public DNS fallback enables Route 53 to retry a query against public DNS when a query for a domain name in a private hosted zone matches no existing name (`NXDOMAIN`). Fallback does not occur when the name exists but has no record of the requested type. Public DNS fallback is supported only for private hosted zones.

## Request Syntax
<a name="API_UpdateHostedZoneFeatures_RequestSyntax"></a>

```
POST /2013-04-01/hostedzone/{{Id}}/features HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHostedZoneFeaturesRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <ChangeGuardrails>
      <ChangeGuardrail>
         <Name>{{string}}</Name>
         <Status>{{string}}</Status>
      </ChangeGuardrail>
   </ChangeGuardrails>
   <DryRun>{{boolean}}</DryRun>
   <EnableAcceleratedRecovery>{{boolean}}</EnableAcceleratedRecovery>
   <EnablePublicDNSFallback>{{boolean}}</EnablePublicDNSFallback>
</UpdateHostedZoneFeaturesRequest>
```

## URI Request Parameters
<a name="API_UpdateHostedZoneFeatures_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateHostedZoneFeatures_RequestSyntax) **   <a name="Route53-UpdateHostedZoneFeatures-request-uri-HostedZoneId"></a>
The ID of the hosted zone for which you want to update features. This is the unique identifier for your hosted zone.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_UpdateHostedZoneFeatures_RequestBody"></a>

The request accepts the following data in XML format.

 ** [UpdateHostedZoneFeaturesRequest](#API_UpdateHostedZoneFeatures_RequestSyntax) **   <a name="Route53-UpdateHostedZoneFeatures-request-UpdateHostedZoneFeaturesRequest"></a>
Root level tag for the UpdateHostedZoneFeaturesRequest parameters.
Required: Yes

 ** [ChangeGuardrails](#API_UpdateHostedZoneFeatures_RequestSyntax) **   <a name="Route53-UpdateHostedZoneFeatures-request-ChangeGuardrails"></a>
Specify the Change Guardrails to turn on or off for the hosted zone. Each entry specifies the name of a guardrail and one of the following statuses:
+  `ENABLED`: Turns on the guardrail.
+  `DISABLED`: Turns off the guardrail.
Guardrails that aren't in the request keep their current status.
You can turn on an optional guardrail only if the tier of the hosted zone offers it. You can't turn off a guardrail that the tier includes, such as `NS_FORMAT_CHECK`. In either case, Route 53 returns an `InvalidInput` error.
Type: Array of [ChangeGuardrail](API_ChangeGuardrail.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [DryRun](#API_UpdateHostedZoneFeatures_RequestSyntax) **   <a name="Route53-UpdateHostedZoneFeatures-request-DryRun"></a>
Specifies whether to validate the request without changing any features. Route 53 returns the same errors as for a real request, but doesn't change the hosted zone. The default is `false`.
Type: Boolean
Required: No

 ** [EnableAcceleratedRecovery](#API_UpdateHostedZoneFeatures_RequestSyntax) **   <a name="Route53-UpdateHostedZoneFeatures-request-EnableAcceleratedRecovery"></a>
Specifies whether to enable accelerated recovery for the hosted zone. Set to `true` to enable accelerated recovery, or `false` to disable it.
Type: Boolean
Required: No

 ** [EnablePublicDNSFallback](#API_UpdateHostedZoneFeatures_RequestSyntax) **   <a name="Route53-UpdateHostedZoneFeatures-request-EnablePublicDNSFallback"></a>
Specifies whether to enable public DNS fallback for the hosted zone. Set to `true` to enable public DNS fallback, or `false` to disable it.
Public DNS fallback applies to the entire hosted zone and to all VPCs that are associated with it. To check whether a change has propagated, call `GetHostedZone` and review `PublicDNSFallbackStatus` in the response.
Public DNS fallback is supported only for private hosted zones.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateHostedZoneFeatures_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateHostedZoneFeatures_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateHostedZoneFeatures_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** LimitsExceeded **
This operation can't be completed because the current account has reached the limit on the resource you are trying to create. To request a higher limit, [create a case](http://aws.amazon.com/route53-request) with the AWS Support Center.
 ** message **

HTTP Status Code: 400

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

 ** PriorRequestNotComplete **
If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an `HTTP 400 error` (`Bad request`). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.
HTTP Status Code: 400

## See Also
<a name="API_UpdateHostedZoneFeatures_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/UpdateHostedZoneFeatures)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/UpdateHostedZoneFeatures)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/UpdateHostedZoneFeatures)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/UpdateHostedZoneFeatures)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/UpdateHostedZoneFeatures)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/UpdateHostedZoneFeatures)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/UpdateHostedZoneFeatures)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/UpdateHostedZoneFeatures)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/UpdateHostedZoneFeatures)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/UpdateHostedZoneFeatures)
