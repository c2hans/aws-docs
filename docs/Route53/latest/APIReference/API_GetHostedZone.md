---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZone.html
---

# GetHostedZone
<a name="API_GetHostedZone"></a>

Gets information about a specified hosted zone including the four name servers assigned to the hosted zone.

 `` returns the VPCs associated with the specified hosted zone and does not reflect the VPC associations by Route 53 Profiles. To get the associations to a Profile, call the [ListProfileAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfileAssociations.html) API.

## Request Syntax
<a name="API_GetHostedZone_RequestSyntax"></a>

```
GET /2013-04-01/hostedzone/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetHostedZone_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetHostedZone_RequestSyntax) **   <a name="Route53-GetHostedZone-request-uri-Id"></a>
The ID of the hosted zone that you want to get information about.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_GetHostedZone_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetHostedZone_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetHostedZoneResponse>
   <DelegationSet>
      <CallerReference>string</CallerReference>
      <Id>string</Id>
      <NameServers>
         <NameServer>string</NameServer>
      </NameServers>
   </DelegationSet>
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
   <VPCs>
      <VPC>
         <VPCId>string</VPCId>
         <VPCRegion>string</VPCRegion>
      </VPC>
   </VPCs>
</GetHostedZoneResponse>
```

## Response Elements
<a name="API_GetHostedZone_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetHostedZoneResponse](#API_GetHostedZone_ResponseSyntax) **   <a name="Route53-GetHostedZone-response-GetHostedZoneResponse"></a>
Root level tag for the GetHostedZoneResponse parameters.
Required: Yes

 ** [DelegationSet](#API_GetHostedZone_ResponseSyntax) **   <a name="Route53-GetHostedZone-response-DelegationSet"></a>
A complex type that lists the Amazon Route 53 name servers for the specified hosted zone.
Type: [DelegationSet](API_DelegationSet.md) object

 ** [HostedZone](#API_GetHostedZone_ResponseSyntax) **   <a name="Route53-GetHostedZone-response-HostedZone"></a>
A complex type that contains general information about the specified hosted zone.
Type: [HostedZone](API_HostedZone.md) object

 ** [VPCs](#API_GetHostedZone_ResponseSyntax) **   <a name="Route53-GetHostedZone-response-VPCs"></a>
A complex type that contains information about the VPCs that are associated with the specified hosted zone.
Type: Array of [VPC](API_VPC.md) objects
Array Members: Minimum number of 1 item.

## Errors
<a name="API_GetHostedZone_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

## Examples
<a name="API_GetHostedZone_Examples"></a>

### Example Request
<a name="API_GetHostedZone_Example_1"></a>

This example illustrates one usage of GetHostedZone.

```
GET /2013-04-01/hostedzone/Z1PA6795UKMFR9
```

### Example Response (Public Hosted Zone, Default Delegation Set Assigned by Route 53)
<a name="API_GetHostedZone_Example_2"></a>

This example illustrates one usage of GetHostedZone.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<GetHostedZoneResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HostedZone>
      <Id>/hostedzone/Z1PA6795UKMFR9</Id>
      <Name>example.com.</Name>
      <CallerReference>2017-03-01T11:22:14Z</CallerReference>
      <Config>
         <Comment>This is my first hosted zone.</Comment>
         <PrivateZone>false</PrivateZone>
      </Config>
      <ResourceRecordSetCount>17</ResourceRecordSetCount>
   </HostedZone>
   <DelegationSet>
      <NameServers>
         <NameServer>ns-2048.awsdns-64.com</NameServer>
         <NameServer>ns-2049.awsdns-65.net</NameServer>
         <NameServer>ns-2050.awsdns-66.org</NameServer>
         <NameServer>ns-2051.awsdns-67.co.uk</NameServer>
      </NameServers>
   </DelegationSet>
</GetHostedZoneResponse>
```

### Example Response (Public Hosted Zone, Reusable Delegation Set)
<a name="API_GetHostedZone_Example_3"></a>

This example illustrates one usage of GetHostedZone.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<GetHostedZoneResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HostedZone>
      <Id>/hostedzone/Z1PA6795UKMFR9</Id>
      <Name>example.com.</Name>
      <CallerReference>2017-03-02T10:44:04Z</CallerReference>
      <Config>
         <Comment>This is my first hosted zone.</Comment>
         <PrivateZone>false</PrivateZone>
      </Config>
      <ResourceRecordSetCount>17</ResourceRecordSetCount>
   </HostedZone>
   <DelegationSet>
      <Id>NU241VPSAMPLE</Id>
      <CallerReference>2017-03-01T11:22:14Z</CallerReference>
      <NameServers>
         <NameServer>ns-2048.awsdns-64.com</NameServer>
         <NameServer>ns-2049.awsdns-65.net</NameServer>
         <NameServer>ns-2050.awsdns-66.org</NameServer>
         <NameServer>ns-2051.awsdns-67.co.uk</NameServer>
      </NameServers>
   </DelegationSet>
</GetHostedZoneResponse>
```

### Example Response (Private Hosted Zone)
<a name="API_GetHostedZone_Example_4"></a>

This example illustrates one usage of GetHostedZone.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<GetHostedZoneResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HostedZone>
      <Id>/hostedzone/Z1PA6795UKMFR9</Id>
      <Name>example.com.</Name>
      <CallerReference>myUniqueIdentifier</CallerReference>
      <Config>
         <Comment>This is my first hosted zone.</Comment>
         <PrivateZone>true</PrivateZone>
      </Config>
      <ResourceRecordSetCount>17</ResourceRecordSetCount>
   </HostedZone>
   <VPCs>
      <VPC>
         <VPCRegion>us-east-2</VPCRegion>
         <VPCId>vpc-1a2b3c4d</VPCId>
      </VPC>
   </VPCs>
</GetHostedZoneResponse>
```

## See Also
<a name="API_GetHostedZone_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetHostedZone)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetHostedZone)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetHostedZone)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetHostedZone)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetHostedZone)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetHostedZone)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetHostedZone)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetHostedZone)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetHostedZone)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetHostedZone)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
