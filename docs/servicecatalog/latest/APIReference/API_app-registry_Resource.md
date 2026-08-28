---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_Resource.html
---

# Resource
<a name="API_app-registry_Resource"></a>

 The information about the resource.

## Contents
<a name="API_app-registry_Resource_Contents"></a>

 ** arn **   <a name="servicecatalog-Type-app-registry_Resource-arn"></a>
The Amazon resource name (ARN) of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
Required: No

 ** associationTime **   <a name="servicecatalog-Type-app-registry_Resource-associationTime"></a>
The time the resource was associated with the application.
Type: Timestamp
Required: No

 ** integrations **   <a name="servicecatalog-Type-app-registry_Resource-integrations"></a>
The service integration information about the resource.
Type: [ResourceIntegrations](API_app-registry_ResourceIntegrations.md) object
Required: No

 ** name **   <a name="servicecatalog-Type-app-registry_Resource-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: No

## See Also
<a name="API_app-registry_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/Resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
