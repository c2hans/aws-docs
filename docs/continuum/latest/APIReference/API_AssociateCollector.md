---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_AssociateCollector.html
---

# AssociateCollector
<a name="API_AssociateCollector"></a>

Associates one Collector with this Environment and configures the customer role Continuum uses to authorize access to associated Collector data. The caller must have permission on the Environment and permission to pass the role. Continuum assumes the supplied role and calls GetCollectorDataAccessAuthorization on the requested Collector; only a successful authorization response permits the association. The caller does not need Collector data-access permission. The Environment retains its other Collector associations. Calling again with an existing association is safe and does not create a duplicate.

## Request Syntax
<a name="API_AssociateCollector_RequestSyntax"></a>

```
POST /environments/{{environmentId}}/collectors HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "collectorArn": "{{string}}",
   "collectorDataAccessRoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateCollector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_AssociateCollector_RequestSyntax) **   <a name="continuum-AssociateCollector-request-uri-environmentId"></a>
The identifier of the environment.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_AssociateCollector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_AssociateCollector_RequestSyntax) **   <a name="continuum-AssociateCollector-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[!-~]{1,128}`
Required: No

 ** [collectorArn](#API_AssociateCollector_RequestSyntax) **   <a name="continuum-AssociateCollector-request-collectorArn"></a>
The Amazon Resource Name (ARN) of the collector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:collectors/[a-z0-9]+`
Required: Yes

 ** [collectorDataAccessRoleArn](#API_AssociateCollector_RequestSyntax) **   <a name="continuum-AssociateCollector-request-collectorDataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the collector Data Access Role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@/-]+`
Required: Yes

## Response Syntax
<a name="API_AssociateCollector_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "associatedCollector": {
      "collectorArn": "string",
      "collectorId": "string"
   },
   "environmentArn": "string",
   "environmentId": "string"
}
```

## Response Elements
<a name="API_AssociateCollector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [associatedCollector](#API_AssociateCollector_ResponseSyntax) **   <a name="continuum-AssociateCollector-response-associatedCollector"></a>
The associated Collector.
Type: [AssociatedCollector](API_AssociatedCollector.md) object

 ** [environmentArn](#API_AssociateCollector_ResponseSyntax) **   <a name="continuum-AssociateCollector-response-environmentArn"></a>
The Amazon Resource Name (ARN) of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:environments/[a-z0-9]+`

 ** [environmentId](#API_AssociateCollector_ResponseSyntax) **   <a name="continuum-AssociateCollector-response-environmentId"></a>
The identifier of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

## Errors
<a name="API_AssociateCollector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_AssociateCollector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/AssociateCollector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/AssociateCollector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/AssociateCollector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/AssociateCollector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/AssociateCollector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/AssociateCollector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/AssociateCollector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/AssociateCollector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/AssociateCollector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/AssociateCollector)
