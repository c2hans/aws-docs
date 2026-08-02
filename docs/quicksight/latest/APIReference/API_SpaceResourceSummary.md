---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SpaceResourceSummary.html
---

# SpaceResourceSummary
<a name="API_SpaceResourceSummary"></a>

A summary of a resource in a space.

## Contents
<a name="API_SpaceResourceSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ResourceDetails **   <a name="QS-Type-SpaceResourceSummary-ResourceDetails"></a>
The details of the resource.
Type: [SpaceQuickSightResourceDetails](API_SpaceQuickSightResourceDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** ResourceType **   <a name="QS-Type-SpaceResourceSummary-ResourceType"></a>
The type of the resource.
Type: String
Valid Values: `TOPIC | DASHBOARD | KNOWLEDGE_BASE | ACTION_CONNECTOR | DATA_SET`
Required: Yes

 ** ResourceName **   <a name="QS-Type-SpaceResourceSummary-ResourceName"></a>
The name of the resource.
Type: String
Required: No

 ** UpdatedAt **   <a name="QS-Type-SpaceResourceSummary-UpdatedAt"></a>
The date and time that the resource was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_SpaceResourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SpaceResourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SpaceResourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SpaceResourceSummary)
