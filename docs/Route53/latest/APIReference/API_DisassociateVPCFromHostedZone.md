---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_DisassociateVPCFromHostedZone.html
---

# DisassociateVPCFromHostedZone
<a name="API_DisassociateVPCFromHostedZone"></a>

Disassociates an Amazon Virtual Private Cloud (Amazon VPC) from an Amazon Route 53 private hosted zone. Note the following:
+ You can't disassociate the last Amazon VPC from a private hosted zone.
+ You can't convert a private hosted zone into a public hosted zone.
+ You can submit a `DisassociateVPCFromHostedZone` request using either the account that created the hosted zone or the account that created the Amazon VPC.
+ Some services, such as AWS Cloud Map and Amazon Elastic File System (Amazon EFS) automatically create hosted zones and associate VPCs with the hosted zones. A service can create a hosted zone using your account or using its own account. You can disassociate a VPC from a hosted zone only if the service created the hosted zone using your account.

  When you run [DisassociateVPCFromHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZonesByVPC.html), if the hosted zone has a value for `OwningAccount`, you can use `DisassociateVPCFromHostedZone`. If the hosted zone has a value for `OwningService`, you can't use `DisassociateVPCFromHostedZone`.

**Note**
When revoking access, the hosted zone and the Amazon VPC must belong to the same partition. A partition is a group of AWS Regions. Each AWS account is scoped to one partition.
The following are the supported partitions:
 `aws` - AWS Regions
 `aws-cn` - China Regions
 `aws-us-gov` - AWS GovCloud (US) Region
For more information, see [Access Management](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.

## Request Syntax
<a name="API_DisassociateVPCFromHostedZone_RequestSyntax"></a>

```
POST /2013-04-01/hostedzone/{{Id}}/disassociatevpc HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<DisassociateVPCFromHostedZoneRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Comment>{{string}}</Comment>
   <VPC>
      <VPCId>{{string}}</VPCId>
      <VPCRegion>{{string}}</VPCRegion>
   </VPC>
</DisassociateVPCFromHostedZoneRequest>
```

## URI Request Parameters
<a name="API_DisassociateVPCFromHostedZone_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DisassociateVPCFromHostedZone_RequestSyntax) **   <a name="Route53-DisassociateVPCFromHostedZone-request-uri-HostedZoneId"></a>
The ID of the private hosted zone that you want to disassociate a VPC from.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_DisassociateVPCFromHostedZone_RequestBody"></a>

The request accepts the following data in XML format.

 ** [DisassociateVPCFromHostedZoneRequest](#API_DisassociateVPCFromHostedZone_RequestSyntax) **   <a name="Route53-DisassociateVPCFromHostedZone-request-DisassociateVPCFromHostedZoneRequest"></a>
Root level tag for the DisassociateVPCFromHostedZoneRequest parameters.
Required: Yes

 ** [Comment](#API_DisassociateVPCFromHostedZone_RequestSyntax) **   <a name="Route53-DisassociateVPCFromHostedZone-request-Comment"></a>
 *Optional:* A comment about the disassociation request.
Type: String
Required: No

 ** [VPC](#API_DisassociateVPCFromHostedZone_RequestSyntax) **   <a name="Route53-DisassociateVPCFromHostedZone-request-VPC"></a>
A complex type that contains information about the VPC that you're disassociating from the specified hosted zone.
Type: [VPC](API_VPC.md) object
Required: Yes

## Response Syntax
<a name="API_DisassociateVPCFromHostedZone_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<DisassociateVPCFromHostedZoneResponse>
   <ChangeInfo>
      <Comment>string</Comment>
      <Id>string</Id>
      <Status>string</Status>
      <SubmittedAt>timestamp</SubmittedAt>
   </ChangeInfo>
</DisassociateVPCFromHostedZoneResponse>
```

## Response Elements
<a name="API_DisassociateVPCFromHostedZone_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [DisassociateVPCFromHostedZoneResponse](#API_DisassociateVPCFromHostedZone_ResponseSyntax) **   <a name="Route53-DisassociateVPCFromHostedZone-response-DisassociateVPCFromHostedZoneResponse"></a>
Root level tag for the DisassociateVPCFromHostedZoneResponse parameters.
Required: Yes

 ** [ChangeInfo](#API_DisassociateVPCFromHostedZone_ResponseSyntax) **   <a name="Route53-DisassociateVPCFromHostedZone-response-ChangeInfo"></a>
A complex type that describes the changes made to the specified private hosted zone.
Type: [ChangeInfo](API_ChangeInfo.md) object

## Errors
<a name="API_DisassociateVPCFromHostedZone_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidVPCId **
The VPC ID that you specified either isn't a valid ID or the current account is not authorized to access this VPC.
 ** message **

HTTP Status Code: 400

 ** LastVPCAssociation **
The VPC that you're trying to disassociate from the private hosted zone is the last VPC that is associated with the hosted zone. Amazon Route 53 doesn't support disassociating the last VPC from a hosted zone.
 ** message **

HTTP Status Code: 400

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

 ** VPCAssociationNotFound **
The specified VPC and hosted zone are not currently associated.
 ** message **
The specified VPC or hosted zone weren't found.
HTTP Status Code: 404

## Examples
<a name="API_DisassociateVPCFromHostedZone_Examples"></a>

### Example Request
<a name="API_DisassociateVPCFromHostedZone_Example_1"></a>

This example illustrates one usage of DisassociateVPCFromHostedZone.

```
POST /2013-04-01/hostedzone/Z1PA6795UKMFR9/disassociatevpc HTTP/1.1
<?xml version="1.0"?>
   <VPC>
      <VPCId>vpc-a1b2c3d4e5</VPCId>
      <VPCRegion>us-east-2</VPCRegion>
   </VPC>
</DisassociateVPCFromHostedZoneRequest>
```

### Example Response
<a name="API_DisassociateVPCFromHostedZone_Example_2"></a>

This example illustrates one usage of DisassociateVPCFromHostedZone.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<DisassociateVPCFromHostedZoneResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <ChangeInfo>
      <Id>/change/a1b2c3d4</Id>
      <Status>INSYNC</Status>
      <SubmittedAt>2017-03-31T01:36:41.958Z</SubmittedAt>
   </ChangeInfo>
</DisassociateVPCFromHostedZoneResponse>
```

## See Also
<a name="API_DisassociateVPCFromHostedZone_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/DisassociateVPCFromHostedZone)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/DisassociateVPCFromHostedZone)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/DisassociateVPCFromHostedZone)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/DisassociateVPCFromHostedZone)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/DisassociateVPCFromHostedZone)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/DisassociateVPCFromHostedZone)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/DisassociateVPCFromHostedZone)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/DisassociateVPCFromHostedZone)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/DisassociateVPCFromHostedZone)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/DisassociateVPCFromHostedZone)
