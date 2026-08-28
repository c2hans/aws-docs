---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribedWebAppEndpointDetails.html
---

# DescribedWebAppEndpointDetails
<a name="API_DescribedWebAppEndpointDetails"></a>

Contains the endpoint configuration details for a web app, including VPC configuration when the endpoint is hosted within a VPC.

## Contents
<a name="API_DescribedWebAppEndpointDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Vpc **   <a name="TransferFamily-Type-DescribedWebAppEndpointDetails-Vpc"></a>
The VPC configuration details when the web app endpoint is hosted within a VPC. This includes the VPC ID, subnet IDs, and VPC endpoint ID.
Type: [DescribedWebAppVpcConfig](API_DescribedWebAppVpcConfig.md) object
Required: No

## See Also
<a name="API_DescribedWebAppEndpointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribedWebAppEndpointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribedWebAppEndpointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribedWebAppEndpointDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
