---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/allow-lists.html
---

# Allow Lists
<a name="allow-lists"></a>

In Amazon Macie, an allow list defines specific text or a text pattern that you want Macie to ignore when it inspects a data source for sensitive data. If data matches text or a text pattern in an allow list, Macie doesn't report the data. This is the case even if the data matches the criteria of a managed data identifier or a custom data identifier. You can create and use allow lists in all the AWS Regions where Macie is currently available except the Asia Pacific (Osaka) Region.

Macie supports two types of allow lists:
+ **Predefined text** - For this type of list (`s3WordsList`), you create a line-delimited plaintext file that lists specific text to ignore. You store the file in an Amazon Simple Storage Service (Amazon S3) general purpose bucket and then configure settings for Macie to access the list in the bucket.

  This type of list typically contains specific words, phrases, and other kinds of character sequences that aren't sensitive, aren't likely to change, and don't necessarily adhere to a common pattern. If you use this type of list, Macie doesn't report occurrences of text that exactly match a complete entry in the list. Macie treats each entry in the list as a string literal value. Matches aren't case sensitive.
+ **Regular expression** - For this type of list (`regex`), you specify a regular expression that defines a text pattern to ignore. Unlike an allow list with predefined text, you create and store the regex and all other list settings in Macie.

  This type of list is helpful if you want to specify text that isn't sensitive but varies or is likely to change while also adhering to a common pattern. If you use this type of list, Macie doesn't report occurrences of text that completely match the pattern defined by the list.

For more information, see [Defining sensitive data exceptions with allow lists](https://docs.aws.amazon.com/macie/latest/user/allow-lists.html) in the *Amazon Macie User Guide*.

You can use the Allow Lists resource to create an allow list or to retrieve a subset of information about all the existing allow lists for your account. To retrieve detailed information about the settings and status of an individual allow list, use the [Allow List](allow-lists-id.md) resource.

## URI
<a name="allow-lists-url"></a>

`/allow-lists`

## HTTP methods
<a name="allow-lists-http-methods"></a>

### GET
<a name="allow-listsget"></a>

**Operation ID:** `ListAllowLists`

Retrieves a subset of information about all the allow lists for an account.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The `nextToken` string that specifies which page of results to return in a paginated response. |
| maxResults | String | False | The maximum number of items to include in each page of a paginated response. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListAllowListsResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### POST
<a name="allow-listspost"></a>

**Operation ID:** `CreateAllowList`

Creates and defines the settings for an allow list.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateAllowListResponse | The request succeeded. The specified allow list was created. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="allow-lists-schemas"></a>

### Request bodies
<a name="allow-lists-request-examples"></a>

#### POST schema
<a name="allow-lists-request-body-post-example"></a>

```
{
  "clientToken": "string",
  "criteria": {
    "regex": "string",
    "s3WordsList": {
      "bucketName": "string",
      "objectKey": "string"
    }
  },
  "description": "string",
  "name": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="allow-lists-response-examples"></a>

#### ListAllowListsResponse schema
<a name="allow-lists-response-body-listallowlistsresponse-example"></a>

```
{
  "allowLists": [
    {
      "arn": "string",
      "createdAt": "string",
      "description": "string",
      "id": "string",
      "name": "string",
      "updatedAt": "string"
    }
  ],
  "nextToken": "string"
}
```

#### CreateAllowListResponse schema
<a name="allow-lists-response-body-createallowlistresponse-example"></a>

```
{
  "arn": "string",
  "id": "string"
}
```

#### ValidationException schema
<a name="allow-lists-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="allow-lists-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="allow-lists-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="allow-lists-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="allow-lists-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="allow-lists-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="allow-lists-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="allow-lists-properties"></a>

### AccessDeniedException
<a name="allow-lists-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### AllowListCriteria
<a name="allow-lists-model-allowlistcriteria"></a>

Specifies the criteria for an allow list. The criteria must specify a regular expression (`regex`) or an S3 object (`s3WordsList`). It can't specify both.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| regex | string<br />Pattern: `^[\s\S]+$`<br />MinLength: 1<br />MaxLength: 512 | False | The regular expression (*regex*) that defines the text pattern to ignore. The expression can contain as many as 512 characters. |
| s3WordsList | [S3WordsList](#allow-lists-model-s3wordslist) | False | The location and name of the S3 object that lists specific text to ignore. |

### AllowListSummary
<a name="allow-lists-model-allowlistsummary"></a>

Provides a subset of information about an allow list.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:(aws\|aws-cn\|aws-us-gov):macie2:[a-z1-9-]{9,20}:\d{12}:allow-list\/[a-z0-9]{22}$`<br />MinLength: 71<br />MaxLength: 89 | False | The Amazon Resource Name (ARN) of the allow list. |
| createdAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the allow list was created in Amazon Macie. |
| description | string<br />Pattern: `^[\s\S]+$`<br />MinLength: 1<br />MaxLength: 512 | False | The custom description of the allow list. |
| id | string<br />Pattern: `^[a-z0-9]{22}$`<br />MinLength: 22<br />MaxLength: 22 | False | The unique identifier for the allow list. |
| name | string<br />Pattern: `^.+$`<br />MinLength: 1<br />MaxLength: 128 | False | The custom name of the allow list. |
| updatedAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the allow list's settings were most recently changed in Amazon Macie. |

### ConflictException
<a name="allow-lists-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### CreateAllowListRequest
<a name="allow-lists-model-createallowlistrequest"></a>

Specifies the settings for an allow list. When Amazon Macie processes the request, Macie tests the list's criteria. If the criteria specify a regular expression that Macie can't compile or an S3 object that Macie can't retrieve or parse, an error occurs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientToken | string | True | A unique, case-sensitive token that you provide to ensure the idempotency of the request. |
| criteria | [AllowListCriteria](#allow-lists-model-allowlistcriteria) | True | The criteria that specify the text or text pattern to ignore. The criteria can be the location and name of an S3 object that lists specific text to ignore (`s3WordsList`), or a regular expression (`regex`) that defines a text pattern to ignore. |
| description | string<br />Pattern: `^[\s\S]+$`<br />MinLength: 1<br />MaxLength: 512 | False | A custom description of the allow list. The description can contain as many as 512 characters. |
| name | string<br />Pattern: `^.+$`<br />MinLength: 1<br />MaxLength: 128 | True | A custom name for the allow list. The name can contain as many as 128 characters. |
| tags | [TagMap](#allow-lists-model-tagmap) | False | A map of key-value pairs that specifies the tags to associate with the allow list.<br />An allow list can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters. |

### CreateAllowListResponse
<a name="allow-lists-model-createallowlistresponse"></a>

Provides information about an allow list that was created in response to a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:(aws\|aws-cn\|aws-us-gov):macie2:[a-z1-9-]{9,20}:\d{12}:allow-list\/[a-z0-9]{22}$`<br />MinLength: 71<br />MaxLength: 89 | True | The Amazon Resource Name (ARN) of the allow list. |
| id | string<br />Pattern: `^[a-z0-9]{22}$`<br />MinLength: 22<br />MaxLength: 22 | True | The unique identifier for the allow list. |

### InternalServerException
<a name="allow-lists-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ListAllowListsResponse
<a name="allow-lists-model-listallowlistsresponse"></a>

Provides the results of a request for information about allow lists.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| allowLists | Array of type [AllowListSummary](#allow-lists-model-allowlistsummary) | False | An array of objects, one for each allow list. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### ResourceNotFoundException
<a name="allow-lists-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### S3WordsList
<a name="allow-lists-model-s3wordslist"></a>

Provides information about an S3 object that lists specific text to ignore.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketName | string<br />Pattern: `^[A-Za-z0-9.\-_]{3,255}$`<br />MinLength: 3<br />MaxLength: 255 | True | The full name of the S3 bucket that contains the object. |
| objectKey | string<br />Pattern: `^[\s\S]+$`<br />MinLength: 1<br />MaxLength: 1024 | True | The full name (key) of the object. |

### ServiceQuotaExceededException
<a name="allow-lists-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### TagMap
<a name="allow-lists-model-tagmap"></a>

A string-to-string map of key-value pairs that specifies the tags (keys and values) for an Amazon Macie resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### ThrottlingException
<a name="allow-lists-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="allow-lists-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="allow-lists-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListAllowLists
<a name="ListAllowLists-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListAllowLists)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListAllowLists)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListAllowLists)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListAllowLists)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListAllowLists)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListAllowLists)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListAllowLists)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListAllowLists)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/ListAllowLists)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListAllowLists)

### CreateAllowList
<a name="CreateAllowList-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/CreateAllowList)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/CreateAllowList)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/CreateAllowList)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/CreateAllowList)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/CreateAllowList)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/CreateAllowList)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/CreateAllowList)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/CreateAllowList)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/CreateAllowList)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/CreateAllowList)
