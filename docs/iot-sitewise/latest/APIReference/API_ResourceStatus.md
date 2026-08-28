---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ResourceStatus.html
---

# ResourceStatus
<a name="API_ResourceStatus"></a>

Contains information about the current status of a resource.

## Contents
<a name="API_ResourceStatus_Contents"></a>

 ** error **   <a name="iotsitewise-Type-ResourceStatus-error"></a>
Contains associated error information, if any.
Type: [ResourceError](API_ResourceError.md) object
Required: No

 ** state **   <a name="iotsitewise-Type-ResourceStatus-state"></a>
The current status of the resource.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | FAILED`
Required: No

## See Also
<a name="API_ResourceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ResourceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ResourceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ResourceStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
