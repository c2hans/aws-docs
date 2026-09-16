---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DisassociateHostedZone.html
---

# DisassociateHostedZone
<a name="API_route53globalresolver_DisassociateHostedZone"></a>

Disassociates a Route 53 private hosted zone from a Route 53 Global Resolver resource.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_DisassociateHostedZone_RequestSyntax"></a>

```
DELETE /hosted-zone-associations/hosted-zone/{{hostedZoneId}}/resource-arn/{{resourceArn+}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53globalresolver_DisassociateHostedZone_RequestParameters"></a>

The request uses the following URI parameters.

 ** [hostedZoneId](#API_route53globalresolver_DisassociateHostedZone_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DisassociateHostedZone-request-uri-hostedZoneId"></a>
The ID of the Route 53 private hosted zone to disassociate.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** [resourceArn](#API_route53globalresolver_DisassociateHostedZone_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DisassociateHostedZone-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the Route 53 Global Resolver resource to disassociate the hosted zone from.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_route53globalresolver_DisassociateHostedZone_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53globalresolver_DisassociateHostedZone_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "hostedZoneId": "string",
   "hostedZoneName": "string",
   "id": "string",
   "name": "string",
   "resourceArn": "string",
   "status": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_route53globalresolver_DisassociateHostedZone_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_route53globalresolver_DisassociateHostedZone_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DisassociateHostedZone-response-createdAt"></a>
The date and time when the association was originally created.
Type: Timestamp

 ** [hostedZoneId](#API_route53globalresolver_DisassociateHostedZone_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DisassociateHostedZone-response-hostedZoneId"></a>
The ID of the Route 53 private hosted zone that was disassociated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.

 ** [hostedZoneName](#API_route53globalresolver_DisassociateHostedZone_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DisassociateHostedZone-response-hostedZoneName"></a>
The name of the Route 53 private hosted zone that was disassociated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [id](#API_route53globalresolver_DisassociateHostedZone_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DisassociateHostedZone-response-id"></a>
The unique identifier of the disassociation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [name](#API_route53globalresolver_DisassociateHostedZone_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DisassociateHostedZone-response-name"></a>
The name of the association that was removed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [resourceArn](#API_route53globalresolver_DisassociateHostedZone_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DisassociateHostedZone-response-resourceArn"></a>
The Amazon Resource Name (ARN) of the Route 53 Global Resolver resource that the hosted zone was disassociated from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [status](#API_route53globalresolver_DisassociateHostedZone_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DisassociateHostedZone-response-status"></a>
The final status of the disassociation.
Type: String
Valid Values: `CREATING | OPERATIONAL | DELETING`

 ** [updatedAt](#API_route53globalresolver_DisassociateHostedZone_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DisassociateHostedZone-response-updatedAt"></a>
The date and time when the association was last updated before disassociation.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_DisassociateHostedZone_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform this operation. Check your IAM permissions and try again.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **
An internal server error occurred. Try again later.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify the resource ID and try again.
 ** resourceId **
The unique ID of the resource referenced in the failed request.
 ** resourceType **
The resource type of the resource referenced in the failed request.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled due to too many requests. Wait a moment and try again.
 ** quotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
 ** serviceCode **
The code for the AWS service that owns the quota.
HTTP Status Code: 429

 ** ValidationException **
The input parameters are invalid. Check the parameter values and try again.
 ** fieldList **
The list of fields that aren't valid.
 ** reason **
Reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_route53globalresolver_DisassociateHostedZone_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/DisassociateHostedZone)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/DisassociateHostedZone)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/DisassociateHostedZone)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/DisassociateHostedZone)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/DisassociateHostedZone)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/DisassociateHostedZone)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/DisassociateHostedZone)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/DisassociateHostedZone)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/DisassociateHostedZone)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/DisassociateHostedZone)
