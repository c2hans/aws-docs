---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DataBindingValueFilter.html
---

# DataBindingValueFilter
<a name="API_DataBindingValueFilter"></a>

A filter used to match specific data binding values based on criteria. This filter allows searching for data bindings by asset, asset model, asset property, or asset model property.

## Contents
<a name="API_DataBindingValueFilter_Contents"></a>

 ** asset **   <a name="iotsitewise-Type-DataBindingValueFilter-asset"></a>
Filter criteria for matching data bindings based on a specific asset. Used to list all data bindings referencing a particular asset or its properties.
Type: [AssetBindingValueFilter](API_AssetBindingValueFilter.md) object
Required: No

 ** assetModel **   <a name="iotsitewise-Type-DataBindingValueFilter-assetModel"></a>
Filter criteria for matching data bindings based on a specific asset model. Used to list all data bindings referencing a particular asset model or its properties.
Type: [AssetModelBindingValueFilter](API_AssetModelBindingValueFilter.md) object
Required: No

 ** assetModelProperty **   <a name="iotsitewise-Type-DataBindingValueFilter-assetModelProperty"></a>
Filter criteria for matching data bindings based on a specific asset model property. Used to list all data bindings referencing a particular property of an asset model.
Type: [AssetModelPropertyBindingValueFilter](API_AssetModelPropertyBindingValueFilter.md) object
Required: No

 ** assetProperty **   <a name="iotsitewise-Type-DataBindingValueFilter-assetProperty"></a>
Filter criteria for matching data bindings based on a specific asset property. Used to list all data bindings referencing a particular property of an asset.
Type: [AssetPropertyBindingValueFilter](API_AssetPropertyBindingValueFilter.md) object
Required: No

## See Also
<a name="API_DataBindingValueFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DataBindingValueFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DataBindingValueFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DataBindingValueFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
