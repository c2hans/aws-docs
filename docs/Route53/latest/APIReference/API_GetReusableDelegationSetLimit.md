---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetReusableDelegationSetLimit.html
---

# GetReusableDelegationSetLimit
<a name="API_GetReusableDelegationSetLimit"></a>

Gets the maximum number of hosted zones that you can associate with the specified reusable delegation set.

For the default limit, see [Limits](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html) in the *Amazon Route 53 Developer Guide*. To request a higher limit, [open a case](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-route53).

## Request Syntax
<a name="API_GetReusableDelegationSetLimit_RequestSyntax"></a>

```
GET /2013-04-01/reusabledelegationsetlimit/{{Id}}/{{Type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetReusableDelegationSetLimit_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetReusableDelegationSetLimit_RequestSyntax) **   <a name="Route53-GetReusableDelegationSetLimit-request-uri-DelegationSetId"></a>
The ID of the delegation set that you want to get the limit for.
Length Constraints: Maximum length of 32.
Required: Yes

 ** [Type](#API_GetReusableDelegationSetLimit_RequestSyntax) **   <a name="Route53-GetReusableDelegationSetLimit-request-uri-Type"></a>
Specify `MAX_ZONES_BY_REUSABLE_DELEGATION_SET` to get the maximum number of hosted zones that you can associate with the specified reusable delegation set.
Valid Values: `MAX_ZONES_BY_REUSABLE_DELEGATION_SET`
Required: Yes

## Request Body
<a name="API_GetReusableDelegationSetLimit_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetReusableDelegationSetLimit_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetReusableDelegationSetLimitResponse>
   <Count>long</Count>
   <Limit>
      <Type>string</Type>
      <Value>long</Value>
   </Limit>
</GetReusableDelegationSetLimitResponse>
```

## Response Elements
<a name="API_GetReusableDelegationSetLimit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetReusableDelegationSetLimitResponse](#API_GetReusableDelegationSetLimit_ResponseSyntax) **   <a name="Route53-GetReusableDelegationSetLimit-response-GetReusableDelegationSetLimitResponse"></a>
Root level tag for the GetReusableDelegationSetLimitResponse parameters.
Required: Yes

 ** [Count](#API_GetReusableDelegationSetLimit_ResponseSyntax) **   <a name="Route53-GetReusableDelegationSetLimit-response-Count"></a>
The current number of hosted zones that you can associate with the specified reusable delegation set.
Type: Long
Valid Range: Minimum value of 0.

 ** [Limit](#API_GetReusableDelegationSetLimit_ResponseSyntax) **   <a name="Route53-GetReusableDelegationSetLimit-response-Limit"></a>
The current setting for the limit on hosted zones that you can associate with the specified reusable delegation set.
Type: [ReusableDelegationSetLimit](API_ReusableDelegationSetLimit.md) object

## Errors
<a name="API_GetReusableDelegationSetLimit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchDelegationSet **
A reusable delegation set with the specified ID does not exist.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_GetReusableDelegationSetLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetReusableDelegationSetLimit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetReusableDelegationSetLimit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetReusableDelegationSetLimit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetReusableDelegationSetLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetReusableDelegationSetLimit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetReusableDelegationSetLimit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetReusableDelegationSetLimit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetReusableDelegationSetLimit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetReusableDelegationSetLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetReusableDelegationSetLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
