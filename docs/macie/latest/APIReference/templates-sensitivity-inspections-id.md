---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/templates-sensitivity-inspections-id.html
---

# Sensitivity Inspection Template
<a name="templates-sensitivity-inspections-id"></a>

The Sensitivity Inspection Template resource provides access to the sensitivity inspection template for your Amazon Macie account. The template stores the collection of settings that specify which allow lists, custom data identifiers, and managed data identifiers you want Macie to use when performing automated sensitive data discovery. For more information, see [Performing automated sensitive data discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd.html) in the *Amazon Macie User Guide*.

The first time you or your Macie administrator enables automated sensitive data discovery for your account, Macie automatically creates the sensitivity inspection template for your account. Macie uses the template's settings to determine whether to use (*include*) or not use (*exclude*) individual allow lists, custom data identifiers, and managed data identifiers when it analyzes data. If your account is part of an organization that centrally manages multiple Macie accounts, Macie uses the template settings for your Macie administrator's account when it analyzes data for accounts in your organization. Contact your Macie administrator for information about the settings for your organization.

By default, Macie analyzes data by using only the set of managed data identifiers that we recommend for automated sensitive data discovery. For a list of these identifiers, see [Default settings for automated sensitive data discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-settings-defaults.html) in the *Amazon Macie User Guide*. If you're a Macie administrator or you have a standalone Macie account, you can customize the analyses by updating the template settings for your account. You can include allow lists and custom data identifiers that you've defined, and include or exclude specific managed data identifiers that Macie provides. You can use allow lists in all the AWS Regions where Macie is currently available except the Asia Pacific (Osaka) Region.

You can use the Sensitivity Inspection Template resource to retrieve or update the template settings for your account. When you use this resource, you have to specify the unique identifier for the template. To obtain this identifier, use the [Sensitivity Inspection Templates](templates-sensitivity-inspections.md) resource.

## URI
<a name="templates-sensitivity-inspections-id-url"></a>

`/templates/sensitivity-inspections/{{id}}`

## HTTP methods
<a name="templates-sensitivity-inspections-id-http-methods"></a>

### GET
<a name="templates-sensitivity-inspections-idget"></a>

**Operation ID:** `GetSensitivityInspectionTemplate`

Retrieves the settings for the sensitivity inspection template for an account.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetSensitivityInspectionTemplateResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### PUT
<a name="templates-sensitivity-inspections-idput"></a>

**Operation ID:** `UpdateSensitivityInspectionTemplate`

Updates the settings for the sensitivity inspection template for an account.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty Schema | The request succeeded. The template's settings were updated and there isn't any content to include in the body of the response (No Content). |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="templates-sensitivity-inspections-id-schemas"></a>

### Request bodies
<a name="templates-sensitivity-inspections-id-request-examples"></a>

#### PUT schema
<a name="templates-sensitivity-inspections-id-request-body-put-example"></a>

```
{
  "description": "string",
  "excludes": {
    "managedDataIdentifierIds": [
      "string"
    ]
  },
  "includes": {
    "allowListIds": [
      "string"
    ],
    "customDataIdentifierIds": [
      "string"
    ],
    "managedDataIdentifierIds": [
      "string"
    ]
  }
}
```

### Response bodies
<a name="templates-sensitivity-inspections-id-response-examples"></a>

#### GetSensitivityInspectionTemplateResponse schema
<a name="templates-sensitivity-inspections-id-response-body-getsensitivityinspectiontemplateresponse-example"></a>

```
{
  "description": "string",
  "excludes": {
    "managedDataIdentifierIds": [
      "string"
    ]
  },
  "includes": {
    "allowListIds": [
      "string"
    ],
    "customDataIdentifierIds": [
      "string"
    ],
    "managedDataIdentifierIds": [
      "string"
    ]
  },
  "name": "string",
  "sensitivityInspectionTemplateId": "string"
}
```

#### Empty Schema schema
<a name="templates-sensitivity-inspections-id-response-body-empty-example"></a>

```
{
}
```

#### ValidationException schema
<a name="templates-sensitivity-inspections-id-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="templates-sensitivity-inspections-id-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="templates-sensitivity-inspections-id-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="templates-sensitivity-inspections-id-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="templates-sensitivity-inspections-id-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="templates-sensitivity-inspections-id-properties"></a>

### AccessDeniedException
<a name="templates-sensitivity-inspections-id-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Empty
<a name="templates-sensitivity-inspections-id-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### GetSensitivityInspectionTemplateResponse
<a name="templates-sensitivity-inspections-id-model-getsensitivityinspectiontemplateresponse"></a>

Provides information about the settings for the sensitivity inspection template for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string | False | The custom description of the template. |
| excludes | [SensitivityInspectionTemplateExcludes](#templates-sensitivity-inspections-id-model-sensitivityinspectiontemplateexcludes) | False | The managed data identifiers that are explicitly excluded (not used) when performing automated sensitive data discovery. |
| includes | [SensitivityInspectionTemplateIncludes](#templates-sensitivity-inspections-id-model-sensitivityinspectiontemplateincludes) | False | The allow lists, custom data identifiers, and managed data identifiers that are explicitly included (used) when performing automated sensitive data discovery. |
| name | string | True | The name of the template: `automated-sensitive-data-discovery`. |
| sensitivityInspectionTemplateId | string | True | The unique identifier for the template. |

### InternalServerException
<a name="templates-sensitivity-inspections-id-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="templates-sensitivity-inspections-id-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### SensitivityInspectionTemplateExcludes
<a name="templates-sensitivity-inspections-id-model-sensitivityinspectiontemplateexcludes"></a>

Specifies managed data identifiers to exclude (not use) when performing automated sensitive data discovery. For information about the managed data identifiers that Amazon Macie currently provides, see [Using managed data identifiers](https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html) in the *Amazon Macie User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| managedDataIdentifierIds | Array of type string | False | An array of unique identifiers, one for each managed data identifier to exclude. To retrieve a list of valid values, use the `ListManagedDataIdentifiers` operation. |

### SensitivityInspectionTemplateIncludes
<a name="templates-sensitivity-inspections-id-model-sensitivityinspectiontemplateincludes"></a>

Specifies the allow lists, custom data identifiers, and managed data identifiers to include (use) when performing automated sensitive data discovery. The configuration must specify at least one custom data identifier or managed data identifier. For information about the managed data identifiers that Amazon Macie currently provides, see [Using managed data identifiers](https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html) in the *Amazon Macie User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| allowListIds | Array of type string | False | An array of unique identifiers, one for each allow list to include. |
| customDataIdentifierIds | Array of type string | False | An array of unique identifiers, one for each custom data identifier to include. |
| managedDataIdentifierIds | Array of type string | False | An array of unique identifiers, one for each managed data identifier to include.<br />Amazon Macie uses these managed data identifiers in addition to managed data identifiers that are subsequently released and recommended for automated sensitive data discovery. To retrieve a list of valid values for the managed data identifiers that are currently available, use the `ListManagedDataIdentifiers` operation.<br /> |

### ThrottlingException
<a name="templates-sensitivity-inspections-id-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UpdateSensitivityInspectionTemplateRequest
<a name="templates-sensitivity-inspections-id-model-updatesensitivityinspectiontemplaterequest"></a>

Specifies settings for the sensitivity inspection template for an Amazon Macie account. To update the settings, automated sensitive data discovery must be enabled for the account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string | False | A custom description of the template. The description can contain as many as 200 characters. |
| excludes | [SensitivityInspectionTemplateExcludes](#templates-sensitivity-inspections-id-model-sensitivityinspectiontemplateexcludes) | False | The managed data identifiers to explicitly exclude (not use) when performing automated sensitive data discovery.<br />To exclude an allow list or custom data identifier that's currently included by the template, update the values for the `SensitivityInspectionTemplateIncludes.allowListIds` and `SensitivityInspectionTemplateIncludes.customDataIdentifierIds` properties, respectively. |
| includes | [SensitivityInspectionTemplateIncludes](#templates-sensitivity-inspections-id-model-sensitivityinspectiontemplateincludes) | False | The allow lists, custom data identifiers, and managed data identifiers to explicitly include (use) when performing automated sensitive data discovery. |

### ValidationException
<a name="templates-sensitivity-inspections-id-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="templates-sensitivity-inspections-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetSensitivityInspectionTemplate
<a name="GetSensitivityInspectionTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetSensitivityInspectionTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetSensitivityInspectionTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetSensitivityInspectionTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetSensitivityInspectionTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetSensitivityInspectionTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetSensitivityInspectionTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetSensitivityInspectionTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetSensitivityInspectionTemplate)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetSensitivityInspectionTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetSensitivityInspectionTemplate)

### UpdateSensitivityInspectionTemplate
<a name="UpdateSensitivityInspectionTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/UpdateSensitivityInspectionTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/UpdateSensitivityInspectionTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/UpdateSensitivityInspectionTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/UpdateSensitivityInspectionTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/UpdateSensitivityInspectionTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/UpdateSensitivityInspectionTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/UpdateSensitivityInspectionTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/UpdateSensitivityInspectionTemplate)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/UpdateSensitivityInspectionTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/UpdateSensitivityInspectionTemplate)
