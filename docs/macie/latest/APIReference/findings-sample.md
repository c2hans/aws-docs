---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/findings-sample.html
---

# Finding Samples
<a name="findings-sample"></a>

The Finding Samples resource provides a set of findings that use example data and placeholder values to help you understand and analyze the types of findings that Amazon Macie can generate. A *finding* is a detailed report of a potential issue with the security or privacy of an Amazon Simple Storage Service (Amazon S3) general purpose bucket or sensitive data in an S3 object. For information about the types of findings that Macie can generate, see [Types of findings](https://docs.aws.amazon.com/macie/latest/user/findings-types.html) in the *Amazon Macie User Guide*.

If you use this resource to create sample findings, Macie generates one sample finding for each supported finding type that you choose to include in the set of samples. You can then review and work with the samples by using the Amazon Macie API or the Amazon Macie console. Depending on the findings filters and publication settings for your Macie account, you can also work with the samples by using Amazon EventBridge and AWS Security Hub CSPM. To help you identify a sample finding, Macie sets the value for the `sample` field of each finding to `true`. For more information about creating and managing sample findings, see [Working with sample findings](https://docs.aws.amazon.com/macie/latest/user/findings-samples.html) in the *Amazon Macie User Guide*.

You can use the Finding Samples resource to create one or more sample findings. To create only certain types of sample findings, use the supported request parameter to specify each type of sample finding that you want to create.

## URI
<a name="findings-sample-url"></a>

`/findings/sample`

## HTTP methods
<a name="findings-sample-http-methods"></a>

### POST
<a name="findings-samplepost"></a>

**Operation ID:** `CreateSampleFindings`

Creates sample findings.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty Schema | The request succeeded and there isn't any content to include in the body of the response (No Content). |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="findings-sample-schemas"></a>

### Request bodies
<a name="findings-sample-request-examples"></a>

#### POST schema
<a name="findings-sample-request-body-post-example"></a>

```
{
  "findingTypes": [
    enum
  ]
}
```

### Response bodies
<a name="findings-sample-response-examples"></a>

#### Empty Schema schema
<a name="findings-sample-response-body-empty-example"></a>

```
{
}
```

#### ValidationException schema
<a name="findings-sample-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="findings-sample-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="findings-sample-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="findings-sample-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="findings-sample-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="findings-sample-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="findings-sample-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="findings-sample-properties"></a>

### AccessDeniedException
<a name="findings-sample-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="findings-sample-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### CreateSampleFindingsRequest
<a name="findings-sample-model-createsamplefindingsrequest"></a>

Specifies the types of sample findings to create.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| findingTypes | Array of type [FindingType](#findings-sample-model-findingtype) | False | An array of finding types, one for each type of sample finding to create. To create a sample of every type of finding that Amazon Macie supports, don't include this array in your request. |

### Empty
<a name="findings-sample-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### FindingType
<a name="findings-sample-model-findingtype"></a>

The type of finding. For details about each type, see [Types of findings](https://docs.aws.amazon.com/macie/latest/user/findings-types.html) in the *Amazon Macie User Guide*. Possible values are:
+ `SensitiveData:S3Object/Multiple`
+ `SensitiveData:S3Object/Financial`
+ `SensitiveData:S3Object/Personal`
+ `SensitiveData:S3Object/Credentials`
+ `SensitiveData:S3Object/CustomIdentifier`
+ `Policy:IAMUser/S3BucketPublic`
+ `Policy:IAMUser/S3BucketSharedExternally`
+ `Policy:IAMUser/S3BucketReplicatedExternally`
+ `Policy:IAMUser/S3BucketEncryptionDisabled`
+ `Policy:IAMUser/S3BlockPublicAccessDisabled`
+ `Policy:IAMUser/S3BucketSharedWithCloudFront`

### InternalServerException
<a name="findings-sample-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="findings-sample-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="findings-sample-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="findings-sample-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="findings-sample-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="findings-sample-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### CreateSampleFindings
<a name="CreateSampleFindings-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/CreateSampleFindings)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/CreateSampleFindings)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/CreateSampleFindings)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/CreateSampleFindings)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/CreateSampleFindings)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/CreateSampleFindings)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/CreateSampleFindings)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/CreateSampleFindings)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/CreateSampleFindings)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/CreateSampleFindings)
