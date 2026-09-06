---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/members.html
---

# Members
<a name="members"></a>

The Members resource provides information about all the accounts that are currently associated with your Amazon Macie account, typically a Macie administrator account. For each account, this resource provides details such as the AWS account ID for the account and the current status of the relationship between your accounts. If you sent a Macie membership invitation to an account, this resource also indicates when you sent that invitation and the email address that you sent it to. For information about the relationship between administrator and member accounts, see [Managing multiple accounts](https://docs.aws.amazon.com/macie/latest/user/macie-accounts.html) in the *Amazon Macie User Guide*.

If you want to associate additional accounts with your Macie account, you can use this resource to do so. You can then invite those accounts to enable Macie and allow you to administer and manage Macie on their behalf. For more information, see [Managing multiple accounts by invitation](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-invitations.html) in the *Amazon Macie User Guide*.

You can use the Members resource to associate one or more accounts with your Macie account. You can also use this resource to retrieve information about the accounts that are currently associated with your Macie account.

## URI
<a name="members-url"></a>

`/members`

## HTTP methods
<a name="members-http-methods"></a>

### GET
<a name="membersget"></a>

**Operation ID:** `ListMembers`

Retrieves information about the accounts that are associated with an Amazon Macie administrator account.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| onlyAssociated | String | False | Specifies which accounts to include in the response, based on the status of an account's relationship with the administrator account. By default, the response includes only current member accounts. To include all accounts, set this value to `false`. |
| nextToken | String | False | The `nextToken` string that specifies which page of results to return in a paginated response. |
| maxResults | String | False | The maximum number of items to include in each page of a paginated response. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListMembersResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### POST
<a name="memberspost"></a>

**Operation ID:** `CreateMember`

Associates an account with an Amazon Macie administrator account.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateMemberResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="members-schemas"></a>

### Request bodies
<a name="members-request-examples"></a>

#### POST schema
<a name="members-request-body-post-example"></a>

```
{
  "account": {
    "accountId": "string",
    "email": "string"
  },
  "tags": {
  }
}
```

### Response bodies
<a name="members-response-examples"></a>

#### ListMembersResponse schema
<a name="members-response-body-listmembersresponse-example"></a>

```
{
  "members": [
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
  ],
  "nextToken": "string"
}
```

#### CreateMemberResponse schema
<a name="members-response-body-creatememberresponse-example"></a>

```
{
  "arn": "string"
}
```

#### ValidationException schema
<a name="members-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="members-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="members-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="members-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="members-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="members-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="members-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="members-properties"></a>

### AccessDeniedException
<a name="members-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### AccountDetail
<a name="members-model-accountdetail"></a>

Specifies the details of an account to associate with an Amazon Macie administrator account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | True | The AWS account ID for the account. |
| email | string | True | The email address for the account. |

### ConflictException
<a name="members-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### CreateMemberRequest
<a name="members-model-creatememberrequest"></a>

Specifies an AWS account to associate with an Amazon Macie administrator account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| account | [AccountDetail](#members-model-accountdetail) | True | The details of the account to associate with the administrator account. |
| tags | [TagMap](#members-model-tagmap) | False | A map of key-value pairs that specifies the tags to associate with the account in Amazon Macie.<br />An account can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters. |

### CreateMemberResponse
<a name="members-model-creatememberresponse"></a>

Provides information about a request to associate an account with an Amazon Macie administrator account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) of the account that was associated with the administrator account. |

### InternalServerException
<a name="members-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ListMembersResponse
<a name="members-model-listmembersresponse"></a>

Provides information about the accounts that are associated with an Amazon Macie administrator account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| members | Array of type [Member](#members-model-member) | False | An array of objects, one for each account that's associated with the administrator account and matches the criteria specified in the request. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### Member
<a name="members-model-member"></a>

Provides information about an account that's associated with an Amazon Macie administrator account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The AWS account ID for the account. |
| administratorAccountId | string | False | The AWS account ID for the administrator account. |
| arn | string | False | The Amazon Resource Name (ARN) of the account. |
| email | string | False | The email address for the account. This value is null if the account is associated with the administrator account through AWS Organizations. |
| invitedAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when an Amazon Macie membership invitation was last sent to the account. This value is null if a Macie membership invitation hasn't been sent to the account. |
| masterAccountId | string | False | (Deprecated) The AWS account ID for the administrator account. This property has been replaced by the `administratorAccountId` property and is retained only for backward compatibility. |
| relationshipStatus | [RelationshipStatus](#members-model-relationshipstatus) | False | The current status of the relationship between the account and the administrator account. |
| tags | [TagMap](#members-model-tagmap) | False | A map of key-value pairs that specifies which tags (keys and values) are associated with the account in Amazon Macie. |
| updatedAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, of the most recent change to the status of the relationship between the account and the administrator account. |

### RelationshipStatus
<a name="members-model-relationshipstatus"></a>

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
<a name="members-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="members-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### TagMap
<a name="members-model-tagmap"></a>

A string-to-string map of key-value pairs that specifies the tags (keys and values) for an Amazon Macie resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### ThrottlingException
<a name="members-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="members-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="members-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListMembers
<a name="ListMembers-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListMembers)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListMembers)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListMembers)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListMembers)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListMembers)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListMembers)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListMembers)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListMembers)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/ListMembers)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListMembers)

### CreateMember
<a name="CreateMember-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/CreateMember)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/CreateMember)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/CreateMember)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/CreateMember)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/CreateMember)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/CreateMember)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/CreateMember)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/CreateMember)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/CreateMember)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/CreateMember)
