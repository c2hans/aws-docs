---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_ExecutionEngineConfig.html
---

# ExecutionEngineConfig
<a name="API_ExecutionEngineConfig"></a>

Specifies the execution engine (cluster) to run the notebook and perform the notebook execution, for example, an Amazon EMR cluster.

## Contents
<a name="API_ExecutionEngineConfig_Contents"></a>

 ** Id **   <a name="EMR-Type-ExecutionEngineConfig-Id"></a>
The unique identifier of the execution engine. For an Amazon EMR cluster, this is the cluster ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** ExecutionRoleArn **   <a name="EMR-Type-ExecutionEngineConfig-ExecutionRoleArn"></a>
The execution role ARN required for the notebook execution.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
Required: No

 ** MasterInstanceSecurityGroupId **   <a name="EMR-Type-ExecutionEngineConfig-MasterInstanceSecurityGroupId"></a>
An optional unique ID of an Amazon EC2 security group to associate with the master instance of the Amazon EMR cluster for this notebook execution. For more information see [Specifying Amazon EC2 Security Groups for Amazon EMR Notebooks](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-security-groups.html) in the *EMR Management Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Type **   <a name="EMR-Type-ExecutionEngineConfig-Type"></a>
The type of execution engine. A value of `EMR` specifies an Amazon EMR cluster.
Type: String
Valid Values: `EMR`
Required: No

## See Also
<a name="API_ExecutionEngineConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ExecutionEngineConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ExecutionEngineConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ExecutionEngineConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
