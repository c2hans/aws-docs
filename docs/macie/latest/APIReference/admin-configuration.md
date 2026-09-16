---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/admin-configuration.html
---

# AWS Organizations - Macie Configuration
<a name="admin-configuration"></a>

The Macie Configuration resource for AWS Organizations provides access to certain Amazon Macie configuration settings for an organization in AWS Organizations. AWS Organizations is a global account management service that enables AWS administrators to consolidate and centrally manage multiple AWS accounts. For more information about this service, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html). For information about integrating Macie with AWS Organizations, see [Managing multiple accounts with AWS Organizations](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao.html) in the *Amazon Macie User Guide*.

If you're the delegated Macie administrator for an organization in AWS Organizations, you can use this resource to retrieve or change the setting that determines whether Macie is enabled automatically for accounts that are added to your organization in AWS Organizations. To retrieve or change the setting that determines whether automated sensitive data discovery is also enabled automatically for new accounts, use the [Configuration](automated-discovery-configuration.md) resource for automated sensitive data discovery.

To use this resource, you must be the delegated Macie administrator for an organization in AWS Organizations.

## URI
<a name="admin-configuration-url"></a>

`/admin/configuration`

## HTTP methods
<a name="admin-configuration-http-methods"></a>

### GET
<a name="admin-configurationget"></a>

**Operation ID:** `DescribeOrganizationConfiguration`

Retrieves the Amazon Macie configuration settings for an organization in AWS Organizations.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DescribeOrganizationConfigurationResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### PATCH
<a name="admin-configurationpatch"></a>

**Operation ID:** `UpdateOrganizationConfiguration`

Updates the Amazon Macie configuration settings for an organization in AWS Organizations.

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
<a name="admin-configuration-schemas"></a>

### Request bodies
<a name="admin-configuration-request-examples"></a>

#### PATCH schema
<a name="admin-configuration-request-body-patch-example"></a>

```
{
  "autoEnable": boolean
}
```

### Response bodies
<a name="admin-configuration-response-examples"></a>

#### DescribeOrganizationConfigurationResponse schema
<a name="admin-configuration-response-body-describeorganizationconfigurationresponse-example"></a>

```
{
  "autoEnable": boolean,
  "maxAccountLimitReached": boolean
}
```

#### Empty Schema schema
<a name="admin-configuration-response-body-empty-example"></a>

```
{
}
```

#### ValidationException schema
<a name="admin-configuration-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="admin-configuration-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="admin-configuration-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="admin-configuration-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="admin-configuration-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="admin-configuration-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="admin-configuration-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="admin-configuration-properties"></a>

### AccessDeniedException
<a name="admin-configuration-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="admin-configuration-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### DescribeOrganizationConfigurationResponse
<a name="admin-configuration-model-describeorganizationconfigurationresponse"></a>

Provides information about the Amazon Macie configuration for an organization in AWS Organizations.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| autoEnable | boolean | False | Specifies whether Amazon Macie is enabled automatically for accounts that are added to the organization. |
| maxAccountLimitReached | boolean | False | Specifies whether the maximum number of Amazon Macie member accounts are part of the organization. |

### Empty
<a name="admin-configuration-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### InternalServerException
<a name="admin-configuration-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="admin-configuration-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="admin-configuration-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="admin-configuration-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UpdateOrganizationConfigurationRequest
<a name="admin-configuration-model-updateorganizationconfigurationrequest"></a>

Specifies whether to enable Amazon Macie automatically for accounts that are added to an organization in AWS Organizations, when the accounts are added to the organization.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| autoEnable | boolean | True | Specifies whether to enable Amazon Macie automatically for accounts that are added to the organization in AWS Organizations. |

### ValidationException
<a name="admin-configuration-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="admin-configuration-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeOrganizationConfiguration
<a name="DescribeOrganizationConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/DescribeOrganizationConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/DescribeOrganizationConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/DescribeOrganizationConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/DescribeOrganizationConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/DescribeOrganizationConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/DescribeOrganizationConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/DescribeOrganizationConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/DescribeOrganizationConfiguration)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/DescribeOrganizationConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/DescribeOrganizationConfiguration)

### UpdateOrganizationConfiguration
<a name="UpdateOrganizationConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/UpdateOrganizationConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/UpdateOrganizationConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/UpdateOrganizationConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/UpdateOrganizationConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/UpdateOrganizationConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/UpdateOrganizationConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/UpdateOrganizationConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/UpdateOrganizationConfiguration)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/UpdateOrganizationConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/UpdateOrganizationConfiguration)
