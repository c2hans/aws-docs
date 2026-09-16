---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/macie-members-id.html
---

# Member Status
<a name="macie-members-id"></a>

The Member Status resource provides access to the status of Amazon Macie for a member account in an organization. If you're the delegated Macie administrator for an organization in AWS Organizations, you can use this resource to manage the status of Macie for a member account in your organization. For more information, see [Managing multiple accounts with AWS Organizations](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao.html) in the *Amazon Macie User Guide*.

If you suspend Macie for an account, Macie stops performing all activities and cancels all classification jobs for that account. However, the service retains the session identifier, settings, and resources for the account. For example, the account's findings remain intact and aren't affected for up to 90 days. If you later re-enable Macie for the account, Macie resumes all activities for the account. For more information, see [Managing member accounts for an organization](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao-administer.html) in the *Amazon Macie User Guide*.

## URI
<a name="macie-members-id-url"></a>

`/macie/members/{{id}}`

## HTTP methods
<a name="macie-members-id-http-methods"></a>

### PATCH
<a name="macie-members-idpatch"></a>

**Operation ID:** `UpdateMemberSession`

Enables an Amazon Macie administrator to suspend or re-enable Macie for a member account.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

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
<a name="macie-members-id-schemas"></a>

### Request bodies
<a name="macie-members-id-request-examples"></a>

#### PATCH schema
<a name="macie-members-id-request-body-patch-example"></a>

```
{
  "status": enum
}
```

### Response bodies
<a name="macie-members-id-response-examples"></a>

#### Empty Schema schema
<a name="macie-members-id-response-body-empty-example"></a>

```
{
}
```

#### ValidationException schema
<a name="macie-members-id-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="macie-members-id-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="macie-members-id-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="macie-members-id-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="macie-members-id-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="macie-members-id-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="macie-members-id-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="macie-members-id-properties"></a>

### AccessDeniedException
<a name="macie-members-id-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="macie-members-id-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Empty
<a name="macie-members-id-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### InternalServerException
<a name="macie-members-id-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### MacieStatus
<a name="macie-members-id-model-maciestatus"></a>

The status of an Amazon Macie account. Valid values are:
+ `PAUSED`
+ `ENABLED`

### ResourceNotFoundException
<a name="macie-members-id-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="macie-members-id-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="macie-members-id-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UpdateMemberSessionRequest
<a name="macie-members-id-model-updatemembersessionrequest"></a>

Suspends (pauses) or re-enables Amazon Macie for a member account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| status | [MacieStatus](#macie-members-id-model-maciestatus) | True | Specifies the new status for the account. Valid values are: `ENABLED`, resume all Amazon Macie activities for the account; and, `PAUSED`, suspend all Macie activities for the account. |

### ValidationException
<a name="macie-members-id-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="macie-members-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateMemberSession
<a name="UpdateMemberSession-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/UpdateMemberSession)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/UpdateMemberSession)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/UpdateMemberSession)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/UpdateMemberSession)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/UpdateMemberSession)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/UpdateMemberSession)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/UpdateMemberSession)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/UpdateMemberSession)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/UpdateMemberSession)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/UpdateMemberSession)
