---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_IotSiteWiseAction.html
---

# IotSiteWiseAction
<a name="API_IotSiteWiseAction"></a>

Describes an action to send data from an MQTT message that triggered the rule to AWS IoT SiteWise asset properties.

## Contents
<a name="API_IotSiteWiseAction_Contents"></a>

 ** putAssetPropertyValueEntries **   <a name="iot-Type-IotSiteWiseAction-putAssetPropertyValueEntries"></a>
A list of asset property value entries.
Type: Array of [PutAssetPropertyValueEntry](API_PutAssetPropertyValueEntry.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** roleArn **   <a name="iot-Type-IotSiteWiseAction-roleArn"></a>
The ARN of the role that grants AWS IoT permission to send an asset property value to AWS IoT SiteWise. (`"Action": "iotsitewise:BatchPutAssetPropertyValue"`). The trust policy can restrict access to specific asset hierarchy paths.
Type: String
Required: Yes

## See Also
<a name="API_IotSiteWiseAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/IotSiteWiseAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/IotSiteWiseAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/IotSiteWiseAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
