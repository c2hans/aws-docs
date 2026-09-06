---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_DestinationS3Location.html
---

# DestinationS3Location
<a name="API_taxSettings_DestinationS3Location"></a>

The location of the Amazon S3 bucket that you specify to download your tax documents to.

## Contents
<a name="API_taxSettings_DestinationS3Location_Contents"></a>

 ** bucket **   <a name="awscostmanagement-Type-taxSettings_DestinationS3Location-bucket"></a>
The name of your Amazon S3 bucket that you specify to download your tax documents to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?=^.{3,63}$)(?!^(\d+\.)+\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)*([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])$)`
Required: Yes

 ** prefix **   <a name="awscostmanagement-Type-taxSettings_DestinationS3Location-prefix"></a>
The Amazon S3 object prefix that you specify for your tax document file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_taxSettings_DestinationS3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/DestinationS3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/DestinationS3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/DestinationS3Location)
