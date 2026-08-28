---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/automated-discovery-accounts.html
---

# Automated Sensitive Data Discovery - Accounts
<a name="automated-discovery-accounts"></a>

The Accounts resource for automated sensitive data discovery provides access to the status of automated sensitive data discovery for accounts that are centrally managed as an organization in Amazon Macie. If you're the Macie administrator for an organization, you can use this resource to check or change the status of automated sensitive data discovery for individual accounts in your organization. If you have a member account, you can use this resource to check the status of automated sensitive data discovery for your account. Contact your Macie administrator if you want to change the status.

If you're a Macie administrator, start by enabling automated sensitive data discovery for your organization. To enable it for your organization, use the [Configuration](automated-discovery-configuration.md) resource for automated sensitive data discovery. By using that resource, you can also enable it automatically for all existing accounts and new member accounts, only new member accounts, or no member accounts. After you enable it for your organization, you can manage the status of automated sensitive data discovery for individual accounts in your organization.

If automated sensitive data discovery is enabled for an account in an organization, Macie analyzes the account's Amazon Simple Storage Service (Amazon S3) data by using the configuration settings specified by the Macie administrator account for the organization:
+ **Classification scope** - This specifies S3 buckets to exclude from the analyses. To exclude particular buckets that an account owns, add the buckets to the classification scope for the administrator account.
+ **Sensitivity inspection template** - This specifies which allow lists, custom data identifiers, and managed data identifiers to use when analyzing data. To customize the analyses, update the sensitivity inspection template for the administrator account.

As the analyses progress, Macie produces records of the sensitive data that it finds and the analysis that it performs: *sensitive data findings*, which report sensitive data that Macie finds in individual S3 objects, and *sensitive data discovery results*, which log details about the analysis of individual S3 objects. Macie also updates statistics, inventory data, and other information that it provides about Amazon S3 data. For more information, see [Performing automated sensitive data discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd.html) in the *Amazon Macie User Guide*.

As a Macie administrator, you can disable automated sensitive data discovery for an account at any time. If you disable it, Macie stops analyzing the account's Amazon S3 data. Instead of disabling it for an account completely, consider excluding only particular S3 buckets that the account owns. If you exclude a bucket, existing sensitive data discovery statistics and details for the bucket persist. For example, the bucket's current sensitivity score remains unchanged. However, Macie skips the bucket when it subsequently performs automated sensitive data discovery for the account. If you exclude a bucket, you can include it again later. To exclude or include a bucket, update the classification scope for your administrator account.

If you're the Macie administrator for an organization, you can use the Accounts resource to check or change the status of automated sensitive data discovery for individual accounts in your organization. If you have a member account, you can use this resource to check the status of automated sensitive data discovery for your account.

## URI
<a name="automated-discovery-accounts-url"></a>

`/automated-discovery/accounts`

## HTTP methods
<a name="automated-discovery-accounts-http-methods"></a>

### GET
<a name="automated-discovery-accountsget"></a>

**Operation ID:** `ListAutomatedDiscoveryAccounts`

Retrieves the status of automated sensitive data discovery for one or more accounts.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The `nextToken` string that specifies which page of results to return in a paginated response. |
| accountIds | String | False | The AWS account ID for each account, for as many as 50 accounts. To retrieve the status for multiple accounts, append the `accountIds` parameter and argument for each account, separated by an ampersand (&). To retrieve the status for all the accounts in an organization, omit this parameter. |
| maxResults | String | False | The maximum number of items to include in each page of a paginated response. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListAutomatedDiscoveryAccountsResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### PATCH
<a name="automated-discovery-accountspatch"></a>

**Operation ID:** `BatchUpdateAutomatedDiscoveryAccounts`

Changes the status of automated sensitive data discovery for one or more accounts.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | BatchUpdateAutomatedDiscoveryAccountsResponse | The request succeeded. However, the update might have failed for one or more accounts. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="automated-discovery-accounts-schemas"></a>

### Request bodies
<a name="automated-discovery-accounts-request-examples"></a>

#### PATCH schema
<a name="automated-discovery-accounts-request-body-patch-example"></a>

```
{
  "accounts": [
    {
      "accountId": "string",
      "status": enum
    }
  ]
}
```

### Response bodies
<a name="automated-discovery-accounts-response-examples"></a>

#### ListAutomatedDiscoveryAccountsResponse schema
<a name="automated-discovery-accounts-response-body-listautomateddiscoveryaccountsresponse-example"></a>

```
{
  "items": [
    {
      "accountId": "string",
      "status": enum
    }
  ],
  "nextToken": "string"
}
```

#### BatchUpdateAutomatedDiscoveryAccountsResponse schema
<a name="automated-discovery-accounts-response-body-batchupdateautomateddiscoveryaccountsresponse-example"></a>

```
{
  "errors": [
    {
      "accountId": "string",
      "errorCode": enum
    }
  ]
}
```

#### ValidationException schema
<a name="automated-discovery-accounts-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="automated-discovery-accounts-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="automated-discovery-accounts-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="automated-discovery-accounts-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="automated-discovery-accounts-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="automated-discovery-accounts-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="automated-discovery-accounts-properties"></a>

### AccessDeniedException
<a name="automated-discovery-accounts-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### AutomatedDiscoveryAccount
<a name="automated-discovery-accounts-model-automateddiscoveryaccount"></a>

Provides information about the status of automated sensitive data discovery for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The AWS account ID for the account. |
| status | [AutomatedDiscoveryAccountStatus](#automated-discovery-accounts-model-automateddiscoveryaccountstatus) | False | The current status of automated sensitive data discovery for the account. Possible values are: `ENABLED`, perform automated sensitive data discovery activities for the account; and, `DISABLED`, don't perform automated sensitive data discovery activities for the account. |

### AutomatedDiscoveryAccountStatus
<a name="automated-discovery-accounts-model-automateddiscoveryaccountstatus"></a>

The status of automated sensitive data discovery for an Amazon Macie account. Valid values are:
+ `ENABLED`
+ `DISABLED`

### AutomatedDiscoveryAccountUpdate
<a name="automated-discovery-accounts-model-automateddiscoveryaccountupdate"></a>

Changes the status of automated sensitive data discovery for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The AWS account ID for the account. |
| status | [AutomatedDiscoveryAccountStatus](#automated-discovery-accounts-model-automateddiscoveryaccountstatus) | False | The new status of automated sensitive data discovery for the account. Valid values are: `ENABLED`, perform automated sensitive data discovery activities for the account; and, `DISABLED`, don't perform automated sensitive data discovery activities for the account. |

### AutomatedDiscoveryAccountUpdateError
<a name="automated-discovery-accounts-model-automateddiscoveryaccountupdateerror"></a>

Provides information about a request that failed to change the status of automated sensitive data discovery for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The AWS account ID for the account that the request applied to. |
| errorCode | [AutomatedDiscoveryAccountUpdateErrorCode](#automated-discovery-accounts-model-automateddiscoveryaccountupdateerrorcode) | False | The error code for the error that caused the request to fail for the account (`accountId`). Possible values are: `ACCOUNT_NOT_FOUND`, the account doesn't exist or you're not the Amazon Macie administrator for the account; and, `ACCOUNT_PAUSED`, Macie isn't enabled for the account in the current AWS Region. |

### AutomatedDiscoveryAccountUpdateErrorCode
<a name="automated-discovery-accounts-model-automateddiscoveryaccountupdateerrorcode"></a>

The error code that indicates why a request failed to change the status of automated sensitive data discovery for an Amazon Macie account. Possible values are:
+ `ACCOUNT_PAUSED`
+ `ACCOUNT_NOT_FOUND`

### BatchUpdateAutomatedDiscoveryAccountsRequest
<a name="automated-discovery-accounts-model-batchupdateautomateddiscoveryaccountsrequest"></a>

Changes the status of automated sensitive data discovery for one or more Amazon Macie accounts.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accounts | Array of type [AutomatedDiscoveryAccountUpdate](#automated-discovery-accounts-model-automateddiscoveryaccountupdate) | False | An array of objects, one for each account to change the status of automated sensitive data discovery for. Each object specifies the AWS account ID for an account and a new status for that account. |

### BatchUpdateAutomatedDiscoveryAccountsResponse
<a name="automated-discovery-accounts-model-batchupdateautomateddiscoveryaccountsresponse"></a>

Provides the results of a request to change the status of automated sensitive data discovery for one or more Amazon Macie accounts.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errors | Array of type [AutomatedDiscoveryAccountUpdateError](#automated-discovery-accounts-model-automateddiscoveryaccountupdateerror) | False | An array of objects, one for each account whose status wasn't changed. Each object identifies the account and explains why the status of automated sensitive data discovery wasn't changed for the account. This value is null if the request succeeded for all specified accounts. |

### ConflictException
<a name="automated-discovery-accounts-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### InternalServerException
<a name="automated-discovery-accounts-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ListAutomatedDiscoveryAccountsResponse
<a name="automated-discovery-accounts-model-listautomateddiscoveryaccountsresponse"></a>

Provides information about the status of automated sensitive data discovery for one or more Amazon Macie accounts.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [AutomatedDiscoveryAccount](#automated-discovery-accounts-model-automateddiscoveryaccount) | False | An array of objects, one for each account specified in the request. Each object specifies the AWS account ID for an account and the current status of automated sensitive data discovery for that account. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### ResourceNotFoundException
<a name="automated-discovery-accounts-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="automated-discovery-accounts-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="automated-discovery-accounts-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="automated-discovery-accounts-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListAutomatedDiscoveryAccounts
<a name="ListAutomatedDiscoveryAccounts-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListAutomatedDiscoveryAccounts)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListAutomatedDiscoveryAccounts)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListAutomatedDiscoveryAccounts)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListAutomatedDiscoveryAccounts)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListAutomatedDiscoveryAccounts)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListAutomatedDiscoveryAccounts)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListAutomatedDiscoveryAccounts)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListAutomatedDiscoveryAccounts)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/ListAutomatedDiscoveryAccounts)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListAutomatedDiscoveryAccounts)

### BatchUpdateAutomatedDiscoveryAccounts
<a name="BatchUpdateAutomatedDiscoveryAccounts-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/BatchUpdateAutomatedDiscoveryAccounts)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/BatchUpdateAutomatedDiscoveryAccounts)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/BatchUpdateAutomatedDiscoveryAccounts)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/BatchUpdateAutomatedDiscoveryAccounts)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/BatchUpdateAutomatedDiscoveryAccounts)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/BatchUpdateAutomatedDiscoveryAccounts)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/BatchUpdateAutomatedDiscoveryAccounts)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/BatchUpdateAutomatedDiscoveryAccounts)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/BatchUpdateAutomatedDiscoveryAccounts)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/BatchUpdateAutomatedDiscoveryAccounts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Macie. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query macie` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
