---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_PermittedWickrEnterpriseNetwork.html
---

# PermittedWickrEnterpriseNetwork
<a name="API_PermittedWickrEnterpriseNetwork"></a>

Identifies a Wickr enterprise network that is permitted for global federation, allowing users to communicate with members of the specified network.

## Contents
<a name="API_PermittedWickrEnterpriseNetwork_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** domain **   <a name="wickr-Type-PermittedWickrEnterpriseNetwork-domain"></a>
The domain identifier for the permitted Wickr enterprise network.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** networkId **   <a name="wickr-Type-PermittedWickrEnterpriseNetwork-networkId"></a>
The network ID of the permitted Wickr enterprise network.
Type: String
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: Yes

## See Also
<a name="API_PermittedWickrEnterpriseNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/PermittedWickrEnterpriseNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/PermittedWickrEnterpriseNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/PermittedWickrEnterpriseNetwork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
