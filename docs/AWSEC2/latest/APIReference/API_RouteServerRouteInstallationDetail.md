---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RouteServerRouteInstallationDetail.html
---

# RouteServerRouteInstallationDetail
<a name="API_RouteServerRouteInstallationDetail"></a>

Describes the installation status of a route in a route table.

## Contents
<a name="API_RouteServerRouteInstallationDetail_Contents"></a>

 ** routeInstallationStatus **
The current installation status of the route in the route table.
Type: String
Valid Values: `installed | rejected`
Required: No

 ** routeInstallationStatusReason **
The reason for the current installation status of the route.
Type: String
Required: No

 ** routeTableId **
The ID of the route table where the route is being installed.
Type: String
Required: No

## See Also
<a name="API_RouteServerRouteInstallationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RouteServerRouteInstallationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RouteServerRouteInstallationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RouteServerRouteInstallationDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
