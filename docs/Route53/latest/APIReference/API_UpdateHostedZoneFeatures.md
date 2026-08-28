---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHostedZoneFeatures.html
---

# UpdateHostedZoneFeatures
<a name="API_UpdateHostedZoneFeatures"></a>

Updates the features configuration for a hosted zone. This operation allows you to enable or disable specific features for your hosted zone, such as accelerated recovery.

Accelerated recovery enables you to update DNS records in your public hosted zone even when the us-east-1 region is unavailable.

## Request Syntax
<a name="API_UpdateHostedZoneFeatures_RequestSyntax"></a>

```
POST /2013-04-01/hostedzone/{{Id}}/features HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHostedZoneFeaturesRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <EnableAcceleratedRecovery>{{boolean}}</EnableAcceleratedRecovery>
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

 ** [EnableAcceleratedRecovery](#API_UpdateHostedZoneFeatures_RequestSyntax) **   <a name="Route53-UpdateHostedZoneFeatures-request-EnableAcceleratedRecovery"></a>
Specifies whether to enable accelerated recovery for the hosted zone. Set to `true` to enable accelerated recovery, or `false` to disable it.
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
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/UpdateHostedZoneFeatures)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/UpdateHostedZoneFeatures)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
