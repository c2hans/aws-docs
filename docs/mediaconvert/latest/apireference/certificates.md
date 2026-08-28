---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/certificates.html
---

# Certificates
<a name="certificates"></a>

## URI
<a name="certificates-url"></a>

`/2017-08-29/certificates`

## HTTP methods
<a name="certificates-http-methods"></a>

### POST
<a name="certificatespost"></a>

**Operation ID:** `AssociateCertificate`

Associates an AWS Certificate Manager (ACM) Amazon Resource Name (ARN) with AWS Elemental MediaConvert.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | AssociateCertificateResponse | 201 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### OPTIONS
<a name="certificatesoptions"></a>

Supports CORS preflight requests.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request completed successfully. |

## Schemas
<a name="certificates-schemas"></a>

### Request bodies
<a name="certificates-request-examples"></a>

#### POST schema
<a name="certificates-request-body-post-example"></a>

```
{
  "arn": "string"
}
```

### Response bodies
<a name="certificates-response-examples"></a>

#### AssociateCertificateResponse schema
<a name="certificates-response-body-associatecertificateresponse-example"></a>

```
{
}
```

#### ExceptionBody schema
<a name="certificates-response-body-exceptionbody-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="certificates-properties"></a>

### AssociateCertificateRequest
<a name="certificates-model-associatecertificaterequest"></a>

Associates the Amazon Resource Name (ARN) of an AWS Certificate Manager (ACM) certificate with an AWS Elemental MediaConvert resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | The ARN of the ACM certificate that you want to associate with your MediaConvert resource. |

### AssociateCertificateResponse
<a name="certificates-model-associatecertificateresponse"></a>

Successful association of Certificate Manager Amazon Resource Name (ARN) with Mediaconvert returns an OK message.

### ExceptionBody
<a name="certificates-model-exceptionbody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

## See also
<a name="certificates-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### AssociateCertificate
<a name="AssociateCertificate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/AssociateCertificate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/AssociateCertificate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/AssociateCertificate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/AssociateCertificate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/AssociateCertificate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/AssociateCertificate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/AssociateCertificate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/AssociateCertificate)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/AssociateCertificate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/AssociateCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
