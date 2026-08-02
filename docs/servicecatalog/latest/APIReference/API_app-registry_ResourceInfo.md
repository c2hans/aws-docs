---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_ResourceInfo.html
---

# ResourceInfo
<a name="API_app-registry_ResourceInfo"></a>

The information about the resource.

## Contents
<a name="API_app-registry_ResourceInfo_Contents"></a>

 ** arn **   <a name="servicecatalog-Type-app-registry_ResourceInfo-arn"></a>
The Amazon resource name (ARN) that specifies the resource across services.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
Required: No

 ** name **   <a name="servicecatalog-Type-app-registry_ResourceInfo-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: No

 ** options **   <a name="servicecatalog-Type-app-registry_ResourceInfo-options"></a>
 Determines whether an application tag is applied or skipped.
Type: Array of strings
Valid Values: `APPLY_APPLICATION_TAG | SKIP_APPLICATION_TAG`
Required: No

 ** resourceDetails **   <a name="servicecatalog-Type-app-registry_ResourceInfo-resourceDetails"></a>
 The details related to the resource.
Type: [ResourceDetails](API_app-registry_ResourceDetails.md) object
Required: No

 ** resourceType **   <a name="servicecatalog-Type-app-registry_ResourceInfo-resourceType"></a>
 Provides information about the AWS Service Catalog AppRegistry resource type.
Type: String
Valid Values: `CFN_STACK | RESOURCE_TAG_VALUE`
Required: No

## See Also
<a name="API_app-registry_ResourceInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ResourceInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ResourceInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ResourceInfo)
