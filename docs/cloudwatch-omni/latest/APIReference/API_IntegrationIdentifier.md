---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_IntegrationIdentifier.html
---

# IntegrationIdentifier
<a name="API_IntegrationIdentifier"></a>

Identifies a single integration by exactly one of its unique keys: the integration id, the integration ARN, or the integration name.

## Contents
<a name="API_IntegrationIdentifier_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** integrationArn **   <a name="cloudwatchomni-Type-IntegrationIdentifier-integrationArn"></a>
The Amazon Resource Name of the integration.
Type: String
Required: No

 ** integrationId **   <a name="cloudwatchomni-Type-IntegrationIdentifier-integrationId"></a>
The unique identifier of the integration.
Type: String
Required: No

 ** integrationName **   <a name="cloudwatchomni-Type-IntegrationIdentifier-integrationName"></a>
The name of the integration; unique within the account.
Type: String
Required: No

## See Also
<a name="API_IntegrationIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/IntegrationIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/IntegrationIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/IntegrationIdentifier)
