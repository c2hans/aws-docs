---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddAssociation.html
---

# AddAssociation
<a name="API_AddAssociation"></a>

Creates an *association* between the source and the destination. A source can be associated with multiple destinations, and a destination can be associated with multiple sources. An association is a lineage tracking entity. For more information, see [Amazon SageMaker ML Lineage Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html).

## Request Syntax
<a name="API_AddAssociation_RequestSyntax"></a>

```
{
   "AssociationType": "{{string}}",
   "DestinationArn": "{{string}}",
   "SourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_AddAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationType](#API_AddAssociation_RequestSyntax) **   <a name="sagemaker-AddAssociation-request-AssociationType"></a>
The type of association. The following are suggested uses for each type. Amazon SageMaker places no restrictions on their use.
+ ContributedTo - The source contributed to the destination or had a part in enabling the destination. For example, the training data contributed to the training job.
+ AssociatedWith - The source is connected to the destination. For example, an approval workflow is associated with a model deployment.
+ DerivedFrom - The destination is a modification of the source. For example, a digest output of a channel input for a processing job is derived from the original inputs.
+ Produced - The source generated the destination. For example, a training job produced a model artifact.
Type: String
Valid Values: `ContributedTo | AssociatedWith | DerivedFrom | Produced | SameAs`
Required: No

 ** [DestinationArn](#API_AddAssociation_RequestSyntax) **   <a name="sagemaker-AddAssociation-request-DestinationArn"></a>
The Amazon Resource Name (ARN) of the destination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`
Required: Yes

 ** [SourceArn](#API_AddAssociation_RequestSyntax) **   <a name="sagemaker-AddAssociation-request-SourceArn"></a>
The ARN of the source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`
Required: Yes

## Response Syntax
<a name="API_AddAssociation_ResponseSyntax"></a>

```
{
   "DestinationArn": "string",
   "SourceArn": "string"
}
```

## Response Elements
<a name="API_AddAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DestinationArn](#API_AddAssociation_ResponseSyntax) **   <a name="sagemaker-AddAssociation-response-DestinationArn"></a>
The Amazon Resource Name (ARN) of the destination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`

 ** [SourceArn](#API_AddAssociation_ResponseSyntax) **   <a name="sagemaker-AddAssociation-response-SourceArn"></a>
The ARN of the source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`

## Errors
<a name="API_AddAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_AddAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/AddAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/AddAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AddAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/AddAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AddAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/AddAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/AddAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/AddAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/AddAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AddAssociation)
