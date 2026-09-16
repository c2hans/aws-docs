---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageFailureContext.html
---

# ImageFailureContext
<a name="API_ImageFailureContext"></a>

Contains details about the failure when the image creation process fails. Properties appear in the failure context when the related information is available for the failure.

## Contents
<a name="API_ImageFailureContext_Contents"></a>

 ** componentFailure **   <a name="imagebuilder-Type-ImageFailureContext-componentFailure"></a>
The details about the component that failed, if the failure occurred while a component was running.
Type: [ComponentFailureContext](API_ComponentFailureContext.md) object
Required: No

 ** distributionFailure **   <a name="imagebuilder-Type-ImageFailureContext-distributionFailure"></a>
The details about the distribution failure, if the failure occurred while Image Builder distributed or configured the image.
Type: [DistributionFailureContext](API_DistributionFailureContext.md) object
Required: No

 ** failedStep **   <a name="imagebuilder-Type-ImageFailureContext-failedStep"></a>
The name of the workflow step that failed, as it appears in the workflow document.
Type: String
Pattern: `^[A-Za-z][A-Za-z0-9-_]{1,99}$`
Required: No

 ** imageStatus **   <a name="imagebuilder-Type-ImageFailureContext-imageStatus"></a>
The status that the image had when the failure occurred. This indicates the stage of the image creation process where the image failed, for example `BUILDING` or `DISTRIBUTING`.
Type: String
Valid Values: `PENDING | CREATING | BUILDING | TESTING | DISTRIBUTING | INTEGRATING | AVAILABLE | CANCELLED | FAILED | DEPRECATED | DELETED | DISABLED`
Required: No

 ** stepExecutionId **   <a name="imagebuilder-Type-ImageFailureContext-stepExecutionId"></a>
The unique identifier of the workflow step execution that failed.
Type: String
Pattern: `^step-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: No

 ** workflowArn **   <a name="imagebuilder-Type-ImageFailureContext-workflowArn"></a>
The Amazon Resource Name (ARN) of the workflow build version that was running when the image failed.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: No

 ** workflowExecutionId **   <a name="imagebuilder-Type-ImageFailureContext-workflowExecutionId"></a>
The unique identifier of the workflow execution that was running when the image failed.
Type: String
Pattern: `^wf-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: No

## See Also
<a name="API_ImageFailureContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImageFailureContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImageFailureContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImageFailureContext)
