---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/allow-lists-id.html
---

# Allow List
<a name="allow-lists-id"></a>

The Allow List resource provides access to existing allow lists for your Amazon Macie account. In Macie, an allow list defines specific text or a text pattern that you want Macie to ignore when it inspects a data source for sensitive data. If data matches text or a text pattern in an allow list, Macie doesn't report the data. This is the case even if the data matches the criteria of a managed data identifier or a custom data identifier. You can create and use allow lists in all the AWS Regions where Macie is currently available except the Asia Pacific (Osaka) Region.

Macie supports two types of allow lists. An allow list can be a line-delimited plaintext file that lists specific text to ignore. For this type of list (`s3WordsList`), you create the list by using a text editor, store the list in an Amazon Simple Storage Service (Amazon S3) general purpose bucket, and then configure settings for Macie to access the list in the bucket. Alternatively, an allow list can specify a regular expression (*regex*) that defines a text pattern to ignore. For this type of list (`regex`), you create and store the regex and all other list settings in Macie. For more information, see [Defining sensitive data exceptions with allow lists](https://docs.aws.amazon.com/macie/latest/user/allow-lists.html) in the *Amazon Macie User Guide*.

You can use the Allow List resource to retrieve detailed information about an allow list, including the current status of the list. If a list is stored in an S3 bucket, the list's status indicates whether Macie can retrieve and parse the list. You can also use the Allow List resource to update the settings for an allow list or to delete an allow list from Macie.

To use this resource, you have to specify the unique identifier for the allow list that your request applies to. To find this identifier, use the [Allow Lists](allow-lists.md) resource.

## URI
<a name="allow-lists-id-url"></a>

`/allow-lists/{{id}}`

## HTTP methods
<a name="allow-lists-id-http-methods"></a>

### DELETE
<a name="allow-lists-iddelete"></a>

**Operation ID:** `DeleteAllowList`

Deletes an allow list.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| ignoreJobChecks | String | False | Specifies whether to force deletion of the allow list, even if active classification jobs are configured to use the list.<br />When you try to delete an allow list, Amazon Macie checks for classification jobs that use the list and have a status other than `COMPLETE` or `CANCELLED`. By default, Macie rejects your request if any jobs meet these criteria. To skip these checks and delete the list, set this value to `true`. To delete the list only if no active jobs are configured to use it, set this value to `false`. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty Schema | The request succeeded. The allow list was deleted and there isn't any content to include in the body of the response (No Content). |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### GET
<a name="allow-lists-idget"></a>

**Operation ID:** `GetAllowList`

Retrieves the settings and status of an allow list.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetAllowListResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### PUT
<a name="allow-lists-idput"></a>

**Operation ID:** `UpdateAllowList`

Updates the settings for an allow list.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateAllowListResponse | The request succeeded. The settings for the allow list were updated. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="allow-lists-id-schemas"></a>

### Request bodies
<a name="allow-lists-id-request-examples"></a>

#### PUT schema
<a name="allow-lists-id-request-body-put-example"></a>

```
{
  "criteria": {
    "regex": "string",
    "s3WordsList": {
      "bucketName": "string",
      "objectKey": "string"
    }
  },
  "description": "string",
  "name": "string"
}
```

### Response bodies
<a name="allow-lists-id-response-examples"></a>

#### Empty Schema schema
<a name="allow-lists-id-response-body-empty-example"></a>

```
{
}
```

#### GetAllowListResponse schema
<a name="allow-lists-id-response-body-getallowlistresponse-example"></a>

```
{
  "arn": "string",
  "createdAt": "string",
  "criteria": {
    "regex": "string",
    "s3WordsList": {
      "bucketName": "string",
      "objectKey": "string"
    }
  },
  "description": "string",
  "id": "string",
  "name": "string",
  "status": {
    "code": enum,
    "description": "string"
  },
  "tags": {
  },
  "updatedAt": "string"
}
```

#### UpdateAllowListResponse schema
<a name="allow-lists-id-response-body-updateallowlistresponse-example"></a>

```
{
  "arn": "string",
  "id": "string"
}
```

#### ValidationException schema
<a name="allow-lists-id-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="allow-lists-id-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="allow-lists-id-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="allow-lists-id-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="allow-lists-id-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="allow-lists-id-properties"></a>

### AccessDeniedException
<a name="allow-lists-id-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### AllowListCriteria
<a name="allow-lists-id-model-allowlistcriteria"></a>

Specifies the criteria for an allow list. The criteria must specify a regular expression (`regex`) or an S3 object (`s3WordsList`). It can't specify both.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| regex | string<br />Pattern: `^[\s\S]+$`<br />MinLength: 1<br />MaxLength: 512 | False | The regular expression (*regex*) that defines the text pattern to ignore. The expression can contain as many as 512 characters. |
| s3WordsList | [S3WordsList](#allow-lists-id-model-s3wordslist) | False | The location and name of the S3 object that lists specific text to ignore. |

### AllowListStatus
<a name="allow-lists-id-model-allowliststatus"></a>

Provides information about the current status of an allow list, which indicates whether Amazon Macie can access and use the list's criteria.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| code | [AllowListStatusCode](#allow-lists-id-model-allowliststatuscode) | True | The current status of the allow list. If the list's criteria specify a regular expression (`regex`), this value is typically `OK`. Amazon Macie can compile the expression.<br />If the list's criteria specify an S3 object, possible values are:+  `OK` - Macie can retrieve and parse the contents of the object. <br />+  `S3_OBJECT_ACCESS_DENIED` - Macie isn't allowed to access the object or the object is encrypted with a customer managed AWS KMS key that Macie isn't allowed to use. Check the bucket policy and other permissions settings for the bucket and the object. If the object is encrypted, make sure it's encrypted with a key that Macie is allowed to use. <br />+  `S3_OBJECT_EMPTY` - Macie can retrieve the object but the object doesn't contain any content. Verify that the object contains the correct entries. Also verify that the list's criteria specify the correct bucket and object names. <br />+  `S3_OBJECT_NOT_FOUND` - The object doesn't exist in Amazon S3. Ensure that the list's criteria specify the correct bucket and object names. <br />+  `S3_OBJECT_OVERSIZE` - Macie can retrieve the object. However, the object contains too many entries or its storage size exceeds the quota for an allow list. Try breaking the list into multiple files and make sure each file doesn't exceed any quotas. Then configure list settings in Macie for each file. <br />+  `S3_THROTTLED` - Amazon S3 throttled the request to retrieve the object. Wait a few minutes and then try again. <br />+  `S3_USER_ACCESS_DENIED` - Amazon S3 denied the request to retrieve the object. If the specified object exists, you're not allowed to access it or it's encrypted with an AWS KMS key that you're not allowed to use. Work with your AWS administrator to confirm that the list's criteria specify the correct bucket and object names, and you have read access to the bucket and the object. If the object is encrypted, also make sure it's encrypted with a key that you're allowed to use. <br />+  `UNKNOWN_ERROR` - A transient or internal error occurred when Macie attempted to retrieve or parse the object. Wait a few minutes and then try again. A list can also have this status if it's encrypted with a key that Amazon S3 and Macie can't access or use.  |
| description | string<br />Pattern: `^[\s\S]+$`<br />MinLength: 1<br />MaxLength: 1024 | False | A brief description of the status of the allow list. Amazon Macie uses this value to provide additional information about an error that occurred when Macie tried to access and use the list's criteria. |

### AllowListStatusCode
<a name="allow-lists-id-model-allowliststatuscode"></a>

Indicates the current status of an allow list. Depending on the type of criteria that the list specifies, possible values are:
+ `OK`
+ `S3_OBJECT_NOT_FOUND`
+ `S3_USER_ACCESS_DENIED`
+ `S3_OBJECT_ACCESS_DENIED`
+ `S3_THROTTLED`
+ `S3_OBJECT_OVERSIZE`
+ `S3_OBJECT_EMPTY`
+ `UNKNOWN_ERROR`

### Empty
<a name="allow-lists-id-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### GetAllowListResponse
<a name="allow-lists-id-model-getallowlistresponse"></a>

Provides information about the settings and status of an allow list.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:(aws\|aws-cn\|aws-us-gov):macie2:[a-z1-9-]{9,20}:\d{12}:allow-list\/[a-z0-9]{22}$`<br />MinLength: 71<br />MaxLength: 89 | True | The Amazon Resource Name (ARN) of the allow list. |
| createdAt | string<br />Format: date-time | True | The date and time, in UTC and extended ISO 8601 format, when the allow list was created in Amazon Macie. |
| criteria | [AllowListCriteria](#allow-lists-id-model-allowlistcriteria) | False | The criteria that specify the text or text pattern to ignore. The criteria can be the location and name of an S3 object that lists specific text to ignore (`s3WordsList`), or a regular expression (`regex`) that defines a text pattern to ignore. |
| description | string<br />Pattern: `^[\s\S]+$`<br />MinLength: 1<br />MaxLength: 512 | False | The custom description of the allow list. |
| id | string<br />Pattern: `^[a-z0-9]{22}$`<br />MinLength: 22<br />MaxLength: 22 | True | The unique identifier for the allow list. |
| name | string<br />Pattern: `^.+$`<br />MinLength: 1<br />MaxLength: 128 | True | The custom name of the allow list. |
| status | [AllowListStatus](#allow-lists-id-model-allowliststatus) | False | The current status of the allow list, which indicates whether Amazon Macie can access and use the list's criteria. |
| tags | [TagMap](#allow-lists-id-model-tagmap) | False | A map of key-value pairs that specifies which tags (keys and values) are associated with the allow list. |
| updatedAt | string<br />Format: date-time | True | The date and time, in UTC and extended ISO 8601 format, when the allow list's settings were most recently changed in Amazon Macie. |

### InternalServerException
<a name="allow-lists-id-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="allow-lists-id-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### S3WordsList
<a name="allow-lists-id-model-s3wordslist"></a>

Provides information about an S3 object that lists specific text to ignore.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketName | string<br />Pattern: `^[A-Za-z0-9.\-_]{3,255}$`<br />MinLength: 3<br />MaxLength: 255 | True | The full name of the S3 bucket that contains the object. |
| objectKey | string<br />Pattern: `^[\s\S]+$`<br />MinLength: 1<br />MaxLength: 1024 | True | The full name (key) of the object. |

### TagMap
<a name="allow-lists-id-model-tagmap"></a>

A string-to-string map of key-value pairs that specifies the tags (keys and values) for an Amazon Macie resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### ThrottlingException
<a name="allow-lists-id-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UpdateAllowListRequest
<a name="allow-lists-id-model-updateallowlistrequest"></a>

Changes the settings for an allow list. If you change the list's criteria, Amazon Macie tests the new criteria when it processes your request. If the criteria specify a regular expression that Macie can't compile or an S3 object that Macie can't retrieve or parse, an error occurs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| criteria | [AllowListCriteria](#allow-lists-id-model-allowlistcriteria) | True | The criteria that specify the text or text pattern to ignore. The criteria can be the location and name of an S3 object that lists specific text to ignore (`s3WordsList`), or a regular expression that defines a text pattern to ignore (`regex`).<br />You can change a list's underlying criteria, such as the name of the S3 object or the regular expression to use. However, you can't change the type from `s3WordsList` to `regex` or the other way around. |
| description | string<br />Pattern: `^[\s\S]+$`<br />MinLength: 1<br />MaxLength: 512 | False | A custom description of the allow list. The description can contain as many as 512 characters. |
| name | string<br />Pattern: `^.+$`<br />MinLength: 1<br />MaxLength: 128 | True | A custom name for the allow list. The name can contain as many as 128 characters. |

### UpdateAllowListResponse
<a name="allow-lists-id-model-updateallowlistresponse"></a>

Provides information about an allow list whose settings were changed in response to a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:(aws\|aws-cn\|aws-us-gov):macie2:[a-z1-9-]{9,20}:\d{12}:allow-list\/[a-z0-9]{22}$`<br />MinLength: 71<br />MaxLength: 89 | True | The Amazon Resource Name (ARN) of the allow list. |
| id | string<br />Pattern: `^[a-z0-9]{22}$`<br />MinLength: 22<br />MaxLength: 22 | True | The unique identifier for the allow list. |

### ValidationException
<a name="allow-lists-id-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="allow-lists-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteAllowList
<a name="DeleteAllowList-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/DeleteAllowList)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/DeleteAllowList)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/DeleteAllowList)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/DeleteAllowList)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/DeleteAllowList)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/DeleteAllowList)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/DeleteAllowList)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/DeleteAllowList)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/DeleteAllowList)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/DeleteAllowList)

### GetAllowList
<a name="GetAllowList-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetAllowList)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetAllowList)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetAllowList)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetAllowList)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetAllowList)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetAllowList)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetAllowList)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetAllowList)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/GetAllowList)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetAllowList)

### UpdateAllowList
<a name="UpdateAllowList-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/UpdateAllowList)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/UpdateAllowList)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/UpdateAllowList)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/UpdateAllowList)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/UpdateAllowList)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/UpdateAllowList)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/UpdateAllowList)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/UpdateAllowList)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/UpdateAllowList)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/UpdateAllowList)
