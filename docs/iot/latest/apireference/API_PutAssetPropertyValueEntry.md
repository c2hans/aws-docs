---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_PutAssetPropertyValueEntry.html
---

# PutAssetPropertyValueEntry
<a name="API_PutAssetPropertyValueEntry"></a>

An asset property value entry containing the following information.

## Contents
<a name="API_PutAssetPropertyValueEntry_Contents"></a>

 ** propertyValues **   <a name="iot-Type-PutAssetPropertyValueEntry-propertyValues"></a>
A list of property values to insert that each contain timestamp, quality, and value (TQV) information.
Type: Array of [AssetPropertyValue](API_AssetPropertyValue.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** assetId **   <a name="iot-Type-PutAssetPropertyValueEntry-assetId"></a>
The ID of the AWS IoT SiteWise asset. You must specify either a `propertyAlias` or both an `aliasId` and a `propertyId`. Accepts substitution templates.
Type: String
Required: No

 ** entryId **   <a name="iot-Type-PutAssetPropertyValueEntry-entryId"></a>
Optional. A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.
Type: String
Required: No

 ** propertyAlias **   <a name="iot-Type-PutAssetPropertyValueEntry-propertyAlias"></a>
The name of the property alias associated with your asset property. You must specify either a `propertyAlias` or both an `aliasId` and a `propertyId`. Accepts substitution templates.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** propertyId **   <a name="iot-Type-PutAssetPropertyValueEntry-propertyId"></a>
The ID of the asset's property. You must specify either a `propertyAlias` or both an `aliasId` and a `propertyId`. Accepts substitution templates.
Type: String
Required: No

## See Also
<a name="API_PutAssetPropertyValueEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/PutAssetPropertyValueEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/PutAssetPropertyValueEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/PutAssetPropertyValueEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
