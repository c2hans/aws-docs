---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PropertyMappingConfiguration.html
---

# PropertyMappingConfiguration
<a name="API_PropertyMappingConfiguration"></a>

Contains configuration options for mapping properties from an interface asset model to an asset model where the interface is applied.

## Contents
<a name="API_PropertyMappingConfiguration_Contents"></a>

 ** createMissingProperty **   <a name="iotsitewise-Type-PropertyMappingConfiguration-createMissingProperty"></a>
If true, missing properties from the interface asset model are automatically created in the asset model where the interface is applied.
Type: Boolean
Required: No

 ** matchByPropertyName **   <a name="iotsitewise-Type-PropertyMappingConfiguration-matchByPropertyName"></a>
If true, properties are matched by name between the interface asset model and the asset model where the interface is applied.
Type: Boolean
Required: No

 ** overrides **   <a name="iotsitewise-Type-PropertyMappingConfiguration-overrides"></a>
A list of specific property mappings that override the automatic mapping by name when an interface is applied to an asset model.
Type: Array of [PropertyMapping](API_PropertyMapping.md) objects
Required: No

## See Also
<a name="API_PropertyMappingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/PropertyMappingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/PropertyMappingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/PropertyMappingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
