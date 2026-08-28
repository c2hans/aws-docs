---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZonesByName.html
---

# ListHostedZonesByName
<a name="API_ListHostedZonesByName"></a>

Retrieves a list of your hosted zones in lexicographic order. The response includes a `HostedZones` child element for each hosted zone created by the current AWS account.

 `ListHostedZonesByName` sorts hosted zones by name with the labels reversed. For example:

 `com.example.www.`

Note the trailing dot, which can change the sort order in some circumstances.

If the domain name includes escape characters or Punycode, `ListHostedZonesByName` alphabetizes the domain name using the escaped or Punycoded value, which is the format that Amazon Route 53 saves in its database. For example, to create a hosted zone for exämple.com, you specify ex\\344mple.com for the domain name. `ListHostedZonesByName` alphabetizes it as:

 `com.ex\344mple.`

The labels are reversed and alphabetized using the escaped value. For more information about valid domain name formats, including internationalized domain names, see [DNS Domain Name Format](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html) in the *Amazon Route 53 Developer Guide*.

Route 53 returns up to 100 items in each response. If you have a lot of hosted zones, use the `MaxItems` parameter to list them in groups of up to 100. The response includes values that help navigate from one group of `MaxItems` hosted zones to the next:
+ The `DNSName` and `HostedZoneId` elements in the response contain the values, if any, specified for the `dnsname` and `hostedzoneid` parameters in the request that produced the current response.
+ The `MaxItems` element in the response contains the value, if any, that you specified for the `maxitems` parameter in the request that produced the current response.
+ If the value of `IsTruncated` in the response is true, there are more hosted zones associated with the current AWS account.

  If `IsTruncated` is false, this response includes the last hosted zone that is associated with the current account. The `NextDNSName` element and `NextHostedZoneId` elements are omitted from the response.
+ The `NextDNSName` and `NextHostedZoneId` elements in the response contain the domain name and the hosted zone ID of the next hosted zone that is associated with the current AWS account. If you want to list more hosted zones, make another call to `ListHostedZonesByName`, and specify the value of `NextDNSName` and `NextHostedZoneId` in the `dnsname` and `hostedzoneid` parameters, respectively.

## Request Syntax
<a name="API_ListHostedZonesByName_RequestSyntax"></a>

```
GET /2013-04-01/hostedzonesbyname?dnsname={{DNSName}}&hostedzoneid={{HostedZoneId}}&maxitems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListHostedZonesByName_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dnsname](#API_ListHostedZonesByName_RequestSyntax) **   <a name="Route53-ListHostedZonesByName-request-uri-DNSName"></a>
(Optional) For your first request to `ListHostedZonesByName`, include the `dnsname` parameter only if you want to specify the name of the first hosted zone in the response. If you don't include the `dnsname` parameter, Amazon Route 53 returns all of the hosted zones that were created by the current AWS account, in ASCII order. For subsequent requests, include both `dnsname` and `hostedzoneid` parameters. For `dnsname`, specify the value of `NextDNSName` from the previous response.
Length Constraints: Maximum length of 1024.

 ** [hostedzoneid](#API_ListHostedZonesByName_RequestSyntax) **   <a name="Route53-ListHostedZonesByName-request-uri-HostedZoneId"></a>
(Optional) For your first request to `ListHostedZonesByName`, do not include the `hostedzoneid` parameter.
If you have more hosted zones than the value of `maxitems`, `ListHostedZonesByName` returns only the first `maxitems` hosted zones. To get the next group of `maxitems` hosted zones, submit another request to `ListHostedZonesByName` and include both `dnsname` and `hostedzoneid` parameters. For the value of `hostedzoneid`, specify the value of the `NextHostedZoneId` element from the previous response.
Length Constraints: Maximum length of 32.

 ** [maxitems](#API_ListHostedZonesByName_RequestSyntax) **   <a name="Route53-ListHostedZonesByName-request-uri-MaxItems"></a>
The maximum number of hosted zones to be included in the response body for this request. If you have more than `maxitems` hosted zones, then the value of the `IsTruncated` element in the response is true, and the values of `NextDNSName` and `NextHostedZoneId` specify the first hosted zone in the next group of `maxitems` hosted zones.

## Request Body
<a name="API_ListHostedZonesByName_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListHostedZonesByName_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListHostedZonesByNameResponse>
   <DNSName>string</DNSName>
   <HostedZoneId>string</HostedZoneId>
   <HostedZones>
      <HostedZone>
         <CallerReference>string</CallerReference>
         <Config>
            <Comment>string</Comment>
            <PrivateZone>boolean</PrivateZone>
         </Config>
         <Features>
            <AcceleratedRecoveryStatus>string</AcceleratedRecoveryStatus>
            <FailureReasons>
               <AcceleratedRecovery>string</AcceleratedRecovery>
            </FailureReasons>
         </Features>
         <Id>string</Id>
         <LinkedService>
            <Description>string</Description>
            <ServicePrincipal>string</ServicePrincipal>
         </LinkedService>
         <Name>string</Name>
         <ResourceRecordSetCount>long</ResourceRecordSetCount>
      </HostedZone>
   </HostedZones>
   <IsTruncated>boolean</IsTruncated>
   <MaxItems>string</MaxItems>
   <NextDNSName>string</NextDNSName>
   <NextHostedZoneId>string</NextHostedZoneId>
</ListHostedZonesByNameResponse>
```

## Response Elements
<a name="API_ListHostedZonesByName_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListHostedZonesByNameResponse](#API_ListHostedZonesByName_ResponseSyntax) **   <a name="Route53-ListHostedZonesByName-response-ListHostedZonesByNameResponse"></a>
Root level tag for the ListHostedZonesByNameResponse parameters.
Required: Yes

 ** [DNSName](#API_ListHostedZonesByName_ResponseSyntax) **   <a name="Route53-ListHostedZonesByName-response-DNSName"></a>
For the second and subsequent calls to `ListHostedZonesByName`, `DNSName` is the value that you specified for the `dnsname` parameter in the request that produced the current response.
Type: String
Length Constraints: Maximum length of 1024.

 ** [HostedZoneId](#API_ListHostedZonesByName_ResponseSyntax) **   <a name="Route53-ListHostedZonesByName-response-HostedZoneId"></a>
The ID that Amazon Route 53 assigned to the hosted zone when you created it.
Type: String
Length Constraints: Maximum length of 32.

 ** [HostedZones](#API_ListHostedZonesByName_ResponseSyntax) **   <a name="Route53-ListHostedZonesByName-response-HostedZones"></a>
A complex type that contains general information about the hosted zone.
Type: Array of [HostedZone](API_HostedZone.md) objects

 ** [IsTruncated](#API_ListHostedZonesByName_ResponseSyntax) **   <a name="Route53-ListHostedZonesByName-response-IsTruncated"></a>
A flag that indicates whether there are more hosted zones to be listed. If the response was truncated, you can get the next group of `maxitems` hosted zones by calling `ListHostedZonesByName` again and specifying the values of `NextDNSName` and `NextHostedZoneId` elements in the `dnsname` and `hostedzoneid` parameters.
Type: Boolean

 ** [MaxItems](#API_ListHostedZonesByName_ResponseSyntax) **   <a name="Route53-ListHostedZonesByName-response-MaxItems"></a>
The value that you specified for the `maxitems` parameter in the call to `ListHostedZonesByName` that produced the current response.
Type: String

 ** [NextDNSName](#API_ListHostedZonesByName_ResponseSyntax) **   <a name="Route53-ListHostedZonesByName-response-NextDNSName"></a>
If `IsTruncated` is true, the value of `NextDNSName` is the name of the first hosted zone in the next group of `maxitems` hosted zones. Call `ListHostedZonesByName` again and specify the value of `NextDNSName` and `NextHostedZoneId` in the `dnsname` and `hostedzoneid` parameters, respectively.
This element is present only if `IsTruncated` is `true`.
Type: String
Length Constraints: Maximum length of 1024.

 ** [NextHostedZoneId](#API_ListHostedZonesByName_ResponseSyntax) **   <a name="Route53-ListHostedZonesByName-response-NextHostedZoneId"></a>
If `IsTruncated` is `true`, the value of `NextHostedZoneId` identifies the first hosted zone in the next group of `maxitems` hosted zones. Call `ListHostedZonesByName` again and specify the value of `NextDNSName` and `NextHostedZoneId` in the `dnsname` and `hostedzoneid` parameters, respectively.
This element is present only if `IsTruncated` is `true`.
Type: String
Length Constraints: Maximum length of 32.

## Errors
<a name="API_ListHostedZonesByName_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidDomainName **
The specified domain name is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_ListHostedZonesByName_Examples"></a>

### Example Request
<a name="API_ListHostedZonesByName_Example_1"></a>

This example illustrates one usage of ListHostedZonesByName.

```
GET /2013-04-01/hostedzonesbyname?maxitems=1
```

### Example Response
<a name="API_ListHostedZonesByName_Example_2"></a>

This example illustrates one usage of ListHostedZonesByName.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<ListHostedZonesByNameResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HostedZones>
      <HostedZone>
         <Id>/hostedzone/Z111111QQQQQQQ</Id>
         <Name>example.com.</Name>
         <CallerReference>MyUniqueIdentifier1</CallerReference>
         <Config>
            <Comment>This is my first hosted zone.</Comment>
            <PrivateZone>false</PrivateZone>
         </Config>
         <ResourceRecordSetCount>42</ResourceRecordSetCount>
      </HostedZone>
   </HostedZones>
   <IsTruncated>true</IsTruncated>
   <NextDNSName>example2.com</NextDNSName>
   <NextHostedZoneId>Z222222VVVVVVV</NextHostedZoneId>
   <MaxItems>1</MaxItems>
</ListHostedZonesByNameResponse>
```

## See Also
<a name="API_ListHostedZonesByName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListHostedZonesByName)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListHostedZonesByName)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListHostedZonesByName)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListHostedZonesByName)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListHostedZonesByName)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListHostedZonesByName)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListHostedZonesByName)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListHostedZonesByName)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListHostedZonesByName)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListHostedZonesByName)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
