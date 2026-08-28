---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceMetadataDefaultsResponse.html
---

# InstanceMetadataDefaultsResponse
<a name="API_InstanceMetadataDefaultsResponse"></a>

The default instance metadata service (IMDS) settings that were set at the account level in the specified AWS  Region.

## Contents
<a name="API_InstanceMetadataDefaultsResponse_Contents"></a>

 ** httpEndpoint **
Indicates whether the IMDS endpoint for an instance is enabled or disabled. When disabled, the instance metadata can't be accessed.
Type: String
Valid Values: `disabled | enabled`
Required: No

 ** httpPutResponseHopLimit **
The maximum number of hops that the metadata token can travel.
Type: Integer
Required: No

 ** httpTokens **
Indicates whether IMDSv2 is required.
+  `optional` – IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.
+  `required` – IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.
Type: String
Valid Values: `optional | required`
Required: No

 ** httpTokensEnforced **
Indicates whether to enforce the requirement of IMDSv2 on an instance at the time of launch. When enforcement is enabled, the instance can't launch unless IMDSv2 (`HttpTokens`) is set to `required`.
Type: String
Valid Values: `disabled | enabled`
Required: No

 ** instanceMetadataTags **
Indicates whether access to instance tags from the instance metadata is enabled or disabled. For more information, see [View tags for your EC2 instances using instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `disabled | enabled`
Required: No

 ** managedBy **
The entity that manages the IMDS default settings. Possible values include:
+  `account` - The IMDS default settings are managed by the account.
+  `declarative-policy` - The IMDS default settings are managed by a declarative policy and can't be modified by the account.
Type: String
Valid Values: `account | declarative-policy`
Required: No

 ** managedExceptionMessage **
The customized exception message that is specified in the declarative policy.
Type: String
Required: No

## See Also
<a name="API_InstanceMetadataDefaultsResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceMetadataDefaultsResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceMetadataDefaultsResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceMetadataDefaultsResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
