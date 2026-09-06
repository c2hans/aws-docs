---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListPermissions.html
---

# ListPermissions
<a name="API_ListPermissions"></a>

List all permissions on a private CA, if any, granted to the AWS Certificate Manager (ACM) service principal (acm.amazonaws.com).

These permissions allow ACM to issue and renew ACM certificates that reside in the same AWS account as the CA.

Permissions can be granted with the [CreatePermission](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreatePermission.html) action and revoked with the [DeletePermission](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePermission.html) action.

**About Permissions**
+ If the private CA and the certificates it issues reside in the same account, you can use `CreatePermission` to grant permissions for ACM to carry out automatic certificate renewals.
+ For automatic certificate renewal to succeed, the ACM service principal needs permissions to create, retrieve, and list certificates.
+ If the private CA and the ACM certificates reside in different accounts, then permissions cannot be used to enable automatic renewals. Instead, the ACM certificate owner must set up a resource-based policy to enable cross-account issuance and renewals. For more information, see [Using a Resource Based Policy with AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html).

## Request Syntax
<a name="API_ListPermissions_RequestSyntax"></a>

```
{
   "CertificateAuthorityArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPermissions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateAuthorityArn](#API_ListPermissions_RequestSyntax) **   <a name="privateca-ListPermissions-request-CertificateAuthorityArn"></a>
The Amazon Resource Number (ARN) of the private CA to inspect. You can find the ARN by calling the [ListCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html) action. This must be of the form: `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012` You can get a private CA's ARN by running the [ListCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html) action.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

 ** [MaxResults](#API_ListPermissions_RequestSyntax) **   <a name="privateca-ListPermissions-request-MaxResults"></a>
When paginating results, use this parameter to specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the **NextToken** element is sent in the response. Use this **NextToken** value in a subsequent request to retrieve additional items.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListPermissions_RequestSyntax) **   <a name="privateca-ListPermissions-request-NextToken"></a>
When paginating results, use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of **NextToken** from the response you just received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 43739.
Required: No

## Response Syntax
<a name="API_ListPermissions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Permissions": [
      {
         "Actions": [ "string" ],
         "CertificateAuthorityArn": "string",
         "CreatedAt": number,
         "Policy": "string",
         "Principal": "string",
         "SourceAccount": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPermissions_ResponseSyntax) **   <a name="privateca-ListPermissions-response-NextToken"></a>
When the list is truncated, this value is present and should be used for the **NextToken** parameter in a subsequent pagination request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 43739.

 ** [Permissions](#API_ListPermissions_ResponseSyntax) **   <a name="privateca-ListPermissions-response-Permissions"></a>
Summary information about each permission assigned by the specified private CA, including the action enabled, the policy provided, and the time of creation.
Type: Array of [Permission](API_Permission.md) objects
Array Members: Minimum number of 0 items.

## Errors
<a name="API_ListPermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **
The requested Amazon Resource Name (ARN) does not refer to an existing resource.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The token specified in the `NextToken` argument is not valid. Use the token returned from your previous call to [ListCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html).
HTTP Status Code: 400

 ** InvalidStateException **
The state of the private CA does not allow this action to occur.
HTTP Status Code: 400

 ** RequestFailedException **
The request has failed for an unspecified reason.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.
HTTP Status Code: 400

## Examples
<a name="API_ListPermissions_Examples"></a>

### Example
<a name="API_ListPermissions_Example_1"></a>

This example illustrates one usage of ListPermissions.

#### Sample Request
<a name="API_ListPermissions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm.us-east-1.privateca/latest/APIReference/
X-Amz-Target: CertificateManager.ListPermissions
X-Amz-Date: 20190113T171333Z
User-Agent: aws-cli/1.10.20 Python/2.7.3 Linux/3.13.0-83-generic botocore/1.4.11
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS,
SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target,
Signature=3c9429306c5a99b9b4be5b35f55c26cc1da32a215d8055a5ed0bdda57bcc881cc

{
  "CertificateArn":"arn:aws:acm:us-east-1:111122223333:certificate-authority/01234567-89ab-cdef-0123-0123456789ab",
  "MaxResults": 10
}
```

### Example
<a name="API_ListPermissions_Example_2"></a>

This example illustrates one usage of ListPermissions.

#### Sample Response
<a name="API_ListPermissions_Example_2_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 3c8d676d-025e-11e6-8823-93164b47113c
Content-Type: application/x-amz-json-1.1
Content-Length: 579
Date: Thu, Feb 13 2019 17:13:36 GMT

{
  "Permissions": [
    {
      "Actions": {
        "IssueCertificate",
        "GetCertificate",
        "ListPermissions"
      },
      "CertificateAuthorityArn": "arn:aws:acm:us-east-1:111122223333:certificate/01234567-89ab-cdef-0123-0123456789ab",
      "CreatedAt": 1.516130652887E9,
      "Principal": "acm.amazonaws.com",
      "SourceAccount": "012345678901"
    },
    {
      "Actions": {
        "LIST_PERMISSIONS"
      },
      "CertificateAuthorityArn": "arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012",
      "CreatedAt": 1.517830652887E9,
      "Principal": "acm.amazonaws.com",
      "SourceAccount": "012345678901"
    }
  ]
}
```

## See Also
<a name="API_ListPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/ListPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/ListPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/ListPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/ListPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/ListPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/ListPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/ListPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/ListPermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/ListPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/ListPermissions)
