---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZoneLimit.html
---

# GetHostedZoneLimit
<a name="API_GetHostedZoneLimit"></a>

Gets the specified limit for a specified hosted zone, for example, the maximum number of records that you can create in the hosted zone.

For the default limit, see [Limits](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html) in the *Amazon Route 53 Developer Guide*. To request a higher limit, [open a case](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-route53).

## Request Syntax
<a name="API_GetHostedZoneLimit_RequestSyntax"></a>

```
GET /2013-04-01/hostedzonelimit/{{Id}}/{{Type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetHostedZoneLimit_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetHostedZoneLimit_RequestSyntax) **   <a name="Route53-GetHostedZoneLimit-request-uri-HostedZoneId"></a>
The ID of the hosted zone that you want to get a limit for.
Length Constraints: Maximum length of 32.
Required: Yes

 ** [Type](#API_GetHostedZoneLimit_RequestSyntax) **   <a name="Route53-GetHostedZoneLimit-request-uri-Type"></a>
The limit that you want to get. Valid values include the following:
+  **MAX\_RRSETS\_BY\_ZONE**: The maximum number of records that you can create in the specified hosted zone.
+  **MAX\_VPCS\_ASSOCIATED\_BY\_ZONE**: The maximum number of Amazon VPCs that you can associate with the specified private hosted zone.
Valid Values: `MAX_RRSETS_BY_ZONE | MAX_VPCS_ASSOCIATED_BY_ZONE`
Required: Yes

## Request Body
<a name="API_GetHostedZoneLimit_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetHostedZoneLimit_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetHostedZoneLimitResponse>
   <Count>long</Count>
   <Limit>
      <Type>string</Type>
      <Value>long</Value>
   </Limit>
</GetHostedZoneLimitResponse>
```

## Response Elements
<a name="API_GetHostedZoneLimit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetHostedZoneLimitResponse](#API_GetHostedZoneLimit_ResponseSyntax) **   <a name="Route53-GetHostedZoneLimit-response-GetHostedZoneLimitResponse"></a>
Root level tag for the GetHostedZoneLimitResponse parameters.
Required: Yes

 ** [Count](#API_GetHostedZoneLimit_ResponseSyntax) **   <a name="Route53-GetHostedZoneLimit-response-Count"></a>
The current number of entities that you have created of the specified type. For example, if you specified `MAX_RRSETS_BY_ZONE` for the value of `Type` in the request, the value of `Count` is the current number of records that you have created in the specified hosted zone.
Type: Long
Valid Range: Minimum value of 0.

 ** [Limit](#API_GetHostedZoneLimit_ResponseSyntax) **   <a name="Route53-GetHostedZoneLimit-response-Limit"></a>
The current setting for the specified limit. For example, if you specified `MAX_RRSETS_BY_ZONE` for the value of `Type` in the request, the value of `Limit` is the maximum number of records that you can create in the specified hosted zone.
Type: [HostedZoneLimit](API_HostedZoneLimit.md) object

## Errors
<a name="API_GetHostedZoneLimit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** HostedZoneNotPrivate **
The specified hosted zone is a public hosted zone, not a private hosted zone.
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
<a name="API_GetHostedZoneLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetHostedZoneLimit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetHostedZoneLimit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetHostedZoneLimit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetHostedZoneLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetHostedZoneLimit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetHostedZoneLimit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetHostedZoneLimit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetHostedZoneLimit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetHostedZoneLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetHostedZoneLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
