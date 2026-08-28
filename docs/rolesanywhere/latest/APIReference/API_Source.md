---
source_url: https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_Source.html
---

# Source
<a name="API_Source"></a>

The trust anchor type and its related certificate data.

## Contents
<a name="API_Source_Contents"></a>

 ** sourceData **   <a name="rolesanywhere-Type-Source-sourceData"></a>
The data field of the trust anchor depending on its type.
Type: [SourceData](API_SourceData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** sourceType **   <a name="rolesanywhere-Type-Source-sourceType"></a>
The type of the trust anchor.
Type: String
Valid Values: `AWS_ACM_PCA | CERTIFICATE_BUNDLE | SELF_SIGNED_REPOSITORY`
Required: No

## See Also
<a name="API_Source_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/Source)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/Source)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/Source)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Roles Anywhere. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rolesanywhere` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
