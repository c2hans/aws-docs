---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VerifiedAccessInstance.html
---

# VerifiedAccessInstance
<a name="API_VerifiedAccessInstance"></a>

Describes a Verified Access instance.

## Contents
<a name="API_VerifiedAccessInstance_Contents"></a>

 ** cidrEndpointsCustomSubDomain **
The custom subdomain.
Type: [VerifiedAccessInstanceCustomSubDomain](API_VerifiedAccessInstanceCustomSubDomain.md) object
Required: No

 ** creationTime **
The creation time.
Type: String
Required: No

 ** description **
A description for the AWS Verified Access instance.
Type: String
Required: No

 ** fipsEnabled **
Indicates whether support for Federal Information Processing Standards (FIPS) is enabled on the instance.
Type: Boolean
Required: No

 ** lastUpdatedTime **
The last updated time.
Type: String
Required: No

 ** TagSet.N **
The tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** verifiedAccessInstanceId **
The ID of the AWS Verified Access instance.
Type: String
Required: No

 ** VerifiedAccessTrustProviderSet.N **
The IDs of the AWS Verified Access trust providers.
Type: Array of [VerifiedAccessTrustProviderCondensed](API_VerifiedAccessTrustProviderCondensed.md) objects
Required: No

## See Also
<a name="API_VerifiedAccessInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VerifiedAccessInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VerifiedAccessInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VerifiedAccessInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
