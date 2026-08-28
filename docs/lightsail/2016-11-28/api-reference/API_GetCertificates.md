---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetCertificates.html
---

# GetCertificates
<a name="API_GetCertificates"></a>

Returns information about one or more Amazon Lightsail SSL/TLS certificates.

**Note**
To get a summary of a certificate, omit `includeCertificateDetails` from your request. The response will include only the certificate Amazon Resource Name (ARN), certificate name, domain name, and tags.

## Request Syntax
<a name="API_GetCertificates_RequestSyntax"></a>

```
{
   "certificateName": "{{string}}",
   "certificateStatuses": [ "{{string}}" ],
   "includeCertificateDetails": {{boolean}},
   "pageToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCertificates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [certificateName](#API_GetCertificates_RequestSyntax) **   <a name="Lightsail-GetCertificates-request-certificateName"></a>
The name for the certificate for which to return information.
When omitted, the response includes all of your certificates in the AWS Region where the request is made.
Type: String
Required: No

 ** [certificateStatuses](#API_GetCertificates_RequestSyntax) **   <a name="Lightsail-GetCertificates-request-certificateStatuses"></a>
The status of the certificates for which to return information.
For example, specify `ISSUED` to return only certificates with an `ISSUED` status.
When omitted, the response includes all of your certificates in the AWS Region where the request is made, regardless of their current status.
Type: Array of strings
Valid Values: `PENDING_VALIDATION | ISSUED | INACTIVE | EXPIRED | VALIDATION_TIMED_OUT | REVOKED | FAILED`
Required: No

 ** [includeCertificateDetails](#API_GetCertificates_RequestSyntax) **   <a name="Lightsail-GetCertificates-request-includeCertificateDetails"></a>
Indicates whether to include detailed information about the certificates in the response.
When omitted, the response includes only the certificate names, Amazon Resource Names (ARNs), domain names, and tags.
Type: Boolean
Required: No

 ** [pageToken](#API_GetCertificates_RequestSyntax) **   <a name="Lightsail-GetCertificates-request-pageToken"></a>
The token to advance to the next page of results from your request.
To get a page token, perform an initial `GetCertificates` request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.
Type: String
Required: No

## Response Syntax
<a name="API_GetCertificates_ResponseSyntax"></a>

```
{
   "certificates": [
      {
         "certificateArn": "string",
         "certificateDetail": {
            "arn": "string",
            "createdAt": number,
            "domainName": "string",
            "domainValidationRecords": [
               {
                  "dnsRecordCreationState": {
                     "code": "string",
                     "message": "string"
                  },
                  "domainName": "string",
                  "resourceRecord": {
                     "name": "string",
                     "type": "string",
                     "value": "string"
                  },
                  "validationStatus": "string"
               }
            ],
            "eligibleToRenew": "string",
            "inUseResourceCount": number,
            "issuedAt": number,
            "issuerCA": "string",
            "keyAlgorithm": "string",
            "name": "string",
            "notAfter": number,
            "notBefore": number,
            "renewalSummary": {
               "domainValidationRecords": [
                  {
                     "dnsRecordCreationState": {
                        "code": "string",
                        "message": "string"
                     },
                     "domainName": "string",
                     "resourceRecord": {
                        "name": "string",
                        "type": "string",
                        "value": "string"
                     },
                     "validationStatus": "string"
                  }
               ],
               "renewalStatus": "string",
               "renewalStatusReason": "string",
               "updatedAt": number
            },
            "requestFailureReason": "string",
            "revocationReason": "string",
            "revokedAt": number,
            "serialNumber": "string",
            "status": "string",
            "subjectAlternativeNames": [ "string" ],
            "supportCode": "string",
            "tags": [
               {
                  "key": "string",
                  "value": "string"
               }
            ]
         },
         "certificateName": "string",
         "domainName": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ],
   "nextPageToken": "string"
}
```

## Response Elements
<a name="API_GetCertificates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificates](#API_GetCertificates_ResponseSyntax) **   <a name="Lightsail-GetCertificates-response-certificates"></a>
An object that describes certificates.
Type: Array of [CertificateSummary](API_CertificateSummary.md) objects

 ** [nextPageToken](#API_GetCertificates_ResponseSyntax) **   <a name="Lightsail-GetCertificates-response-nextPageToken"></a>
If `NextPageToken` is returned there are more results available. The value of `NextPageToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

## Errors
<a name="API_GetCertificates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_GetCertificates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetCertificates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetCertificates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetCertificates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetCertificates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetCertificates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetCertificates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetCertificates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetCertificates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetCertificates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetCertificates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
