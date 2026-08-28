---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ComputationModelSummary.html
---

# ComputationModelSummary
<a name="API_ComputationModelSummary"></a>

Contains a summary of a computation model.

## Contents
<a name="API_ComputationModelSummary_Contents"></a>

 ** arn **   <a name="iotsitewise-Type-ComputationModelSummary-arn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the computation model, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:computation-model/${ComputationModelId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: Yes

 ** creationDate **   <a name="iotsitewise-Type-ComputationModelSummary-creationDate"></a>
The model creation date, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** id **   <a name="iotsitewise-Type-ComputationModelSummary-id"></a>
The ID of the computation model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** lastUpdateDate **   <a name="iotsitewise-Type-ComputationModelSummary-lastUpdateDate"></a>
The time the model was last updated, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** name **   <a name="iotsitewise-Type-ComputationModelSummary-name"></a>
The name of the computation model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9 _\-#$*!@.]+$`
Required: Yes

 ** status **   <a name="iotsitewise-Type-ComputationModelSummary-status"></a>
The current status of the computation model.
Type: [ComputationModelStatus](API_ComputationModelStatus.md) object
Required: Yes

 ** type **   <a name="iotsitewise-Type-ComputationModelSummary-type"></a>
The type of the computation model.
Type: String
Valid Values: `ANOMALY_DETECTION`
Required: Yes

 ** version **   <a name="iotsitewise-Type-ComputationModelSummary-version"></a>
The version of the computation model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`
Required: Yes

 ** description **   <a name="iotsitewise-Type-ComputationModelSummary-description"></a>
The description of the computation model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9 _\-#$*!@]+$`
Required: No

## See Also
<a name="API_ComputationModelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ComputationModelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ComputationModelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ComputationModelSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
