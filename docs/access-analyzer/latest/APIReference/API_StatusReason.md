---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_StatusReason.html
---

# StatusReason
<a name="API_StatusReason"></a>

Provides more details about the current status of the analyzer. For example, if the creation for the analyzer fails, a `Failed` status is returned. For an analyzer with organization as the type, this failure can be due to an issue with creating the service-linked roles required in the member accounts of the AWS organization.

## Contents
<a name="API_StatusReason_Contents"></a>

 ** code **   <a name="accessanalyzer-Type-StatusReason-code"></a>
The reason code for the current status of the analyzer.
Type: String
Valid Values: `AWS_SERVICE_ACCESS_DISABLED | DELEGATED_ADMINISTRATOR_DEREGISTERED | ORGANIZATION_DELETED | SERVICE_LINKED_ROLE_CREATION_FAILED`
Required: Yes

## See Also
<a name="API_StatusReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/StatusReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/StatusReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/StatusReason)
