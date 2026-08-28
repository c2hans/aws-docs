---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_NodeFilter.html
---

# NodeFilter
<a name="API_NodeFilter"></a>

The filters for the operation.

## Contents
<a name="API_NodeFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-NodeFilter-Key"></a>
The name of the filter.
Type: String
Valid Values: `AgentType | AgentVersion | ComputerName | InstanceId | InstanceStatus | IpAddress | ManagedStatus | PlatformName | PlatformType | PlatformVersion | ResourceType | OrganizationalUnitId | OrganizationalUnitPath | Region | AccountId | SourceType | SourceId | SourceLocation | AvailabilityZone | AvailabilityZoneId`
Required: Yes

 ** Values **   <a name="systemsmanager-Type-NodeFilter-Values"></a>
A filter value supported by the specified key. For example, for the key `PlatformType`, supported values include `Linux` and `Windows`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** Type **   <a name="systemsmanager-Type-NodeFilter-Type"></a>
The type of filter operator.
Type: String
Valid Values: `Equal | NotEqual | BeginWith`
Required: No

## See Also
<a name="API_NodeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/NodeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/NodeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/NodeFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
