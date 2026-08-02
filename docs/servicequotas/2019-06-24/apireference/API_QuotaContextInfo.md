---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_QuotaContextInfo.html
---

# QuotaContextInfo
<a name="API_QuotaContextInfo"></a>

A structure that describes the context for a resource-level quota. For resource-level quotas, such as `Instances per OpenSearch Service Domain`, you can apply the quota value at the resource-level for each OpenSearch Service Domain in your AWS account. Together the attributes of this structure help you understand how the quota is implemented by AWS and how you can manage it. For quotas such as `Amazon OpenSearch Service Domains` which can be managed at the account-level for each AWS Region, the `QuotaContext` field is absent. See the attribute descriptions below to further understand how to use them.

## Contents
<a name="API_QuotaContextInfo_Contents"></a>

 ** ContextId **   <a name="servicequotas-Type-QuotaContextInfo-ContextId"></a>
Specifies the resource, or resources, to which the quota applies. The value for this field is either an Amazon Resource Name (ARN) or \*. If the value is an ARN, the quota value applies to that resource. If the value is \*, then the quota value applies to all resources listed in the `ContextScopeType` field. The quota value applies to all resources for which you haven’t previously applied a quota value, and any new resources you create in your AWS account.
Type: String
Required: No

 ** ContextScope **   <a name="servicequotas-Type-QuotaContextInfo-ContextScope"></a>
Specifies the scope to which the quota value is applied. If the scope is `RESOURCE`, the quota value is applied to each resource in the AWS account. If the scope is `ACCOUNT`, the quota value is applied to the AWS account.
Type: String
Valid Values: `RESOURCE | ACCOUNT`
Required: No

 ** ContextScopeType **   <a name="servicequotas-Type-QuotaContextInfo-ContextScopeType"></a>
Specifies the resource type to which the quota can be applied.
Type: String
Required: No

## See Also
<a name="API_QuotaContextInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/QuotaContextInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/QuotaContextInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/QuotaContextInfo)
