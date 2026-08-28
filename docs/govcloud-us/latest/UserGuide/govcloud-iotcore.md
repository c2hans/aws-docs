---
source_url: https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-iotcore.html
---

# AWS IoT Core in AWS GovCloud (US)
<a name="govcloud-iotcore"></a>

AWS IoT enables secure, bi-directional communication between Internet-connected things (such as sensors, actuators, embedded devices, or smart appliances) and the AWS Cloud over MQTT and HTTP.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West)
+  AWS GovCloud (US-East)

## How AWS IoT Core differs
<a name="govcloud-iotcore-diffs"></a>

The following differences apply to AWS IoT Core:
+ Use of Amazon Cognito Identities to grant permissions to users of your AWS IoT applications, via your own identity provider or other popular identity providers, is not available.

## Documentation
<a name="govcloud-iotcore-docs"></a>
+  [AWS IoT Core documentation](https://docs.aws.amazon.com/documentation/iot/)

## Export-controlled content
<a name="govcloud-iotcore-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Message topics and topic filters
+ Thing names
+ Thing types
+ Thing group names
+ Rule definitions (including SQL statements and actions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS GovCloud (US). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query govcloud-us` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
