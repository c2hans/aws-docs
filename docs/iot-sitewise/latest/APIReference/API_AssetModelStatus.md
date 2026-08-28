---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetModelStatus.html
---

# AssetModelStatus
<a name="API_AssetModelStatus"></a>

Contains current status information for an asset model. For more information, see [Asset and model states](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-and-model-states.html) in the * AWS IoT SiteWise User Guide*.

## Contents
<a name="API_AssetModelStatus_Contents"></a>

 ** state **   <a name="iotsitewise-Type-AssetModelStatus-state"></a>
The current state of the asset model.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | PROPAGATING | DELETING | FAILED`
Required: Yes

 ** error **   <a name="iotsitewise-Type-AssetModelStatus-error"></a>
Contains associated error information, if any.
Type: [ErrorDetails](API_ErrorDetails.md) object
Required: No

## See Also
<a name="API_AssetModelStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetModelStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetModelStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetModelStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
