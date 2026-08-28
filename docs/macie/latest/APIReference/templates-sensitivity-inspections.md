---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/templates-sensitivity-inspections.html
---

# Sensitivity Inspection Templates
<a name="templates-sensitivity-inspections"></a>

The Sensitivity Inspection Templates resource provides a subset of information about the sensitivity inspection template for your Amazon Macie account. This template stores the collection of settings that specify which allow lists, custom data identifiers, and managed data identifiers you want Macie to use when performing automated sensitive data discovery. The first time you or your Macie administrator enables automated sensitive data discovery for your account, Macie automatically creates the template for your account.

You can use this resource to retrieve the unique identifier and name of the template that Macie created for your account. You can then use the unique identifier to retrieve or update the template's settings by using the [Sensitivity Inspection Template](templates-sensitivity-inspections-id.md) resource.

If your account is part of an organization that centrally manages multiple Macie accounts, Macie uses the sensitivity inspection template for your Macie administrator's account when it analyzes data for accounts in your organization. Contact your Macie administrator for information about the template settings for your organization.

## URI
<a name="templates-sensitivity-inspections-url"></a>

`/templates/sensitivity-inspections`

## HTTP methods
<a name="templates-sensitivity-inspections-http-methods"></a>

### GET
<a name="templates-sensitivity-inspectionsget"></a>

**Operation ID:** `ListSensitivityInspectionTemplates`

Retrieves a subset of information about the sensitivity inspection template for an account.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The `nextToken` string that specifies which page of results to return in a paginated response. |
| maxResults | String | False | The maximum number of items to include in each page of a paginated response. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListSensitivityInspectionTemplatesResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="templates-sensitivity-inspections-schemas"></a>

### Response bodies
<a name="templates-sensitivity-inspections-response-examples"></a>

#### ListSensitivityInspectionTemplatesResponse schema
<a name="templates-sensitivity-inspections-response-body-listsensitivityinspectiontemplatesresponse-example"></a>

```
{
  "nextToken": "string",
  "sensitivityInspectionTemplates": [
    {
      "id": "string",
      "name": "string"
    }
  ]
}
```

#### ValidationException schema
<a name="templates-sensitivity-inspections-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="templates-sensitivity-inspections-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="templates-sensitivity-inspections-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="templates-sensitivity-inspections-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="templates-sensitivity-inspections-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="templates-sensitivity-inspections-properties"></a>

### AccessDeniedException
<a name="templates-sensitivity-inspections-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### InternalServerException
<a name="templates-sensitivity-inspections-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ListSensitivityInspectionTemplatesResponse
<a name="templates-sensitivity-inspections-model-listsensitivityinspectiontemplatesresponse"></a>

Provides the results of a request for information about the sensitivity inspection template for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |
| sensitivityInspectionTemplates | Array of type [SensitivityInspectionTemplatesEntry](#templates-sensitivity-inspections-model-sensitivityinspectiontemplatesentry) | False | An array that specifies the unique identifier and name of the sensitivity inspection template for the account. |

### SensitivityInspectionTemplatesEntry
<a name="templates-sensitivity-inspections-model-sensitivityinspectiontemplatesentry"></a>

Provides information about the sensitivity inspection template for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | The unique identifier for the sensitivity inspection template. |
| name | string | False | The name of the sensitivity inspection template: `automated-sensitive-data-discovery`. |

### ServiceQuotaExceededException
<a name="templates-sensitivity-inspections-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="templates-sensitivity-inspections-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="templates-sensitivity-inspections-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="templates-sensitivity-inspections-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListSensitivityInspectionTemplates
<a name="ListSensitivityInspectionTemplates-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListSensitivityInspectionTemplates)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListSensitivityInspectionTemplates)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListSensitivityInspectionTemplates)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListSensitivityInspectionTemplates)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListSensitivityInspectionTemplates)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListSensitivityInspectionTemplates)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListSensitivityInspectionTemplates)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListSensitivityInspectionTemplates)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/ListSensitivityInspectionTemplates)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListSensitivityInspectionTemplates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Macie. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query macie` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
