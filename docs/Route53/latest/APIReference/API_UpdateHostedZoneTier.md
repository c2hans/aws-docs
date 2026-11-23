---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHostedZoneTier.html
---

# UpdateHostedZoneTier

You can change the tier of a hosted zone. The tier determines which features the hosted zone includes and which optional features you can turn on.

When the hosted zone moves to a new tier, Route 53 turns on the features that the new tier includes. Route 53 also disables any enabled features that the new tier doesn't include.

Before you move a hosted zone to a tier that doesn't offer an optional feature that you turned on, turn off that feature. You can't change the tier of a hosted zone that uses a CloudFront flat-rate pricing plan.

## Request Syntax
<a name="API_UpdateHostedZoneTier_RequestSyntax"></a>

```
POST /2013-04-01/hostedzone/{{Id}}/tier HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHostedZoneTierRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <DryRun>{{boolean}}</DryRun>
   <HostedZoneTier>{{string}}</HostedZoneTier>
</UpdateHostedZoneTierRequest>
```

## URI Request Parameters
<a name="API_UpdateHostedZoneTier_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateHostedZoneTier_RequestSyntax) **   <a name="Route53-UpdateHostedZoneTier-request-uri-HostedZoneId"></a>
Specify the ID of the hosted zone whose tier you want to change.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_UpdateHostedZoneTier_RequestBody"></a>

The request accepts the following data in XML format.

 ** [UpdateHostedZoneTierRequest](#API_UpdateHostedZoneTier_RequestSyntax) **   <a name="Route53-UpdateHostedZoneTier-request-UpdateHostedZoneTierRequest"></a>
Root level tag for the UpdateHostedZoneTierRequest parameters.
Required: Yes

 ** [DryRun](#API_UpdateHostedZoneTier_RequestSyntax) **   <a name="Route53-UpdateHostedZoneTier-request-DryRun"></a>
Specifies whether to validate the request without changing the tier. Route 53 returns the same errors as for a real request, but doesn't change the hosted zone. The default is `false`.
Type: Boolean
Required: No

 ** [HostedZoneTier](#API_UpdateHostedZoneTier_RequestSyntax) **   <a name="Route53-UpdateHostedZoneTier-request-HostedZoneTier"></a>
Specify the tier to move the hosted zone to. Valid values are the following:
+  `STANDARD`: The default tier for new hosted zones.
+  `ADVANCED`: A tier that includes Change History and offers more optional features.
Type: String
Valid Values: `STANDARD | ADVANCED`
Required: Yes

## Response Syntax
<a name="API_UpdateHostedZoneTier_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateHostedZoneTier_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateHostedZoneTier_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
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
<a name="API_UpdateHostedZoneTier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/UpdateHostedZoneTier)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/UpdateHostedZoneTier)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/UpdateHostedZoneTier)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/UpdateHostedZoneTier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/UpdateHostedZoneTier)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/UpdateHostedZoneTier)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/UpdateHostedZoneTier)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/UpdateHostedZoneTier)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/UpdateHostedZoneTier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/UpdateHostedZoneTier)
