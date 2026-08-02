---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_OperationEvent.html
---

# OperationEvent
<a name="API_OperationEvent"></a>

An operation event returns details for an operation, including key milestones which can be used to monitor and track operations in progress.

Operation events contain:
+ Description string
+ Resource, including its ARN and type
+ Status
+ StatusMessage string
+ TimeStamp

Operation event examples include StartApplication or StopApplication.

## Contents
<a name="API_OperationEvent_Contents"></a>

 ** Description **   <a name="ssmsap-Type-OperationEvent-Description"></a>
A description of the operation event. For example, "Stop the EC2 instance i-abcdefgh987654321".
Type: String
Required: No

 ** Resource **   <a name="ssmsap-Type-OperationEvent-Resource"></a>
The resource involved in the operations event.
Contains `ResourceArn` ARN and `ResourceType`.
Type: [Resource](API_Resource.md) object
Required: No

 ** Status **   <a name="ssmsap-Type-OperationEvent-Status"></a>
The status of the operation event. The possible statuses are: `IN_PROGRESS`, `COMPLETED`, and `FAILED`.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED`
Required: No

 ** StatusMessage **   <a name="ssmsap-Type-OperationEvent-StatusMessage"></a>
The status message relating to a specific operation event.
Type: String
Required: No

 ** Timestamp **   <a name="ssmsap-Type-OperationEvent-Timestamp"></a>
The timestamp of the specified operation event.
Type: Timestamp
Required: No

## See Also
<a name="API_OperationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/OperationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/OperationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/OperationEvent)
