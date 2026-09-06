---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ItemIdentifier.html
---

# ItemIdentifier
<a name="API_ItemIdentifier"></a>

Details and type of a related item.

## Contents
<a name="API_ItemIdentifier_Contents"></a>

 ** type **   <a name="IncidentManager-Type-ItemIdentifier-type"></a>
The type of related item.
Type: String
Valid Values: `ANALYSIS | INCIDENT | METRIC | PARENT | ATTACHMENT | OTHER | AUTOMATION | INVOLVED_RESOURCE | TASK`
Required: Yes

 ** value **   <a name="IncidentManager-Type-ItemIdentifier-value"></a>
Details about the related item.
Type: [ItemValue](API_ItemValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_ItemIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/ItemIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/ItemIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/ItemIdentifier)
