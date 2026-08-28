---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ServerlessV2FeaturesSupport.html
---

# ServerlessV2FeaturesSupport
<a name="API_ServerlessV2FeaturesSupport"></a>

Specifies any Aurora Serverless v2 properties or limits that differ between Aurora engine versions and platform versions. You can test the values of this attribute when deciding which Aurora version to use in a new or upgraded DB cluster. You can also retrieve the version of an existing DB cluster and check whether that version supports certain Aurora Serverless v2 features before you attempt to use those features.

## Contents
<a name="API_ServerlessV2FeaturesSupport_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MaxCapacity **
 Specifies the upper Aurora Serverless v2 capacity limit for a particular engine version or platform version. Depending on the engine version, the maximum capacity for an Aurora Serverless v2 cluster might be `256` or `128`.
Type: Double
Required: No

 ** MinCapacity **
If the minimum capacity is 0 ACUs, the engine version or platform version supports the automatic pause/resume feature of Aurora Serverless v2.
Type: Double
Required: No

## See Also
<a name="API_ServerlessV2FeaturesSupport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ServerlessV2FeaturesSupport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ServerlessV2FeaturesSupport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ServerlessV2FeaturesSupport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
