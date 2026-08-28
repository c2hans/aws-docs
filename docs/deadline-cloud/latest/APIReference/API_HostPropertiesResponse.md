---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_HostPropertiesResponse.html
---

# HostPropertiesResponse
<a name="API_HostPropertiesResponse"></a>

The host property details.

## Contents
<a name="API_HostPropertiesResponse_Contents"></a>

 ** ec2InstanceArn **   <a name="deadlinecloud-Type-HostPropertiesResponse-ec2InstanceArn"></a>
The ARN of the host EC2 instance.
Type: String
Required: No

 ** ec2InstanceType **   <a name="deadlinecloud-Type-HostPropertiesResponse-ec2InstanceType"></a>
The instance type of the host EC2 instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** hostName **   <a name="deadlinecloud-Type-HostPropertiesResponse-hostName"></a>
The host name.
Type: String
Pattern: `[a-zA-Z0-9_\.\-]{0,255}`
Required: No

 ** ipAddresses **   <a name="deadlinecloud-Type-HostPropertiesResponse-ipAddresses"></a>
The IP address of the host.
Type: [IpAddresses](API_IpAddresses.md) object
Required: No

## See Also
<a name="API_HostPropertiesResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/HostPropertiesResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/HostPropertiesResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/HostPropertiesResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
