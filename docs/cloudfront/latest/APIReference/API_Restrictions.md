---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_Restrictions.html
---

# Restrictions
<a name="API_Restrictions"></a>

A complex type that identifies ways in which you want to restrict distribution of your content.

## Contents
<a name="API_Restrictions_Contents"></a>

 ** GeoRestriction **   <a name="cloudfront-Type-Restrictions-GeoRestriction"></a>
A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using `MaxMind` GeoIP databases.
Type: [GeoRestriction](API_GeoRestriction.md) object
Required: Yes

## See Also
<a name="API_Restrictions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/Restrictions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/Restrictions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/Restrictions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
