---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/application-configuration.html
---

# Application configuration
<a name="application-configuration"></a>

Configuring SDK for SAP ABAP is similar to configuring other ABAP-based applications. It is organized into different *profiles* to group the settings of various scenarios. An ABAP SDK profile defines the settings required for a specific application scenario. For example, if transactions `ZVA01`, `ZVA02`, and `ZVA03` are invoice-related transactions enhanced and runs on AWS services, such as Amazon S3, AWS Lambda, and Amazon SageMaker AI, then an SDK profile called `ZINVOICE` can be made. This profile can group the technical settings, SAP authorizations, and IAM role mappings for the invoice-related functionality.

Use `/n/AWS1/IMG` transacation for AWS SDK for SAP ABAP, and Custom Business Configuration application for AWS SDK for SAP ABAP - BTP edition to configure the global settings. This topic uses IMG and Custom Business Configuration interchangeably.

**Topics**
+ [SDK profile](#sdk-profile)
+ [Logical resource resolver](#logical-resource)
+ [Example](#example)

## SDK profile
<a name="sdk-profile"></a>

An ABAP SDK profile defines the following for each SID and client.

**Note**
The client is always 100 in SAP BTP, ABAP environment.
+ The default AWS Region for all API calls. For example, if your SAP systems are running in the `us-east-1` Region, it is likely that your other AWS resources are also in the same Region, and this should be your default Region. Your ABAP code can override the default Region.
+ Authentication method
  + For SAP systems running on Amazon EC2, we strongly recommend choosing instance role metadata to benefit from the short-lived, automatically rotating credentials.
  + For SAP systems running on-premises or in another cloud, you must choose credentials from SSF storage.
  + For ABAP systems running on SAP BTP, you must choose credentials from SAP Credential Store. For more information, see [Using SAP Credential Store for authentication](https://docs.aws.amazon.com/).
  + For cross-account role chaining scenarios, choose Source Profile and specify a source profile ID. This enables automatic resolution and execution of role assumption chains. For more information, see [Using Source Profile for Cross-Account Access](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/source-profile.html).
+ A mapping of logical IAM roles to IAM roles.
  + This mapping is sorted in the order of descending priority.
  + An IAM role of highest priority for which a user is authorized in a PFCG role will automatically be selected for the user.
+ An optional mapping of services to custom endpoints. This configuration is discussed in [Advanced connectivity scenarios](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/connectivity-scenarios.html#advanced-routing)

**Note**
PFGC roles are called Business Roles in SAP BTP, ABAP environment.

When an ABAP program wants to connect to an AWS service, it will specify an ABAP SDK profile that pulls the necessary settings. An `AUTHORIZATION-CHECK` will be performed to confirm that the user has permissions to access the SDK profile. Your SAP Security Administrator can define a PFCG role granting you access to the appropriate users.

## Logical resource resolver
<a name="logical-resource"></a>

Logical resource resolver enables you with a standard place to store resource names. It ships with SDK for SAP ABAP. Its action is similar to the way that `FILE` transaction maps logical file names to physical file names.

A logical resource defines the concept of an AWS resource, such as the Amazon S3 bucket that holds our invoices. This logical resource, for example, can be named `ZINVOICES_OUTBOUND` and it can map to a different physical bucket name, depending on whether the SAP system is development, QA, or production.

SDK for SAP ABAP is set up such that a QA system resolves logical resources to the QA physical resources, even after a system refresh from production. The resource mappings for ALL systems is defined in your development SAP system and transported forward. This approach is different from the usual setup in SAP systems where the mapping is handled as master data and set in each system. The advantage of logical resource resolver offered by SDK for SAP ABAP is that the chances of a mistaken transport after system refreshes are almost none.

## Example
<a name="example"></a>

There are four separate Amazon S3 buckets - one each for development, production, and QA, as well as a second QA bucket for regression testing.

When the SDK resolves a logical resource like `ZINVOICE_OUTBOUND` to a physical resource, it checks `SY-SYSID` and `SY-MANDT` to ask *Which SID and client am I running in?*, and automatically selects the correct physical resource.

If the mapping of a resource in production needs to change, you must change the mapping in the `IMG` of the development system and transport it forward. This ensures that reassigning AWS resources to an SAP system is subject to change control as with any other transport.

**Note**
As the SDK configuration is client-dependent, reassignment of resources is transported in a customizing request, and the transport must be imported into each client.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
