---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html
---

# CreateCertificateFromCsr
<a name="API_CreateCertificateFromCsr"></a>

Creates an X.509 certificate using the specified certificate signing request.

Requires permission to access the [CreateCertificateFromCsr](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

**Note**
The CSR must include a public key that is either an RSA key with a length of at least 2048 bits or an ECC key from NIST P-256, NIST P-384, or NIST P-521 curves. For supported certificates, consult [ Certificate signing algorithms supported by AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html#x509-cert-algorithms).

**Note**
Reusing the same certificate signing request (CSR) results in a distinct certificate.

You can create multiple certificates in a batch by creating a directory, copying multiple `.csr` files into that directory, and then specifying that directory on the command line. The following commands show how to create a batch of certificates given a batch of CSRs. In the following commands, we assume that a set of CSRs are located inside of the directory my-csr-directory:

On Linux and OS X, the command is:

 `$ ls my-csr-directory/ | xargs -I {} aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/{}`

This command lists all of the CSRs in my-csr-directory and pipes each CSR file name to the `aws iot create-certificate-from-csr` AWS CLI command to create a certificate for the corresponding CSR.

You can also run the `aws iot create-certificate-from-csr` part of the command in parallel to speed up the certificate creation process:

 `$ ls my-csr-directory/ | xargs -P 10 -I {} aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/{} `

On Windows PowerShell, the command to create certificates for all CSRs in my-csr-directory is:

 `> ls -Name my-csr-directory | %{aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/$_} `

On a Windows command prompt, the command to create certificates for all CSRs in my-csr-directory is:

 `> forfiles /p my-csr-directory /c "cmd /c aws iot create-certificate-from-csr --certificate-signing-request file://@path" `

## Request Syntax
<a name="API_CreateCertificateFromCsr_RequestSyntax"></a>

```
POST /certificates?setAsActive={{setAsActive}} HTTP/1.1
Content-type: application/json

{
   "certificateSigningRequest": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateCertificateFromCsr_RequestParameters"></a>

The request uses the following URI parameters.

 ** [setAsActive](#API_CreateCertificateFromCsr_RequestSyntax) **   <a name="iot-CreateCertificateFromCsr-request-uri-setAsActive"></a>
Specifies whether the certificate is active.

## Request Body
<a name="API_CreateCertificateFromCsr_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [certificateSigningRequest](#API_CreateCertificateFromCsr_RequestSyntax) **   <a name="iot-CreateCertificateFromCsr-request-certificateSigningRequest"></a>
The certificate signing request (CSR).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\s\S]*`
Required: Yes

## Response Syntax
<a name="API_CreateCertificateFromCsr_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateArn": "string",
   "certificateId": "string",
   "certificatePem": "string"
}
```

## Response Elements
<a name="API_CreateCertificateFromCsr_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateArn](#API_CreateCertificateFromCsr_ResponseSyntax) **   <a name="iot-CreateCertificateFromCsr-response-certificateArn"></a>
The Amazon Resource Name (ARN) of the certificate. You can use the ARN as a principal for policy operations.
Type: String

 ** [certificateId](#API_CreateCertificateFromCsr_ResponseSyntax) **   <a name="iot-CreateCertificateFromCsr-response-certificateId"></a>
The ID of the certificate. Certificate management operations only take a certificateId.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`

 ** [certificatePem](#API_CreateCertificateFromCsr_ResponseSyntax) **   <a name="iot-CreateCertificateFromCsr-response-certificatePem"></a>
The certificate data, in PEM format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Pattern: `[\s\S]*`

## Errors
<a name="API_CreateCertificateFromCsr_Errors"></a>

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
<a name="API_CreateCertificateFromCsr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateCertificateFromCsr)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateCertificateFromCsr)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateCertificateFromCsr)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateCertificateFromCsr)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateCertificateFromCsr)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateCertificateFromCsr)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateCertificateFromCsr)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateCertificateFromCsr)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateCertificateFromCsr)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateCertificateFromCsr)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
