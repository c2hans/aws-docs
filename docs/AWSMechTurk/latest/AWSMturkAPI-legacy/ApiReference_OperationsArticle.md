---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_OperationsArticle.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# Operations
<a name="ApiReference_OperationsArticle"></a>

 The Amazon Mechanical Turk API consists of web service operations for every task the service can perform. This section describes each operation in detail.
+ [ApproveAssignment](ApiReference_ApproveAssignmentOperation.md)
+ [ApproveRejectedAssignment](ApiReference_ApproveRejectedAssignmentOperation.md)
+ [AssignQualification](ApiReference_AssignQualificationOperation.md)
+ [BlockWorker](ApiReference_BlockWorkerOperation.md)
+ [ChangeHITTypeOfHIT](ApiReference_ChangeHITTypeOfHITOperation.md)
+ [CreateHIT](ApiReference_CreateHITOperation.md)
+ [CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md)
+ [DisableHIT](ApiReference_DisableHITOperation.md)
+ [DisposeHIT](ApiReference_DisposeHITOperation.md)
+ [DisposeQualificationType](ApiReference_DisposeQualificationTypeOperation.md)
+ [ExtendHIT](ApiReference_ExtendHITOperation.md)
+ [ForceExpireHIT](ApiReference_ForceExpireHITOperation.md)
+ [GetAccountBalance](ApiReference_GetAccountBalanceOperation.md)
+ [GetAssignment](ApiReference_GetAssignmentOperation.md)
+ [GetAssignmentsForHIT](ApiReference_GetAssignmentsForHITOperation.md)
+ [GetBlockedWorkers](ApiReference_GetBlockedWorkersOperation.md)
+ [GetBonusPayments](ApiReference_GetBonusPaymentsOperation.md)
+ [GetFileUploadURL](ApiReference_GetFileUploadURLOperation.md)
+ [GetHIT](ApiReference_GetHITOperation.md)
+ [GetHITsForQualificationType](ApiReference_GetHITsForQualificationTypeOperation.md)
+ [GetQualificationsForQualificationType](ApiReference_GetQualificationsForQualificationTypeOperation.md)
+ [GetQualificationRequests](ApiReference_GetQualificationRequestsOperation.md)
+ [GetQualificationScore](ApiReference_GetQualificationScoreOperation.md)
+ [GetQualificationType](ApiReference_GetQualificationTypeOperation.md)
+ [GetReviewableHITs](ApiReference_GetReviewableHITsOperation.md)
+ [GetReviewResultsForHIT](ApiReference_GetReviewResultsForHitOperation.md)
+ [GetRequesterStatistic](ApiReference_GetRequesterStatisticOperation.md)
+ [GetRequesterWorkerStatistic](ApiReference_GetRequesterWorkerStatisticOperation.md)
+ [GrantBonus](ApiReference_GrantBonusOperation.md)
+ [GrantQualification](ApiReference_GrantQualificationOperation.md)
+ [NotifyWorkers](ApiReference_NotifyWorkersOperation.md)
+ [RegisterHITType](ApiReference_RegisterHITTypeOperation.md)
+ [RejectAssignment](ApiReference_RejectAssignmentOperation.md)
+ [RejectQualificationRequest](ApiReference_RejectQualificationRequestOperation.md)
+ [RevokeQualification](ApiReference_RevokeQualificationOperation.md)
+ [SearchHITs](ApiReference_SearchHITsOperation.md)
+ [SearchQualificationTypes](ApiReference_SearchQualificationTypesOperation.md)
+ [SendTestEventNotification](ApiReference_SendTestEventNotificationOperation.md)
+ [SetHITAsReviewing](ApiReference_SetHITAsReviewingOperation.md)
+ [SetHITTypeNotification](ApiReference_SetHITTypeNotificationOperation.md)
+ [UnblockWorker](ApiReference_UnblockWorkerOperation.md)
+ [UpdateQualificationScore](ApiReference_UpdateQualificationScoreOperation.md)
+ [UpdateQualificationType](ApiReference_UpdateQualificationTypeOperation.md)
