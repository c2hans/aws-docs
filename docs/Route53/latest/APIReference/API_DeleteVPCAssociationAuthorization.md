---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteVPCAssociationAuthorization.html
---

# DeleteVPCAssociationAuthorization
<a name="API_DeleteVPCAssociationAuthorization"></a>

Removes authorization to submit an `AssociateVPCWithHostedZone` request to associate a specified VPC with a hosted zone that was created by a different account. You must use the account that created the hosted zone to submit a `DeleteVPCAssociationAuthorization` request.

**Important**
Sending this request only prevents the AWS account that created the VPC from associating the VPC with the Amazon Route 53 hosted zone in the future. If the VPC is already associated with the hosted zone, `DeleteVPCAssociationAuthorization` won't disassociate the VPC from the hosted zone. If you want to delete an existing association, use `DisassociateVPCFromHostedZone`.

## Request Syntax
<a name="API_DeleteVPCAssociationAuthorization_RequestSyntax"></a>

```
POST /2013-04-01/hostedzone/{{Id}}/deauthorizevpcassociation HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<DeleteVPCAssociationAuthorizationRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <VPC>
      <VPCId>{{string}}</VPCId>
      <VPCRegion>{{string}}</VPCRegion>
   </VPC>
</DeleteVPCAssociationAuthorizationRequest>
```

## URI Request Parameters
<a name="API_DeleteVPCAssociationAuthorization_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DeleteVPCAssociationAuthorization_RequestSyntax) **   <a name="Route53-DeleteVPCAssociationAuthorization-request-uri-HostedZoneId"></a>
When removing authorization to associate a VPC that was created by one AWS account with a hosted zone that was created with a different AWS account, the ID of the hosted zone.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_DeleteVPCAssociationAuthorization_RequestBody"></a>

The request accepts the following data in XML format.

 ** [DeleteVPCAssociationAuthorizationRequest](#API_DeleteVPCAssociationAuthorization_RequestSyntax) **   <a name="Route53-DeleteVPCAssociationAuthorization-request-DeleteVPCAssociationAuthorizationRequest"></a>
Root level tag for the DeleteVPCAssociationAuthorizationRequest parameters.
Required: Yes

 ** [VPC](#API_DeleteVPCAssociationAuthorization_RequestSyntax) **   <a name="Route53-DeleteVPCAssociationAuthorization-request-VPC"></a>
When removing authorization to associate a VPC that was created by one AWS account with a hosted zone that was created with a different AWS account, a complex type that includes the ID and region of the VPC.
Type: [VPC](API_VPC.md) object
Required: Yes

## Response Syntax
<a name="API_DeleteVPCAssociationAuthorization_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteVPCAssociationAuthorization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteVPCAssociationAuthorization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidVPCId **
The VPC ID that you specified either isn't a valid ID or the current account is not authorized to access this VPC.
 ** message **

HTTP Status Code: 400

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

 ** VPCAssociationAuthorizationNotFound **
The VPC that you specified is not authorized to be associated with the hosted zone.
 ** message **

HTTP Status Code: 404

## Examples
<a name="API_DeleteVPCAssociationAuthorization_Examples"></a>

### Example Request
<a name="API_DeleteVPCAssociationAuthorization_Example_1"></a>

This example illustrates one usage of DeleteVPCAssociationAuthorization.

```
POST /2013-04-01/hostedzone/Z1PA6795UKMFR9/deauthorizevpcassociation HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<DeleteVPCAssociationAuthorizationRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <VPC>
      <VPCId>vpc-a1b2c3d4e5</VPCId>
      <VPCRegion>us-east-2</VPCRegion>
   </VPC>
</DeleteVPCAssociationAuthorizationRequest>
```

### Example Response
<a name="API_DeleteVPCAssociationAuthorization_Example_2"></a>

This example illustrates one usage of DeleteVPCAssociationAuthorization.

```
HTTP/1.1 200
```

## See Also
<a name="API_DeleteVPCAssociationAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/DeleteVPCAssociationAuthorization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/DeleteVPCAssociationAuthorization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/DeleteVPCAssociationAuthorization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/DeleteVPCAssociationAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/DeleteVPCAssociationAuthorization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/DeleteVPCAssociationAuthorization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/DeleteVPCAssociationAuthorization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/DeleteVPCAssociationAuthorization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/DeleteVPCAssociationAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/DeleteVPCAssociationAuthorization)
