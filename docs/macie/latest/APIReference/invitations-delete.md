---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/invitations-delete.html
---

# Invitation Deletion
<a name="invitations-delete"></a>

In Amazon Macie, an *invitation*, also referred to as a *membership invitation*, is a request to become a member of an organization in Macie. An *organization* is a set of Macie accounts that are centrally managed as a group of related accounts. For more information, see [Managing multiple accounts](https://docs.aws.amazon.com/macie/latest/user/macie-accounts.html) in the *Amazon Macie User Guide*.

You can use the Invitation Deletion resource to access membership invitations that you've received and declined, and to delete one or more of those invitations. If you accepted an invitation to join your current organization, you cannot delete that invitation.

To delete an invitation, you have to specify the account ID for the AWS account that sent the invitation. To find this ID, you can use the [Invitation List](invitations.md) resource.

## URI
<a name="invitations-delete-url"></a>

`/invitations/delete`

## HTTP methods
<a name="invitations-delete-http-methods"></a>

### POST
<a name="invitations-deletepost"></a>

**Operation ID:** `DeleteInvitations`

Deletes Amazon Macie membership invitations that were received from specific accounts.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DeleteInvitationsResponse | The request succeeded. Processing might not be complete. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="invitations-delete-schemas"></a>

### Request bodies
<a name="invitations-delete-request-examples"></a>

#### POST schema
<a name="invitations-delete-request-body-post-example"></a>

```
{
  "accountIds": [
    "string"
  ]
}
```

### Response bodies
<a name="invitations-delete-response-examples"></a>

#### DeleteInvitationsResponse schema
<a name="invitations-delete-response-body-deleteinvitationsresponse-example"></a>

```
{
  "unprocessedAccounts": [
    {
      "accountId": "string",
      "errorCode": enum,
      "errorMessage": "string"
    }
  ]
}
```

#### ValidationException schema
<a name="invitations-delete-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="invitations-delete-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="invitations-delete-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="invitations-delete-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="invitations-delete-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="invitations-delete-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="invitations-delete-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="invitations-delete-properties"></a>

### AccessDeniedException
<a name="invitations-delete-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="invitations-delete-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### DeleteInvitationsRequest
<a name="invitations-delete-model-deleteinvitationsrequest"></a>

Specifies one or more accounts that sent Amazon Macie membership invitations to delete.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountIds | Array of type string | True | An array that lists AWS account IDs, one for each account that sent an invitation to delete. |

### DeleteInvitationsResponse
<a name="invitations-delete-model-deleteinvitationsresponse"></a>

Provides information about unprocessed requests to delete Amazon Macie membership invitations that were received from specific accounts.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| unprocessedAccounts | Array of type [UnprocessedAccount](#invitations-delete-model-unprocessedaccount) | False | An array of objects, one for each account whose invitation hasn't been deleted. Each object identifies the account and explains why the request hasn't been processed for that account. |

### ErrorCode
<a name="invitations-delete-model-errorcode"></a>

The source of an issue or delay. Possible values are:
+ `ClientError`
+ `InternalError`

### InternalServerException
<a name="invitations-delete-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="invitations-delete-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="invitations-delete-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="invitations-delete-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UnprocessedAccount
<a name="invitations-delete-model-unprocessedaccount"></a>

Provides information about an account-related request that hasn't been processed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The AWS account ID for the account that the request applies to. |
| errorCode | [ErrorCode](#invitations-delete-model-errorcode) | False | The source of the issue or delay in processing the request. |
| errorMessage | string | False | The reason why the request hasn't been processed. |

### ValidationException
<a name="invitations-delete-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="invitations-delete-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteInvitations
<a name="DeleteInvitations-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/DeleteInvitations)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/DeleteInvitations)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/DeleteInvitations)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/DeleteInvitations)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/DeleteInvitations)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/DeleteInvitations)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/DeleteInvitations)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/DeleteInvitations)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/DeleteInvitations)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/DeleteInvitations)
