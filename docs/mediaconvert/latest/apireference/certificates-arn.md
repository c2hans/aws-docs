---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/certificates-arn.html
---

# Certificates arn
<a name="certificates-arn"></a>

## URI
<a name="certificates-arn-url"></a>

`/2017-08-29/certificates/{{arn}}`

## HTTP methods
<a name="certificates-arn-http-methods"></a>

### DELETE
<a name="certificates-arndelete"></a>

**Operation ID:** `DisassociateCertificate`

Removes an association between the Amazon Resource Name (ARN) of an AWS Certificate Manager (ACM) certificate and an AWS Elemental MediaConvert resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{arn}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 202 | DisassociateCertificateResponse | 202 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### OPTIONS
<a name="certificates-arnoptions"></a>

Supports CORS preflight requests.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{arn}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request completed successfully. |

## Schemas
<a name="certificates-arn-schemas"></a>

### Request bodies
<a name="certificates-arn-request-examples"></a>

#### DELETE schema
<a name="certificates-arn-request-body-delete-example"></a>

```
{
  "arn": "string"
}
```

### Response bodies
<a name="certificates-arn-response-examples"></a>

#### DisassociateCertificateResponse schema
<a name="certificates-arn-response-body-disassociatecertificateresponse-example"></a>

```
{
}
```

#### ExceptionBody schema
<a name="certificates-arn-response-body-exceptionbody-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="certificates-arn-properties"></a>

### DisassociateCertificateRequest
<a name="certificates-arn-model-disassociatecertificaterequest"></a>

Removes an association between the Amazon Resource Name (ARN) of an AWS Certificate Manager (ACM) certificate and an AWS Elemental MediaConvert resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The ARN of the ACM certificate that you want to disassociate from your MediaConvert resource. |

### DisassociateCertificateResponse
<a name="certificates-arn-model-disassociatecertificateresponse"></a>

Successful disassociation of Certificate Manager Amazon Resource Name (ARN) with Mediaconvert returns an OK message.

### ExceptionBody
<a name="certificates-arn-model-exceptionbody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

## See also
<a name="certificates-arn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DisassociateCertificate
<a name="DisassociateCertificate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/DisassociateCertificate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/DisassociateCertificate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/DisassociateCertificate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/DisassociateCertificate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/DisassociateCertificate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/DisassociateCertificate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/DisassociateCertificate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/DisassociateCertificate)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mediaconvert-2017-08-29/DisassociateCertificate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/DisassociateCertificate)
