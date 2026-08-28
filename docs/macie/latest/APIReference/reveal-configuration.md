---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/reveal-configuration.html
---

# Findings - Reveal Sensitive Data Occurrences Configuration
<a name="reveal-configuration"></a>

The Reveal Sensitive Data Occurrences Configuration resource provides access to settings for retrieving sample occurrences of sensitive data that Amazon Macie reports in findings. The samples can help you verify the nature of the sensitive data that Macie found. They can also help you tailor your investigation of an affected Amazon Simple Storage Service (Amazon S3) object or bucket. You can retrieve sensitive data samples for findings in all the AWS Regions where Macie is currently available except the Asia Pacific (Osaka) and Israel (Tel Aviv) Regions.

When you retrieve sensitive data samples, you specify the unique identifier for a sensitive data finding. Macie then uses location data in the corresponding sensitive data discovery result to locate and extract sample occurrences of sensitive data from the affected S3 object. Macie encrypts the extracted data with an AWS Key Management Service (AWS KMS) key that you specify, temporarily stores the encrypted data in a cache, and returns the data in your results. Soon after extraction and encryption, Macie permanently deletes the data from the cache unless additional retention is temporarily required to resolve an operational issue.

By using the Reveal Sensitive Data Occurrences Configuration resource, you can specify configuration settings for retrieving sensitive data samples from affected S3 objects. When you configure the settings for your Macie account, you specify how to access affected objects and which AWS KMS key to use to encrypt the samples.

To access affected S3 objects, you have two options. You can configure Macie to use AWS Identity and Access Management (IAM) user credentials or assume an IAM role:
+ **Use IAM user credentials** - With this option (`CALLER_CREDENTIALS`), each user of your account uses their individual IAM identity to locate, retrieve, encrypt, and reveal sensitive data samples for a finding.
+ **Assume an IAM role** - With this option (`ASSUME_ROLE`), you create an IAM role that delegates access to Macie. You also make sure the trust and permissions policies for the role meet all requirements for Macie to assume the role. Macie then assumes the role when a user of your account chooses to locate, retrieve, encrypt, and reveal sensitive data samples for a finding.

To encrypt sensitive data samples, configure Macie to use an AWS KMS key that you specify. The KMS key must be a customer managed, symmetric encryption key. It must also be a single-Region key that's enabled in the same AWS Region as your Macie account.

For more information about configuration options and requirements, see [Configuring Macie to retrieve sensitive data samples](https://docs.aws.amazon.com/macie/latest/user/findings-retrieve-sd-configure.html) in the *Amazon Macie User Guide*.

In addition to specifying configuration settings, you can use the Reveal Sensitive Data Occurrences Configuration resource to enable or disable the configuration for your Macie account. If you enable the configuration, use the [Reveal Sensitive Data Occurrences](findings-findingid-reveal.md) resource to retrieve sensitive data samples for individual findings.

Before you enable the configuration, verify that you configured Macie to store your sensitive data discovery results in an S3 bucket. Otherwise, you won't be able to retrieve sensitive data samples for findings. To check your configuration, use the [Export Configuration](classification-export-configuration.md) resource for data classification results.

## URI
<a name="reveal-configuration-url"></a>

`/reveal-configuration`

## HTTP methods
<a name="reveal-configuration-http-methods"></a>

### GET
<a name="reveal-configurationget"></a>

**Operation ID:** `GetRevealConfiguration`

Retrieves the status and configuration settings for retrieving occurrences of sensitive data reported by findings.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetRevealConfigurationResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### PUT
<a name="reveal-configurationput"></a>

**Operation ID:** `UpdateRevealConfiguration`

Updates the status and configuration settings for retrieving occurrences of sensitive data reported by findings.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateRevealConfigurationResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="reveal-configuration-schemas"></a>

### Request bodies
<a name="reveal-configuration-request-examples"></a>

#### PUT schema
<a name="reveal-configuration-request-body-put-example"></a>

```
{
  "configuration": {
    "kmsKeyId": "string",
    "status": enum
  },
  "retrievalConfiguration": {
    "retrievalMode": enum,
    "roleName": "string"
  }
}
```

### Response bodies
<a name="reveal-configuration-response-examples"></a>

#### GetRevealConfigurationResponse schema
<a name="reveal-configuration-response-body-getrevealconfigurationresponse-example"></a>

```
{
  "configuration": {
    "kmsKeyId": "string",
    "status": enum
  },
  "retrievalConfiguration": {
    "externalId": "string",
    "retrievalMode": enum,
    "roleName": "string"
  }
}
```

#### UpdateRevealConfigurationResponse schema
<a name="reveal-configuration-response-body-updaterevealconfigurationresponse-example"></a>

```
{
  "configuration": {
    "kmsKeyId": "string",
    "status": enum
  },
  "retrievalConfiguration": {
    "externalId": "string",
    "retrievalMode": enum,
    "roleName": "string"
  }
}
```

#### ValidationException schema
<a name="reveal-configuration-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="reveal-configuration-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="reveal-configuration-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="reveal-configuration-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="reveal-configuration-properties"></a>

### AccessDeniedException
<a name="reveal-configuration-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### GetRevealConfigurationResponse
<a name="reveal-configuration-model-getrevealconfigurationresponse"></a>

Provides information about the configuration settings for retrieving occurrences of sensitive data reported by findings, and the status of the configuration for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configuration | [RevealConfiguration](#reveal-configuration-model-revealconfiguration) | True | The AWS KMS key that's used to encrypt the sensitive data, and the status of the configuration for the Amazon Macie account. |
| retrievalConfiguration | [RetrievalConfiguration](#reveal-configuration-model-retrievalconfiguration) | False | The access method and settings that are used to retrieve the sensitive data. |

### InternalServerException
<a name="reveal-configuration-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### RetrievalConfiguration
<a name="reveal-configuration-model-retrievalconfiguration"></a>

Provides information about the access method and settings that are used to retrieve occurrences of sensitive data reported by findings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| externalId | string | False | The external ID to specify in the trust policy for the IAM role to assume when retrieving sensitive data from affected S3 objects (`roleName`). This value is null if the value for `retrievalMode` is `CALLER_CREDENTIALS`.<br />This ID is a unique alphanumeric string that Amazon Macie generates automatically after you configure it to assume an IAM role. For a Macie administrator to retrieve sensitive data from an affected S3 object for a member account, the trust policy for the role in the member account must include an `sts:ExternalId` condition that requires this ID. |
| retrievalMode | [RetrievalMode](#reveal-configuration-model-retrievalmode) | True | The access method that's used to retrieve sensitive data from affected S3 objects. Valid values are: `ASSUME_ROLE`, assume an IAM role that is in the affected AWS account and delegates access to Amazon Macie (`roleName`); and, `CALLER_CREDENTIALS`, use the credentials of the IAM user who requests the sensitive data. |
| roleName | string<br />Pattern: `^[\w+=,.@-]*$`<br />MinLength: 1<br />MaxLength: 64 | False | The name of the IAM role that is in the affected AWS account and Amazon Macie is allowed to assume when retrieving sensitive data from affected S3 objects for the account. This value is null if the value for `retrievalMode` is `CALLER_CREDENTIALS`. |

### RetrievalMode
<a name="reveal-configuration-model-retrievalmode"></a>

The access method to use when retrieving occurrences of sensitive data reported by findings. Valid values are:
+ `CALLER_CREDENTIALS`
+ `ASSUME_ROLE`

### RevealConfiguration
<a name="reveal-configuration-model-revealconfiguration"></a>

Specifies the status of the Amazon Macie configuration for retrieving occurrences of sensitive data reported by findings, and the AWS Key Management Service (AWS KMS) key to use to encrypt sensitive data that's retrieved. When you enable the configuration for the first time, your request must specify an AWS KMS key. Otherwise, an error occurs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| kmsKeyId | string<br />MinLength: 1<br />MaxLength: 2048 | False | The Amazon Resource Name (ARN), ID, or alias of the AWS KMS key to use to encrypt sensitive data that's retrieved. The key must be an existing, customer managed, symmetric encryption key that's enabled in the same AWS Region as the Amazon Macie account.<br />If this value specifies an alias, it must include the following prefix: `alias/`. If this value specifies a key that's owned by another AWS account, it must specify the ARN of the key or the ARN of the key's alias. |
| status | [RevealStatus](#reveal-configuration-model-revealstatus) | True | The status of the configuration for the Amazon Macie account. In a response, possible values are: `ENABLED`, the configuration is currently enabled for the account; and, `DISABLED`, the configuration is currently disabled for the account. In a request, valid values are: `ENABLED`, enable the configuration for the account; and, `DISABLED`, disable the configuration for the account. If you disable the configuration, you also permanently delete current settings that specify how to access affected S3 objects. If your current access method is `ASSUME_ROLE`, Macie also deletes the external ID and role name currently specified for the configuration. These settings can't be recovered after they're deleted.  |

### RevealStatus
<a name="reveal-configuration-model-revealstatus"></a>

The status of the configuration for retrieving occurrences of sensitive data reported by findings. Valid values are:
+ `ENABLED`
+ `DISABLED`

### ThrottlingException
<a name="reveal-configuration-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UpdateRetrievalConfiguration
<a name="reveal-configuration-model-updateretrievalconfiguration"></a>

Specifies the access method and settings to use when retrieving occurrences of sensitive data reported by findings. If your request specifies an AWS Identity and Access Management (IAM) role to assume, Amazon Macie verifies that the role exists and the attached policies are configured correctly. If there's an issue, Macie returns an error. For information about addressing the issue, see [Configuration options for retrieving sensitive data samples](https://docs.aws.amazon.com/macie/latest/user/findings-retrieve-sd-options.html) in the *Amazon Macie User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| retrievalMode | [RetrievalMode](#reveal-configuration-model-retrievalmode) | True | The access method to use when retrieving sensitive data from affected S3 objects. Valid values are: `ASSUME_ROLE`, assume an IAM role that is in the affected AWS account and delegates access to Amazon Macie; and, `CALLER_CREDENTIALS`, use the credentials of the IAM user who requests the sensitive data. If you specify `ASSUME_ROLE`, also specify the name of an existing IAM role for Macie to assume (`roleName`). If you change this value from `ASSUME_ROLE` to `CALLER_CREDENTIALS` for an existing configuration, Macie permanently deletes the external ID and role name currently specified for the configuration. These settings can't be recovered after they're deleted.  |
| roleName | string<br />Pattern: `^[\w+=,.@-]*$`<br />MinLength: 1<br />MaxLength: 64 | False | The name of the IAM role that is in the affected AWS account and Amazon Macie is allowed to assume when retrieving sensitive data from affected S3 objects for the account. The trust and permissions policies for the role must meet all requirements for Macie to assume the role. |

### UpdateRevealConfigurationRequest
<a name="reveal-configuration-model-updaterevealconfigurationrequest"></a>

Specifies configuration settings for retrieving occurrences of sensitive data reported by findings, and the status of the configuration for an Amazon Macie account. If you don't specify `retrievalConfiguration` settings for an existing configuration, Macie sets the access method to `CALLER_CREDENTIALS`. If your current access method is `ASSUME_ROLE`, Macie also deletes the external ID and role name currently specified for the configuration. To keep these settings for an existing configuration, specify your current `retrievalConfiguration` settings in your request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configuration | [RevealConfiguration](#reveal-configuration-model-revealconfiguration) | True | The AWS KMS key to use to encrypt the sensitive data, and the status of the configuration for the Amazon Macie account. |
| retrievalConfiguration | [UpdateRetrievalConfiguration](#reveal-configuration-model-updateretrievalconfiguration) | False | The access method and settings to use when retrieving the sensitive data. |

### UpdateRevealConfigurationResponse
<a name="reveal-configuration-model-updaterevealconfigurationresponse"></a>

Provides information about updated configuration settings for retrieving occurrences of sensitive data reported by findings, and the status of the configuration for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configuration | [RevealConfiguration](#reveal-configuration-model-revealconfiguration) | True | The AWS KMS key to use to encrypt the sensitive data, and the status of the configuration for the Amazon Macie account. |
| retrievalConfiguration | [RetrievalConfiguration](#reveal-configuration-model-retrievalconfiguration) | False | The access method and settings to use when retrieving the sensitive data. |

### ValidationException
<a name="reveal-configuration-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="reveal-configuration-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetRevealConfiguration
<a name="GetRevealConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetRevealConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetRevealConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetRevealConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetRevealConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetRevealConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetRevealConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetRevealConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetRevealConfiguration)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetRevealConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetRevealConfiguration)

### UpdateRevealConfiguration
<a name="UpdateRevealConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/UpdateRevealConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/UpdateRevealConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/UpdateRevealConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/UpdateRevealConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/UpdateRevealConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/UpdateRevealConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/UpdateRevealConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/UpdateRevealConfiguration)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/UpdateRevealConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/UpdateRevealConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Macie. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query macie` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
