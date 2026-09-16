---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListEmailIdentityCertificates.html
---

# ListEmailIdentityCertificates
<a name="API_ListEmailIdentityCertificates"></a>

Lists the S/MIME certificates that are associated with the specified email identity. The results include certificates in all states, such as `PROVISIONING`, `ACTIVE`, `INACTIVE`, `DEPROVISIONING`, and `FAILED`.

If a certificate has passed its expiration time, it's returned with a status of `FAILED`.

We recommend using pagination to ensure that the operation returns quickly and successfully. When there are more results than fit in a single response, the response includes a `NextToken` value that you use in a subsequent call to retrieve the next set of results.

## Request Syntax
<a name="API_ListEmailIdentityCertificates_RequestSyntax"></a>

```
POST /v2/email/identity/certificates/list HTTP/1.1
Content-type: application/json

{
   "EmailIdentity": "{{string}}",
   "NextToken": "{{string}}",
   "PageSize": {{number}}
}
```

## URI Request Parameters
<a name="API_ListEmailIdentityCertificates_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListEmailIdentityCertificates_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EmailIdentity](#API_ListEmailIdentityCertificates_RequestSyntax) **   <a name="SES-ListEmailIdentityCertificates-request-EmailIdentity"></a>
The email identity whose certificate associations you want to list.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [NextToken](#API_ListEmailIdentityCertificates_RequestSyntax) **   <a name="SES-ListEmailIdentityCertificates-request-NextToken"></a>
A token returned from a previous call to `ListEmailIdentityCertificates` to indicate the position in the list of certificates.
Type: String
Required: No

 ** [PageSize](#API_ListEmailIdentityCertificates_RequestSyntax) **   <a name="SES-ListEmailIdentityCertificates-request-PageSize"></a>
The number of results to show in a single call to `ListEmailIdentityCertificates`. If the number of results is larger than the number you specified in this parameter, then the response includes a `NextToken` element, which you can use to obtain additional results.
Type: Integer
Required: No

## Response Syntax
<a name="API_ListEmailIdentityCertificates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Certificates": [
      {
         "CertificateArn": "string",
         "CertificateExpiryTime": number,
         "FromAddress": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEmailIdentityCertificates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Certificates](#API_ListEmailIdentityCertificates_ResponseSyntax) **   <a name="SES-ListEmailIdentityCertificates-response-Certificates"></a>
An array that contains the certificate associations for the email identity. Each entry includes the from address, the certificate's status, its Amazon Resource Name (ARN), and its expiry time.
Type: Array of [IdentityCertificate](API_IdentityCertificate.md) objects

 ** [NextToken](#API_ListEmailIdentityCertificates_ResponseSyntax) **   <a name="SES-ListEmailIdentityCertificates-response-NextToken"></a>
A token that indicates that there are additional certificates to list. To view additional certificates, issue another request to `ListEmailIdentityCertificates`, and pass this token in the `NextToken` parameter.
Type: String

## Errors
<a name="API_ListEmailIdentityCertificates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** NotFoundException **
The resource you attempted to access doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_ListEmailIdentityCertificates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/ListEmailIdentityCertificates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/ListEmailIdentityCertificates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ListEmailIdentityCertificates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/ListEmailIdentityCertificates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ListEmailIdentityCertificates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/ListEmailIdentityCertificates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/ListEmailIdentityCertificates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/ListEmailIdentityCertificates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/ListEmailIdentityCertificates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ListEmailIdentityCertificates)
