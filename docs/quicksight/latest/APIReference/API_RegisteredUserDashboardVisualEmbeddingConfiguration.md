---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisteredUserDashboardVisualEmbeddingConfiguration.html
---

# RegisteredUserDashboardVisualEmbeddingConfiguration
<a name="API_RegisteredUserDashboardVisualEmbeddingConfiguration"></a>

The experience that you are embedding. You can use this object to generate a url that embeds a visual into your application.

## Contents
<a name="API_RegisteredUserDashboardVisualEmbeddingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InitialDashboardVisualId **   <a name="QS-Type-RegisteredUserDashboardVisualEmbeddingConfiguration-InitialDashboardVisualId"></a>
The visual ID for the visual that you want the user to embed. This ID is included in the output URL. When the URL in response is accessed, Amazon Quick Sight renders this visual.
The Amazon Resource Name (ARN) of the dashboard that the visual belongs to must be included in the `AuthorizedResourceArns` parameter. Otherwise, the request will fail with `InvalidParameterValueException`.
Type: [DashboardVisualId](API_DashboardVisualId.md) object
Required: Yes

## See Also
<a name="API_RegisteredUserDashboardVisualEmbeddingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RegisteredUserDashboardVisualEmbeddingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RegisteredUserDashboardVisualEmbeddingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RegisteredUserDashboardVisualEmbeddingConfiguration)
