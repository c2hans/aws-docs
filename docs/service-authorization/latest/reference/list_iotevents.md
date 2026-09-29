---
source_url: https://docs.aws.amazon.com/service-authorization/latest/reference/list_iotevents.html
---

# Actions, resources, and condition keys for iotevents
<a name="list_iotevents"></a>

iotevents (service prefix: `iotevents`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iotevents/iotevents.json) for this service.

**Topics**
+ [Actions defined by iotevents](#list_iotevents-actions-as-permissions)
+ [Resource types defined by iotevents](#list_iotevents-resources-for-iam-policies)
+ [Condition keys for iotevents](#list_iotevents-policy-keys)

## Actions defined by iotevents
<a name="list_iotevents-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.

- **   BatchAcknowledgeAlarm  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   BatchDeleteDetector  **
  - **Description:**
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   BatchDisableAlarm  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   BatchEnableAlarm  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   BatchPutMessage  **
  - **Description:**
  - **Resource types (\*required):** [input](#list_iotevents-resource-input)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   BatchResetAlarm  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   BatchSnoozeAlarm  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   BatchUpdateDetector  **
  - **Description:**
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   CreateAlarmModel  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotevents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Access level:** Write

- **   CreateDetectorModel  **
  - **Description:**
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotevents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Access level:** Write

- **   CreateInput  **
  - **Description:**
  - **Resource types (\*required):** [input](#list_iotevents-resource-input)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotevents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Access level:** Write

- **   DeleteAlarmModel  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   DeleteDetectorModel  **
  - **Description:**
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   DeleteInput  **
  - **Description:**
  - **Resource types (\*required):** [input](#list_iotevents-resource-input)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   DescribeAlarm  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   DescribeAlarmModel  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   DescribeDetector  **
  - **Description:**
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   DescribeDetectorModel  **
  - **Description:**
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   DescribeDetectorModelAnalysis  **
  - **Description:**
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Read

- **   DescribeInput  **
  - **Description:**
  - **Resource types (\*required):** [input](#list_iotevents-resource-input)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   DescribeLoggingOptions  **
  - **Description:**
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Read

- **   GetDetectorModelAnalysisResults  **
  - **Description:**
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Read

- **   ListAlarmModelVersions  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   ListAlarmModels  **
  - **Description:**
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   ListAlarms  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   ListDetectorModelVersions  **
  - **Description:**
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   ListDetectorModels  **
  - **Description:**
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   ListDetectors  **
  - **Description:**
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   ListInputRoutings  **
  - **Description:**
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   ListInputs  **
  - **Description:**
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   ListTagsForResource  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [input](#list_iotevents-resource-input) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   PutLoggingOptions  **
  - **Description:**
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Write

- **   StartDetectorModelAnalysis  **
  - **Description:**
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Write

- **   TagResource  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotevents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotevents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Resource types (\*required):** [input](#list_iotevents-resource-input) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotevents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Resource types (\*required):** [input](#list_iotevents-resource-input) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   UpdateAlarmModel  **
  - **Description:**
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   UpdateDetectorModel  **
  - **Description:**
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   UpdateInput  **
  - **Description:**
  - **Resource types (\*required):** [input](#list_iotevents-resource-input)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   UpdateInputRouting  **
  - **Description:**
  - **Resource types (\*required):** [input](#list_iotevents-resource-input)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

## Resource types defined by iotevents
<a name="list_iotevents-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.

| Resource types | ARN | Condition keys |
| --- | --- | --- |
|  alarmModel  | arn:${Partition}:iotevents:${Region}:${Account}:alarmModel/${AlarmModelName} | [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_) |
|  detectorModel  | arn:${Partition}:iotevents:${Region}:${Account}:detectorModel/${DetectorModelName} | [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_) |
|  input  | arn:${Partition}:iotevents:${Region}:${Account}:input/${InputName} | [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_) |

## Condition keys for iotevents
<a name="list_iotevents-policy-keys"></a>

iotevents defines the following condition keys that can be used in the `Condition` element of an IAM policy.

| Condition keys | Description | Type |
| --- | --- | --- |
|   aws:RequestTag/${TagKey}  |  | String |
|   aws:ResourceTag/${TagKey}  |  | String |
|   aws:TagKeys  |  | ArrayOfString |
|   iotevents:keyValue  |  | String |
