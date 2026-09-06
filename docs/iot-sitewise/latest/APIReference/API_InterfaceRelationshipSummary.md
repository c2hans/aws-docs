---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_InterfaceRelationshipSummary.html
---

# InterfaceRelationshipSummary
<a name="API_InterfaceRelationshipSummary"></a>

Contains summary information about an interface relationship, which defines how an interface is applied to an asset model. This summary provides the essential identifiers needed to retrieve detailed information about the relationship.

## Contents
<a name="API_InterfaceRelationshipSummary_Contents"></a>

 ** id **   <a name="iotsitewise-Type-InterfaceRelationshipSummary-id"></a>
The ID of the asset model that has the interface applied to it.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## See Also
<a name="API_InterfaceRelationshipSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/InterfaceRelationshipSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/InterfaceRelationshipSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/InterfaceRelationshipSummary)
