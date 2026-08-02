---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/macie.html
---

# Account Administration
<a name="macie"></a>

The Account Administration resource provides access to the status of your Amazon Macie account, and certain configuration settings for the account.

You can use this resource to enable Macie for your AWS account. When you enable Macie, the service generates a Macie *session* for your AWS account in the current AWS Region. The service also assigns a unique identifier to that session. A *session* is a resource that represents the Macie service for a specific AWS account in a specific Region. It enables Macie to become operational in a Region. An AWS account can have only one Macie session in each Region.

After you enable Macie, you can use this resource to review or update certain Macie configuration settings. You can also use it to change the status of your Macie account. This includes suspending (pausing) and later re-enabling Macie. If you suspend Macie, the service stops performing all activities for your account and it cancels all of your classification jobs. However, the service retains the session identifier, settings, resources, and certain data that it stores or maintains for your account. For more information, see [ Suspending Macie](https://docs.aws.amazon.com/macie/latest/user/suspend-macie.html) in the *Amazon Macie User Guide*.

If you want to disable Macie completely, you can use this resource to do so. If you disable Macie, the service stops performing all activities for your account. In addition, the service permanently deletes all settings, resources, and data that it stores or maintains for your account. For example, Macie permanently deletes your findings, classification jobs, custom data identifiers, and the session resource and identifier for your account. For more information, see [Disabling Macie](https://docs.aws.amazon.com/macie/latest/user/disable-macie.html) in the *Amazon Macie User Guide*.

If your account is part of an organization that centrally manages multiple Macie accounts, you must do the following before you suspend or disable Macie for your account:
+ If your account is the Macie administrator account for the organization, you must remove all member accounts that are associated with your account before you suspend or disable Macie for your account. To disable Macie for your account, you must also delete the associations between your account and those accounts.
+ If you have a member account in the organization, you must disassociate your account from its Macie administrator account before you disable Macie for your account.

How you complete the preceding tasks depends on whether your account is associated with other accounts through AWS Organizations or by invitation. For more information, see [Managing multiple accounts](https://docs.aws.amazon.com/macie/latest/user/macie-accounts.html) in the *Amazon Macie User Guide*.

If Macie isn't enabled for your account and [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) uses the `GetMacieSession` operation on your behalf, Macie returns an HTTP 200 response with an empty body instead of an HTTP 403 response. For more information, see [Amazon Macie resource types](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#amazonmacie) in the *AWS Config Developer Guide*.

## URI
<a name="macie-url"></a>

`/macie`

## HTTP methods
<a name="macie-http-methods"></a>

### DELETE
<a name="maciedelete"></a>

**Operation ID:** `DisableMacie`

Disables Amazon Macie and deletes all settings and resources for a Macie account.

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
<a name="macieget"></a>

**Operation ID:** `GetMacieSession`

Retrieves the status and configuration settings for an Amazon Macie account.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetMacieSessionResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### PATCH
<a name="maciepatch"></a>

**Operation ID:** `UpdateMacieSession`

Suspends or re-enables Amazon Macie, or updates the configuration settings for a Macie account.

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

### POST
<a name="maciepost"></a>

**Operation ID:** `EnableMacie`

Enables Amazon Macie and specifies the configuration settings for a Macie account.

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
<a name="macie-schemas"></a>

### Request bodies
<a name="macie-request-examples"></a>

#### PATCH schema
<a name="macie-request-body-patch-example"></a>

```
{
  "findingPublishingFrequency": enum,
  "status": enum
}
```

#### POST schema
<a name="macie-request-body-post-example"></a>

```
{
  "clientToken": "string",
  "findingPublishingFrequency": enum,
  "status": enum
}
```

### Response bodies
<a name="macie-response-examples"></a>

#### Empty Schema schema
<a name="macie-response-body-empty-example"></a>

```
{
}
```

#### GetMacieSessionResponse schema
<a name="macie-response-body-getmaciesessionresponse-example"></a>

```
{
  "createdAt": "string",
  "findingPublishingFrequency": enum,
  "serviceRole": "string",
  "status": enum,
  "updatedAt": "string"
}
```

#### ValidationException schema
<a name="macie-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="macie-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="macie-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="macie-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="macie-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="macie-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="macie-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="macie-properties"></a>

### AccessDeniedException
<a name="macie-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="macie-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Empty
<a name="macie-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### EnableMacieRequest
<a name="macie-model-enablemacierequest"></a>

Enables Amazon Macie and specifies the configuration settings for a Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientToken | string | False | A unique, case-sensitive token that you provide to ensure the idempotency of the request. |
| findingPublishingFrequency | [FindingPublishingFrequency](#macie-model-findingpublishingfrequency) | False | Specifies how often to publish updates to policy findings for the account. This includes publishing updates to AWS Security Hub CSPM and Amazon EventBridge (formerly Amazon CloudWatch Events). |
| status | [MacieStatus](#macie-model-maciestatus) | False | Specifies the new status for the account. To enable Amazon Macie and start all Macie activities for the account, set this value to `ENABLED`. |

### FindingPublishingFrequency
<a name="macie-model-findingpublishingfrequency"></a>

The frequency with which Amazon Macie publishes updates to policy findings for an account. This includes publishing updates to AWS Security Hub CSPM and Amazon EventBridge (formerly Amazon CloudWatch Events). For more information, see [Monitoring and processing findings](https://docs.aws.amazon.com/macie/latest/user/findings-monitor.html) in the *Amazon Macie User Guide*. Valid values are:
+ `FIFTEEN_MINUTES`
+ `ONE_HOUR`
+ `SIX_HOURS`

### GetMacieSessionResponse
<a name="macie-model-getmaciesessionresponse"></a>

Provides information about the status and configuration settings for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| createdAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the Amazon Macie account was created. |
| findingPublishingFrequency | [FindingPublishingFrequency](#macie-model-findingpublishingfrequency) | False | The frequency with which Amazon Macie publishes updates to policy findings for the account. This includes publishing updates to AWS Security Hub CSPM and Amazon EventBridge (formerly Amazon CloudWatch Events). |
| serviceRole | string | False | The Amazon Resource Name (ARN) of the service-linked role that allows Amazon Macie to monitor and analyze data in AWS resources for the account. |
| status | [MacieStatus](#macie-model-maciestatus) | False | The current status of the Amazon Macie account. Possible values are: `PAUSED`, the account is enabled but all Macie activities are suspended (paused) for the account; and, `ENABLED`, the account is enabled and all Macie activities are enabled for the account. |
| updatedAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, of the most recent change to the status or configuration settings for the Amazon Macie account. |

### InternalServerException
<a name="macie-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### MacieStatus
<a name="macie-model-maciestatus"></a>

The status of an Amazon Macie account. Valid values are:
+ `PAUSED`
+ `ENABLED`

### ResourceNotFoundException
<a name="macie-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="macie-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="macie-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UpdateMacieSessionRequest
<a name="macie-model-updatemaciesessionrequest"></a>

Changes the status or configuration settings for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| findingPublishingFrequency | [FindingPublishingFrequency](#macie-model-findingpublishingfrequency) | False | Specifies how often to publish updates to policy findings for the account. This includes publishing updates to AWS Security Hub CSPM and Amazon EventBridge (formerly Amazon CloudWatch Events). |
| status | [MacieStatus](#macie-model-maciestatus) | False | Specifies a new status for the account. Valid values are: `ENABLED`, resume all Amazon Macie activities for the account; and, `PAUSED`, suspend all Macie activities for the account. |

### ValidationException
<a name="macie-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="macie-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DisableMacie
<a name="DisableMacie-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/DisableMacie)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/DisableMacie)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/DisableMacie)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/DisableMacie)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/DisableMacie)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/DisableMacie)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/DisableMacie)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/DisableMacie)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/DisableMacie)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/DisableMacie)

### GetMacieSession
<a name="GetMacieSession-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetMacieSession)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetMacieSession)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetMacieSession)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetMacieSession)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetMacieSession)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetMacieSession)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetMacieSession)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetMacieSession)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetMacieSession)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetMacieSession)

### UpdateMacieSession
<a name="UpdateMacieSession-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/UpdateMacieSession)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/UpdateMacieSession)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/UpdateMacieSession)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/UpdateMacieSession)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/UpdateMacieSession)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/UpdateMacieSession)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/UpdateMacieSession)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/UpdateMacieSession)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/UpdateMacieSession)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/UpdateMacieSession)

### EnableMacie
<a name="EnableMacie-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/EnableMacie)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/EnableMacie)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/EnableMacie)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/EnableMacie)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/EnableMacie)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/EnableMacie)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/EnableMacie)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/EnableMacie)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/EnableMacie)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/EnableMacie)
