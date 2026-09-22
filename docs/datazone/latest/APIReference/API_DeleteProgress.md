---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DeleteProgress.html
---

# DeleteProgress
<a name="API_DeleteProgress"></a>

The progress of a domain deletion, including the number of projects that Amazon DataZone successfully deleted. Amazon DataZone returns this structure in the response to a `GetDomain` request while a cascade deletion is in progress.

## Contents
<a name="API_DeleteProgress_Contents"></a>

 ** successfullyDeletedProjectCount **   <a name="datazone-Type-DeleteProgress-successfullyDeletedProjectCount"></a>
The number of projects that Amazon DataZone successfully deleted during the domain deletion.
Type: Integer
Required: No

## See Also
<a name="API_DeleteProgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DeleteProgress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DeleteProgress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DeleteProgress)
