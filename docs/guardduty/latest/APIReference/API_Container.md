---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Container.html
---

# Container
<a name="API_Container"></a>

Details of a container.

## Contents
<a name="API_Container_Contents"></a>

 ** containerRuntime **   <a name="guardduty-Type-Container-containerRuntime"></a>
The container runtime (such as, Docker or containerd) used to run the container.
Type: String
Required: No

 ** id **   <a name="guardduty-Type-Container-id"></a>
Container ID.
Type: String
Required: No

 ** image **   <a name="guardduty-Type-Container-image"></a>
Container image.
Type: String
Required: No

 ** imagePrefix **   <a name="guardduty-Type-Container-imagePrefix"></a>
Part of the image name before the last slash. For example, imagePrefix for public.ecr.aws/amazonlinux/amazonlinux:latest would be public.ecr.aws/amazonlinux. If the image name is relative and does not have a slash, this field is empty.
Type: String
Required: No

 ** name **   <a name="guardduty-Type-Container-name"></a>
Container name.
Type: String
Required: No

 ** securityContext **   <a name="guardduty-Type-Container-securityContext"></a>
Container security context.
Type: [SecurityContext](API_SecurityContext.md) object
Required: No

 ** volumeMounts **   <a name="guardduty-Type-Container-volumeMounts"></a>
Container volume mounts.
Type: Array of [VolumeMount](API_VolumeMount.md) objects
Required: No

## See Also
<a name="API_Container_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Container)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Container)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Container)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
