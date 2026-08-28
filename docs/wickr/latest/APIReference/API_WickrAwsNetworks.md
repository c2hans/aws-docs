---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_WickrAwsNetworks.html
---

# WickrAwsNetworks
<a name="API_WickrAwsNetworks"></a>

Identifies a AWS Wickr network by region and network ID, used for configuring permitted networks for global federation.

## Contents
<a name="API_WickrAwsNetworks_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** networkId **   <a name="wickr-Type-WickrAwsNetworks-networkId"></a>
The network ID of the Wickr AWS network.
Type: String
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: Yes

 ** region **   <a name="wickr-Type-WickrAwsNetworks-region"></a>
The AWS region identifier where the network is hosted (e.g., 'us-east-1').
Type: String
Pattern: `[\S\s]*`
Required: Yes

## See Also
<a name="API_WickrAwsNetworks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/WickrAwsNetworks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/WickrAwsNetworks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/WickrAwsNetworks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
