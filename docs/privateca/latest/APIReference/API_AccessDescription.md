---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_AccessDescription.html
---

# AccessDescription
<a name="API_AccessDescription"></a>

Provides access information used by the `authorityInfoAccess` and `subjectInfoAccess` extensions described in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280).

## Contents
<a name="API_AccessDescription_Contents"></a>

 ** AccessLocation **   <a name="privateca-Type-AccessDescription-AccessLocation"></a>
The location of `AccessDescription` information.
Type: [GeneralName](API_GeneralName.md) object
Required: Yes

 ** AccessMethod **   <a name="privateca-Type-AccessDescription-AccessMethod"></a>
The type and format of `AccessDescription` information.
Type: [AccessMethod](API_AccessMethod.md) object
Required: Yes

## See Also
<a name="API_AccessDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/AccessDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/AccessDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/AccessDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
