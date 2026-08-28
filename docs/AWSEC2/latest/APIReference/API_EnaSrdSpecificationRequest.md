---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnaSrdSpecificationRequest.html
---

# EnaSrdSpecificationRequest
<a name="API_EnaSrdSpecificationRequest"></a>

Launch instances with ENA Express settings configured from your launch template.

## Contents
<a name="API_EnaSrdSpecificationRequest_Contents"></a>

 ** EnaSrdEnabled ** (request), ** EnaSrdEnabled ** (response)
Specifies whether ENA Express is enabled for the network interface when you launch an instance.
Type: Boolean
Required: No

 ** EnaSrdUdpSpecification ** (request), ** EnaSrdUdpSpecification ** (response)
Contains ENA Express settings for UDP network traffic for the network interface attached to the instance.
Type: [EnaSrdUdpSpecificationRequest](API_EnaSrdUdpSpecificationRequest.md) object
Required: No

## See Also
<a name="API_EnaSrdSpecificationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EnaSrdSpecificationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EnaSrdSpecificationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EnaSrdSpecificationRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
