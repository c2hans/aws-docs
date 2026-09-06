---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SpaceQuickSightResource.html
---

# SpaceQuickSightResource
<a name="API_SpaceQuickSightResource"></a>

A QuickSight resource that is associated with a space.

## Contents
<a name="API_SpaceQuickSightResource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** resourceDetails **   <a name="QS-Type-SpaceQuickSightResource-resourceDetails"></a>
The details of the QuickSight resource.
Type: [SpaceQuickSightResourceDetails](API_SpaceQuickSightResourceDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** resourceType **   <a name="QS-Type-SpaceQuickSightResource-resourceType"></a>
The type of the QuickSight resource.
Type: String
Valid Values: `TOPIC | DASHBOARD | KNOWLEDGE_BASE | ACTION_CONNECTOR | DATA_SET`
Required: Yes

## See Also
<a name="API_SpaceQuickSightResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SpaceQuickSightResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SpaceQuickSightResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SpaceQuickSightResource)
