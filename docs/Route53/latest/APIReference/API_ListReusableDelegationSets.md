---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListReusableDelegationSets.html
---

# ListReusableDelegationSets
<a name="API_ListReusableDelegationSets"></a>

Retrieves a list of the reusable delegation sets that are associated with the current AWS account.

## Request Syntax
<a name="API_ListReusableDelegationSets_RequestSyntax"></a>

```
GET /2013-04-01/delegationset?marker={{Marker}}&maxitems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListReusableDelegationSets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [marker](#API_ListReusableDelegationSets_RequestSyntax) **   <a name="Route53-ListReusableDelegationSets-request-uri-Marker"></a>
If the value of `IsTruncated` in the previous response was `true`, you have more reusable delegation sets. To get another group, submit another `ListReusableDelegationSets` request.
For the value of `marker`, specify the value of `NextMarker` from the previous response, which is the ID of the first reusable delegation set that Amazon Route 53 will return if you submit another request.
If the value of `IsTruncated` in the previous response was `false`, there are no more reusable delegation sets to get.
Length Constraints: Maximum length of 64.

 ** [maxitems](#API_ListReusableDelegationSets_RequestSyntax) **   <a name="Route53-ListReusableDelegationSets-request-uri-MaxItems"></a>
The number of reusable delegation sets that you want Amazon Route 53 to return in the response to this request. If you specify a value greater than 100, Route 53 returns only the first 100 reusable delegation sets.

## Request Body
<a name="API_ListReusableDelegationSets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListReusableDelegationSets_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListReusableDelegationSetsResponse>
   <DelegationSets>
      <DelegationSet>
         <CallerReference>string</CallerReference>
         <Id>string</Id>
         <NameServers>
            <NameServer>string</NameServer>
         </NameServers>
      </DelegationSet>
   </DelegationSets>
   <IsTruncated>boolean</IsTruncated>
   <Marker>string</Marker>
   <MaxItems>string</MaxItems>
   <NextMarker>string</NextMarker>
</ListReusableDelegationSetsResponse>
```

## Response Elements
<a name="API_ListReusableDelegationSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListReusableDelegationSetsResponse](#API_ListReusableDelegationSets_ResponseSyntax) **   <a name="Route53-ListReusableDelegationSets-response-ListReusableDelegationSetsResponse"></a>
Root level tag for the ListReusableDelegationSetsResponse parameters.
Required: Yes

 ** [DelegationSets](#API_ListReusableDelegationSets_ResponseSyntax) **   <a name="Route53-ListReusableDelegationSets-response-DelegationSets"></a>
A complex type that contains one `DelegationSet` element for each reusable delegation set that was created by the current AWS account.
Type: Array of [DelegationSet](API_DelegationSet.md) objects

 ** [IsTruncated](#API_ListReusableDelegationSets_ResponseSyntax) **   <a name="Route53-ListReusableDelegationSets-response-IsTruncated"></a>
A flag that indicates whether there are more reusable delegation sets to be listed.
Type: Boolean

 ** [Marker](#API_ListReusableDelegationSets_ResponseSyntax) **   <a name="Route53-ListReusableDelegationSets-response-Marker"></a>
For the second and subsequent calls to `ListReusableDelegationSets`, `Marker` is the value that you specified for the `marker` parameter in the request that produced the current response.
Type: String
Length Constraints: Maximum length of 64.

 ** [MaxItems](#API_ListReusableDelegationSets_ResponseSyntax) **   <a name="Route53-ListReusableDelegationSets-response-MaxItems"></a>
The value that you specified for the `maxitems` parameter in the call to `ListReusableDelegationSets` that produced the current response.
Type: String

 ** [NextMarker](#API_ListReusableDelegationSets_ResponseSyntax) **   <a name="Route53-ListReusableDelegationSets-response-NextMarker"></a>
If `IsTruncated` is `true`, the value of `NextMarker` identifies the next reusable delegation set that Amazon Route 53 will return if you submit another `ListReusableDelegationSets` request and specify the value of `NextMarker` in the `marker` parameter.
Type: String
Length Constraints: Maximum length of 64.

## Errors
<a name="API_ListReusableDelegationSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_ListReusableDelegationSets_Examples"></a>

### Example Request
<a name="API_ListReusableDelegationSets_Example_1"></a>

This example illustrates one usage of ListReusableDelegationSets.

```
GET /2013-04-01/delegationset?maxitems=2
```

### Example Response
<a name="API_ListReusableDelegationSets_Example_2"></a>

This example illustrates one usage of ListReusableDelegationSets.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<ListReusableDelegationSetsResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <DelegationSets>
      <DelegationSet>
         <Id>/delegationset/N1PA6795SAMPLE</Id>
         <CallerReference>2017-03-15T01:36:41.958Z</CallerReference>
         <NameServers>
            <NameServer>ns-2042.awsdns-64.com</NameServer>
            <NameServer>ns-2043.awsdns-65.net</NameServer>
            <NameServer>ns-2044.awsdns-66.org</NameServer>
            <NameServer>ns-2045.awsdns-67.co.uk</NameServer>
         </NameServers>
      </DelegationSet>
      <DelegationSet>
         <Id>/delegationset/N1PA7000SAMPLE</Id>
         <CallerReference>2017-03-16T01:37:42.959Z</CallerReference>
         <NameServers>
            <NameServer>ns-2046.awsdns-68.com</NameServer>
            <NameServer>ns-2047.awsdns-69.net</NameServer>
            <NameServer>ns-2048.awsdns-70.org</NameServer>
            <NameServer>ns-2049.awsdns-71.co.uk</NameServer>
         </NameServers>
      </DelegationSet>
   </DelegationSets>
   <IsTruncated>true</IsTruncated>
   <NextMarker>N1PA6797SAMPLE</NextMarker>
   <MaxItems>2</MaxItems>
</ListReusableDelegationSetsResponse>
```

## See Also
<a name="API_ListReusableDelegationSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListReusableDelegationSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListReusableDelegationSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListReusableDelegationSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListReusableDelegationSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListReusableDelegationSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListReusableDelegationSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListReusableDelegationSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListReusableDelegationSets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListReusableDelegationSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListReusableDelegationSets)
