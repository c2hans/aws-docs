---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_AssociateVPCWithHostedZone.html
---

# AssociateVPCWithHostedZone
<a name="API_AssociateVPCWithHostedZone"></a>

Associates an Amazon VPC with a private hosted zone.

**Important**
To perform the association, the VPC and the private hosted zone must already exist. You can't convert a public hosted zone into a private hosted zone.

**Note**
If you want to associate a VPC that was created by using one AWS account with a private hosted zone that was created by using a different account, the AWS account that created the private hosted zone must first submit a `CreateVPCAssociationAuthorization` request. Then the account that created the VPC must submit an `AssociateVPCWithHostedZone` request.

**Note**
When granting access, the hosted zone and the Amazon VPC must belong to the same partition. A partition is a group of AWS Regions. Each AWS account is scoped to one partition.
The following are the supported partitions:
 `aws` - AWS Regions
 `aws-cn` - China Regions
 `aws-us-gov` - AWS GovCloud (US) Region
For more information, see [Access Management](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.

## Request Syntax
<a name="API_AssociateVPCWithHostedZone_RequestSyntax"></a>

```
POST /2013-04-01/hostedzone/{{Id}}/associatevpc HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<AssociateVPCWithHostedZoneRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Comment>{{string}}</Comment>
   <VPC>
      <VPCId>{{string}}</VPCId>
      <VPCRegion>{{string}}</VPCRegion>
   </VPC>
</AssociateVPCWithHostedZoneRequest>
```

## URI Request Parameters
<a name="API_AssociateVPCWithHostedZone_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_AssociateVPCWithHostedZone_RequestSyntax) **   <a name="Route53-AssociateVPCWithHostedZone-request-uri-HostedZoneId"></a>
The ID of the private hosted zone that you want to associate an Amazon VPC with.
Note that you can't associate a VPC with a hosted zone that doesn't have an existing VPC association.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_AssociateVPCWithHostedZone_RequestBody"></a>

The request accepts the following data in XML format.

 ** [AssociateVPCWithHostedZoneRequest](#API_AssociateVPCWithHostedZone_RequestSyntax) **   <a name="Route53-AssociateVPCWithHostedZone-request-AssociateVPCWithHostedZoneRequest"></a>
Root level tag for the AssociateVPCWithHostedZoneRequest parameters.
Required: Yes

 ** [Comment](#API_AssociateVPCWithHostedZone_RequestSyntax) **   <a name="Route53-AssociateVPCWithHostedZone-request-Comment"></a>
 *Optional:* A comment about the association request.
Type: String
Required: No

 ** [VPC](#API_AssociateVPCWithHostedZone_RequestSyntax) **   <a name="Route53-AssociateVPCWithHostedZone-request-VPC"></a>
A complex type that contains information about the VPC that you want to associate with a private hosted zone.
Type: [VPC](API_VPC.md) object
Required: Yes

## Response Syntax
<a name="API_AssociateVPCWithHostedZone_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<AssociateVPCWithHostedZoneResponse>
   <ChangeInfo>
      <Comment>string</Comment>
      <Id>string</Id>
      <Status>string</Status>
      <SubmittedAt>timestamp</SubmittedAt>
   </ChangeInfo>
</AssociateVPCWithHostedZoneResponse>
```

## Response Elements
<a name="API_AssociateVPCWithHostedZone_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [AssociateVPCWithHostedZoneResponse](#API_AssociateVPCWithHostedZone_ResponseSyntax) **   <a name="Route53-AssociateVPCWithHostedZone-response-AssociateVPCWithHostedZoneResponse"></a>
Root level tag for the AssociateVPCWithHostedZoneResponse parameters.
Required: Yes

 ** [ChangeInfo](#API_AssociateVPCWithHostedZone_ResponseSyntax) **   <a name="Route53-AssociateVPCWithHostedZone-response-ChangeInfo"></a>
A complex type that describes the changes made to your hosted zone.
Type: [ChangeInfo](API_ChangeInfo.md) object

## Errors
<a name="API_AssociateVPCWithHostedZone_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictingDomainExists **
The cause of this error depends on the operation that you're performing:
+  **Create a public hosted zone:** Two hosted zones that have the same name or that have a parent/child relationship (example.com and test.example.com) can't have any common name servers. You tried to create a hosted zone that has the same name as an existing hosted zone or that's the parent or child of an existing hosted zone, and you specified a delegation set that shares one or more name servers with the existing hosted zone. For more information, see [CreateReusableDelegationSet](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateReusableDelegationSet.html).
+  **Create a private hosted zone:** A hosted zone with the specified name already exists and is already associated with the Amazon VPC that you specified.
+  **Associate VPCs with a private hosted zone:** The VPC that you specified is already associated with another hosted zone that has the same name.
HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidVPCId **
The VPC ID that you specified either isn't a valid ID or the current account is not authorized to access this VPC.
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

 ** NotAuthorizedException **
Associating the specified VPC with the specified hosted zone has not been authorized.
 ** message **

HTTP Status Code: 401

 ** PriorRequestNotComplete **
If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an `HTTP 400 error` (`Bad request`). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.
HTTP Status Code: 400

 ** PublicZoneVPCAssociation **
You're trying to associate a VPC with a public hosted zone. Amazon Route 53 doesn't support associating a VPC with a public hosted zone.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_AssociateVPCWithHostedZone_Examples"></a>

### Example Request
<a name="API_AssociateVPCWithHostedZone_Example_1"></a>

This example illustrates one usage of AssociateVPCWithHostedZone.

```
POST /2013-04-01/hostedzone/Z1PA6795UKMFR9/associatevpc HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<AssociateVPCWithHostedZoneRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <VPC>
      <VPCId>vpc-a1b2c3d4e5</VPCId>
      <VPCRegion>us-east-2</VPCRegion>
   <VPC>
</AssociateVPCWithHostedZoneRequest>
```

### Example Response
<a name="API_AssociateVPCWithHostedZone_Example_2"></a>

This example illustrates one usage of AssociateVPCWithHostedZone.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<AssociateVPCWithHostedZoneResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <ChangeInfo>
      <Id>/change/a1b2c3d4</Id>
      <Status>INSYNC</Status>
      <SubmittedAt>2017-03-31T01:36:41.958Z</SubmittedAt>
   </ChangeInfo>
</AssociateVPCWithHostedZoneResponse>
```

## See Also
<a name="API_AssociateVPCWithHostedZone_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/AssociateVPCWithHostedZone)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/AssociateVPCWithHostedZone)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/AssociateVPCWithHostedZone)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/AssociateVPCWithHostedZone)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/AssociateVPCWithHostedZone)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/AssociateVPCWithHostedZone)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/AssociateVPCWithHostedZone)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/AssociateVPCWithHostedZone)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/AssociateVPCWithHostedZone)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/AssociateVPCWithHostedZone)
