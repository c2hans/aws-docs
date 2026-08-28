---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Deployment.html
---

# Deployment
<a name="API_Deployment"></a>

Contains information about a deployment.

## Contents
<a name="API_Deployment_Contents"></a>

 ** creationTimestamp **   <a name="greengrassv2-Type-Deployment-creationTimestamp"></a>
The time at which the deployment was created, expressed in ISO 8601 format.
Type: Timestamp
Required: No

 ** deploymentId **   <a name="greengrassv2-Type-Deployment-deploymentId"></a>
The ID of the deployment.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** deploymentName **   <a name="greengrassv2-Type-Deployment-deploymentName"></a>
The name of the deployment.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** deploymentStatus **   <a name="greengrassv2-Type-Deployment-deploymentStatus"></a>
The status of the deployment.
Type: String
Valid Values: `ACTIVE | COMPLETED | CANCELED | FAILED | INACTIVE`
Required: No

 ** isLatestForTarget **   <a name="greengrassv2-Type-Deployment-isLatestForTarget"></a>
Whether or not the deployment is the latest revision for its target.
Type: Boolean
Required: No

 ** parentTargetArn **   <a name="greengrassv2-Type-Deployment-parentTargetArn"></a>
The parent deployment's target [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) within a subdeployment.
Type: String
Pattern: `arn:[^:]*:iot:[^:]*:[0-9]+:(thing|thinggroup)/.+`
Required: No

 ** revisionId **   <a name="greengrassv2-Type-Deployment-revisionId"></a>
The revision number of the deployment.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** targetArn **   <a name="greengrassv2-Type-Deployment-targetArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the target AWS IoT thing or thing group. When creating a subdeployment, the targetARN can only be a thing group.
Type: String
Pattern: `arn:[^:]*:iot:[^:]*:[0-9]+:(thing|thinggroup)/.+`
Required: No

## See Also
<a name="API_Deployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/Deployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/Deployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/Deployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
