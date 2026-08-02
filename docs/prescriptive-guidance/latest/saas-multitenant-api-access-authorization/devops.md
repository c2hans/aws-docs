---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/devops.html
---

# DevOps, monitoring, logging, and retrieving data for a PDP
<a name="devops"></a>

In this proposed authorization paradigm, policies are centralized in the authorization service. This centralization is deliberate because one of the goals of the design models discussed in this guide is to achieve *policy decoupling*, or the removal of authorization logic from other components in the application. Both Amazon Verified Permissions and the Open Policy Agent (OPA) provide mechanisms for updating policies when changes to authorization logic are necessary.

In the case of Verified Permissions, mechanisms for programmatically updating policies are offered by the AWS SDK (see the [Amazon Verified Permissions API Reference Guide](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/Welcome.html)). Using the SDK, you can push new policies on demand. Additionally, because Verified Permissions is a managed service, you don't have to manage, configure, or maintain control planes or agents to perform updates. However, we recommend that you use a continuous integration and continuous deployment (CI/CD) pipeline to administer the deployment of Verified Permissions policy stores and policy updates using the AWS SDK.

Verified Permissions provides easy access to observability features. It can be configured to log all access attempts to AWS CloudTrail, Amazon CloudWatch log groups, Amazon Simple Storage Service (Amazon S3) buckets, or Amazon Data Firehose delivery streams to enable a quick response to security incidents and audit requests. Additionally, you can monitor the health of the Verified Permissions service through the AWS Health Dashboard. Because Verified Permissions is a managed service, its health is maintained by AWS, and you can configure observability features by using other AWS managed services.

In the case of OPA, REST APIs offer ways to programmatically update policies. You can configure the APIs to pull new versions of policy bundles from established locations or to push policies on demand. Additionally, OPA offers a basic discovery service where new agents can be configured dynamically and managed centrally by a control plane that distributes discovery bundles. (The control plane for OPA must be set up and configured by the OPA operator.) We recommend that you create a robust CI/CD pipeline for versioning, verifying, and updating policies, whether the policy engine is Verified Permissions, OPA, or another solution.

For OPA, the control plane also provides options for monitoring and auditing. You can export the logs that contain OPA's authorization decisions to remote HTTP servers for log aggregation. These decision logs are invaluable for auditing purposes.

If you are considering adopting an authorization model where access control decisions are decoupled from your application, make sure that your authorization service has effective monitoring, logging, and CI/CD management capabilities for onboarding new PDPs or updating policies.
