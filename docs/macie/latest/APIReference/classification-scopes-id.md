---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/classification-scopes-id.html
---

# Classification Scope
<a name="classification-scopes-id"></a>

The Classification Scope resource provides access to the classification scope settings for your Amazon Macie account. The classification scope specifies Amazon Simple Storage Service (Amazon S3) buckets that you don't want Macie to analyze when it performs automated sensitive data discovery. It defines an S3 bucket exclusion list for automated sensitive data discovery. For more information, see [Performing automated sensitive data discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd.html) in the *Amazon Macie User Guide*.

The first time you or your Macie administrator enables automated sensitive data discovery for your account, Macie automatically creates the classification scope for your account. If you have a standalone Macie account, Macie then uses the scope's settings to determine which S3 buckets to exclude from analyses. If your account is part of an organization that centrally manages multiple Macie accounts, Macie uses the scope settings for your Macie administrator's account to determine which buckets to exclude. Contact your Macie administrator for information about the settings for your organization.

By default, Macie analyzes data in all the S3 general purpose buckets for an account. If you're the Macie administrator for an organization, this includes buckets that your member accounts own. If you're a Macie administrator or you have a standalone Macie account, you can adjust the scope of the analyses by adding buckets to and removing buckets from the list of buckets to exclude. For example, you might exclude buckets that typically store AWS logging data, such as a bucket that stores AWS CloudTrail event logs. To exclude all buckets for a particular account in an organization, you can disable automated sensitive data discovery for the account. To do this, use the [Accounts](automated-discovery-accounts.md) resource for automated sensitive data discovery.

If you're a Macie administrator or you have a standalone Macie account, you can use the Classification Scope resource to retrieve or update the classification scope settings for your organization or account. When you use this resource, you have to specify the unique identifier for the classification scope that specifies the settings. To obtain this identifier, use the [Classification Scopes](classification-scopes.md) resource.

## URI
<a name="classification-scopes-id-url"></a>

`/classification-scopes/{{id}}`

## HTTP methods
<a name="classification-scopes-id-http-methods"></a>

### GET
<a name="classification-scopes-idget"></a>

**Operation ID:** `GetClassificationScope`

Retrieves the classification scope settings for an account.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetClassificationScopeResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### PATCH
<a name="classification-scopes-idpatch"></a>

**Operation ID:** `UpdateClassificationScope`

Updates the classification scope settings for an account.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty Schema | The request succeeded. The specified settings were updated and there isn't any content to include in the body of the response (No Content). |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="classification-scopes-id-schemas"></a>

### Request bodies
<a name="classification-scopes-id-request-examples"></a>

#### PATCH schema
<a name="classification-scopes-id-request-body-patch-example"></a>

```
{
  "s3": {
    "excludes": {
      "bucketNames": [
        "string"
      ],
      "operation": enum
    }
  }
}
```

### Response bodies
<a name="classification-scopes-id-response-examples"></a>

#### GetClassificationScopeResponse schema
<a name="classification-scopes-id-response-body-getclassificationscoperesponse-example"></a>

```
{
  "id": "string",
  "name": "string",
  "s3": {
    "excludes": {
      "bucketNames": [
        "string"
      ]
    }
  }
}
```

#### Empty Schema schema
<a name="classification-scopes-id-response-body-empty-example"></a>

```
{
}
```

#### ValidationException schema
<a name="classification-scopes-id-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="classification-scopes-id-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="classification-scopes-id-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="classification-scopes-id-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="classification-scopes-id-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="classification-scopes-id-properties"></a>

### AccessDeniedException
<a name="classification-scopes-id-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ClassificationScopeUpdateOperation
<a name="classification-scopes-id-model-classificationscopeupdateoperation"></a>

Specifies how to apply changes to the S3 bucket exclusion list defined by the classification scope for an Amazon Macie account. Valid values are:
+ `ADD`
+ `REPLACE`
+ `REMOVE`

### Empty
<a name="classification-scopes-id-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### GetClassificationScopeResponse
<a name="classification-scopes-id-model-getclassificationscoperesponse"></a>

Provides information about the classification scope settings for an Amazon Macie account. Macie uses these settings when it performs automated sensitive data discovery for the account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | The unique identifier for the classification scope. |
| name | string | False | The name of the classification scope: `automated-sensitive-data-discovery`. |
| s3 | [S3ClassificationScope](#classification-scopes-id-model-s3classificationscope) | False | The S3 buckets that are excluded from automated sensitive data discovery. |

### InternalServerException
<a name="classification-scopes-id-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="classification-scopes-id-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### S3ClassificationScope
<a name="classification-scopes-id-model-s3classificationscope"></a>

Specifies the S3 buckets that are excluded from automated sensitive data discovery for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| excludes | [S3ClassificationScopeExclusion](#classification-scopes-id-model-s3classificationscopeexclusion) | True | The S3 buckets that are excluded. |

### S3ClassificationScopeExclusion
<a name="classification-scopes-id-model-s3classificationscopeexclusion"></a>

Specifies the names of the S3 buckets that are excluded from automated sensitive data discovery.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketNames | Array of type string | True | An array of strings, one for each S3 bucket that is excluded. Each string is the full name of an excluded bucket. |

### S3ClassificationScopeExclusionUpdate
<a name="classification-scopes-id-model-s3classificationscopeexclusionupdate"></a>

Specifies S3 buckets to add or remove from the exclusion list defined by the classification scope for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketNames | Array of type string | True | Depending on the value specified for the update operation (`ClassificationScopeUpdateOperation`), an array of strings that: lists the names of buckets to add or remove from the list, or specifies a new set of bucket names that overwrites all existing names in the list. Each string must be the full name of an existing S3 bucket. Values are case sensitive. |
| operation | [ClassificationScopeUpdateOperation](#classification-scopes-id-model-classificationscopeupdateoperation) | True | Specifies how to apply the changes to the exclusion list. Valid values are:+  `ADD` - Append the specified bucket names to the current list. <br />+  `REMOVE` - Remove the specified bucket names from the current list. <br />+  `REPLACE` - Overwrite the current list with the specified list of bucket names. If you specify this value, Amazon Macie removes all existing names from the list and adds all the specified names to the list.  |

### S3ClassificationScopeUpdate
<a name="classification-scopes-id-model-s3classificationscopeupdate"></a>

Specifies changes to the list of S3 buckets that are excluded from automated sensitive data discovery for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| excludes | [S3ClassificationScopeExclusionUpdate](#classification-scopes-id-model-s3classificationscopeexclusionupdate) | True | The names of the S3 buckets to add or remove from the list. |

### ThrottlingException
<a name="classification-scopes-id-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UpdateClassificationScopeRequest
<a name="classification-scopes-id-model-updateclassificationscoperequest"></a>

Specifies new classification scope settings for an Amazon Macie account. Macie uses these settings when it performs automated sensitive data discovery for the account. To update the settings, automated sensitive data discovery must be enabled for the account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| s3 | [S3ClassificationScopeUpdate](#classification-scopes-id-model-s3classificationscopeupdate) | False | The S3 buckets to add or remove from the exclusion list defined by the classification scope. |

### ValidationException
<a name="classification-scopes-id-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="classification-scopes-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetClassificationScope
<a name="GetClassificationScope-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetClassificationScope)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetClassificationScope)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetClassificationScope)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetClassificationScope)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetClassificationScope)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetClassificationScope)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetClassificationScope)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetClassificationScope)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetClassificationScope)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetClassificationScope)

### UpdateClassificationScope
<a name="UpdateClassificationScope-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/UpdateClassificationScope)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/UpdateClassificationScope)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/UpdateClassificationScope)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/UpdateClassificationScope)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/UpdateClassificationScope)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/UpdateClassificationScope)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/UpdateClassificationScope)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/UpdateClassificationScope)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/UpdateClassificationScope)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/UpdateClassificationScope)
