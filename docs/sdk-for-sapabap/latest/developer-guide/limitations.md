---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/limitations.html
---

# Limitations
<a name="limitations"></a>

AWS SDK for SAP ABAP includes SDK modules for all AWS services. Some of these modules may have limitations, as described here.
+ Modules that rely on `MQTT` protocol bindings, such as `iotevents`, will not work. `MQTT` is not an HTTP-based protocol and is currently not supported by AWS SDK for SAP ABAP.
+ Operations that return event streams are supported, but will wait until the entire stream is received before returning control to ABAP. Examples are Amazon Bedrock Agents Runtime `InvokeAgent` and AWS Lambda `InvokeWithResponseStream`
+ Operations that receive event streams are not supported due to limitations in the underlying ABAP platform. Examples are Amazon Q Business `Chat` and Amazon Lex `StartConversation`

AWS SDK for SAP ABAP has the following feature limitations.
+ The following Amazon S3 features are not yet supported.
  + Multi-Region access points
  + Amazon S3 client-side encryption

AWS SDK for SAP ABAP - BTP edition has the following limitations during the developer preview.
+ Some modules may not be available.
+ It cannot be uninstalled.
+ It is updated less frequently.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
