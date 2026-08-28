---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TotalLocalStorageGBRequest.html
---

# TotalLocalStorageGBRequest
<a name="API_TotalLocalStorageGBRequest"></a>

The minimum and maximum total local storage in gigabytes (GB) for instance types with local storage. This is useful for workloads that require local storage for temporary data or caching.

## Contents
<a name="API_TotalLocalStorageGBRequest_Contents"></a>

 ** max **   <a name="ECS-Type-TotalLocalStorageGBRequest-max"></a>
The maximum total local storage in GB. Instance types with more local storage are excluded from selection.
Type: Double
Required: No

 ** min **   <a name="ECS-Type-TotalLocalStorageGBRequest-min"></a>
The minimum total local storage in GB. Instance types with less local storage are excluded from selection.
Type: Double
Required: No

## See Also
<a name="API_TotalLocalStorageGBRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/TotalLocalStorageGBRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/TotalLocalStorageGBRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/TotalLocalStorageGBRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
