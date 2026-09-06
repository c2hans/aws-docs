---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_MapRunRedrivenEventDetails.html
---

# MapRunRedrivenEventDetails
<a name="API_MapRunRedrivenEventDetails"></a>

Contains details about a Map Run that was redriven.

## Contents
<a name="API_MapRunRedrivenEventDetails_Contents"></a>

 ** mapRunArn **   <a name="StepFunctions-Type-MapRunRedrivenEventDetails-mapRunArn"></a>
The Amazon Resource Name (ARN) of a Map Run that was redriven.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** redriveCount **   <a name="StepFunctions-Type-MapRunRedrivenEventDetails-redriveCount"></a>
The number of times the Map Run has been redriven at this point in the execution's history including this event. The redrive count for a redriven Map Run is always greater than 0.
Type: Integer
Required: No

## See Also
<a name="API_MapRunRedrivenEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/MapRunRedrivenEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/MapRunRedrivenEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/MapRunRedrivenEventDetails)
