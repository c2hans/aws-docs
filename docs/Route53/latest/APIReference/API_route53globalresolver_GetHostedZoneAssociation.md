---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetHostedZoneAssociation.html
---

# GetHostedZoneAssociation
<a name="API_route53globalresolver_GetHostedZoneAssociation"></a>

Retrieves information about a hosted zone association.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_GetHostedZoneAssociation_RequestSyntax"></a>

```
GET /hosted-zone-associations/{{hostedZoneAssociationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53globalresolver_GetHostedZoneAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [hostedZoneAssociationId](#API_route53globalresolver_GetHostedZoneAssociation_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetHostedZoneAssociation-request-uri-hostedZoneAssociationId"></a>
ID of the private hosted zone association.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_route53globalresolver_GetHostedZoneAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53globalresolver_GetHostedZoneAssociation_ResponseSyntax"></a>

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
<a name="API_route53globalresolver_GetHostedZoneAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_route53globalresolver_GetHostedZoneAssociation_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetHostedZoneAssociation-response-createdAt"></a>
The time and date the private hosted zone association was created.
Type: Timestamp

 ** [hostedZoneId](#API_route53globalresolver_GetHostedZoneAssociation_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetHostedZoneAssociation-response-hostedZoneId"></a>
ID of the hosted zone associated to the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.

 ** [hostedZoneName](#API_route53globalresolver_GetHostedZoneAssociation_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetHostedZoneAssociation-response-hostedZoneName"></a>
Name of the domain associated with the private hosted zone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [id](#API_route53globalresolver_GetHostedZoneAssociation_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetHostedZoneAssociation-response-id"></a>
ID of the private hosted zone association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [name](#API_route53globalresolver_GetHostedZoneAssociation_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetHostedZoneAssociation-response-name"></a>
Name of the private hosted zone association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [resourceArn](#API_route53globalresolver_GetHostedZoneAssociation_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetHostedZoneAssociation-response-resourceArn"></a>
Amazon Resource Name (ARN) of the DNS view the private hosted zone is associated to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [status](#API_route53globalresolver_GetHostedZoneAssociation_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetHostedZoneAssociation-response-status"></a>
The operational status of the private hosted zone association.
Type: String
Valid Values: `CREATING | OPERATIONAL | DELETING`

 ** [updatedAt](#API_route53globalresolver_GetHostedZoneAssociation_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetHostedZoneAssociation-response-updatedAt"></a>
The time and date the private hosted zone association was updated.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_GetHostedZoneAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform this operation. Check your IAM permissions and try again.
HTTP Status Code: 403

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
<a name="API_route53globalresolver_GetHostedZoneAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/GetHostedZoneAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/GetHostedZoneAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/GetHostedZoneAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/GetHostedZoneAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/GetHostedZoneAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/GetHostedZoneAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/GetHostedZoneAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/GetHostedZoneAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/GetHostedZoneAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/GetHostedZoneAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
