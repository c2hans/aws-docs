---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/classification-scopes.html
---

# Classification Scopes
<a name="classification-scopes"></a>

The Classification Scopes resource provides a subset of information about the classification scope for your Amazon Macie account. The classification scope specifies Amazon Simple Storage Service (Amazon S3) buckets that you don't want Macie to analyze when it performs automated sensitive data discovery. It defines an S3 bucket exclusion list for automated sensitive data discovery.

The first time you or your Macie administrator enables automated sensitive data discovery for your account, Macie automatically creates the classification scope for your account. If you have a standalone Macie account, Macie then uses the scope's settings to determine which S3 buckets to exclude from analyses. If your account is part of an organization that centrally manages multiple Macie accounts, Macie uses the scope settings for your Macie administrator's account to determine which buckets to exclude. Contact your Macie administrator for information about the settings for your organization.

If you're the Macie administrator for an organization or you have a standalone Macie account, you can use this resource to retrieve the unique identifier and name of the classification scope that Macie created for your account. You can then use the unique identifier to retrieve or update the scope's settings by using the [Classification Scope](classification-scopes-id.md) resource.

## URI
<a name="classification-scopes-url"></a>

`/classification-scopes`

## HTTP methods
<a name="classification-scopes-http-methods"></a>

### GET
<a name="classification-scopesget"></a>

**Operation ID:** `ListClassificationScopes`

Retrieves a subset of information about the classification scope for an account.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| name | String | False | The name of the classification scope to retrieve the unique identifier for. |
| nextToken | String | False | The `nextToken` string that specifies which page of results to return in a paginated response. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListClassificationScopesResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="classification-scopes-schemas"></a>

### Response bodies
<a name="classification-scopes-response-examples"></a>

#### ListClassificationScopesResponse schema
<a name="classification-scopes-response-body-listclassificationscopesresponse-example"></a>

```
{
  "classificationScopes": [
    {
      "id": "string",
      "name": "string"
    }
  ],
  "nextToken": "string"
}
```

#### ValidationException schema
<a name="classification-scopes-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="classification-scopes-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="classification-scopes-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="classification-scopes-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="classification-scopes-properties"></a>

### AccessDeniedException
<a name="classification-scopes-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ClassificationScopeSummary
<a name="classification-scopes-model-classificationscopesummary"></a>

Provides information about the classification scope for an Amazon Macie account. Macie uses the scope's settings when it performs automated sensitive data discovery for the account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | The unique identifier for the classification scope. |
| name | string | False | The name of the classification scope: `automated-sensitive-data-discovery`. |

### InternalServerException
<a name="classification-scopes-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ListClassificationScopesResponse
<a name="classification-scopes-model-listclassificationscopesresponse"></a>

Provides the results of a request for information about the classification scope for an Amazon Macie account. Macie uses the scope's settings when it performs automated sensitive data discovery for the account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| classificationScopes | Array of type [ClassificationScopeSummary](#classification-scopes-model-classificationscopesummary) | False | An array that specifies the unique identifier and name of the classification scope for the account. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### ThrottlingException
<a name="classification-scopes-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="classification-scopes-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="classification-scopes-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListClassificationScopes
<a name="ListClassificationScopes-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListClassificationScopes)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListClassificationScopes)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListClassificationScopes)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListClassificationScopes)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListClassificationScopes)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListClassificationScopes)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListClassificationScopes)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListClassificationScopes)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/ListClassificationScopes)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListClassificationScopes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Macie. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query macie` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
