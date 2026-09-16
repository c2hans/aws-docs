---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/members-disassociate-id.html
---

# Member Disassociation
<a name="members-disassociate-id"></a>

The Member Disassociation resource provides access to associations between an Amazon Macie administrator account and its member accounts. If you're a Macie administrator, you can use this resource to disassociate a member account from your account. For information about managing relationships between administrator and member accounts, see [Managing multiple accounts](https://docs.aws.amazon.com/macie/latest/user/macie-accounts.html) in the *Amazon Macie User Guide*.

To use this resource, you have to specify the AWS account ID for the member account to disassociate. To find this ID, you can use the [Members](members.md) resource.

If you have a member account and you want to disassociate your account from its Macie administrator account, use the [Administrator Disassociation](administrator-disassociate.md) resource.

## URI
<a name="members-disassociate-id-url"></a>

`/members/disassociate/{{id}}`

## HTTP methods
<a name="members-disassociate-id-http-methods"></a>

### POST
<a name="members-disassociate-idpost"></a>

**Operation ID:** `DisassociateMember`

Disassociates an Amazon Macie administrator account from a member account.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty Schema | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="members-disassociate-id-schemas"></a>

### Response bodies
<a name="members-disassociate-id-response-examples"></a>

#### Empty Schema schema
<a name="members-disassociate-id-response-body-empty-example"></a>

```
{
}
```

#### ValidationException schema
<a name="members-disassociate-id-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="members-disassociate-id-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="members-disassociate-id-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="members-disassociate-id-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="members-disassociate-id-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="members-disassociate-id-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="members-disassociate-id-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="members-disassociate-id-properties"></a>

### AccessDeniedException
<a name="members-disassociate-id-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="members-disassociate-id-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Empty
<a name="members-disassociate-id-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### InternalServerException
<a name="members-disassociate-id-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="members-disassociate-id-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="members-disassociate-id-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="members-disassociate-id-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="members-disassociate-id-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="members-disassociate-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DisassociateMember
<a name="DisassociateMember-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/DisassociateMember)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/DisassociateMember)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/DisassociateMember)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/DisassociateMember)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/DisassociateMember)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/DisassociateMember)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/DisassociateMember)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/DisassociateMember)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/DisassociateMember)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/DisassociateMember)
