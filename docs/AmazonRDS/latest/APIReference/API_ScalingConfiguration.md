---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ScalingConfiguration.html
---

# ScalingConfiguration
<a name="API_ScalingConfiguration"></a>

Contains the scaling configuration of an Aurora Serverless v1 DB cluster.

For more information, see [Using Amazon Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html) in the *Amazon Aurora User Guide*.

## Contents
<a name="API_ScalingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AutoPause **
Indicates whether to allow or disallow automatic pause for an Aurora DB cluster in `serverless` DB engine mode. A DB cluster can be paused only when it's idle (it has no connections).
If a DB cluster is paused for more than seven days, the DB cluster might be backed up with a snapshot. In this case, the DB cluster is restored when there is a request to connect to it.
Type: Boolean
Required: No

 ** MaxCapacity **
The maximum capacity for an Aurora DB cluster in `serverless` DB engine mode.
For Aurora MySQL, valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`.
For Aurora PostgreSQL, valid capacity values are `2`, `4`, `8`, `16`, `32`, `64`, `192`, and `384`.
The maximum capacity must be greater than or equal to the minimum capacity.
Type: Integer
Required: No

 ** MinCapacity **
The minimum capacity for an Aurora DB cluster in `serverless` DB engine mode.
For Aurora MySQL, valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`.
For Aurora PostgreSQL, valid capacity values are `2`, `4`, `8`, `16`, `32`, `64`, `192`, and `384`.
The minimum capacity must be less than or equal to the maximum capacity.
Type: Integer
Required: No

 ** SecondsBeforeTimeout **
The amount of time, in seconds, that Aurora Serverless v1 tries to find a scaling point to perform seamless scaling before enforcing the timeout action. The default is 300.
Specify a value between 60 and 600 seconds.
Type: Integer
Required: No

 ** SecondsUntilAutoPause **
The time, in seconds, before an Aurora DB cluster in `serverless` mode is paused.
Specify a value between 300 and 86,400 seconds.
Type: Integer
Required: No

 ** TimeoutAction **
The action to take when the timeout is reached, either `ForceApplyCapacityChange` or `RollbackCapacityChange`.
 `ForceApplyCapacityChange` sets the capacity to the specified value as soon as possible.
 `RollbackCapacityChange`, the default, ignores the capacity change if a scaling point isn't found in the timeout period.
If you specify `ForceApplyCapacityChange`, connections that prevent Aurora Serverless v1 from finding a scaling point might be dropped.
For more information, see [ Autoscaling for Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html#aurora-serverless.how-it-works.auto-scaling) in the *Amazon Aurora User Guide*.
Type: String
Required: No

## See Also
<a name="API_ScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ScalingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
