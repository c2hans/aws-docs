---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GetRequesterWorkerStatisticOperation.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GetRequesterWorkerStatistic
<a name="ApiReference_GetRequesterWorkerStatisticOperation"></a>

## Description
<a name="ApiReference_GetRequesterWorkerStatisticOperation-description"></a>

The `GetRequesterWorkerStatistic` operation retrieves statistics about a specific Worker who has completed Human Intelligence Tasks (HITs) for you. If you have used Review Policies with known answers or plurality, Mechanical Turk will summarize the following statistics about the Worker's known answers and agreement level. These statistics are only for your Requester account. For more information about Review Policies, see [Review Policies](ApiReference_ReviewPoliciesArticle.md).

The following table describes the available statistics:

| Name | Description |
| --- | --- |
|  NumberAssignmentsApproved  | The number of assignments you have approved for the Worker. <br />Type: Long  |
|  NumberAssignmentsRejected  | The number of assignments you have rejected for the Worker.<br />Type: Long  |
|  PercentAssignmentsApproved  | The percentage of assignments approved, which is the Number of assignments approved divided by the number of assignments approved or rejected. <br />Type: Double  |
|  PercentAssignmentsRejected  | The percentage of assignments rejected, which is the Number of assignments rejected divided by the number of assignments approved or rejected. <br />Type: Double  |
|  NumberKnownAnswersCorrect  | The total number of *known answer* questions that the Worker has answered correctly. <br />Type: Long  |
|  NumberKnownAnswersIncorrect  | The total number of *known answer* questions that the Worker has answered incorrectly. <br />Type: Long  |
|  NumberKnownAnswersEvaluated  | The total number of *known answer* questions in assignments the Worker has submitted. <br />Type: Long  |
|  PercentKnownAnswersCorrect  | The rounded percentage of *known answer* questions the Worker has answered correctly, which is the number of correct known answers divided by the number of known answers evaluated. <br />Type: Double  |
|  NumberPluralityAnswersCorrect  | The number of evaluated questions that the Worker provided the agreed-upon answer for. <br />Type: Long  |
|  NumberPluralityAnswersIncorrect  | The number of evaluated questions that the Worker did not provide the agreed-upon answer for.<br />Type: Long  |
|  NumberPluralityAnswersEvaluated  | The number of evaluated questions answered by the Worker participating in the HIT. <br />Type: Long  |
|  PercentPluralityAnswersCorrect  | The number of questions that the Worker provided the agreed-upon answer for, divided by the number of evaluated questions.<br />Type: Double  |

## Request Parameters
<a name="ApiReference_GetRequesterWorkerStatisticOperation-request-parameters"></a>

The `GetRequesterWorkerStatistic` operation accepts parameters common to all operations. Some common parameters are required. For more information, see [Common Parameters](ApiReference_CommonParametersArticle.md).

 The following parameters are specific to the `GetRequesterWorkerStatistic` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation.<br />Type: String<br />Valid Values: GetRequesterWorkerStatistic<br />Default: None | Yes |
|  `Statistic`  | The statistic to return.<br />Type: String<br />Valid Values: See the preceding available statistics table.<br />Default: None | Yes |
|  `WorkerId`  | The Worker you want to return the statistics for.<br />Type: String<br />Default: None | Yes |
|  `TimePeriod`  | The time period of the statistic to return.<br />Type: String<br />Valid Values: OneDay \| SevenDays \| ThirtyDays \| LifeToDate<br />Default: None | Yes |
|  `Count`  | The number of data points to return.<br />Type: Positive Integer<br />Default: 1<br />Conditions: only used if `TimePeriod` is `OneDay`. <br />For example, if `TimePeriod` is `OneDay` and `Count` is `12`, the operation returns 12 data points for the statistic, one for each of 12 calendar days leading up to the current date, including the current day.  | Conditional |

## Response Elements
<a name="ApiReference_GetRequesterWorkerStatisticOperation-response-elements"></a>

A successful request for the `GetRequesterWorkerStatistic` operation has a `GetStatisticResult` element in the response.

 The `GetStatisticResult` element contains the elements in the following table for each value requested.

| Name | Description |
| --- | --- |
|  `WorkerId`  | The Worker ID you are requesting the statistics for.<br />Type: String |
|  `Statistic` | The named statistic you specified in the Request. See the preceding table for a list of statistics. <br />Type: String |
|  `TimePeriod` | The time period you specified in the Request.<br />Type: String |
|  `DataPoint` | The data point data structure described in the next table.<br />Type: DataPoint structure |

Each `DataPoint` data structure contains the following elements:

| Name | Description |
| --- | --- |
|  `Date`  | The date represented by the data point. For aggregate values, this is the current date. <br /> Type: A [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) structure in the Coordinated Universal Time (Greenwich Mean Time) time zone, such as `2005-01-31T23:59:59Z`  |
|  `LongValue` \| `DoubleValue`  | The value of the statistic over the specified time period. The element name and data type depend on which statistic was requested. <br />Type: A Long or a Double, depending on the requested statistic. |

## Examples
<a name="ApiReference_GetRequesterWorkerStatisticOperation-examples"></a>

The following example shows how to use the `GetRequesterWorkerStatistic` operation.

### Sample Request
<a name="ApiReference_GetRequesterWorkerStatisticOperation-examples-sample-request"></a>

The following GetRequesterWorkerStatistic operation request retrieves the number of assignments approved for the Worker ID A1Z4X5D207ALZF in the last 30 days.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2011-09-01
&Operation=GetRequesterWorkerStatistic
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&Statistic=NumberAssignmentsApproved
&WorkerId=A1Z4X5D207ALZF
&TimePeriod=ThirtyDays
&Count=1
```

### Sample Response
<a name="ApiReference_GetRequesterWorkerStatisticOperation-examples-sample-response"></a>

The following is an example response where the Worker had 281 assignments approved in the last 30 days.

```
<GetStatisticResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <WorkerId>A1Z4X5D207ALZF</WorkerId>
  <Statistic>NumberAssignmentsApproved</Statistic>
  <TimePeriod>ThirtyDays</TimePeriod>
  <DataPoint>
    <Date>2011-09-05T07:00:00Z</Date>
    <DoubleValue>281</DoubleValue>
  </DataPoint>
</GetStatisticResult>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
