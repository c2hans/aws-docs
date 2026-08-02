---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_CommonParametersArticle.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# Common Parameters
<a name="ApiReference_CommonParametersArticle"></a>

**Topics**
+ [Common Request Parameters](#common-request-parameters)
+ [Response Groups](#response-groups)

The Amazon Mechanical Turk Service accepts a set of parameters in the request common to every operation. Each required parameter must be included in a request for the request to be successful. Parameters common to all operations are explained in **Common Request Parameters**. For more information about the parameters for a specific operation, see the description of the operation in the [Operations](ApiReference_OperationsArticle.md) section of this reference.

Response groups specify what data is returned by Mechanical Turk for an operation request and are explained in [Response Groups](#response-groups).

## Common Request Parameters
<a name="common-request-parameters"></a>

Requests to the Amazon Mechanical Turk service can include the parameters described in the following table. Required parameters must be included with each request for the request to succeed.

| Name | Description | Required |
| --- | --- | --- |
|  `AWSAccessKeyId`  | The Requester's Access Key ID, a unique identifier that corresponds to a Secret Access Key and an Amazon.com account. <br />Type: String<br />Default: None | Yes |
|  `Service`  | The name of the Amazon Web Services service.<br />Type: String<br />Valid Values: AWSMechanicalTurkRequester<br />Default: None<br />Constraints: For REST requests only.<br /> For SOAP requests the name of the service is part of the SOAP entry point, and does not need to be specified in the request.  | Yes |
|  `Operation`  | The name of the operation.<br />Type: String<br />Default: None<br />Contraints: For REST requests only<br /> For SOAP requests, the operation name is part of the SOAP message structure provided by your SOAP toolkit, and is not part of the request.  | Yes |
|  `Signature`  | The signature for this request, an encrypted string calculated from elements of the request and the AWS access key that corresponds to your AWS Access Key ID. For information about how to calculate a `Signature`, see [AWS Request Authentication](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/MakingRequests_RequestAuthenticationArticle.html). <br />Type: String<br />Default: None | Yes |
|  `Timestamp`  |  The current time on your system. This value is included to validate against the `Signature` parameter. <br /> Type: a [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) in the Coordinated Universal Time (Greenwich Mean Time) time zone, such as **2005-01-31T23:59:59Z**. <br />Default: None | Yes |
|  `ResponseGroup`  | A list of response groups. For more information about response groups, see [Response Groups](#response-groups). <br />Type: String<br />Default: None | Yes |
|  `Version`  | Specifies what version of the API to use.<br />Type: String<br />Default: None. If not specified, the latest version of the API is used.<br />Constraints: Used only for REST requests | No |
|  `Validate`  | {{Deprecated}} | No |
|  `Credential`  | This parameter is reserved for future use.<br />Type: None<br />Default: None | Not used |

## Response Groups
<a name="response-groups"></a>

Response groups specify what data is returned by the service for an operation, to control the data included in the response. Most operations in the Amazon Mechanical Turk service allow the use of two common response groups: `Minimal` and `Request`. `Minimal` provides a minimal set of results of the operation call. `Request` echoes the content of the original request. What gets included in `Minimal` varies depending upon the API call.

The following table lists the operations that can return more response groups than `Minimal` and `Request`.

| Operation | Allowable Response Groups | Default Response Groups |
| --- | --- | --- |
| `CreateHit` | `Request`, `Minimal`, `HITDetail`, `HITQuestion`, `HITAssignmentSummary` | `Minimal` |
| `GetAssignment` | `Request`, `Minimal`, `AssignmentFeedback`, `HITDetail`, `HITQuestion` | `Minimal` |
| `GetAssignmentsForHIT` | `Request`, `Minimal`, `AssignmentFeedback` | `Minimal` |
| `GetHIT` | `Request`, `Minimal`, `HITDetail`, `HITQuestion`, `HITAssignmentSummary` | `Minimal`, `HITDetail`, `HITQuestion` |
| `GetRequesterStatistic` | `Request`, `Minimal`, `Parameters` | `Minimal`, `Parameters` |
| `GetRequesterWorkerStatistic` | `Request`, `Minimal`, `Parameters` | `Minimal`, `Parameters` |
| `SearchHITS` | `Request`, `Minimal`, `HITDetail`, `HITQuestion`, `HITAssignmentSummary` | `Minimal`, `HITDetail`, `HITAssignmentSummary` |

### Response Groups Content
<a name="response-groups-contents"></a>

The following table lists the elements returned in the response groups other than the `Minimal` and `Request` groups. The table also lists the response group elements associated with each response group.

| Response Group | Response Group Elements (alpha order) |
| --- | --- |
| `AssignmentFeedback` | `RequesterFeedback`<br />For more information on this element, see the [Assignment](ApiReference_AssignmentDataStructureArticle.md) data structure.  |
| `HITAssignmentSummary` | `NumberOfAssignmentsAvailable`<br />`NumberOfAssignmentsCompleted`<br />`NumberOfAssignmentsPending`<br />For more information on these elements, see the [HIT](ApiReference_HITDataStructureArticle.md) data structure.  |
| `HITDetail` | `AssignmentDurationInSeconds`<br />`AutoApprovalDelayInSeconds`<br />`CreationTime`<br />`Description`<br />`Expiration`<br />`Keywords`<br />`HITGroupId`<br />`HITLayoutId`<br />`HITReviewStatus`<br />`HITStatus`<br />`MaxAssignments`<br />`QualificationRequirement`<br />`RequesterAnnotation`<br />`Reward`<br />`Title`<br />For more information on these elements, see the [HIT](ApiReference_HITDataStructureArticle.md) data structure.  |
| `HITQuestion` | `Question`<br />For more information on this elements, see the [HIT](ApiReference_HITDataStructureArticle.md) data structure.  |
| `Parameters` | `Statistic`<br />`TimePeriod` |
