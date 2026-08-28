---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeConnectionResourceParameters.html
---

# DescribeConnectionResourceParameters
<a name="API_DescribeConnectionResourceParameters"></a>

The parameters for EventBridge to use when invoking the resource endpoint.

## Contents
<a name="API_DescribeConnectionResourceParameters_Contents"></a>

 ** ResourceAssociationArn **   <a name="eventbridge-Type-DescribeConnectionResourceParameters-ResourceAssociationArn"></a>
For connections to private APIs, the Amazon Resource Name (ARN) of the resource association EventBridge created between the connection and the private API's resource configuration.
For more information, see [ Managing service network resource associations for connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html#connection-private-snra) in the * *Amazon EventBridge User Guide* *.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `^arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:servicenetworkresourceassociation/snra-[0-9a-z]{17}$`
Required: Yes

 ** ResourceConfigurationArn **   <a name="eventbridge-Type-DescribeConnectionResourceParameters-ResourceConfigurationArn"></a>
The Amazon Resource Name (ARN) of the resource configuration for the private API.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `^(?:^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}$|^$)`
Required: Yes

## See Also
<a name="API_DescribeConnectionResourceParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DescribeConnectionResourceParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DescribeConnectionResourceParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DescribeConnectionResourceParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
