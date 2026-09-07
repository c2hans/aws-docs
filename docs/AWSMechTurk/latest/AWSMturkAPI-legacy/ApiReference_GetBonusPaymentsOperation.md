---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GetBonusPaymentsOperation.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GetBonusPayments
<a name="ApiReference_GetBonusPaymentsOperation"></a>

## Description
<a name="ApiReference_GetBonusPaymentsOperation-description"></a>

 The `GetBonusPayments` operation retrieves the amounts of bonuses you have paid to Workers for a given HIT or assignment.

## Request Parameters
<a name="ApiReference_GetBonusPaymentsOperation-request-parameters"></a>

 The `GetBonusPayments` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `GetBonusPayments` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: GetBonusPayments<br />Default: None | Yes |
|  `HITId`  |  The ID of the HIT associated with the bonus payments to retrieve. If not specified, all bonus payments for all assignments for the given HIT are returned. <br />Type: String<br />Default: None<br /> Conditions: Either the `HITId` parameter or the `AssignmentId` parameter must be specified.  | Conditional |
|  `AssignmentId`  |  The ID of the assignment associated with the bonus payments to retrieve. If specified, only bonus payments for the given assignment are returned. <br />Type: String<br />Default: None<br /> Conditions: Either the `HITId` parameter or the `AssignmentId` parameter must be specified.  | Conditional |
|  `PageSize`  |  The number of bonus payments to include in a page of results. The complete result set is divided into pages of this many bonus payments. <br />Type: positive integer<br />Valid Values: any integer between 1 and 100<br />Default: 10 | No |
|  `PageNumber`  |  The page of results to return. Once the list of bonus payments has been divided into pages of size `PageSize`, the page corresponding to `PageNumber` is returned as the results of the operation. <br />Type: positive integer<br />Default: 1 | No |

## Response Elements
<a name="ApiReference_GetBonusPaymentsOperation-response-elements"></a>

 A successful request for the `GetBonusPayments` operation has a `GetBonusPaymentsResult` element in the response.

 The `GetBonusPaymentsResult` element contains the following elements:

| Name | Description |
| --- | --- |
| PageNumber |  The page of results to return. Once the list of bonus payments has been divided into pages of size `PageSize`, the page corresponding to the `PageNumber` parameter is returned as the results of the operation. <br />Type: positive integer |
| NumResults |  The number of bonus payments on this page in the filtered results list, equivalent to the number of bonus payments being returned by this call. <br />Type: non-negative integer |
| TotalNumResults |  The total number of bonus payments in the filtered results list based on this call. <br />Type: non-negative integer |
| BonusPayment |  A bonus payment. The response includes one `BonusPayment` element for each bonus payment returned by the query. <br />Type: A BonusPayment data structure, described in the next table. |

 Each `BonusPayment` is a data structure with the following elements:

| Name | Description |
| --- | --- |
|  `WorkerId`  |  The ID of the Worker to whom the bonus was paid. <br />Type: String |
|  `BonusAmount`  | The amount of the bonus payment.<br /> Type: A [Price](ApiReference_PriceDataStructureArticle.md) data structure  |
|  `AssignmentId`  |  The ID of the assignment associated with this bonus payment <br />Type: String |
|  `Reason`  |  The **Reason** text given when the bonus was granted, if any. <br />Type: String |
|  `GrantTime`  | The date and time of when the bonus was granted.<br /> Type: A [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) structure in the Coordinated Universal Time (Greenwich Mean Time) time zone, such as **2005-01-31T23:59:59Z**.  |

## Examples
<a name="ApiReference_GetBonusPaymentsOperation-examples"></a>

The following example shows how to use the `GetBonusPayments` operation.

### Sample Request
<a name="ApiReference_GetBonusPaymentsOperation-examples-sample-request"></a>

 The following example retrieves all bonus payments associated with the specified HIT.

```
1. https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
2. &AWSAccessKeyId={{[the Requester's Access Key ID]}}
3. &Version=2017-01-17
4. &Operation=GetBonusPayments
5. &Signature={{[signature for this request]}}
6. &Timestamp={{[your system's local time]}}
7. &HITId=123RVWYBAZW00EXAMPLE
```

### Sample Response
<a name="ApiReference_GetBonusPaymentsOperation-examples-sample-response"></a>

The following is an example response.

```
<GetBonusPaymentsResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <NumResults>0</NumResults>
  <TotalNumResults>0</TotalNumResults>
  <PageNumber>1</PageNumber>
</GetBonusPaymentsResult>
```
