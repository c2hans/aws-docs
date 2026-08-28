---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/invitations-accept.html
---

# Invitation Acceptance
<a name="invitations-accept"></a>

In Amazon Macie, an *invitation*, also referred to as a *membership invitation*, is a request to become a member of an organization in Macie. An *organization* is a set of Macie accounts that are centrally managed as a group of related accounts. For more information, see [Managing multiple accounts](https://docs.aws.amazon.com/macie/latest/user/macie-accounts.html) in the *Amazon Macie User Guide*.

You can use the Invitation Acceptance resource to access membership invitations that you've received and haven't responded to, and to accept one of those invitations. To accept an invitation, you have to specify the unique identifier for the invitation and the account ID for the AWS account that sent the invitation. To find these IDs, you can use the [Invitation List](invitations.md) resource.

## URI
<a name="invitations-accept-url"></a>

`/invitations/accept`

## HTTP methods
<a name="invitations-accept-http-methods"></a>

### POST
<a name="invitations-acceptpost"></a>

**Operation ID:** `AcceptInvitation`

Accepts an Amazon Macie membership invitation that was received from a specific account.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty Schema | The request succeeded and there isn't any content to include in the body of the response (No Content). |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="invitations-accept-schemas"></a>

### Request bodies
<a name="invitations-accept-request-examples"></a>

#### POST schema
<a name="invitations-accept-request-body-post-example"></a>

```
{
  "administratorAccountId": "string",
  "invitationId": "string",
  "masterAccount": "string"
}
```

### Response bodies
<a name="invitations-accept-response-examples"></a>

#### Empty Schema schema
<a name="invitations-accept-response-body-empty-example"></a>

```
{
}
```

#### ValidationException schema
<a name="invitations-accept-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="invitations-accept-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="invitations-accept-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="invitations-accept-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="invitations-accept-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="invitations-accept-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="invitations-accept-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="invitations-accept-properties"></a>

### AcceptInvitationRequest
<a name="invitations-accept-model-acceptinvitationrequest"></a>

Specifies an Amazon Macie membership invitation to accept. In the request, you have to specify the ID for the AWS account that sent the invitation. Otherwise, a validation error occurs. To specify this ID, we recommend that you use the `administratorAccountId` property instead of the `masterAccount` property. The `masterAccount` property has been deprecated and is retained only for backward compatibility.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| administratorAccountId | string | False | The AWS account ID for the account that sent the invitation. |
| invitationId | string | True | The unique identifier for the invitation to accept. |
| masterAccount | string | False | (Deprecated) The AWS account ID for the account that sent the invitation. This property has been replaced by the `administratorAccountId` property and is retained only for backward compatibility. |

### AccessDeniedException
<a name="invitations-accept-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="invitations-accept-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Empty
<a name="invitations-accept-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### InternalServerException
<a name="invitations-accept-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="invitations-accept-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="invitations-accept-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="invitations-accept-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="invitations-accept-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="invitations-accept-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### AcceptInvitation
<a name="AcceptInvitation-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/AcceptInvitation)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/AcceptInvitation)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/AcceptInvitation)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/AcceptInvitation)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/AcceptInvitation)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/AcceptInvitation)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/AcceptInvitation)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/AcceptInvitation)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/AcceptInvitation)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/AcceptInvitation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Macie. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query macie` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
