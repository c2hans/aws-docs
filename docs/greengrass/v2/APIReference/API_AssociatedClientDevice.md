---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_AssociatedClientDevice.html
---

# AssociatedClientDevice
<a name="API_AssociatedClientDevice"></a>

Contains information about a client device that is associated to a core device for cloud discovery.

## Contents
<a name="API_AssociatedClientDevice_Contents"></a>

 ** associationTimestamp **   <a name="greengrassv2-Type-AssociatedClientDevice-associationTimestamp"></a>
The time that the client device was associated, expressed in ISO 8601 format.
Type: Timestamp
Required: No

 ** thingName **   <a name="greengrassv2-Type-AssociatedClientDevice-thingName"></a>
The name of the AWS IoT thing that represents the associated client device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_AssociatedClientDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/AssociatedClientDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/AssociatedClientDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/AssociatedClientDevice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
