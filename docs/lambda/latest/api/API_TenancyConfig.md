---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_TenancyConfig.html
---

# TenancyConfig
<a name="API_TenancyConfig"></a>

Specifies the tenant isolation mode configuration for a Lambda function. This allows you to configure specific tenant isolation strategies for your function invocations. Tenant isolation configuration cannot be modified after function creation.

## Contents
<a name="API_TenancyConfig_Contents"></a>

 ** TenantIsolationMode **   <a name="lambda-Type-TenancyConfig-TenantIsolationMode"></a>
Tenant isolation mode allows for invocation to be sent to a corresponding execution environment dedicated to a specific tenant ID.
Type: String
Valid Values: `PER_TENANT`
Required: Yes

## See Also
<a name="API_TenancyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/TenancyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/TenancyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/TenancyConfig)
