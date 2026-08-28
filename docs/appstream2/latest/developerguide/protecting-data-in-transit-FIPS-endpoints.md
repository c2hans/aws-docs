---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/protecting-data-in-transit-FIPS-endpoints.html
---

# Protecting Data in Transit with FIPS Endpoints
<a name="protecting-data-in-transit-FIPS-endpoints"></a>

By default, when you communicate with the WorkSpaces Applications service, whether as an administrator using the WorkSpaces Applications console, the AWS Command Line Interface (AWS CLI), or an AWS SDK, or as a user streaming from an image builder or a fleet instance, all data in transit is encrypted using TLS 1.2.

If you require FIPS 140-2 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. WorkSpaces Applications offers FIPS endpoints in all United States AWS Regions where WorkSpaces Applications is available. When you use a FIPS endpoint, all data in transit is encrypted using cryptographic standards that comply with Federal Information Processing Standard (FIPS) 140-2. For information about FIPS endpoints, including a list of WorkSpaces Applications endpoints, see [Federal Information Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips).

**Topics**
+ [FIPS Endpoints for Administrative Use](FIPS-for-administrative-use.md)
+ [FIPS Endpoints for User Streaming Sessions](FIPS-for-user-streaming-sessions.md)
+ [Exceptions](FIPS-exceptions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
