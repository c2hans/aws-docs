---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TemplateError.html
---

# TemplateError
<a name="API_TemplateError"></a>

List of errors that occurred when the template version creation failed.

## Contents
<a name="API_TemplateError_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Message **   <a name="QS-Type-TemplateError-Message"></a>
Description of the error type.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="QS-Type-TemplateError-Type"></a>
Type of error.
Type: String
Valid Values: `SOURCE_NOT_FOUND | DATA_SET_NOT_FOUND | INTERNAL_FAILURE | ACCESS_DENIED`
Required: No

 ** ViolatedEntities **   <a name="QS-Type-TemplateError-ViolatedEntities"></a>
An error path that shows which entities caused the template error.
Type: Array of [Entity](API_Entity.md) objects
Array Members: Maximum number of 200 items.
Required: No

## See Also
<a name="API_TemplateError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TemplateError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TemplateError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TemplateError)
