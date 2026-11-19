---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_ConfigureTagsForOrganization.html
---

# ConfigureTagsForOrganization

Configures which tag keys are tracked by Health for all accounts in your organization. This operation replaces the existing configuration with the specified tag keys. Only configured tag keys will appear in Health event data across the organization.

## Request Syntax
<a name="API_ConfigureTagsForOrganization_RequestSyntax"></a>

```
{
   "tagKeys": [
      {
         "enabledForEventBridge": {{boolean}},
         "key": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ConfigureTagsForOrganization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [tagKeys](#API_ConfigureTagsForOrganization_RequestSyntax) **   <a name="AWSHealth-ConfigureTagsForOrganization-request-tagKeys"></a>
The list of tag keys to configure for Health event tracking across the organization.
Type: Array of [TagKeyForOrganization](API_TagKeyForOrganization.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_ConfigureTagsForOrganization_ResponseSyntax"></a>

```
{
   "configuredTagKeys": [
      {
         "enabledForEventBridge": boolean,
         "key": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ConfigureTagsForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuredTagKeys](#API_ConfigureTagsForOrganization_ResponseSyntax) **   <a name="AWSHealth-ConfigureTagsForOrganization-response-configuredTagKeys"></a>
The list of tag keys that were successfully configured for the organization, with the current status of each tag key.
Type: Array of [OrganizationTagKey](API_OrganizationTagKey.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

## Errors
<a name="API_ConfigureTagsForOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ConfigureTagsForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/ConfigureTagsForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/ConfigureTagsForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/ConfigureTagsForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/ConfigureTagsForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/ConfigureTagsForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/ConfigureTagsForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/ConfigureTagsForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/ConfigureTagsForOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/ConfigureTagsForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/ConfigureTagsForOrganization)
