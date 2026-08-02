---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_Goal.html
---

# Goal
<a name="API_Goal"></a>

Represents a goal with all its properties and metadata

## Contents
<a name="API_Goal_Contents"></a>

 ** agentSpaceArn **   <a name="devopsagent-Type-Goal-agentSpaceArn"></a>
The unique identifier for the agent space containing this goal
Type: String
Required: Yes

 ** content **   <a name="devopsagent-Type-Goal-content"></a>
Content of the goal
Type: [GoalContent](API_GoalContent.md) object
Required: Yes

 ** createdAt **   <a name="devopsagent-Type-Goal-createdAt"></a>
Timestamp when this goal was created
Type: Timestamp
Required: Yes

 ** goalId **   <a name="devopsagent-Type-Goal-goalId"></a>
The unique identifier for this goal
Type: String
Required: Yes

 ** goalType **   <a name="devopsagent-Type-Goal-goalType"></a>
Type of goal based on its origin
Type: String
Valid Values: `CUSTOMER_DEFINED | ONCALL_REPORT`
Required: Yes

 ** status **   <a name="devopsagent-Type-Goal-status"></a>
Current status of the goal itself
Type: String
Valid Values: `ACTIVE | PAUSED | COMPLETE`
Required: Yes

 ** title **   <a name="devopsagent-Type-Goal-title"></a>
The title of the goal
Type: String
Required: Yes

 ** updatedAt **   <a name="devopsagent-Type-Goal-updatedAt"></a>
Timestamp when this goal was last updated
Type: Timestamp
Required: Yes

 ** version **   <a name="devopsagent-Type-Goal-version"></a>
Version number for optimistic locking
Type: Integer
Required: Yes

 ** evaluationSchedule **   <a name="devopsagent-Type-Goal-evaluationSchedule"></a>
Goal Schedule. Allows to schedule the goal to run periodically, as well as disable a goal temporarily
Type: [GoalSchedule](API_GoalSchedule.md) object
Required: No

 ** lastEvaluatedAt **   <a name="devopsagent-Type-Goal-lastEvaluatedAt"></a>
Timestamp when the goal was last evaluated
Type: Timestamp
Required: No

 ** lastSuccessfulTaskId **   <a name="devopsagent-Type-Goal-lastSuccessfulTaskId"></a>
ID of the most recent successful task associated with this goal
Type: String
Required: No

 ** lastTaskId **   <a name="devopsagent-Type-Goal-lastTaskId"></a>
ID of the most recent task associated with this goal
Type: String
Required: No

## See Also
<a name="API_Goal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/Goal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/Goal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/Goal)
