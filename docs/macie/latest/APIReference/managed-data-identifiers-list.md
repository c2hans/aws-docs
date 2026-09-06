---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/managed-data-identifiers-list.html
---

# Managed Data Identifiers
<a name="managed-data-identifiers-list"></a>

The Managed Data Identifiers resource represents the repository of managed data identifiers that Amazon Macie currently provides. A *managed data identifier* is a set of built-in criteria and techniques that are designed to detect a specific type of sensitive data. The types include credit card numbers, AWS secret access keys, and passport numbers for particular countries and regions. Managed data identifiers can detect a large and growing list of sensitive data types for many countries and regions, including multiple types of personally identifiable information (PII), financial information, and credentials data. For information about the categories and types of sensitive data that they can detect, see [Using managed data identifiers](https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html) in the *Amazon Macie User Guide*.

To detect sensitive data with managed data identifiers, create and run classification jobs. If you're the Macie administrator for an organization or you have a standalone Macie account, you can also enable automated sensitive data discovery. Both options provide settings for specifying which managed data identifiers you want Macie to use when it analyzes objects in Amazon Simple Storage Service (Amazon S3) buckets. When you configure the settings, you specify the unique identifier (ID) for one or more managed data identifiers. You can use this resource to determine which IDs to specify.

You can use the Managed Data Identifiers resource to retrieve information about the managed data identifiers that Macie currently provides.

## URI
<a name="managed-data-identifiers-list-url"></a>

`/managed-data-identifiers/list`

## HTTP methods
<a name="managed-data-identifiers-list-http-methods"></a>

### POST
<a name="managed-data-identifiers-listpost"></a>

**Operation ID:** `ListManagedDataIdentifiers`

Retrieves information about all the managed data identifiers that Amazon Macie currently provides.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListManagedDataIdentifiersResponse | The request succeeded. |

## Schemas
<a name="managed-data-identifiers-list-schemas"></a>

### Request bodies
<a name="managed-data-identifiers-list-request-examples"></a>

#### POST schema
<a name="managed-data-identifiers-list-request-body-post-example"></a>

```
{
  "nextToken": "string"
}
```

### Response bodies
<a name="managed-data-identifiers-list-response-examples"></a>

#### ListManagedDataIdentifiersResponse schema
<a name="managed-data-identifiers-list-response-body-listmanageddataidentifiersresponse-example"></a>

```
{
  "items": [
    {
      "category": enum,
      "id": "string"
    }
  ],
  "nextToken": "string"
}
```

## Properties
<a name="managed-data-identifiers-list-properties"></a>

### ListManagedDataIdentifiersRequest
<a name="managed-data-identifiers-list-model-listmanageddataidentifiersrequest"></a>

Specifies criteria for paginating the results of a request for information about managed data identifiers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | The `nextToken` string that specifies which page of results to return in a paginated response. |

### ListManagedDataIdentifiersResponse
<a name="managed-data-identifiers-list-model-listmanageddataidentifiersresponse"></a>

Provides information about the managed data identifiers that Amazon Macie currently provides.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [ManagedDataIdentifierSummary](#managed-data-identifiers-list-model-manageddataidentifiersummary) | False | An array of objects, one for each managed data identifier. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### ManagedDataIdentifierSummary
<a name="managed-data-identifiers-list-model-manageddataidentifiersummary"></a>

Provides information about a managed data identifier. For additional information, see [Using managed data identifiers](https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html) in the *Amazon Macie User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| category | [SensitiveDataItemCategory](#managed-data-identifiers-list-model-sensitivedataitemcategory) | False | The category of sensitive data that the managed data identifier detects: `CREDENTIALS`, for credentials data such as private keys or AWS secret access keys; `FINANCIAL_INFORMATION`, for financial data such as credit card numbers; or, `PERSONAL_INFORMATION`, for personal health information, such as health insurance identification numbers, or personally identifiable information, such as passport numbers. |
| id | string | False | The unique identifier for the managed data identifier. This is a string that describes the type of sensitive data that the managed data identifier detects. For example: `OPENSSH_PRIVATE_KEY` for OpenSSH private keys, `CREDIT_CARD_NUMBER` for credit card numbers, or `USA_PASSPORT_NUMBER` for US passport numbers. |

### SensitiveDataItemCategory
<a name="managed-data-identifiers-list-model-sensitivedataitemcategory"></a>

For a finding, the category of sensitive data that was detected and produced the finding. For a managed data identifier, the category of sensitive data that the managed data identifier detects. Possible values are:
+ `FINANCIAL_INFORMATION`
+ `PERSONAL_INFORMATION`
+ `CREDENTIALS`
+ `CUSTOM_IDENTIFIER`

## See also
<a name="managed-data-identifiers-list-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListManagedDataIdentifiers
<a name="ListManagedDataIdentifiers-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListManagedDataIdentifiers)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListManagedDataIdentifiers)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListManagedDataIdentifiers)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListManagedDataIdentifiers)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListManagedDataIdentifiers)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListManagedDataIdentifiers)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListManagedDataIdentifiers)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListManagedDataIdentifiers)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/ListManagedDataIdentifiers)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListManagedDataIdentifiers)
