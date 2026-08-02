---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StatusDetails.html
---

# StatusDetails
<a name="API_StatusDetails"></a>

A structure containing information about an asynchronous change to a table.

## Contents
<a name="API_StatusDetails_Contents"></a>

 ** RequestedChange **   <a name="Glue-Type-StatusDetails-RequestedChange"></a>
A `Table` object representing the requested changes.
Type: [Table](API_Table.md) object
Required: No

 ** ViewValidations **   <a name="Glue-Type-StatusDetails-ViewValidations"></a>
A list of `ViewValidation` objects that contain information for an analytical engine to validate a view.
Type: Array of [ViewValidation](API_ViewValidation.md) objects
Required: No

## See Also
<a name="API_StatusDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StatusDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StatusDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StatusDetails)
