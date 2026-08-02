---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetSearchSuggestions.html
---

# GetSearchSuggestions
<a name="API_GetSearchSuggestions"></a>

An auto-complete API for the search functionality in the SageMaker console. It returns suggestions of possible matches for the property name to use in `Search` queries. Provides suggestions for `HyperParameters`, `Tags`, and `Metrics`.

## Request Syntax
<a name="API_GetSearchSuggestions_RequestSyntax"></a>

```
{
   "Resource": "{{string}}",
   "SuggestionQuery": {
      "PropertyNameQuery": {
         "PropertyNameHint": "{{string}}"
      }
   }
}
```

## Request Parameters
<a name="API_GetSearchSuggestions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Resource](#API_GetSearchSuggestions_RequestSyntax) **   <a name="sagemaker-GetSearchSuggestions-request-Resource"></a>
The name of the SageMaker resource to search for.
Type: String
Valid Values: `TrainingJob | Experiment | ExperimentTrial | ExperimentTrialComponent | Endpoint | Model | ModelPackage | ModelPackageGroup | Pipeline | PipelineExecution | FeatureGroup | FeatureMetadata | Image | ImageVersion | Project | HyperParameterTuningJob | ModelCard | PipelineVersion | Job`
Required: Yes

 ** [SuggestionQuery](#API_GetSearchSuggestions_RequestSyntax) **   <a name="sagemaker-GetSearchSuggestions-request-SuggestionQuery"></a>
Limits the property names that are included in the response.
Type: [SuggestionQuery](API_SuggestionQuery.md) object
Required: No

## Response Syntax
<a name="API_GetSearchSuggestions_ResponseSyntax"></a>

```
{
   "PropertyNameSuggestions": [
      {
         "PropertyName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetSearchSuggestions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PropertyNameSuggestions](#API_GetSearchSuggestions_ResponseSyntax) **   <a name="sagemaker-GetSearchSuggestions-response-PropertyNameSuggestions"></a>
A list of property names for a `Resource` that match a `SuggestionQuery`.
Type: Array of [PropertyNameSuggestion](API_PropertyNameSuggestion.md) objects

## Errors
<a name="API_GetSearchSuggestions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetSearchSuggestions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/GetSearchSuggestions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/GetSearchSuggestions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/GetSearchSuggestions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/GetSearchSuggestions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/GetSearchSuggestions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/GetSearchSuggestions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/GetSearchSuggestions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/GetSearchSuggestions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/GetSearchSuggestions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/GetSearchSuggestions)
