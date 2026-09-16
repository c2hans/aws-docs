---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/admin.html
---

# AWS Organizations - Macie Administrator
<a name="admin"></a>

The Macie Administrator resource for AWS Organizations provides settings for designating the delegated Amazon Macie administrator account for an organization in AWS Organizations. AWS Organizations is a global account management service that enables AWS administrators to consolidate and centrally manage multiple AWS accounts. For more information about this service, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html). For information about integrating Macie with AWS Organizations, see [Managing multiple accounts with AWS Organizations](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao.html) in the *Amazon Macie User Guide*.

If you're a user of the AWS Organizations management account for an organization, you can use this resource to designate the delegated Macie administrator account for your organization. You can also use this resource to retrieve information about and change that designation. Note that an organization can have only one delegated Macie administrator account at a time.

To use this resource, you must be a user of the AWS Organizations management account for your organization.

## URI
<a name="admin-url"></a>

`/admin`

## HTTP methods
<a name="admin-http-methods"></a>

### DELETE
<a name="admindelete"></a>

**Operation ID:** `DisableOrganizationAdminAccount`

Disables an account as the delegated Amazon Macie administrator account for an organization in AWS Organizations.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| adminAccountId | String | True | The AWS account ID of the delegated Amazon Macie administrator account. |

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

### GET
<a name="adminget"></a>

**Operation ID:** `ListOrganizationAdminAccounts`

Retrieves information about the delegated Amazon Macie administrator account for an organization in AWS Organizations.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The `nextToken` string that specifies which page of results to return in a paginated response. |
| maxResults | String | False | The maximum number of items to include in each page of a paginated response. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListOrganizationAdminAccountsResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### POST
<a name="adminpost"></a>

**Operation ID:** `EnableOrganizationAdminAccount`

Designates an account as the delegated Amazon Macie administrator account for an organization in AWS Organizations.

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
<a name="admin-schemas"></a>

### Request bodies
<a name="admin-request-examples"></a>

#### POST schema
<a name="admin-request-body-post-example"></a>

```
{
  "adminAccountId": "string",
  "clientToken": "string"
}
```

### Response bodies
<a name="admin-response-examples"></a>

#### Empty Schema schema
<a name="admin-response-body-empty-example"></a>

```
{
}
```

#### ListOrganizationAdminAccountsResponse schema
<a name="admin-response-body-listorganizationadminaccountsresponse-example"></a>

```
{
  "adminAccounts": [
    {
      "accountId": "string",
      "status": enum
    }
  ],
  "nextToken": "string"
}
```

#### ValidationException schema
<a name="admin-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="admin-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="admin-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="admin-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="admin-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="admin-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="admin-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="admin-properties"></a>

### AccessDeniedException
<a name="admin-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### AdminAccount
<a name="admin-model-adminaccount"></a>

Provides information about the delegated Amazon Macie administrator account for an organization in AWS Organizations.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The AWS account ID for the account. |
| status | [AdminStatus](#admin-model-adminstatus) | False | The current status of the account as the delegated Amazon Macie administrator account for the organization. |

### AdminStatus
<a name="admin-model-adminstatus"></a>

The current status of an account as the delegated Amazon Macie administrator account for an organization in AWS Organizations. Possible values are:
+ `ENABLED`
+ `DISABLING_IN_PROGRESS`

### ConflictException
<a name="admin-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Empty
<a name="admin-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### EnableOrganizationAdminAccountRequest
<a name="admin-model-enableorganizationadminaccountrequest"></a>

Specifies an account to designate as the delegated Amazon Macie administrator account for an organization in AWS Organizations. To submit this request, you must be a user of the AWS Organizations management account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adminAccountId | string | True | The AWS account ID for the account to designate as the delegated Amazon Macie administrator account for the organization. |
| clientToken | string | False | A unique, case-sensitive token that you provide to ensure the idempotency of the request. |

### InternalServerException
<a name="admin-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ListOrganizationAdminAccountsResponse
<a name="admin-model-listorganizationadminaccountsresponse"></a>

Provides information about the delegated Amazon Macie administrator accounts for an organization in AWS Organizations.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| adminAccounts | Array of type [AdminAccount](#admin-model-adminaccount) | False | An array of objects, one for each delegated Amazon Macie administrator account for the organization. Only one of these accounts can have a status of `ENABLED`. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### ResourceNotFoundException
<a name="admin-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="admin-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="admin-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="admin-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="admin-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DisableOrganizationAdminAccount
<a name="DisableOrganizationAdminAccount-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/DisableOrganizationAdminAccount)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/DisableOrganizationAdminAccount)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/DisableOrganizationAdminAccount)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/DisableOrganizationAdminAccount)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/DisableOrganizationAdminAccount)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/DisableOrganizationAdminAccount)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/DisableOrganizationAdminAccount)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/DisableOrganizationAdminAccount)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/DisableOrganizationAdminAccount)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/DisableOrganizationAdminAccount)

### ListOrganizationAdminAccounts
<a name="ListOrganizationAdminAccounts-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListOrganizationAdminAccounts)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListOrganizationAdminAccounts)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListOrganizationAdminAccounts)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListOrganizationAdminAccounts)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListOrganizationAdminAccounts)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListOrganizationAdminAccounts)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListOrganizationAdminAccounts)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListOrganizationAdminAccounts)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/ListOrganizationAdminAccounts)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListOrganizationAdminAccounts)

### EnableOrganizationAdminAccount
<a name="EnableOrganizationAdminAccount-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/EnableOrganizationAdminAccount)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/EnableOrganizationAdminAccount)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/EnableOrganizationAdminAccount)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/EnableOrganizationAdminAccount)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/EnableOrganizationAdminAccount)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/EnableOrganizationAdminAccount)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/EnableOrganizationAdminAccount)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/EnableOrganizationAdminAccount)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/EnableOrganizationAdminAccount)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/EnableOrganizationAdminAccount)
