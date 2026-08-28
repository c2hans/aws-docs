---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_RetrievedService.html
---

# RetrievedService
<a name="API_RetrievedService"></a>

 Retrieved information about an application that processed requests, users that made requests, or downstream services, resources, and applications that an application used.

## Contents
<a name="API_RetrievedService_Contents"></a>

 ** Links **   <a name="xray-Type-RetrievedService-Links"></a>
 Relation between two 2 services.
Type: Array of [GraphLink](API_GraphLink.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Service **   <a name="xray-Type-RetrievedService-Service"></a>
Information about an application that processed requests, users that made requests, or downstream services, resources, and applications that an application used.
Type: [Service](API_Service.md) object
Required: No

## See Also
<a name="API_RetrievedService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/RetrievedService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/RetrievedService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/RetrievedService)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
