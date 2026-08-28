---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/administrator.html
---

# Administrator
<a name="administrator"></a>

If your account is an Amazon Macie member account in an organization, the Administrator resource provides information about the Macie administrator account for your account. If you joined the organization by accepting a Macie membership invitation, this resource also provides information about that invitation. For information about the relationship between your account and its Macie administrator account, see [Managing multiple accounts](https://docs.aws.amazon.com/macie/latest/user/macie-accounts.html) in the *Amazon Macie User Guide*.

You can use the Administrator resource to retrieve information about the Macie administrator account for your account.

## URI
<a name="administrator-url"></a>

`/administrator`

## HTTP methods
<a name="administrator-http-methods"></a>

### GET
<a name="administratorget"></a>

**Operation ID:** `GetAdministratorAccount`

Retrieves information about the Amazon Macie administrator account for an account.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetAdministratorAccountResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="administrator-schemas"></a>

### Response bodies
<a name="administrator-response-examples"></a>

#### GetAdministratorAccountResponse schema
<a name="administrator-response-body-getadministratoraccountresponse-example"></a>

```
{
  "administrator": {
    "accountId": "string",
    "invitationId": "string",
    "invitedAt": "string",
    "relationshipStatus": enum
  }
}
```

#### ValidationException schema
<a name="administrator-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="administrator-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="administrator-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="administrator-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="administrator-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="administrator-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="administrator-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="administrator-properties"></a>

### AccessDeniedException
<a name="administrator-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="administrator-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### GetAdministratorAccountResponse
<a name="administrator-model-getadministratoraccountresponse"></a>

Provides information about the Amazon Macie administrator account for an account. If the accounts are associated by a Macie membership invitation, the response also provides information about that invitation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| administrator | [Invitation](#administrator-model-invitation) | False | The AWS account ID for the administrator account. If the accounts are associated by an Amazon Macie membership invitation, this object also provides details about the invitation that was sent to establish the relationship between the accounts. |

### InternalServerException
<a name="administrator-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Invitation
<a name="administrator-model-invitation"></a>

Provides information about an Amazon Macie membership invitation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The AWS account ID for the account that sent the invitation. |
| invitationId | string | False | The unique identifier for the invitation. |
| invitedAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the invitation was sent. |
| relationshipStatus | [RelationshipStatus](#administrator-model-relationshipstatus) | False | The status of the relationship between the account that sent the invitation and the account that received the invitation. |

### RelationshipStatus
<a name="administrator-model-relationshipstatus"></a>

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
<a name="administrator-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="administrator-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="administrator-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="administrator-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="administrator-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetAdministratorAccount
<a name="GetAdministratorAccount-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetAdministratorAccount)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetAdministratorAccount)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetAdministratorAccount)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetAdministratorAccount)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetAdministratorAccount)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetAdministratorAccount)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetAdministratorAccount)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetAdministratorAccount)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetAdministratorAccount)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetAdministratorAccount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Macie. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query macie` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
