---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateReusableDelegationSet.html
---

# CreateReusableDelegationSet
<a name="API_CreateReusableDelegationSet"></a>

Creates a delegation set (a group of four name servers) that can be reused by multiple hosted zones that were created by the same AWS account.

You can also create a reusable delegation set that uses the four name servers that are associated with an existing hosted zone. Specify the hosted zone ID in the `CreateReusableDelegationSet` request.

**Note**
You can't associate a reusable delegation set with a private hosted zone.

For information about using a reusable delegation set to configure white label name servers, see [Configuring White Label Name Servers](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/white-label-name-servers.html).

The process for migrating existing hosted zones to use a reusable delegation set is comparable to the process for configuring white label name servers. You need to perform the following steps:

1. Create a reusable delegation set.

1. Recreate hosted zones, and reduce the TTL to 60 seconds or less.

1. Recreate resource record sets in the new hosted zones.

1. Change the registrar's name servers to use the name servers for the new hosted zones.

1. Monitor traffic for the website or application.

1. Change TTLs back to their original values.

If you want to migrate existing hosted zones to use a reusable delegation set, the existing hosted zones can't use any of the name servers that are assigned to the reusable delegation set. If one or more hosted zones do use one or more name servers that are assigned to the reusable delegation set, you can do one of the following:
+ For small numbers of hosted zones—up to a few hundred—it's relatively easy to create reusable delegation sets until you get one that has four name servers that don't overlap with any of the name servers in your hosted zones.
+ For larger numbers of hosted zones, the easiest solution is to use more than one reusable delegation set.
+ For larger numbers of hosted zones, you can also migrate hosted zones that have overlapping name servers to hosted zones that don't have overlapping name servers, then migrate the hosted zones again to use the reusable delegation set.

## Request Syntax
<a name="API_CreateReusableDelegationSet_RequestSyntax"></a>

```
POST /2013-04-01/delegationset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateReusableDelegationSetRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <CallerReference>{{string}}</CallerReference>
   <HostedZoneId>{{string}}</HostedZoneId>
</CreateReusableDelegationSetRequest>
```

## URI Request Parameters
<a name="API_CreateReusableDelegationSet_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateReusableDelegationSet_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateReusableDelegationSetRequest](#API_CreateReusableDelegationSet_RequestSyntax) **   <a name="Route53-CreateReusableDelegationSet-request-CreateReusableDelegationSetRequest"></a>
Root level tag for the CreateReusableDelegationSetRequest parameters.
Required: Yes

 ** [CallerReference](#API_CreateReusableDelegationSet_RequestSyntax) **   <a name="Route53-CreateReusableDelegationSet-request-CallerReference"></a>
A unique string that identifies the request, and that allows you to retry failed `CreateReusableDelegationSet` requests without the risk of executing the operation twice. You must use a unique `CallerReference` string every time you submit a `CreateReusableDelegationSet` request. `CallerReference` can be any unique string, for example a date/time stamp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [HostedZoneId](#API_CreateReusableDelegationSet_RequestSyntax) **   <a name="Route53-CreateReusableDelegationSet-request-HostedZoneId"></a>
If you want to mark the delegation set for an existing hosted zone as reusable, the ID for that hosted zone.
Type: String
Length Constraints: Maximum length of 32.
Required: No

## Response Syntax
<a name="API_CreateReusableDelegationSet_ResponseSyntax"></a>

```
HTTP/1.1 201
Location: {{Location}}
<?xml version="1.0" encoding="UTF-8"?>
<CreateReusableDelegationSetResponse>
   <DelegationSet>
      <CallerReference>string</CallerReference>
      <Id>string</Id>
      <NameServers>
         <NameServer>string</NameServer>
      </NameServers>
   </DelegationSet>
</CreateReusableDelegationSetResponse>
```

## Response Elements
<a name="API_CreateReusableDelegationSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The response returns the following HTTP headers.

 ** [Location](#API_CreateReusableDelegationSet_ResponseSyntax) **   <a name="Route53-CreateReusableDelegationSet-response-Location"></a>
The unique URL representing the new reusable delegation set.
Length Constraints: Maximum length of 1024.

The following data is returned in XML format by the service.

 ** [CreateReusableDelegationSetResponse](#API_CreateReusableDelegationSet_ResponseSyntax) **   <a name="Route53-CreateReusableDelegationSet-response-CreateReusableDelegationSetResponse"></a>
Root level tag for the CreateReusableDelegationSetResponse parameters.
Required: Yes

 ** [DelegationSet](#API_CreateReusableDelegationSet_ResponseSyntax) **   <a name="Route53-CreateReusableDelegationSet-response-DelegationSet"></a>
A complex type that contains name server information.
Type: [DelegationSet](API_DelegationSet.md) object

## Errors
<a name="API_CreateReusableDelegationSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DelegationSetAlreadyCreated **
A delegation set with the same owner and caller reference combination has already been created.
 ** message **

HTTP Status Code: 400

 ** DelegationSetAlreadyReusable **
The specified delegation set has already been marked as reusable.
 ** message **

HTTP Status Code: 400

 ** DelegationSetNotAvailable **
You can create a hosted zone that has the same name as an existing hosted zone (example.com is common), but there is a limit to the number of hosted zones that have the same name. If you get this error, Amazon Route 53 has reached that limit. If you own the domain name and Route 53 generates this error, contact Customer Support.
 ** message **

HTTP Status Code: 400

 ** HostedZoneNotFound **
The specified HostedZone can't be found.
 ** message **

HTTP Status Code: 400

 ** InvalidArgument **
Parameter name is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** LimitsExceeded **
This operation can't be completed because the current account has reached the limit on the resource you are trying to create. To request a higher limit, [create a case](http://aws.amazon.com/route53-request) with the AWS Support Center.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_CreateReusableDelegationSet_Examples"></a>

### Example Request
<a name="API_CreateReusableDelegationSet_Example_1"></a>

This example illustrates one usage of CreateReusableDelegationSet.

```
POST /2013-04-01/delegationset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateReusableDelegationSetRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <CallerReference>2017-03-15T01:36:41.958Z</CallerReference>
   <HostedZoneId>Z1D633PEXAMPLE</HostedZoneId>
</CreateReusableDelegationSetRequest>
```

### Example Response
<a name="API_CreateReusableDelegationSet_Example_2"></a>

This example illustrates one usage of CreateReusableDelegationSet.

```
HTTP/1.1 201 Created
<?xml version="1.0" encoding="UTF-8"?>
<CreateReusableDelegationSetResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <DelegationSet>
      <Id>/delegationset/N1PA6795SAMPLE</Id>
      <CallerReference>2017-03-15T01:36:41.958Z</CallerReference>
      <NameServers>
         <NameServer>ns-2048.awsdns-64.com</NameServer>
         <NameServer>ns-2049.awsdns-65.net</NameServer>
         <NameServer>ns-2050.awsdns-66.org</NameServer>
         <NameServer>ns-2051.awsdns-67.co.uk</NameServer>
      </NameServers>
   </DelegationSet>
</CreateReusableDelegationSetResponse>
```

## See Also
<a name="API_CreateReusableDelegationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/CreateReusableDelegationSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/CreateReusableDelegationSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CreateReusableDelegationSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/CreateReusableDelegationSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CreateReusableDelegationSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/CreateReusableDelegationSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/CreateReusableDelegationSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/CreateReusableDelegationSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/CreateReusableDelegationSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CreateReusableDelegationSet)
