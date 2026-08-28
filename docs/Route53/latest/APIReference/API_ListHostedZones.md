---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZones.html
---

# ListHostedZones
<a name="API_ListHostedZones"></a>

Retrieves a list of the public and private hosted zones that are associated with the current AWS account. The response includes a `HostedZones` child element for each hosted zone.

Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of hosted zones, you can use the `maxitems` parameter to list them in groups of up to 100.

## Request Syntax
<a name="API_ListHostedZones_RequestSyntax"></a>

```
GET /2013-04-01/hostedzone?delegationsetid={{DelegationSetId}}&hostedzonetype={{HostedZoneType}}&marker={{Marker}}&maxitems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListHostedZones_RequestParameters"></a>

The request uses the following URI parameters.

 ** [delegationsetid](#API_ListHostedZones_RequestSyntax) **   <a name="Route53-ListHostedZones-request-uri-DelegationSetId"></a>
If you're using reusable delegation sets and you want to list all of the hosted zones that are associated with a reusable delegation set, specify the ID of that reusable delegation set.
Length Constraints: Maximum length of 32.

 ** [hostedzonetype](#API_ListHostedZones_RequestSyntax) **   <a name="Route53-ListHostedZones-request-uri-HostedZoneType"></a>
 (Optional) Specifies if the hosted zone is private.
Valid Values: `PrivateHostedZone`

 ** [marker](#API_ListHostedZones_RequestSyntax) **   <a name="Route53-ListHostedZones-request-uri-Marker"></a>
If the value of `IsTruncated` in the previous response was `true`, you have more hosted zones. To get more hosted zones, submit another `ListHostedZones` request.
For the value of `marker`, specify the value of `NextMarker` from the previous response, which is the ID of the first hosted zone that Amazon Route 53 will return if you submit another request.
If the value of `IsTruncated` in the previous response was `false`, there are no more hosted zones to get.
Length Constraints: Maximum length of 64.

 ** [maxitems](#API_ListHostedZones_RequestSyntax) **   <a name="Route53-ListHostedZones-request-uri-MaxItems"></a>
(Optional) The maximum number of hosted zones that you want Amazon Route 53 to return. If you have more than `maxitems` hosted zones, the value of `IsTruncated` in the response is `true`, and the value of `NextMarker` is the hosted zone ID of the first hosted zone that Route 53 will return if you submit another request.

## Request Body
<a name="API_ListHostedZones_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListHostedZones_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListHostedZonesResponse>
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
   <Marker>string</Marker>
   <MaxItems>string</MaxItems>
   <NextMarker>string</NextMarker>
</ListHostedZonesResponse>
```

## Response Elements
<a name="API_ListHostedZones_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListHostedZonesResponse](#API_ListHostedZones_ResponseSyntax) **   <a name="Route53-ListHostedZones-response-ListHostedZonesResponse"></a>
Root level tag for the ListHostedZonesResponse parameters.
Required: Yes

 ** [HostedZones](#API_ListHostedZones_ResponseSyntax) **   <a name="Route53-ListHostedZones-response-HostedZones"></a>
A complex type that contains general information about the hosted zone.
Type: Array of [HostedZone](API_HostedZone.md) objects

 ** [IsTruncated](#API_ListHostedZones_ResponseSyntax) **   <a name="Route53-ListHostedZones-response-IsTruncated"></a>
A flag indicating whether there are more hosted zones to be listed. If the response was truncated, you can get more hosted zones by submitting another `ListHostedZones` request and specifying the value of `NextMarker` in the `marker` parameter.
Type: Boolean

 ** [Marker](#API_ListHostedZones_ResponseSyntax) **   <a name="Route53-ListHostedZones-response-Marker"></a>
For the second and subsequent calls to `ListHostedZones`, `Marker` is the value that you specified for the `marker` parameter in the request that produced the current response.
Type: String
Length Constraints: Maximum length of 64.

 ** [MaxItems](#API_ListHostedZones_ResponseSyntax) **   <a name="Route53-ListHostedZones-response-MaxItems"></a>
The value that you specified for the `maxitems` parameter in the call to `ListHostedZones` that produced the current response.
Type: String

 ** [NextMarker](#API_ListHostedZones_ResponseSyntax) **   <a name="Route53-ListHostedZones-response-NextMarker"></a>
If `IsTruncated` is `true`, the value of `NextMarker` identifies the first hosted zone in the next group of hosted zones. Submit another `ListHostedZones` request, and specify the value of `NextMarker` from the response in the `marker` parameter.
This element is present only if `IsTruncated` is `true`.
Type: String
Length Constraints: Maximum length of 64.

## Errors
<a name="API_ListHostedZones_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DelegationSetNotReusable **
A reusable delegation set with the specified ID does not exist.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchDelegationSet **
A reusable delegation set with the specified ID does not exist.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_ListHostedZones_Examples"></a>

### Example Request
<a name="API_ListHostedZones_Example_1"></a>

This example illustrates one usage of ListHostedZones.

```
GET /2013-04-01/hostedzone?maxitems=1
```

### Example Response
<a name="API_ListHostedZones_Example_2"></a>

This example illustrates one usage of ListHostedZones.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<ListHostedZonesResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
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
   <NextMarker>Z222222VVVVVVV</NextMarker>
   <MaxItems>1</MaxItems>
</ListHostedZonesResponse>
```

## See Also
<a name="API_ListHostedZones_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListHostedZones)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListHostedZones)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListHostedZones)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListHostedZones)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListHostedZones)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListHostedZones)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListHostedZones)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListHostedZones)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListHostedZones)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListHostedZones)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
