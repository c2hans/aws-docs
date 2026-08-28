---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCertificate.html
---

# DeleteCertificate
<a name="API_DeleteCertificate"></a>

Deletes the specified certificate.

A certificate cannot be deleted if it has a policy or IoT thing attached to it or if its status is set to ACTIVE. To delete a certificate, first use the [DetachPolicy](API_DetachPolicy.md) action to detach all policies. Next, use the [UpdateCertificate](API_UpdateCertificate.md) action to set the certificate to the INACTIVE status.

Requires permission to access the [DeleteCertificate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DeleteCertificate_RequestSyntax"></a>

```
DELETE /certificates/{{certificateId}}?forceDelete={{forceDelete}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCertificate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [certificateId](#API_DeleteCertificate_RequestSyntax) **   <a name="iot-DeleteCertificate-request-uri-certificateId"></a>
The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`
Required: Yes

 ** [forceDelete](#API_DeleteCertificate_RequestSyntax) **   <a name="iot-DeleteCertificate-request-uri-forceDelete"></a>
Forces the deletion of a certificate if it is inactive and is not attached to an IoT thing.

## Request Body
<a name="API_DeleteCertificate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCertificate_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCertificate_Errors"></a>

 ** CertificateStateException **
The certificate operation is not allowed.
 ** message **
The message for the exception.
HTTP Status Code: 406

 ** DeleteConflictException **
You can't delete the resource because it is attached to one or more resources.
 ** message **
The message for the exception.
HTTP Status Code: 409

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_DeleteCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DeleteCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DeleteCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DeleteCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DeleteCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DeleteCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DeleteCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DeleteCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DeleteCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DeleteCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DeleteCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
