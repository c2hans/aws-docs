---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificateDomainValidations.html
---

# ListCertificateDomainValidations
<a name="API_ListCertificateDomainValidations"></a>

Returns per-domain validation summaries for an ACM certificate. Each summary includes the domain name, the active validation configuration, and the requested validation configuration when a validation method migration is in progress. You can use the results to monitor the progress of an email-to-DNS validation migration and to retrieve the CNAME records required for DNS validation.

## Request Syntax
<a name="API_ListCertificateDomainValidations_RequestSyntax"></a>

```
{
   "CertificateArn": "{{string}}",
   "MaxItems": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCertificateDomainValidations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [CertificateArn](#API_ListCertificateDomainValidations_RequestSyntax) **   <a name="ACM-ListCertificateDomainValidations-request-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate for which to list domain validation summaries.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:certificate/[\w+=,.@-]+.*`
Required: Yes

 ** [MaxItems](#API_ListCertificateDomainValidations_RequestSyntax) **   <a name="ACM-ListCertificateDomainValidations-request-MaxItems"></a>
The maximum number of domain validation summaries to return. If you don't specify a value, the default is 1000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListCertificateDomainValidations_RequestSyntax) **   <a name="ACM-ListCertificateDomainValidations-request-NextToken"></a>
A token returned by a previous call to `ListCertificateDomainValidations`. If the number of results exceeds `MaxItems`, use this token to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]*`
Required: No

## Response Syntax
<a name="API_ListCertificateDomainValidations_ResponseSyntax"></a>

```
{
   "DomainValidationSummaryList": [
      {
         "ActiveValidationConfiguration": {
            "ValidationChallenge": { ... },
            "ValidationMethod": "string",
            "ValidationStatus": "string"
         },
         "DomainName": "string",
         "RequestedValidationConfiguration": {
            "ValidationChallenge": { ... },
            "ValidationMethod": "string",
            "ValidationStatus": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCertificateDomainValidations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainValidationSummaryList](#API_ListCertificateDomainValidations_ResponseSyntax) **   <a name="ACM-ListCertificateDomainValidations-response-DomainValidationSummaryList"></a>
A list of [DomainValidationSummary](API_DomainValidationSummary.md) objects, one for each domain on the certificate. Each object contains the domain name and its active and requested validation configurations.
Type: Array of [DomainValidationSummary](API_DomainValidationSummary.md) objects

 ** [NextToken](#API_ListCertificateDomainValidations_ResponseSyntax) **   <a name="ACM-ListCertificateDomainValidations-response-NextToken"></a>
If the number of results exceeds `MaxItems`, this token is included in the response. Use this token in a subsequent `ListCertificateDomainValidations` request to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]*`

## Errors
<a name="API_ListCertificateDomainValidations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have access required to perform this action.
HTTP Status Code: 400

 ** InvalidArgsException **
One or more of request parameters specified is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified certificate cannot be found in the caller's account or the caller's account cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because it exceeded a quota.
 ** throttlingReasons **
One or more reasons why the request was throttled.
HTTP Status Code: 400

## Examples
<a name="API_ListCertificateDomainValidations_Examples"></a>

### ListCertificateDomainValidations
<a name="API_ListCertificateDomainValidations_Example_1"></a>

This example illustrates one usage of ListCertificateDomainValidations.

#### Sample Request
<a name="API_ListCertificateDomainValidations_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 112
X-Amz-Target: CertificateManager.ListCertificateDomainValidations
X-Amz-Date: 20260520T153200Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20260520/us-east-1/acm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=EXAMPLE

{
  "CertificateArn": "arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012",
  "MaxItems": 10
}
```

### Example
<a name="API_ListCertificateDomainValidations_Example_2"></a>

This example illustrates one usage of ListCertificateDomainValidations.

#### Sample Response
<a name="API_ListCertificateDomainValidations_Example_2_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: a1b2c3d4-5678-90ab-cdef-EXAMPLE22222
Content-Type: application/x-amz-json-1.1
Content-Length: 742
Date: Wed, 20 May 2026 15:32:00 GMT

{
  "DomainValidationSummaryList": [
    {
      "DomainName": "example.com",
      "ActiveValidationConfiguration": {
        "ValidationMethod": "EMAIL",
        "ValidationStatus": "SUCCESS",
        "ValidationChallenge": {
          "EmailValidationChallenge": {
            "ValidationDomain": "example.com",
            "ValidationEmails": [
              "admin@example.com",
              "postmaster@example.com"
            ]
          }
        }
      },
      "RequestedValidationConfiguration": {
        "ValidationMethod": "DNS",
        "ValidationStatus": "PENDING_VALIDATION",
        "ValidationChallenge": {
          "DnsValidationChallenge": {
            "ResourceRecord": {
              "Name": "_uoc1c1qsw7poexampleewjeno1pte3rw.example.com.",
              "Type": "CNAME",
              "Value": "_hc30uowyhpzoexample6jjr5.3ym756xh7yj.acm-validations.aws."
            }
          }
        }
      }
    },
    {
      "DomainName": "www.example.com",
      "ActiveValidationConfiguration": {
        "ValidationMethod": "EMAIL",
        "ValidationStatus": "SUCCESS",
        "ValidationChallenge": {
          "EmailValidationChallenge": {
            "ValidationDomain": "www.example.com",
            "ValidationEmails": [
              "admin@example.com"
            ]
          }
        }
      },
      "RequestedValidationConfiguration": {
        "ValidationMethod": "DNS",
        "ValidationStatus": "PENDING_VALIDATION",
        "ValidationChallenge": {
          "DnsValidationChallenge": {
            "ResourceRecord": {
              "Name": "_r4b8xf2q9kexamplep7o2n1v5m.www.example.com.",
              "Type": "CNAME",
              "Value": "_w3t9y1d6h2nexample8k4j0.q5m7v2x8r1p.acm-validations.aws."
            }
          }
        }
      }
    }
  ]
}
```

## See Also
<a name="API_ListCertificateDomainValidations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/ListCertificateDomainValidations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/ListCertificateDomainValidations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/ListCertificateDomainValidations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/ListCertificateDomainValidations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/ListCertificateDomainValidations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/ListCertificateDomainValidations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/ListCertificateDomainValidations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/ListCertificateDomainValidations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/ListCertificateDomainValidations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/ListCertificateDomainValidations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
