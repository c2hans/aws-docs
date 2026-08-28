---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/dev/security-iam-resources.html
---

# Amazon Comprehend Medical API Permissions: actions, resources, and conditions reference
<a name="security-iam-resources"></a>

Use the following table as a reference when setting up [Access Control](security-iam.md#access-control-med) and writing a permissions' policy that you can attach to a user. The list includes each Amazon Comprehend Medical API operation, the corresponding action for which you can grant permissions to perform the action, and the AWS resource for which you can grant the permissions. You specify the actions in the policy's `Action` field, and you specify the resource value in the policy's `Resource` field.

To express conditions, you can use AWS condition keys in your Amazon Comprehend Medical policies. For a complete list of keys, see [Available Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys) in the *IAM User Guide*.

**Note**
To specify an action, use the `comprehendmedical:` prefix followed by the API operation name, for example, `comprehendmedical:DetectEntities`.

Use the scroll bars to see the rest of the table.

**Amazon Comprehend Medical API and Required Permissions for Actions**

| Amazon Comprehend Medical API Operations | Required Permissions (API Actions) | Resources |
| --- | --- | --- |
| DescribeEntitiesDetectionV2Job | comprehendmedical:DescribeEntitiesDetectionV2Job | \* |
| DescribePHIDetectionJob | comprehendmedical:DescribePHIDetectionJob | \* |
| DetectEntities | comprehendmedical:DetectEntities | \* |
| DetectEntitiesV2 | comprehendmedical:DetectEntitiesV2 | \* |
| DetectPHI | comprehendmedical:DetectPHI | \* |
| ListEntitiesDetectionV2Jobs | comprehendmedical:ListEntitiesDetectionV2Jobs | \* |
| ListPHIDetectionJobs | comprehendmedical:ListPHIDetectionJobs | \* |
| StartEntitiesDetectionV2Job | comprehendmedical:StartEntitiesDetectionV2Job | \* |
| StartPHIDetectionJob | comprehendmedical:StartPHIDetectionJob | \* |
| StopEntitiesDetectionV2Job | comprehendmedical:StopEntitiesDetectionV2Job | \* |
| StopPHIDetectionJob | comprehendmedical:StopPHIDetectionJob | \* |
| InferICD10CM | comprehendmedical:InferICD10CM | \* |
| InferRxNorm | comprehendmedical:InferRxNorm | \* |
| InferSNOMEDCT | comprehendmedical:InferSNOMEDCT | \* |
| StartICD10CMInferenceJob | comprehendmedical:StartICD10CMInferenceJob | \* |
| StartRxNormInferenceJob | comprehendmedical:StartRxNormInferenceJob | \* |
| StartSNOMEDCTInferenceJob | comprehendmedical:StartSNOMEDCTInferenceJob | \* |
| ListICD10CMInferenceJobs | comprehendmedical:ListICD10CMInferenceJobs | \* |
| ListRxNormInferenceJobs | comprehendmedical:ListRxNormInferenceJobs | \* |
| ListSNOMEDCTInferenceJobs | comprehendmedical:ListSNOMEDCTInferenceJobs | \* |
| StopICD10CMInferenceJob | comprehendmedical:StopICD10CMInferenceJob | \* |
| StopRxNormInferenceJob | comprehendmedical:StopRxNormInferenceJob | \* |
| StopSNOMEDCTInferenceJob | comprehendmedical:StopSNOMEDCTInferenceJob | \* |
| DescribeICD10CMInferenceJob | comprehendmedical:DescribeICD10CMInferenceJob | \* |
| DescribeRxNormInferenceJob | comprehendmedical:DescribeRxNormInferenceJob | \* |
| DescribeSNOMEDCTInferenceJob | comprehendmedical:DescribeSNOMEDCTInferenceJob | \* |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend Medical. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend-medical` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
