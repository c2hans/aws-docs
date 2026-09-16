---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/findings-publication-configuration.html
---

# Findings - Publication Configuration
<a name="findings-publication-configuration"></a>

The Publication Configuration resource for findings provides settings for publishing findings to AWS Security Hub CSPM. With these settings, you can configure Amazon Macie to automatically publish all policy findings, all sensitive data findings, or both policy and sensitive data findings to Security Hub CSPM. This doesn't include findings that were suppressed (automatically archived) by a findings filter. You can also use these settings to stop publishing any findings to Security Hub CSPM. To learn more about how Macie publishes findings to Security Hub CSPM, see [Evaluating findings with AWS Security Hub CSPM](https://docs.aws.amazon.com/macie/latest/user/securityhub-integration.html) in the *Amazon Macie User Guide*.

Security Hub CSPM is a service that provides you with a comprehensive view of your security state across your AWS environment. It also helps you check your environment against security industry standards and best practices. It does this partly by consuming, aggregating, organizing, and prioritizing findings from multiple AWS services and supported AWS Partner Network (APN) security solutions. It helps you analyze your security trends and identify the highest priority security issues. To learn more about Security Hub CSPM, see the [AWS Security Hub User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html).

You can use the Publication Configuration resource for findings to retrieve information about or update your configuration settings for publishing findings to Security Hub CSPM automatically. If you configure Macie to publish policy findings to Security Hub CSPM, Macie publishes updates to those findings on a recurring basis. To specify the publication frequency for these updates, use the [Account Administration](macie.md) resource.

## URI
<a name="findings-publication-configuration-url"></a>

`/findings-publication-configuration`

## HTTP methods
<a name="findings-publication-configuration-http-methods"></a>

### GET
<a name="findings-publication-configurationget"></a>

**Operation ID:** `GetFindingsPublicationConfiguration`

Retrieves the configuration settings for publishing findings to AWS Security Hub CSPM.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetFindingsPublicationConfigurationResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### PUT
<a name="findings-publication-configurationput"></a>

**Operation ID:** `PutFindingsPublicationConfiguration`

Updates the configuration settings for publishing findings to AWS Security Hub CSPM.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded and there isn't any content to include in the body of the response (No Content). |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="findings-publication-configuration-schemas"></a>

### Request bodies
<a name="findings-publication-configuration-request-examples"></a>

#### PUT schema
<a name="findings-publication-configuration-request-body-put-example"></a>

```
{
  "clientToken": "string",
  "securityHubConfiguration": {
    "publishClassificationFindings": boolean,
    "publishPolicyFindings": boolean
  }
}
```

### Response bodies
<a name="findings-publication-configuration-response-examples"></a>

#### GetFindingsPublicationConfigurationResponse schema
<a name="findings-publication-configuration-response-body-getfindingspublicationconfigurationresponse-example"></a>

```
{
  "securityHubConfiguration": {
    "publishClassificationFindings": boolean,
    "publishPolicyFindings": boolean
  }
}
```

#### ValidationException schema
<a name="findings-publication-configuration-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="findings-publication-configuration-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="findings-publication-configuration-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="findings-publication-configuration-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="findings-publication-configuration-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="findings-publication-configuration-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="findings-publication-configuration-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="findings-publication-configuration-properties"></a>

### AccessDeniedException
<a name="findings-publication-configuration-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="findings-publication-configuration-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### GetFindingsPublicationConfigurationResponse
<a name="findings-publication-configuration-model-getfindingspublicationconfigurationresponse"></a>

Provides information about the current configuration settings for publishing findings to AWS Security Hub CSPM automatically.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| securityHubConfiguration | [SecurityHubConfiguration](#findings-publication-configuration-model-securityhubconfiguration) | False | The configuration settings that determine which findings are published to AWS Security Hub CSPM. |

### InternalServerException
<a name="findings-publication-configuration-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### PutFindingsPublicationConfigurationRequest
<a name="findings-publication-configuration-model-putfindingspublicationconfigurationrequest"></a>

Specifies configuration settings for publishing findings to AWS Security Hub CSPM automatically.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientToken | string | False | A unique, case-sensitive token that you provide to ensure the idempotency of the request. |
| securityHubConfiguration | [SecurityHubConfiguration](#findings-publication-configuration-model-securityhubconfiguration) | False | The configuration settings that determine which findings to publish to AWS Security Hub CSPM. |

### ResourceNotFoundException
<a name="findings-publication-configuration-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### SecurityHubConfiguration
<a name="findings-publication-configuration-model-securityhubconfiguration"></a>

Specifies configuration settings that determine which findings are published to AWS Security Hub CSPM automatically. For information about how Macie publishes findings to Security Hub CSPM, see [Evaluating findings with AWS Security Hub CSPM](https://docs.aws.amazon.com/macie/latest/user/securityhub-integration.html) in the *Amazon Macie User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| publishClassificationFindings | boolean | True | Specifies whether to publish sensitive data findings to AWS Security Hub CSPM. If you set this value to `true`, Amazon Macie automatically publishes all sensitive data findings that weren't suppressed by a findings filter. The default value is `false`. |
| publishPolicyFindings | boolean | True | Specifies whether to publish policy findings to AWS Security Hub CSPM. If you set this value to `true`, Amazon Macie automatically publishes all new and updated policy findings that weren't suppressed by a findings filter. The default value is `true`. |

### ServiceQuotaExceededException
<a name="findings-publication-configuration-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="findings-publication-configuration-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="findings-publication-configuration-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="findings-publication-configuration-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetFindingsPublicationConfiguration
<a name="GetFindingsPublicationConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetFindingsPublicationConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetFindingsPublicationConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetFindingsPublicationConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetFindingsPublicationConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetFindingsPublicationConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetFindingsPublicationConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetFindingsPublicationConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetFindingsPublicationConfiguration)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/GetFindingsPublicationConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetFindingsPublicationConfiguration)

### PutFindingsPublicationConfiguration
<a name="PutFindingsPublicationConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/PutFindingsPublicationConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/PutFindingsPublicationConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/PutFindingsPublicationConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/PutFindingsPublicationConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/PutFindingsPublicationConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/PutFindingsPublicationConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/PutFindingsPublicationConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/PutFindingsPublicationConfiguration)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/PutFindingsPublicationConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/PutFindingsPublicationConfiguration)
