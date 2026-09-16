---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusters.html
---

# ListClusters
<a name="API_ListClusters"></a>

Retrieves the list of SageMaker HyperPod clusters.

## Request Syntax
<a name="API_ListClusters_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "TrainingPlanArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListClusters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListClusters_RequestSyntax) **   <a name="sagemaker-ListClusters-request-MaxResults"></a>
Specifies the maximum number of clusters to evaluate for the operation (not necessarily the number of matching items). After SageMaker processes the number of clusters up to `MaxResults`, it stops the operation and returns the matching clusters up to that point. If all the matching clusters are desired, SageMaker will go through all the clusters until `NextToken` is empty.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListClusters_RequestSyntax) **   <a name="sagemaker-ListClusters-request-NameContains"></a>
Set the maximum number of instances to print in the list.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListClusters_RequestSyntax) **   <a name="sagemaker-ListClusters-request-NextToken"></a>
Set the next token to retrieve the list of SageMaker HyperPod clusters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListClusters_RequestSyntax) **   <a name="sagemaker-ListClusters-request-SortBy"></a>
The field by which to sort results. The default value is `CREATION_TIME`.
Type: String
Valid Values: `CREATION_TIME | NAME`
Required: No

 ** [SortOrder](#API_ListClusters_RequestSyntax) **   <a name="sagemaker-ListClusters-request-SortOrder"></a>
The sort order for results. The default value is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [TrainingPlanArn](#API_ListClusters_RequestSyntax) **   <a name="sagemaker-ListClusters-request-TrainingPlanArn"></a>
The Amazon Resource Name (ARN); of the training plan to filter clusters by. For more information about reserving GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see ` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`
Required: No

## Response Syntax
<a name="API_ListClusters_ResponseSyntax"></a>

```
{
   "ClusterSummaries": [
      {
         "ClusterArn": "string",
         "ClusterName": "string",
         "ClusterStatus": "string",
         "ImageVersionStatus": "string",
         "TrainingPlanArns": [ "string" ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListClusters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterSummaries](#API_ListClusters_ResponseSyntax) **   <a name="sagemaker-ListClusters-response-ClusterSummaries"></a>
The summaries of listed SageMaker HyperPod clusters.
Type: Array of [ClusterSummary](API_ClusterSummary.md) objects

 ** [NextToken](#API_ListClusters_ResponseSyntax) **   <a name="sagemaker-ListClusters-response-NextToken"></a>
If the result of the previous `ListClusters` request was truncated, the response includes a `NextToken`. To retrieve the next set of clusters, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListClusters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListClusters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListClusters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListClusters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListClusters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListClusters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListClusters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListClusters)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListClusters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListClusters)
