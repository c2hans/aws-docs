---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Transform.html
---

# Transform
<a name="API_Transform"></a>

Contains an asset transform property. A transform is a one-to-one mapping of a property's data points from one form to another. For example, you can use a transform to convert a Celsius data stream to Fahrenheit by applying the transformation expression to each data point of the Celsius stream. A transform can only have a data type of `DOUBLE` and consume properties with data types of `INTEGER` or `DOUBLE`.

For more information, see [Transforms](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html#transforms) in the * AWS IoT SiteWise User Guide*.

## Contents
<a name="API_Transform_Contents"></a>

 ** expression **   <a name="iotsitewise-Type-Transform-expression"></a>
The mathematical expression that defines the transformation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** variables **   <a name="iotsitewise-Type-Transform-variables"></a>
The list of variables used in the expression.
Type: Array of [ExpressionVariable](API_ExpressionVariable.md) objects
Required: Yes

 ** processingConfig **   <a name="iotsitewise-Type-Transform-processingConfig"></a>
The processing configuration for the given transform property. You can configure transforms to be kept at the edge or forwarded to the AWS Cloud. You can also configure transforms to be computed at the edge or in the cloud.
Type: [TransformProcessingConfig](API_TransformProcessingConfig.md) object
Required: No

## See Also
<a name="API_Transform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/Transform)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/Transform)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/Transform)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
