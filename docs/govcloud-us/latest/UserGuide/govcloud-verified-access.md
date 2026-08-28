---
source_url: https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-verified-access.html
---

# AWS Verified Access in AWS GovCloud (US)
<a name="govcloud-verified-access"></a>

AWS Verified Access provides secure access to corporate applications without a VPN connection. It evaluates each request in real time and determines whether the user has access to the application.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West)
+  AWS GovCloud (US-East)

## How AWS Verified Access differs
<a name="govcloud-diffs-32"></a>

The following differences apply to AWS Verified Access:
+ Use SSL (HTTPS) when you make calls to the service in the AWS GovCloud (US) Region. In other AWS Regions, you can use HTTP or HTTPS.
+ Non-HTTP endpoints are not available in the AWS GovCloud (US) Regions.

## Documentation
<a name="govcloud-docs-71"></a>
+  [Verified Access documentation](https://docs.aws.amazon.com/verified-access/landingpage.html)

## Export-controlled content
<a name="govcloud-itar-content-110"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Any metadata that you provide when setting up and maintaining your Verified Access resources, including all configuration data that you enter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS GovCloud (US). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query govcloud-us` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
