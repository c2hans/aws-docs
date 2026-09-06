---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/resource-profiles-artifacts.html
---

# Resource Sensitivity Profile - Artifacts
<a name="resource-profiles-artifacts"></a>

The Resource Sensitivity Profile Artifacts resource provides information about Amazon Simple Storage Service (Amazon S3) objects that Amazon Macie selected for analysis from individual S3 buckets for your account. If you're the Macie administrator for an organization, this includes objects in S3 buckets that your member accounts own.

For each S3 object, the information includes:
+ The Amazon Resource Name (ARN) of the object.
+ Whether Macie successfully completed its analysis of the object.
+ Whether Macie found sensitive data in the object.

The information captures the results of automated sensitive data discovery activities that Macie has performed for an S3 bucket. For more information, see [Performing automated sensitive data discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd.html) in the *Amazon Macie User Guide*.

You can use the Resource Sensitivity Profile Artifacts resource to retrieve information about objects that Macie selected for analysis from an S3 bucket, and the status and results of the analysis. To use this resource, you must first enable automated sensitive data discovery. To enable it for an organization or a standalone account, use the [Configuration](automated-discovery-configuration.md) resource for automated sensitive data discovery. To enable it for a member account in an organization, use the [Accounts](automated-discovery-accounts.md) resource for automated sensitive data discovery.

## URI
<a name="resource-profiles-artifacts-url"></a>

`/resource-profiles/artifacts`

## HTTP methods
<a name="resource-profiles-artifacts-http-methods"></a>

### GET
<a name="resource-profiles-artifactsget"></a>

**Operation ID:** `ListResourceProfileArtifacts`

Retrieves information about objects that Amazon Macie selected from an S3 bucket for automated sensitive data discovery.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| resourceArn | String | True | The Amazon Resource Name (ARN) of the S3 bucket that the request applies to. |
| nextToken | String | False | The `nextToken` string that specifies which page of results to return in a paginated response. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListResourceProfileArtifactsResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="resource-profiles-artifacts-schemas"></a>

### Response bodies
<a name="resource-profiles-artifacts-response-examples"></a>

#### ListResourceProfileArtifactsResponse schema
<a name="resource-profiles-artifacts-response-body-listresourceprofileartifactsresponse-example"></a>

```
{
  "artifacts": [
    {
      "arn": "string",
      "classificationResultStatus": "string",
      "sensitive": boolean
    }
  ],
  "nextToken": "string"
}
```

#### ValidationException schema
<a name="resource-profiles-artifacts-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="resource-profiles-artifacts-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="resource-profiles-artifacts-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="resource-profiles-artifacts-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="resource-profiles-artifacts-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="resource-profiles-artifacts-properties"></a>

### AccessDeniedException
<a name="resource-profiles-artifacts-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### InternalServerException
<a name="resource-profiles-artifacts-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ListResourceProfileArtifactsResponse
<a name="resource-profiles-artifacts-model-listresourceprofileartifactsresponse"></a>

Provides information about objects that Amazon Macie selected from an S3 bucket while performing automated sensitive data discovery for an account. This information is available only if automated sensitive data discovery has been enabled for the account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| artifacts | Array of type [ResourceProfileArtifact](#resource-profiles-artifacts-model-resourceprofileartifact) | True | An array of objects, one for each of 1-100 S3 objects that Amazon Macie selected for analysis.<br />If Macie has analyzed more than 100 objects in the bucket, Macie populates the array based on the value for the `ResourceProfileArtifact.sensitive` field for an object: `true` (sensitive), followed by `false` (not sensitive). Macie then populates any remaining items in the array with information about objects where the value for the `ResourceProfileArtifact.classificationResultStatus` field is `SKIPPED`. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### ResourceNotFoundException
<a name="resource-profiles-artifacts-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceProfileArtifact
<a name="resource-profiles-artifacts-model-resourceprofileartifact"></a>

Provides information about an S3 object that Amazon Macie selected for analysis while performing automated sensitive data discovery for an account, and the status and results of the analysis. This information is available only if automated sensitive data discovery has been enabled for the account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | The Amazon Resource Name (ARN) of the object. |
| classificationResultStatus | string | True | The status of the analysis. Possible values are:+   `COMPLETE` - Amazon Macie successfully completed its analysis of the object. <br />+   `PARTIAL` - Macie analyzed only a subset of data in the object. For example, the object is an archive file that contains files in an unsupported format. <br />+   `SKIPPED` - Macie wasn't able to analyze the object. For example, the object is a malformed file.  |
| sensitive | boolean | False | Specifies whether Amazon Macie found sensitive data in the object. |

### ThrottlingException
<a name="resource-profiles-artifacts-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="resource-profiles-artifacts-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="resource-profiles-artifacts-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListResourceProfileArtifacts
<a name="ListResourceProfileArtifacts-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListResourceProfileArtifacts)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListResourceProfileArtifacts)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListResourceProfileArtifacts)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListResourceProfileArtifacts)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListResourceProfileArtifacts)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListResourceProfileArtifacts)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListResourceProfileArtifacts)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListResourceProfileArtifacts)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/ListResourceProfileArtifacts)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListResourceProfileArtifacts)
