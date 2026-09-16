---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GetRequesterStatisticOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GetRequesterStatistic
<a name="ApiReference_GetRequesterStatisticOperation"></a>

## Description
<a name="ApiReference_GetRequesterStatisticOperation-description"></a>

 The `GetRequesterStatistic` operation retrieves statistics about you (the Requester calling the operation). The following table describes the available statistics:

| Name | Description |
| --- | --- |
|  NumberAssignmentsAvailable  | DEPRECATED\* as of 11/01/2016 - The number of times Workers can accept an available HIT, totaled over all available HITs. In other words, a HIT with 3 `MaxAssignments` can be described as having 3 available assignments, each of become **Accepted** when a Worker accepts the HIT. (Technically, Amazon Mechanical Turk does not create an assignment with an assignment ID until a Worker accepts a HIT.) <br />Type: Long |
|  NumberAssignmentsAccepted  | DEPRECATED\* as of 11/01/2016 - The number of times Workers have accepted your HITs. <br />Type: Long |
|  NumberAssignmentsPending  | The total number of assignments for your HITs that have been submitted by Workers and are awaiting approval. The total increases and decreases as assignments are submitted by Workers and approved or rejected by you. <br />Type: Long |
|  NumberAssignmentsApproved  | The number of assignments you have approved.<br />Type: Long |
|  NumberAssignmentsRejected  | The number of assignments you have rejected.<br />Type: Long |
|  NumberAssignmentsReturned  | DEPRECATED\* as of 11/01/2016 - The number of times Workers have returned assignments for your HITs.<br />Type: Long |
|  NumberAssignmentsAbandoned  | The number of times Workers have abandoned assignments (allowed the deadline to elapse without submitting results) for your HITs. <br />Type: Long |
|  PercentAssignmentsApproved  | The percentage of assignments that you have approved, computed over all assignments that you have approved or rejected. The percentage is represented as a decimal fraction between 0 and 1. The statistic value for a given day represents a change in the overall percentage due to activity for that day. <br />Type: Double |
|  PercentAssignmentsRejected  | The percentage of assignments that you have rejected, computed over all assignments that you have approved or rejected. The percentage is represented as a decimal fraction between 0 and 1. The statistic value for a given day represents a change in the overall percentage due to activity for that day. <br />Type: Double |
|  TotalRewardPayout  | The total amount of the rewards paid for approved assignments. The amount is given in U.S. dollars. <br />Type: Double |
|  AverageRewardAmount  | The change in the average amount of the rewards paid for approved assignments. The amount is given in U.S. dollars. <br />Type: Double |
|  TotalRewardFeePayout  | The total amount of the HIT listing fees paid for approved assignments. The amount is given in U.S. dollars. <br />Type: Double |
|  TotalFeePayout  | The total amount of the HIT listing fees paid for approved assignments and bonus payments. The amount is given in U.S. dollars. <br /> *This statistic is deprecated. * To get the total amount of fees paid for rewards and bonuses, get the `TotalRewardFeePayout` statistic and the `TotalBonusFeePayout` statistic and add them together. <br />Type: Double |
|  TotalRewardAndFeePayout  | The total amount of money paid for approved assignments, including rewards and fees. The amount is given in U.S. dollars. <br /> This total does *not* include fees for bonus payments made with the [GrantBonus](ApiReference_GrantBonusOperation.md) operation. <br /> *This statistic is deprecated.* To get the total amount of money paid for rewards and reward fees, get the `TotalRewardPayout` and `TotalRewardFeePayout` statistics and add them together. <br />Type: Double |
|  TotalBonusPayout  | The total amount of the bonuses paid to Workers. The amount is given in U.S. dollars. <br />Type: Double |
|  TotalBonusFeePayout  | The total amount of the fees paid for bonus payments. The amount is given in U.S. dollars. <br />Type: Double |
|  NumberHITsCreated  | The number of HITs you created. <br />Type: Long |
|  NumberHITsCompleted  | The total number of your HITs that have been completed to their final state of either **Disposed** or **Disabled**. <br />Type: Long |
|  NumberHITsAssignable  | The number of your HITs with status **Assignable**.   `NumberHITsAssignable` can only be queried as a **LifeToDate** value. While most statistics change in real time, a day's value for this statistic is added to the `LifeToDate` total at the end of the day.  <br />Type: Long |
|  NumberHITsReviewable  | The number of your HITs with status **Reviewable**. <br />Type: Long |
|  EstimatedRewardLiability  | The total amount of all of the rewards for HITs and assignments that have not yet been completed. This includes the reward for each unclaimed assignment for HITs that have not yet expired, each assignment in progress, and each submitted assignment that has not yet been approved or rejected. This is an estimate, because it is possible that not all of a HIT's assignments will be completed before the HIT expires. The amount is given in U.S. dollars. <br />Type: Double |
|  EstimatedFeeLiability  | The total amount of all of the HIT listing fees for HITs and assignments that have not yet been completed at a given point in time. The amount is given in U.S. dollars. <br />Type: Double |
|  EstimatedTotalLiability  | The total amount of all of the rewards and fees for HITs and assignments that have not yet been completed at a given point in time. The amount is given in U.S. dollars. <br />Type: Double |

\*Deprecated statistics are not expected to be accurate. The `GetRequesterStatistic` operation may return an exception when a deprecated metric is requested.

## Request Parameters
<a name="ApiReference_GetRequesterStatisticOperation-request-parameters"></a>

 The `GetRequesterStatistic` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `GetRequesterStatistic` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: GetRequesterStatistic<br />Default: None | Yes |
|  `Statistic`  | The statistic to return<br />Type: String<br />Valid Values: See the preceding table.<br />Default: None | Yes |
|  `TimePeriod`  | The time period of the statistic to return.<br />Type: String<br />Valid Values: OneDay \| SevenDays \| ThirtyDays \| LifeToDate<br />Default: None | Yes |
|  `Count`  | The number of data points to return<br />Type: positive integer<br />Default: 1<br /> Conditions: only used if `TimePeriod` is `OneDay` <br /> For example, if `TimePeriod` is `OneDay` and `Count` is `12`, the operation returns 12 data points for the statistic, one for each of 12 calendar days leading up to the current date, including the current day.  | Conditional |

## Response Elements
<a name="ApiReference_GetRequesterStatisticOperation-response-elements"></a>

A successful request for the `GetRequesterStatistic` operation has a `GetStatisticResult` element in the response.

 The `GetStatisticResult` element contains a the following elements for each value requested.

| Name | Description |
| --- | --- |
|  `Statistic`  | The named statistic you specified in the Request. See the preceding table for a list of statistics.<br />Type: String |
|  `TimePeriod`  | The time period you specified in the Request. <br />Type: String |
|  `DataPoint`  | The data point data structure described in the next table.<br />Type: DataPoint structure |

 Each `DataPoint` element contains the following elements:

| Name | Description |
| --- | --- |
|  `Date`  | The date represented by the data point. For aggregate values, this is the current date. <br />Type: A [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) structure in the Coordinated Universal Time (Greenwich Mean Time) time zone, such as `2005-01-31T23:59:59Z`  |
|  `LongValue` \| `DoubleValue`  | The value of the statistic over the specified time period. The element name and data type depend on which statistic was requested. <br />Type: a long or a double, depending on the requested statistic. |

## Examples
<a name="ApiReference_GetRequesterStatisticOperation-examples"></a>

The following example shows how to use the `GetRequesterStatistic` operation.

### Sample Request
<a name="ApiReference_GetRequesterStatisticOperation-examples-sample-request"></a>

The following example of a call to the `GetRequesterStatistic` operation retrieves the total reward payout for the thirty days leading up to the current date.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2011-09-01
&Operation=GetRequesterStatistic
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&Statistic=NumberAssignmentsApproved
&TimePeriod=ThirtyDays
&Count=1
```

### Sample Response
<a name="ApiReference_GetRequesterStatisticOperation-examples-sample-response"></a>

The following is an example response.

```
<GetStatisticResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <Statistic>NumberAssignmentsApproved</Statistic>
  <TimePeriod>ThirtyDays</TimePeriod>
  <DataPoint>
    <Date>2011-09-05T07:00:00Z</Date>
    <DoubleValue>281</DoubleValue>
  </DataPoint>
</GetStatisticResult>
```
