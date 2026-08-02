---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateJsonClassifierRequest.html
---

# CreateJsonClassifierRequest
<a name="API_CreateJsonClassifierRequest"></a>

Specifies a JSON classifier for `CreateClassifier` to create.

## Contents
<a name="API_CreateJsonClassifierRequest_Contents"></a>

 ** JsonPath **   <a name="Glue-Type-CreateJsonClassifierRequest-JsonPath"></a>
A `JsonPath` string defining the JSON data for the classifier to classify. AWS Glue supports a subset of JsonPath, as described in [Writing JsonPath Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json).
Type: String
Required: Yes

 ** Name **   <a name="Glue-Type-CreateJsonClassifierRequest-Name"></a>
The name of the classifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## See Also
<a name="API_CreateJsonClassifierRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateJsonClassifierRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateJsonClassifierRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateJsonClassifierRequest)
