---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/invitations-count.html
---

# Invitation Count
<a name="invitations-count"></a>

In Amazon Macie, an *invitation*, also referred to as a *membership invitation*, is a request to become a member of an organization in Macie. An *organization* is a set of Macie accounts that are centrally managed as a group of related accounts. For more information, see [Managing multiple accounts](https://docs.aws.amazon.com/macie/latest/user/macie-accounts.html) in the *Amazon Macie User Guide*.

You can use the Invitation Count resource to retrieve the total number of Macie membership invitations that you've received and haven't deleted. If you accepted an invitation to join your current organization, this number doesn't include that invitation.

## URI
<a name="invitations-count-url"></a>

`/invitations/count`

## HTTP methods
<a name="invitations-count-http-methods"></a>

### GET
<a name="invitations-countget"></a>

**Operation ID:** `GetInvitationsCount`

Retrieves the count of Amazon Macie membership invitations that were received by an account.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetInvitationsCountResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="invitations-count-schemas"></a>

### Response bodies
<a name="invitations-count-response-examples"></a>

#### GetInvitationsCountResponse schema
<a name="invitations-count-response-body-getinvitationscountresponse-example"></a>

```
{
  "invitationsCount": integer
}
```

#### ValidationException schema
<a name="invitations-count-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="invitations-count-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="invitations-count-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="invitations-count-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="invitations-count-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="invitations-count-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="invitations-count-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="invitations-count-properties"></a>

### AccessDeniedException
<a name="invitations-count-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="invitations-count-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### GetInvitationsCountResponse
<a name="invitations-count-model-getinvitationscountresponse"></a>

Provides the count of all the Amazon Macie membership invitations that were received by an account, not including the currently accepted invitation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invitationsCount | integer<br />Format: int64 | False | The total number of invitations that were received by the account, not including the currently accepted invitation. |

### InternalServerException
<a name="invitations-count-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="invitations-count-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="invitations-count-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="invitations-count-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="invitations-count-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="invitations-count-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetInvitationsCount
<a name="GetInvitationsCount-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetInvitationsCount)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetInvitationsCount)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetInvitationsCount)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetInvitationsCount)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetInvitationsCount)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetInvitationsCount)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetInvitationsCount)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetInvitationsCount)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetInvitationsCount)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetInvitationsCount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Macie. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query macie` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
