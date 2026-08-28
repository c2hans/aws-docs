---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_EbsInstanceBlockDevice.html
---

# EbsInstanceBlockDevice
<a name="API_devicemanagement_EbsInstanceBlockDevice"></a>

Describes a parameter used to set up an Amazon Elastic Block Store (Amazon EBS) volume in a block device mapping.

## Contents
<a name="API_devicemanagement_EbsInstanceBlockDevice_Contents"></a>

 ** attachTime **   <a name="Snowball-Type-devicemanagement_EbsInstanceBlockDevice-attachTime"></a>
When the attachment was initiated.
Type: Timestamp
Required: No

 ** deleteOnTermination **   <a name="Snowball-Type-devicemanagement_EbsInstanceBlockDevice-deleteOnTermination"></a>
A value that indicates whether the volume is deleted on instance termination.
Type: Boolean
Required: No

 ** status **   <a name="Snowball-Type-devicemanagement_EbsInstanceBlockDevice-status"></a>
The attachment state.
Type: String
Valid Values: `ATTACHING | ATTACHED | DETACHING | DETACHED`
Required: No

 ** volumeId **   <a name="Snowball-Type-devicemanagement_EbsInstanceBlockDevice-volumeId"></a>
The ID of the Amazon EBS volume.
Type: String
Required: No

## See Also
<a name="API_devicemanagement_EbsInstanceBlockDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/EbsInstanceBlockDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/EbsInstanceBlockDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/EbsInstanceBlockDevice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
