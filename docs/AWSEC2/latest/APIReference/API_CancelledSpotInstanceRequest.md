---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelledSpotInstanceRequest.html
---

# CancelledSpotInstanceRequest
<a name="API_CancelledSpotInstanceRequest"></a>

Describes a request to cancel a Spot Instance.

## Contents
<a name="API_CancelledSpotInstanceRequest_Contents"></a>

 ** spotInstanceRequestId **
The ID of the Spot Instance request.
Type: String
Required: No

 ** state **
The state of the Spot Instance request.
Type: String
Valid Values: `active | open | closed | cancelled | completed`
Required: No

## See Also
<a name="API_CancelledSpotInstanceRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CancelledSpotInstanceRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CancelledSpotInstanceRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CancelledSpotInstanceRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
