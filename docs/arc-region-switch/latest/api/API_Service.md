---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Service.html
---

# Service
<a name="API_Service"></a>

The service for a cross account role.

## Contents
<a name="API_Service_Contents"></a>

 ** clusterArn **   <a name="regionswitch-Type-Service-clusterArn"></a>
The cluster Amazon Resource Name (ARN) for a service.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:ecs:[a-z0-9-]+:\d{12}:cluster/[a-zA-Z0-9_-]{1,255}`
Required: No

 ** crossAccountRole **   <a name="regionswitch-Type-Service-crossAccountRole"></a>
The cross account role for a service.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** externalId **   <a name="regionswitch-Type-Service-externalId"></a>
The external ID (secret key) for the service.
Type: String
Required: No

 ** serviceArn **   <a name="regionswitch-Type-Service-serviceArn"></a>
The Amazon Resource Name (ARN) for a service.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:ecs:[a-z0-9-]+:\d{12}:service/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]{1,255}`
Required: No

## See Also
<a name="API_Service_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/Service)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/Service)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/Service)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
