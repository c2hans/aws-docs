---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_InspectionData.html
---

# InspectionData
<a name="API_InspectionData"></a>

Contains additional details about the state's execution, including its input and output data processing flow, and HTTP request and response information.

## Contents
<a name="API_InspectionData_Contents"></a>

 ** afterArguments **   <a name="StepFunctions-Type-InspectionData-afterArguments"></a>
The input after Step Functions applies an Arguments filter. This event will only be present when QueryLanguage for the state machine or individual states is set to JSONata. For more info, see [Transforming data with Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/data-transform.html).
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** afterInputPath **   <a name="StepFunctions-Type-InspectionData-afterInputPath"></a>
The input after Step Functions applies the [InputPath](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-inputpath) filter. Not populated when QueryLanguage is JSONata.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** afterItemBatcher **   <a name="StepFunctions-Type-InspectionData-afterItemBatcher"></a>
The effective input after the ItemBatcher filter is applied in a Map state.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** afterItemSelector **   <a name="StepFunctions-Type-InspectionData-afterItemSelector"></a>
An array containing the inputs for each Map iteration, transformed by the ItemSelector specified in a Map state.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** afterItemsPath **   <a name="StepFunctions-Type-InspectionData-afterItemsPath"></a>
The effective input after the ItemsPath filter is applied. Not populated when the QueryLanguage is JSONata.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** afterItemsPointer **   <a name="StepFunctions-Type-InspectionData-afterItemsPointer"></a>
The effective input after the ItemsPointer filter is applied in a Map state.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** afterParameters **   <a name="StepFunctions-Type-InspectionData-afterParameters"></a>
The effective input after Step Functions applies the [Parameters](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-parameters) filter. Not populated when QueryLanguage is JSONata.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** afterResultPath **   <a name="StepFunctions-Type-InspectionData-afterResultPath"></a>
The effective result combined with the raw state input after Step Functions applies the [ResultPath](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-resultpath.html) filter. Not populated when QueryLanguage is JSONata.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** afterResultSelector **   <a name="StepFunctions-Type-InspectionData-afterResultSelector"></a>
The effective result after Step Functions applies the [ResultSelector](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector) filter. Not populated when QueryLanguage is JSONata.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** errorDetails **   <a name="StepFunctions-Type-InspectionData-errorDetails"></a>
An object containing data about a handled exception in the tested state.
Type: [InspectionErrorDetails](API_InspectionErrorDetails.md) object
Required: No

 ** input **   <a name="StepFunctions-Type-InspectionData-input"></a>
The raw state input.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** maxConcurrency **   <a name="StepFunctions-Type-InspectionData-maxConcurrency"></a>
The max concurrency of the Map state.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** request **   <a name="StepFunctions-Type-InspectionData-request"></a>
The raw HTTP request that is sent when you test an HTTP Task.
Type: [InspectionDataRequest](API_InspectionDataRequest.md) object
Required: No

 ** response **   <a name="StepFunctions-Type-InspectionData-response"></a>
The raw HTTP response that is returned when you test an HTTP Task.
Type: [InspectionDataResponse](API_InspectionDataResponse.md) object
Required: No

 ** result **   <a name="StepFunctions-Type-InspectionData-result"></a>
The state's raw result.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** toleratedFailureCount **   <a name="StepFunctions-Type-InspectionData-toleratedFailureCount"></a>
The tolerated failure threshold for a Map state as defined in number of Map state iterations.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** toleratedFailurePercentage **   <a name="StepFunctions-Type-InspectionData-toleratedFailurePercentage"></a>
The tolerated failure threshold for a Map state as defined in percentage of Map state iterations.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** variables **   <a name="StepFunctions-Type-InspectionData-variables"></a>
JSON string that contains the set of workflow variables after execution of the state. The set will include variables assigned in the state and variables set up as test state input.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

## See Also
<a name="API_InspectionData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/InspectionData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/InspectionData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/InspectionData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
