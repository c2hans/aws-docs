---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_MonitoredResourceIdentifier.html
---

# MonitoredResourceIdentifier
<a name="API_MonitoredResourceIdentifier"></a>

 Information about the resource that is being monitored, including the name of the resource, the type of resource, and whether or not permission is given to DevOps Guru to access that resource.

## Contents
<a name="API_MonitoredResourceIdentifier_Contents"></a>

 ** LastUpdated **   <a name="DevOpsGuru-Type-MonitoredResourceIdentifier-LastUpdated"></a>
 The time at which DevOps Guru last updated this resource.
Type: Timestamp
Required: No

 ** MonitoredResourceName **   <a name="DevOpsGuru-Type-MonitoredResourceIdentifier-MonitoredResourceName"></a>
 The name of the resource being monitored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_\/#A-Za-z0-9]+`
Required: No

 ** ResourceCollection **   <a name="DevOpsGuru-Type-MonitoredResourceIdentifier-ResourceCollection"></a>
 A collection of AWS resources supported by DevOps Guru. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks.
Type: [ResourceCollection](API_ResourceCollection.md) object
Required: No

 ** ResourcePermission **   <a name="DevOpsGuru-Type-MonitoredResourceIdentifier-ResourcePermission"></a>
 The permission status of a resource.
Type: String
Valid Values: `FULL_PERMISSION | MISSING_PERMISSION`
Required: No

 ** Type **   <a name="DevOpsGuru-Type-MonitoredResourceIdentifier-Type"></a>
 The type of resource being monitored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z]+[a-zA-Z0-9-_:]*$`
Required: No

## See Also
<a name="API_MonitoredResourceIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/MonitoredResourceIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/MonitoredResourceIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/MonitoredResourceIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
