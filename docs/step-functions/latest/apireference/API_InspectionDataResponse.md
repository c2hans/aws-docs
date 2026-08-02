---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_InspectionDataResponse.html
---

# InspectionDataResponse
<a name="API_InspectionDataResponse"></a>

Contains additional details about the state's execution, including its input and output data processing flow, and HTTP response information. The `inspectionLevel` request parameter specifies which details are returned.

## Contents
<a name="API_InspectionDataResponse_Contents"></a>

 ** body **   <a name="StepFunctions-Type-InspectionDataResponse-body"></a>
The HTTP response returned.
Type: String
Required: No

 ** headers **   <a name="StepFunctions-Type-InspectionDataResponse-headers"></a>
The response headers associated with the HTTP response.
Type: String
Required: No

 ** protocol **   <a name="StepFunctions-Type-InspectionDataResponse-protocol"></a>
The protocol used to return the HTTP response.
Type: String
Required: No

 ** statusCode **   <a name="StepFunctions-Type-InspectionDataResponse-statusCode"></a>
The HTTP response status code for the HTTP response.
Type: String
Required: No

 ** statusMessage **   <a name="StepFunctions-Type-InspectionDataResponse-statusMessage"></a>
The message associated with the HTTP status code.
Type: String
Required: No

## See Also
<a name="API_InspectionDataResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/InspectionDataResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/InspectionDataResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/InspectionDataResponse)
