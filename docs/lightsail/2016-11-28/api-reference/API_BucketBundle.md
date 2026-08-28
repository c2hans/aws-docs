---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_BucketBundle.html
---

# BucketBundle
<a name="API_BucketBundle"></a>

Describes the specifications of a bundle that can be applied to an Amazon Lightsail bucket.

A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket.

## Contents
<a name="API_BucketBundle_Contents"></a>

 ** bundleId **   <a name="Lightsail-Type-BucketBundle-bundleId"></a>
The ID of the bundle.
Type: String
Pattern: `.*\S.*`
Required: No

 ** isActive **   <a name="Lightsail-Type-BucketBundle-isActive"></a>
Indicates whether the bundle is active. Use for a new or existing bucket.
Type: Boolean
Required: No

 ** name **   <a name="Lightsail-Type-BucketBundle-name"></a>
The name of the bundle.
Type: String
Pattern: `.*\S.*`
Required: No

 ** price **   <a name="Lightsail-Type-BucketBundle-price"></a>
The monthly price of the bundle, in US dollars.
Type: Float
Required: No

 ** storagePerMonthInGb **   <a name="Lightsail-Type-BucketBundle-storagePerMonthInGb"></a>
The storage size of the bundle, in GB.
Type: Integer
Required: No

 ** transferPerMonthInGb **   <a name="Lightsail-Type-BucketBundle-transferPerMonthInGb"></a>
The monthly network transfer quota of the bundle.
Type: Integer
Required: No

## See Also
<a name="API_BucketBundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/BucketBundle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/BucketBundle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/BucketBundle)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
