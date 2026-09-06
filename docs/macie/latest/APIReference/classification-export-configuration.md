---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/classification-export-configuration.html
---

# Classification Results - Export Configuration
<a name="classification-export-configuration"></a>

The Export Configuration resource for classification results provides access to settings for storing data classification results in an Amazon Simple Storage Service (Amazon S3) bucket. A *data classification result*, also referred to as a *sensitive data discovery result*, is a record that logs details about the analysis that Amazon Macie performed on an Amazon S3 object to determine whether the object contains sensitive data.

When you run a classification job or Macie performs automated sensitive data discovery, Macie automatically creates a data classification result for each S3 object that's included in the scope of the analysis. This includes objects that Macie doesn't find sensitive data in, and therefore don't produce findings, and objects that Macie can't analyze due to issues such as permissions settings. Data classification results provide you with analysis records that can be helpful for data privacy and protection audits or investigations. You can configure Macie to store these records in an S3 general purpose bucket and encrypt them with an AWS Key Management Service (AWS KMS) key. For more information, see [Storing and retaining sensitive data discovery results](https://docs.aws.amazon.com/macie/latest/user/discovery-results-repository-s3.html) in the *Amazon Macie User Guide*.

If you use Macie in multiple AWS Regions, configure these settings for each Region in which you use Macie. You can optionally store data classification results for multiple Regions in the same S3 bucket. However, note the following requirements:
+ To store the results for a Region that AWS enables by default for AWS accounts, such as the US East (N. Virginia) Region, you have to specify a bucket in a Region that's enabled by default. The results can't be stored in a bucket in an opt-in Region (Region that's disabled by default).
+ To store the results for an opt-in Region, such as the Middle East (Bahrain) Region, you have to specify a bucket in that same Region or a Region that's enabled by default. The results can't be stored in a bucket in a different opt-in Region.

To determine whether a Region is enabled by default, see [Enable or disable AWS Regions in your account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) in the *AWS Account Management Reference Guide*. In addition to the preceding requirements, also consider whether you want to [retrieve samples of sensitive data](findings-findingid-reveal.md) that Macie reports in individual findings. To retrieve sensitive data samples from an affected S3 object, all of the following resources and data must be stored in the same Region: the affected object, the applicable finding, and the corresponding sensitive data discovery result.

You can use the Export Configuration resource to specify or retrieve information about your configuration settings for storing data classification results in an S3 bucket.

## URI
<a name="classification-export-configuration-url"></a>

`/classification-export-configuration`

## HTTP methods
<a name="classification-export-configuration-http-methods"></a>

### GET
<a name="classification-export-configurationget"></a>

**Operation ID:** `GetClassificationExportConfiguration`

Retrieves the configuration settings for storing data classification results.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetClassificationExportConfigurationResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### PUT
<a name="classification-export-configurationput"></a>

**Operation ID:** `PutClassificationExportConfiguration`

Adds or updates the configuration settings for storing data classification results.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | PutClassificationExportConfigurationResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="classification-export-configuration-schemas"></a>

### Request bodies
<a name="classification-export-configuration-request-examples"></a>

#### PUT schema
<a name="classification-export-configuration-request-body-put-example"></a>

```
{
  "configuration": {
    "s3Destination": {
      "bucketName": "string",
      "expectedBucketOwner": "string",
      "keyPrefix": "string",
      "kmsKeyArn": "string"
    }
  }
}
```

### Response bodies
<a name="classification-export-configuration-response-examples"></a>

#### GetClassificationExportConfigurationResponse schema
<a name="classification-export-configuration-response-body-getclassificationexportconfigurationresponse-example"></a>

```
{
  "configuration": {
    "s3Destination": {
      "bucketName": "string",
      "expectedBucketOwner": "string",
      "keyPrefix": "string",
      "kmsKeyArn": "string"
    }
  }
}
```

#### PutClassificationExportConfigurationResponse schema
<a name="classification-export-configuration-response-body-putclassificationexportconfigurationresponse-example"></a>

```
{
  "configuration": {
    "s3Destination": {
      "bucketName": "string",
      "expectedBucketOwner": "string",
      "keyPrefix": "string",
      "kmsKeyArn": "string"
    }
  }
}
```

#### ValidationException schema
<a name="classification-export-configuration-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="classification-export-configuration-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="classification-export-configuration-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="classification-export-configuration-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="classification-export-configuration-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="classification-export-configuration-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="classification-export-configuration-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="classification-export-configuration-properties"></a>

### AccessDeniedException
<a name="classification-export-configuration-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ClassificationExportConfiguration
<a name="classification-export-configuration-model-classificationexportconfiguration"></a>

Specifies where to store data classification results, and the encryption settings to use when storing results in that location. The location must be an S3 general purpose bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| s3Destination | [S3Destination](#classification-export-configuration-model-s3destination) | False | The S3 bucket to store data classification results in, and the encryption settings to use when storing results in that bucket. |

### ConflictException
<a name="classification-export-configuration-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### GetClassificationExportConfigurationResponse
<a name="classification-export-configuration-model-getclassificationexportconfigurationresponse"></a>

Provides information about the current configuration settings for storing data classification results.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configuration | [ClassificationExportConfiguration](#classification-export-configuration-model-classificationexportconfiguration) | False | The location where data classification results are stored, and the encryption settings that are used when storing results in that location. |

### InternalServerException
<a name="classification-export-configuration-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### PutClassificationExportConfigurationRequest
<a name="classification-export-configuration-model-putclassificationexportconfigurationrequest"></a>

Specifies where to store data classification results, and the encryption settings to use when storing results in that location.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configuration | [ClassificationExportConfiguration](#classification-export-configuration-model-classificationexportconfiguration) | True | The location to store data classification results in, and the encryption settings to use when storing results in that location. |

### PutClassificationExportConfigurationResponse
<a name="classification-export-configuration-model-putclassificationexportconfigurationresponse"></a>

Provides information about updated settings for storing data classification results.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configuration | [ClassificationExportConfiguration](#classification-export-configuration-model-classificationexportconfiguration) | False | The location where the data classification results are stored, and the encryption settings that are used when storing results in that location. |

### ResourceNotFoundException
<a name="classification-export-configuration-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### S3Destination
<a name="classification-export-configuration-model-s3destination"></a>

Specifies an S3 bucket to store data classification results in, and the encryption settings to use when storing results in that bucket. The bucket must be an existing general purpose bucket. It can be a bucket in your own account or a bucket that another account owns. If another account owns the bucket, you must specify both the unique identifier for the account and the name of the bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketName | string | True | The name of the bucket. This must be the name of an existing general purpose bucket that's owned by the specified account (`expectedBucketOwner`). |
| expectedBucketOwner | string | False | The unique identifier (ID) for the AWS account that owns the bucket. This must be the ID for the account that owns the specified bucket (`bucketName`). |
| keyPrefix | string | False | The path prefix to use in the path to the location in the bucket. This prefix specifies where to store classification results in the bucket. |
| kmsKeyArn | string | True | The Amazon Resource Name (ARN) of the customer managed AWS KMS key to use for encryption of the results. This must be the ARN of an existing, symmetric encryption AWS KMS key that's enabled in the same AWS Region as the bucket. |

### ServiceQuotaExceededException
<a name="classification-export-configuration-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="classification-export-configuration-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="classification-export-configuration-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="classification-export-configuration-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetClassificationExportConfiguration
<a name="GetClassificationExportConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetClassificationExportConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetClassificationExportConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetClassificationExportConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetClassificationExportConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetClassificationExportConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetClassificationExportConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetClassificationExportConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetClassificationExportConfiguration)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetClassificationExportConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetClassificationExportConfiguration)

### PutClassificationExportConfiguration
<a name="PutClassificationExportConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/PutClassificationExportConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/PutClassificationExportConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/PutClassificationExportConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/PutClassificationExportConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/PutClassificationExportConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/PutClassificationExportConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/PutClassificationExportConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/PutClassificationExportConfiguration)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/PutClassificationExportConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/PutClassificationExportConfiguration)
