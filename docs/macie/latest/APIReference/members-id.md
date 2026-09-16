---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/members-id.html
---

# Member
<a name="members-id"></a>

The Member resource provides information about an individual account that's currently associated with your Amazon Macie account, typically a Macie administrator account. This information includes details such as the AWS account ID for the account and the current status of the relationship between your accounts. If you sent a Macie membership invitation to an account, this resource also indicates when you sent that invitation and the email address that you sent it to. For information about the relationship between administrator and member accounts, see [Managing multiple accounts](https://docs.aws.amazon.com/macie/latest/user/macie-accounts.html) in the *Amazon Macie User Guide*.

You can use the Member resource to retrieve information about an account that's associated with your Macie account. You can also use this resource to delete an existing association between your Macie account and another account. To use this resource, you have to specify the AWS account ID for the account that your request applies to. To find this ID, you can use the [Members](members.md) resource.

## URI
<a name="members-id-url"></a>

`/members/{{id}}`

## HTTP methods
<a name="members-id-http-methods"></a>

### DELETE
<a name="members-iddelete"></a>

**Operation ID:** `DeleteMember`

Deletes the association between an Amazon Macie administrator account and an account.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty Schema | The request succeeded. The association was deleted and there isn't any content to include in the body of the response (No Content). |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### GET
<a name="members-idget"></a>

**Operation ID:** `GetMember`

Retrieves information about an account that's associated with an Amazon Macie administrator account.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetMemberResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="members-id-schemas"></a>

### Response bodies
<a name="members-id-response-examples"></a>

#### Empty Schema schema
<a name="members-id-response-body-empty-example"></a>

```
{
}
```

#### GetMemberResponse schema
<a name="members-id-response-body-getmemberresponse-example"></a>

```
{
  "accountId": "string",
  "administratorAccountId": "string",
  "arn": "string",
  "email": "string",
  "invitedAt": "string",
  "masterAccountId": "string",
  "relationshipStatus": enum,
  "tags": {
  },
  "updatedAt": "string"
}
```

#### ValidationException schema
<a name="members-id-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="members-id-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="members-id-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="members-id-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="members-id-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="members-id-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="members-id-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="members-id-properties"></a>

### AccessDeniedException
<a name="members-id-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="members-id-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Empty
<a name="members-id-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### GetMemberResponse
<a name="members-id-model-getmemberresponse"></a>

Provides information about an account that's associated with an Amazon Macie administrator account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The AWS account ID for the account. |
| administratorAccountId | string | False | The AWS account ID for the administrator account. |
| arn | string | False | The Amazon Resource Name (ARN) of the account. |
| email | string | False | The email address for the account. This value is null if the account is associated with the administrator account through AWS Organizations. |
| invitedAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when an Amazon Macie membership invitation was last sent to the account. This value is null if a Macie membership invitation hasn't been sent to the account. |
| masterAccountId | string | False | (Deprecated) The AWS account ID for the administrator account. This property has been replaced by the `administratorAccountId` property and is retained only for backward compatibility. |
| relationshipStatus | [RelationshipStatus](#members-id-model-relationshipstatus) | False | The current status of the relationship between the account and the administrator account. |
| tags | [TagMap](#members-id-model-tagmap) | False | A map of key-value pairs that specifies which tags (keys and values) are associated with the account in Amazon Macie. |
| updatedAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, of the most recent change to the status of the relationship between the account and the administrator account. |

### InternalServerException
<a name="members-id-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### RelationshipStatus
<a name="members-id-model-relationshipstatus"></a>

The current status of the relationship between an account and an associated Amazon Macie administrator account. Possible values are:
+ `Enabled`
+ `Paused`
+ `Invited`
+ `Created`
+ `Removed`
+ `Resigned`
+ `EmailVerificationInProgress`
+ `EmailVerificationFailed`
+ `RegionDisabled`
+ `AccountSuspended`

### ResourceNotFoundException
<a name="members-id-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="members-id-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### TagMap
<a name="members-id-model-tagmap"></a>

A string-to-string map of key-value pairs that specifies the tags (keys and values) for an Amazon Macie resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### ThrottlingException
<a name="members-id-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="members-id-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="members-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteMember
<a name="DeleteMember-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/DeleteMember)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/DeleteMember)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/DeleteMember)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/DeleteMember)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/DeleteMember)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/DeleteMember)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/DeleteMember)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/DeleteMember)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/DeleteMember)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/DeleteMember)

### GetMember
<a name="GetMember-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetMember)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetMember)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetMember)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetMember)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetMember)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetMember)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetMember)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetMember)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/GetMember)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetMember)
