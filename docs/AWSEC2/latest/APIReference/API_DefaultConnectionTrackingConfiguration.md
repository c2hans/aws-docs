---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DefaultConnectionTrackingConfiguration.html
---

# DefaultConnectionTrackingConfiguration
<a name="API_DefaultConnectionTrackingConfiguration"></a>

Indicates default conntrack information for the instance type. For more information, see [ Connection tracking timeouts ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts) in the Amazon EC2 User Guide.

## Contents
<a name="API_DefaultConnectionTrackingConfiguration_Contents"></a>

 ** defaultTcpEstablishedTimeout **
Default timeout (in seconds) for idle TCP connections in an established state.
Type: Integer
Required: No

 ** defaultUdpStreamTimeout **
Default timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction.
Type: Integer
Required: No

 ** defaultUdpTimeout **
Default timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction.
Type: Integer
Required: No

## See Also
<a name="API_DefaultConnectionTrackingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DefaultConnectionTrackingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DefaultConnectionTrackingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DefaultConnectionTrackingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
