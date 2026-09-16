---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/master-disassociate.html
---

# Master Disassociation
<a name="master-disassociate"></a>

This resource has been deprecated and is retained only for backward compatibility. If you joined an organization by accepting an Amazon Macie membership invitation, use the [Administrator Disassociation](administrator-disassociate.md) resource instead of this resource to disassociate your Macie account from its Macie administrator account. To learn more about disassociating your account from its administrator account, see [Managing your membership in an organization](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-invitations-membership-manage.html) in the *Amazon Macie User Guide*.

## URI
<a name="master-disassociate-url"></a>

`/master/disassociate`

## HTTP methods
<a name="master-disassociate-http-methods"></a>

### POST
<a name="master-disassociatepost"></a>

**Operation ID:** `DisassociateFromMasterAccount`

(Deprecated) Disassociates a member account from its Amazon Macie administrator account. This operation has been replaced by the [DisassociateFromAdministratorAccount](administrator-disassociate.md#DisassociateFromAdministratorAccount) operation.

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
<a name="master-disassociate-schemas"></a>

### Response bodies
<a name="master-disassociate-response-examples"></a>

#### Empty Schema schema
<a name="master-disassociate-response-body-empty-example"></a>

```
{
}
```

#### ValidationException schema
<a name="master-disassociate-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="master-disassociate-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="master-disassociate-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="master-disassociate-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="master-disassociate-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="master-disassociate-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="master-disassociate-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="master-disassociate-properties"></a>

### AccessDeniedException
<a name="master-disassociate-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="master-disassociate-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Empty
<a name="master-disassociate-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### InternalServerException
<a name="master-disassociate-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="master-disassociate-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="master-disassociate-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="master-disassociate-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="master-disassociate-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="master-disassociate-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DisassociateFromMasterAccount
<a name="DisassociateFromMasterAccount-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/DisassociateFromMasterAccount)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/DisassociateFromMasterAccount)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/DisassociateFromMasterAccount)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/DisassociateFromMasterAccount)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/DisassociateFromMasterAccount)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/DisassociateFromMasterAccount)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/DisassociateFromMasterAccount)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/DisassociateFromMasterAccount)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/DisassociateFromMasterAccount)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/DisassociateFromMasterAccount)
