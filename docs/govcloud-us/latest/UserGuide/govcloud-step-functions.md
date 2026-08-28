---
source_url: https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-step-functions.html
---

# AWS Step Functions in AWS GovCloud (US)
<a name="govcloud-step-functions"></a>

AWS Step Functions makes it easy to coordinate the components of distributed applications as a series of steps in a visual workflow. You can quickly build and run state machines to execute the steps of your application in a reliable and scalable fashion.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West)
+  AWS GovCloud (US-East)

## How AWS Step Functions differs
<a name="govcloud-sf-diffs"></a>

The following differences apply to AWS Step Functions:
+ US Commercial Regions supports FIPS and Non-FIPS endpoints.
+ US GovCloud East supports FIPS and Non-FIPS endpoints.
+ US GovCloud West only supports FIPS endpoints.
+ US Commercial Regions only supports AWS PrivateLink for Non-FIPS endpoints.
+ US GovCloud East Region only supports AWS PrivateLink for FIPS endpoints.
+ US GovCloud West Region only supports AWS PrivateLink for FIPS endpoints.
+ Support to call HTTPS APIs is not available.

## Documentation
<a name="govcloud-sf-docs"></a>
+  [AWS Step Functions documentation](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)

## Export-controlled content
<a name="govcloud-step-functions-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ No data will leave the AWS GovCloud (US) Regions for this service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS GovCloud (US). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query govcloud-us` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
