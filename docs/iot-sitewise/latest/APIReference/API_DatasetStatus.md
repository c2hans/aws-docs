---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DatasetStatus.html
---

# DatasetStatus
<a name="API_DatasetStatus"></a>

The status of the dataset. This contains the state and any error messages. The state is `ACTIVE` when ready to use.

## Contents
<a name="API_DatasetStatus_Contents"></a>

 ** state **   <a name="iotsitewise-Type-DatasetStatus-state"></a>
The current status of the dataset.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | FAILED`
Required: Yes

 ** error **   <a name="iotsitewise-Type-DatasetStatus-error"></a>
Contains the details of an AWS IoT SiteWise error.
Type: [ErrorDetails](API_ErrorDetails.md) object
Required: No

## See Also
<a name="API_DatasetStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DatasetStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DatasetStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DatasetStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
