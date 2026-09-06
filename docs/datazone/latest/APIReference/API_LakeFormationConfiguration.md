---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_LakeFormationConfiguration.html
---

# LakeFormationConfiguration
<a name="API_LakeFormationConfiguration"></a>

The Lake Formation configuration of the Data Lake blueprint.

## Contents
<a name="API_LakeFormationConfiguration_Contents"></a>

 ** locationRegistrationExcludeS3Locations **   <a name="datazone-Type-LakeFormationConfiguration-locationRegistrationExcludeS3Locations"></a>
Specifies certain Amazon S3 locations if you do not want Amazon DataZone to automatically register them in hybrid mode.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://.+`
Required: No

 ** locationRegistrationRole **   <a name="datazone-Type-LakeFormationConfiguration-locationRegistrationRole"></a>
The role that is used to manage read/write access to the chosen Amazon S3 bucket(s) for Data Lake using AWS Lake Formation hybrid access mode.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`
Required: No

## See Also
<a name="API_LakeFormationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/LakeFormationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/LakeFormationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/LakeFormationConfiguration)
