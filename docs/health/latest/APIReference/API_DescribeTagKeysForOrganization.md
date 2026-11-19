---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeTagKeysForOrganization.html
---

# DescribeTagKeysForOrganization

Returns the list of tag keys configured for Health event tracking across your organization.

## Response Syntax
<a name="API_DescribeTagKeysForOrganization_ResponseSyntax"></a>

```
{
   "keys": [
      {
         "enabledForEventBridge": boolean,
         "key": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeTagKeysForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [keys](#API_DescribeTagKeysForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeTagKeysForOrganization-response-keys"></a>
The list of configured tag keys for the organization and their status.
Type: Array of [OrganizationTagKey](API_OrganizationTagKey.md) objects

## Errors
<a name="API_DescribeTagKeysForOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeTagKeysForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeTagKeysForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeTagKeysForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeTagKeysForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeTagKeysForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeTagKeysForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeTagKeysForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeTagKeysForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeTagKeysForOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeTagKeysForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeTagKeysForOrganization)
