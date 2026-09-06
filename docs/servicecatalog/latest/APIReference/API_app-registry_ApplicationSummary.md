---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_ApplicationSummary.html
---

# ApplicationSummary
<a name="API_app-registry_ApplicationSummary"></a>

Summary of a AWS Service Catalog AppRegistry application.

## Contents
<a name="API_app-registry_ApplicationSummary_Contents"></a>

 ** arn **   <a name="servicecatalog-Type-app-registry_ApplicationSummary-arn"></a>
The Amazon resource name (ARN) that specifies the application across services.
Type: String
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`
Required: No

 ** creationTime **   <a name="servicecatalog-Type-app-registry_ApplicationSummary-creationTime"></a>
The ISO-8601 formatted timestamp of the moment when the application was created.
Type: Timestamp
Required: No

 ** description **   <a name="servicecatalog-Type-app-registry_ApplicationSummary-description"></a>
The description of the application.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** id **   <a name="servicecatalog-Type-app-registry_ApplicationSummary-id"></a>
The identifier of the application.
Type: String
Length Constraints: Fixed length of 26.
Pattern: `[a-z0-9]+`
Required: No

 ** lastUpdateTime **   <a name="servicecatalog-Type-app-registry_ApplicationSummary-lastUpdateTime"></a>
 The ISO-8601 formatted timestamp of the moment when the application was last updated.
Type: Timestamp
Required: No

 ** name **   <a name="servicecatalog-Type-app-registry_ApplicationSummary-name"></a>
The name of the application. The name must be unique in the region in which you are creating the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`
Required: No

## See Also
<a name="API_app-registry_ApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ApplicationSummary)
