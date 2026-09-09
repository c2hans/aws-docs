---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AssociationSummary.html
---

# AssociationSummary
<a name="API_AssociationSummary"></a>

Lists a summary of the properties of an association. An association is an entity that links other lineage or experiment entities. An example would be an association between a training job and a model.

## Contents
<a name="API_AssociationSummary_Contents"></a>

 ** AssociationType **   <a name="sagemaker-Type-AssociationSummary-AssociationType"></a>
The type of the association.
Type: String
Valid Values: `ContributedTo | AssociatedWith | DerivedFrom | Produced | SameAs`
Required: No

 ** CreatedBy **   <a name="sagemaker-Type-AssociationSummary-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** DestinationArn **   <a name="sagemaker-Type-AssociationSummary-DestinationArn"></a>
The Amazon Resource Name (ARN) of the destination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`
Required: No

 ** DestinationName **   <a name="sagemaker-Type-AssociationSummary-DestinationName"></a>
The name of the destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** DestinationType **   <a name="sagemaker-Type-AssociationSummary-DestinationType"></a>
The destination type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** SourceArn **   <a name="sagemaker-Type-AssociationSummary-SourceArn"></a>
The ARN of the source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`
Required: No

 ** SourceName **   <a name="sagemaker-Type-AssociationSummary-SourceName"></a>
The name of the source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** SourceType **   <a name="sagemaker-Type-AssociationSummary-SourceType"></a>
The source type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_AssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AssociationSummary)
