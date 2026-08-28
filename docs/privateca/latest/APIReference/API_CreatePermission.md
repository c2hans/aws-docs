---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreatePermission.html
---

# CreatePermission
<a name="API_CreatePermission"></a>

Grants one or more permissions on a private CA to the AWS Certificate Manager (ACM) service principal (`acm.amazonaws.com`). These permissions allow ACM to issue and renew ACM certificates that reside in the same AWS account as the CA.

You can list current permissions with the [ListPermissions](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListPermissions.html) action and revoke them with the [DeletePermission](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePermission.html) action.

**About Permissions**
+ If the private CA and the certificates it issues reside in the same account, you can use `CreatePermission` to grant permissions for ACM to carry out automatic certificate renewals.
+ For automatic certificate renewal to succeed, the ACM service principal needs permissions to create, retrieve, and list certificates.
+ If the private CA and the ACM certificates reside in different accounts, then permissions cannot be used to enable automatic renewals. Instead, the ACM certificate owner must set up a resource-based policy to enable cross-account issuance and renewals. For more information, see [Using a Resource Based Policy with AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html).

## Request Syntax
<a name="API_CreatePermission_RequestSyntax"></a>

```
{
   "Actions": [ "{{string}}" ],
   "CertificateAuthorityArn": "{{string}}",
   "Principal": "{{string}}",
   "SourceAccount": "{{string}}"
}
```

## Request Parameters
<a name="API_CreatePermission_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Actions](#API_CreatePermission_RequestSyntax) **   <a name="privateca-CreatePermission-request-Actions"></a>
The actions that the specified AWS service principal can use. These include `IssueCertificate`, `GetCertificate`, and `ListPermissions`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `IssueCertificate | GetCertificate | ListPermissions`
Required: Yes

 ** [CertificateAuthorityArn](#API_CreatePermission_RequestSyntax) **   <a name="privateca-CreatePermission-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) of the CA that grants the permissions. You can find the ARN by calling the [ListCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html) action. This must have the following form:
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012 `.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

 ** [Principal](#API_CreatePermission_RequestSyntax) **   <a name="privateca-CreatePermission-request-Principal"></a>
The AWS service or identity that receives the permission. At this time, the only valid principal is `acm.amazonaws.com`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[^*]+`
Required: Yes

 ** [SourceAccount](#API_CreatePermission_RequestSyntax) **   <a name="privateca-CreatePermission-request-SourceAccount"></a>
The ID of the calling account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

## Response Elements
<a name="API_CreatePermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreatePermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **
The requested Amazon Resource Name (ARN) does not refer to an existing resource.
HTTP Status Code: 400

 ** InvalidStateException **
The state of the private CA does not allow this action to occur.
HTTP Status Code: 400

 ** LimitExceededException **
An AWS Private CA quota has been exceeded. See the exception message returned to determine the quota that was exceeded.
HTTP Status Code: 400

 ** PermissionAlreadyExistsException **
The designated permission has already been given to the user.
HTTP Status Code: 400

 ** RequestFailedException **
The request has failed for an unspecified reason.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.
HTTP Status Code: 400

## Examples
<a name="API_CreatePermission_Examples"></a>

### Example
<a name="API_CreatePermission_Example_1"></a>

This example illustrates one usage of CreatePermission.

#### Sample Request
<a name="API_CreatePermission_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm.us-east-1.privateca/latest/APIReference/
X-Amz-Target: CertificateManager.CreatePermission
X-Amz-Date: 20190207T170903Z
User-Agent: aws-cli/1.10.20 Python/2.7.3 Linux/3.13.0-83-generic botocore/1.4.11
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS,
SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target,
Signature=379429306c5e89b9b4be5b35e29c26cc1da38215d8055a5ed0bdda57bcc881cc

{
  "Actions": {
    "IssueCertificate",
    "GetCertificate",
    "ListPermissions"
  },
  "CertificateArn":"arn:aws:acm:us-east-1:111122223333:certificate-authority/01234567-89ab-cdef-0123-0123456789ab",
  "Principal":"acm.amazonaws.com",
  "SourceAccount":"012345678901"
}
```

### Example
<a name="API_CreatePermission_Example_2"></a>

This example illustrates one usage of CreatePermission.

#### Sample Response
<a name="API_CreatePermission_Example_2_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 3c8d676d-025e-11e6-8823-93164b47113c
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Thu, Feb 7 2019 17:09:05 GMT
```

## See Also
<a name="API_CreatePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/CreatePermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/CreatePermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/CreatePermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/CreatePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/CreatePermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/CreatePermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/CreatePermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/CreatePermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/CreatePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/CreatePermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
