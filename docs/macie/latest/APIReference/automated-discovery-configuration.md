---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/automated-discovery-configuration.html
---

# Automated Sensitive Data Discovery - Configuration
<a name="automated-discovery-configuration"></a>

The Configuration resource for automated sensitive data discovery provides access to configuration settings for performing automated sensitive data discovery, and the status of the configuration. To configure the settings or change the status of the configuration, you must be the Amazon Macie administrator for an organization or have a standalone Macie account.

If you enable automated sensitive data discovery, Macie continually evaluates your inventory of Amazon Simple Storage Service (Amazon S3) general purpose buckets and uses sampling techniques to identify and select representative objects in the buckets. Macie then retrieves and analyzes the selected objects, inspecting them for sensitive data. If you're the Macie administrator for an organization, by default this includes objects in buckets that your member accounts own.

You can monitor and review analyses' results in resource sensitivity profiles, statistical data, and other information that Macie produces and provides about your Amazon S3 data. These results are in addition to *sensitive data findings*, which report sensitive data that Macie finds in individual S3 objects, and *sensitive data discovery results*, which log details about the analysis of individual S3 objects. For more information, see [Performing automated sensitive data discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd.html) in the *Amazon Macie User Guide*.

To customize the analyses, change the configuration settings for your account. The settings include a *classification scope* and a *sensitivity inspection template*. The *classification scope* specifies S3 buckets that you want to exclude from analyses, such as buckets that typically store AWS logging data. The *sensitivity inspection template* specifies the allow lists, custom data identifiers, and managed data identifiers that you want Macie to use when it analyzes S3 objects. To change these settings, use the [Classification Scope](classification-scopes-id.md) and [Sensitivity Inspection Template](templates-sensitivity-inspections-id.md) resources.

If you're the Macie administrator for an organization, Macie uses the classification scope and sensitivity inspection template for your account when it analyzes data for other accounts in your organization. To refine the scope of the analyses, you have several options:
+ **Automatically include or exclude accounts** - When you enable automated sensitive data discovery, you also specify whether to enable it automatically for all existing accounts and new member accounts, only new member accounts, or no accounts. If it's enabled for an account, Macie includes S3 buckets that the account owns. If it's disabled for an account, Macie excludes buckets that the account owns.
+ **Include or exclude specific accounts** - After you enable automated sensitive data discovery, you can enable or disable it for individual accounts on a case-by-case basis. To do this, use the [Accounts](automated-discovery-accounts.md) resource for automated sensitive data discovery. If you enable it for an account, Macie includes S3 buckets that the account owns. If you disable it for an account, Macie excludes buckets that the account owns.
+ **Exclude specific S3 buckets** - If you enable automated sensitive data discovery for one or more accounts, you can exclude particular buckets that the accounts own. Macie then skips those buckets when it analyzes data for your organization. To exclude particular buckets, update the classification scope for your administrator account. You can do this by using the [Classification Scope](classification-scopes-id.md) resource.

If you disable automated sensitive data discovery for your organization or standalone account, Macie retains your configuration settings. However, Macie stops performing all automated sensitive data discovery activities for your organization or account. In addition, you lose access to all resource sensitivity profiles, statistical data, and other information that Macie produced and directly provided about your Amazon S3 data while performing those activities. This doesn't include sensitive data findings. Macie stores findings for 90 days.

After you disable automated sensitive data discovery for your organization or standalone account, you can enable it again. Macie then resumes all automated sensitive data discovery activities for your organization or account. If you re-enable it within 30 days, you regain access to resource sensitivity profiles, statistical data, and other information that Macie previously produced and directly provided while performing those activities. If you don't re-enable it within 30 days, Macie permanently deletes these profiles and the statistical data and other information that it produced and directly provided.

If you're the Macie administrator for an organization or you have a standalone Macie account, you can use the Configuration resource to retrieve your current configuration settings for automated sensitive data discovery. You can also enable or disable automated sensitive data discovery for your organization or account.

## URI
<a name="automated-discovery-configuration-url"></a>

`/automated-discovery/configuration`

## HTTP methods
<a name="automated-discovery-configuration-http-methods"></a>

### GET
<a name="automated-discovery-configurationget"></a>

**Operation ID:** `GetAutomatedDiscoveryConfiguration`

Retrieves the configuration settings and status of automated sensitive data discovery for an organization or standalone account.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetAutomatedDiscoveryConfigurationResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### PUT
<a name="automated-discovery-configurationput"></a>

**Operation ID:** `UpdateAutomatedDiscoveryConfiguration`

Changes the configuration settings and status of automated sensitive data discovery for an organization or standalone account.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty Schema | The request succeeded. The status was updated and there isn't any content to include in the body of the response (No Content). |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="automated-discovery-configuration-schemas"></a>

### Request bodies
<a name="automated-discovery-configuration-request-examples"></a>

#### PUT schema
<a name="automated-discovery-configuration-request-body-put-example"></a>

```
{
  "autoEnableOrganizationMembers": enum,
  "status": enum
}
```

### Response bodies
<a name="automated-discovery-configuration-response-examples"></a>

#### GetAutomatedDiscoveryConfigurationResponse schema
<a name="automated-discovery-configuration-response-body-getautomateddiscoveryconfigurationresponse-example"></a>

```
{
  "autoEnableOrganizationMembers": enum,
  "classificationScopeId": "string",
  "disabledAt": "string",
  "firstEnabledAt": "string",
  "lastUpdatedAt": "string",
  "sensitivityInspectionTemplateId": "string",
  "status": enum
}
```

#### Empty Schema schema
<a name="automated-discovery-configuration-response-body-empty-example"></a>

```
{
}
```

#### ValidationException schema
<a name="automated-discovery-configuration-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="automated-discovery-configuration-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="automated-discovery-configuration-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="automated-discovery-configuration-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="automated-discovery-configuration-properties"></a>

### AccessDeniedException
<a name="automated-discovery-configuration-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### AutoEnableMode
<a name="automated-discovery-configuration-model-autoenablemode"></a>

Specifies whether to automatically enable automated sensitive data discovery for accounts that are part of an organization in Amazon Macie. Valid values are:
+ `ALL`
+ `NEW`
+ `NONE`

### AutomatedDiscoveryStatus
<a name="automated-discovery-configuration-model-automateddiscoverystatus"></a>

The status of the automated sensitive data discovery configuration for an organization in Amazon Macie or a standalone Macie account. Valid values are:
+ `ENABLED`
+ `DISABLED`

### Empty
<a name="automated-discovery-configuration-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### GetAutomatedDiscoveryConfigurationResponse
<a name="automated-discovery-configuration-model-getautomateddiscoveryconfigurationresponse"></a>

Provides information about the configuration settings and status of automated sensitive data discovery for an organization in Amazon Macie or a standalone Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| autoEnableOrganizationMembers | [AutoEnableMode](#automated-discovery-configuration-model-autoenablemode) | False | Specifies whether automated sensitive data discovery is enabled automatically for accounts in the organization. Possible values are: `ALL`, enable it for all existing accounts and new member accounts; `NEW`, enable it only for new member accounts; and, `NONE`, don't enable it for any accounts. |
| classificationScopeId | string | False | The unique identifier for the classification scope that's used when performing automated sensitive data discovery. The classification scope specifies S3 buckets to exclude from analyses. |
| disabledAt | string | False | The date and time, in UTC and extended ISO 8601 format, when automated sensitive data discovery was most recently disabled. This value is null if automated sensitive data discovery is currently enabled. |
| firstEnabledAt | string | False | The date and time, in UTC and extended ISO 8601 format, when automated sensitive data discovery was initially enabled. This value is null if automated sensitive data discovery has never been enabled. |
| lastUpdatedAt | string | False | The date and time, in UTC and extended ISO 8601 format, when the configuration settings or status of automated sensitive data discovery was most recently changed. |
| sensitivityInspectionTemplateId | string | False | The unique identifier for the sensitivity inspection template that's used when performing automated sensitive data discovery. The template specifies which allow lists, custom data identifiers, and managed data identifiers to use when analyzing data. |
| status | [AutomatedDiscoveryStatus](#automated-discovery-configuration-model-automateddiscoverystatus) | False | The current status of automated sensitive data discovery for the organization or account. Possible values are: `ENABLED`, use the specified settings to perform automated sensitive data discovery activities; and, `DISABLED`, don't perform automated sensitive data discovery activities. |

### InternalServerException
<a name="automated-discovery-configuration-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="automated-discovery-configuration-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UpdateAutomatedDiscoveryConfigurationRequest
<a name="automated-discovery-configuration-model-updateautomateddiscoveryconfigurationrequest"></a>

Changes the configuration settings and status of automated sensitive data discovery for an organization in Amazon Macie or a standalone Macie account. To change additional settings, such as the managed data identifiers to use when analyzing data, update the sensitivity inspection template and classification scope for the organization's Macie administrator account or the standalone account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| autoEnableOrganizationMembers | [AutoEnableMode](#automated-discovery-configuration-model-autoenablemode) | False | Specifies whether to automatically enable automated sensitive data discovery for accounts in the organization. Valid values are: `ALL` (default), enable it for all existing accounts and new member accounts; `NEW`, enable it only for new member accounts; and, `NONE`, don't enable it for any accounts.<br />If you specify `NEW` or `NONE`, automated sensitive data discovery continues to be enabled for any existing accounts that it's currently enabled for. To enable or disable it for individual member accounts, specify `NEW` or `NONE`, and then enable or disable it for each account by using the `BatchUpdateAutomatedDiscoveryAccounts` operation. |
| status | [AutomatedDiscoveryStatus](#automated-discovery-configuration-model-automateddiscoverystatus) | True | The new status of automated sensitive data discovery for the organization or account. Valid values are: `ENABLED`, start or resume all automated sensitive data discovery activities; and, `DISABLED`, stop performing all automated sensitive data discovery activities.<br />If you specify `DISABLED` for an administrator account, you also disable automated sensitive data discovery for all member accounts in the organization.  |

### ValidationException
<a name="automated-discovery-configuration-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="automated-discovery-configuration-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetAutomatedDiscoveryConfiguration
<a name="GetAutomatedDiscoveryConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetAutomatedDiscoveryConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetAutomatedDiscoveryConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetAutomatedDiscoveryConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetAutomatedDiscoveryConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetAutomatedDiscoveryConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetAutomatedDiscoveryConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetAutomatedDiscoveryConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetAutomatedDiscoveryConfiguration)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/GetAutomatedDiscoveryConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetAutomatedDiscoveryConfiguration)

### UpdateAutomatedDiscoveryConfiguration
<a name="UpdateAutomatedDiscoveryConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/UpdateAutomatedDiscoveryConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/UpdateAutomatedDiscoveryConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/UpdateAutomatedDiscoveryConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/UpdateAutomatedDiscoveryConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/UpdateAutomatedDiscoveryConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/UpdateAutomatedDiscoveryConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/UpdateAutomatedDiscoveryConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/UpdateAutomatedDiscoveryConfiguration)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/UpdateAutomatedDiscoveryConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/UpdateAutomatedDiscoveryConfiguration)
