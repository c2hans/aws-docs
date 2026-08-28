---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_OutputResources.html
---

# OutputResources
<a name="API_OutputResources"></a>

The resources produced by this image.

## Contents
<a name="API_OutputResources_Contents"></a>

 ** amis **   <a name="imagebuilder-Type-OutputResources-amis"></a>
The Amazon EC2 AMIs created by this image.
Type: Array of [Ami](API_Ami.md) objects
Required: No

 ** containers **   <a name="imagebuilder-Type-OutputResources-containers"></a>
Container images that the pipeline has generated and stored in the output repository.
Type: Array of [Container](API_Container.md) objects
Required: No

## See Also
<a name="API_OutputResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/OutputResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/OutputResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/OutputResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
