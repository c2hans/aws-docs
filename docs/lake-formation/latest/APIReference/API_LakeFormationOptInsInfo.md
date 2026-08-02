---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_LakeFormationOptInsInfo.html
---

# LakeFormationOptInsInfo
<a name="API_LakeFormationOptInsInfo"></a>

A single principal-resource pair that has Lake Formation permissins enforced.

## Contents
<a name="API_LakeFormationOptInsInfo_Contents"></a>

 ** Condition **   <a name="lakeformation-Type-LakeFormationOptInsInfo-Condition"></a>
A Lake Formation condition, which applies to permissions and opt-ins that contain an expression.
Type: [Condition](API_Condition.md) object
Required: No

 ** LastModified **   <a name="lakeformation-Type-LakeFormationOptInsInfo-LastModified"></a>
The last modified date and time of the record.
Type: Timestamp
Required: No

 ** LastUpdatedBy **   <a name="lakeformation-Type-LakeFormationOptInsInfo-LastUpdatedBy"></a>
The user who updated the record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Principal **   <a name="lakeformation-Type-LakeFormationOptInsInfo-Principal"></a>
The AWS Lake Formation principal. Supported principals are IAM users or IAM roles.
Type: [DataLakePrincipal](API_DataLakePrincipal.md) object
Required: No

 ** Resource **   <a name="lakeformation-Type-LakeFormationOptInsInfo-Resource"></a>
A structure for the resource.
Type: [Resource](API_Resource.md) object
Required: No

## See Also
<a name="API_LakeFormationOptInsInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/LakeFormationOptInsInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/LakeFormationOptInsInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/LakeFormationOptInsInfo)
