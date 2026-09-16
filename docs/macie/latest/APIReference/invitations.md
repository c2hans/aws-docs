---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/invitations.html
---

# Invitation List
<a name="invitations"></a>

In Amazon Macie, an *invitation*, also referred to as a *membership invitation*, is a request to become a member of an organization in Macie. An *organization* is a set of Macie accounts that are centrally managed as a group of related accounts. For more information, see [Managing multiple accounts](https://docs.aws.amazon.com/macie/latest/user/macie-accounts.html) in the *Amazon Macie User Guide*.

You can use the Invitation List resource to retrieve information about all the Macie membership invitations that you've received and haven't deleted. For each invitation, this information includes:
+ The unique identifier for the invitation.
+ The account ID for the AWS account that sent the invitation.
+ The current status of the relationship between your account and the account that sent the invitation.

You can also use this resource to send a membership invitation to other AWS accounts. To send an invitation to another account, you first have to associate the account with your account. You can do this by using the [Members](members.md) resource.

## URI
<a name="invitations-url"></a>

`/invitations`

## HTTP methods
<a name="invitations-http-methods"></a>

### GET
<a name="invitationsget"></a>

**Operation ID:** `ListInvitations`

Retrieves information about Amazon Macie membership invitations that were received by an account.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The `nextToken` string that specifies which page of results to return in a paginated response. |
| maxResults | String | False | The maximum number of items to include in each page of a paginated response. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListInvitationsResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### POST
<a name="invitationspost"></a>

**Operation ID:** `CreateInvitations`

Sends an Amazon Macie membership invitation to one or more accounts.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateInvitationsResponse | The request succeeded. Processing might not be complete. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="invitations-schemas"></a>

### Request bodies
<a name="invitations-request-examples"></a>

#### POST schema
<a name="invitations-request-body-post-example"></a>

```
{
  "accountIds": [
    "string"
  ],
  "disableEmailNotification": boolean,
  "message": "string"
}
```

### Response bodies
<a name="invitations-response-examples"></a>

#### ListInvitationsResponse schema
<a name="invitations-response-body-listinvitationsresponse-example"></a>

```
{
  "invitations": [
    {
      "accountId": "string",
      "invitationId": "string",
      "invitedAt": "string",
      "relationshipStatus": enum
    }
  ],
  "nextToken": "string"
}
```

#### CreateInvitationsResponse schema
<a name="invitations-response-body-createinvitationsresponse-example"></a>

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
<a name="invitations-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="invitations-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="invitations-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="invitations-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="invitations-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="invitations-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="invitations-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="invitations-properties"></a>

### AccessDeniedException
<a name="invitations-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="invitations-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### CreateInvitationsRequest
<a name="invitations-model-createinvitationsrequest"></a>

Specifies the settings for an Amazon Macie membership invitation. When you send an invitation, Macie notifies the recipient by creating an AWS Health event for the recipient's account and, if Macie is already enabled for the account, displaying an **Accounts** badge and notification on the recipient's console. You can optionally notify the recipient by also sending the invitation as an email message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountIds | Array of type string | True | An array that lists AWS account IDs, one for each account to send the invitation to. |
| disableEmailNotification | boolean | False | Specifies whether to send the invitation as an email message. If this value is `false`, Amazon Macie sends the invitation (as an email message) to the email address that you specified for the recipient's account when you associated the account with your account. The default value is `false`. |
| message | string | False | Custom text to include in the email message that contains the invitation. The text can contain as many as 80 alphanumeric characters. |

### CreateInvitationsResponse
<a name="invitations-model-createinvitationsresponse"></a>

Provides information about an unprocessed request to send an Amazon Macie membership invitation to a specific account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| unprocessedAccounts | Array of type [UnprocessedAccount](#invitations-model-unprocessedaccount) | False | An array of objects, one for each account whose invitation hasn't been processed. Each object identifies the account and explains why the invitation hasn't been processed for the account. |

### ErrorCode
<a name="invitations-model-errorcode"></a>

The source of an issue or delay. Possible values are:
+ `ClientError`
+ `InternalError`

### InternalServerException
<a name="invitations-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Invitation
<a name="invitations-model-invitation"></a>

Provides information about an Amazon Macie membership invitation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The AWS account ID for the account that sent the invitation. |
| invitationId | string | False | The unique identifier for the invitation. |
| invitedAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the invitation was sent. |
| relationshipStatus | [RelationshipStatus](#invitations-model-relationshipstatus) | False | The status of the relationship between the account that sent the invitation and the account that received the invitation. |

### ListInvitationsResponse
<a name="invitations-model-listinvitationsresponse"></a>

Provides information about the Amazon Macie membership invitations that were received by an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invitations | Array of type [Invitation](#invitations-model-invitation) | False | An array of objects, one for each invitation that was received by the account. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### RelationshipStatus
<a name="invitations-model-relationshipstatus"></a>

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
<a name="invitations-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="invitations-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="invitations-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UnprocessedAccount
<a name="invitations-model-unprocessedaccount"></a>

Provides information about an account-related request that hasn't been processed.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The AWS account ID for the account that the request applies to. |
| errorCode | [ErrorCode](#invitations-model-errorcode) | False | The source of the issue or delay in processing the request. |
| errorMessage | string | False | The reason why the request hasn't been processed. |

### ValidationException
<a name="invitations-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="invitations-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListInvitations
<a name="ListInvitations-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListInvitations)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListInvitations)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListInvitations)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListInvitations)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListInvitations)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListInvitations)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListInvitations)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListInvitations)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/ListInvitations)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListInvitations)

### CreateInvitations
<a name="CreateInvitations-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/CreateInvitations)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/CreateInvitations)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/CreateInvitations)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/CreateInvitations)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/CreateInvitations)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/CreateInvitations)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/CreateInvitations)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/CreateInvitations)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/CreateInvitations)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/CreateInvitations)
