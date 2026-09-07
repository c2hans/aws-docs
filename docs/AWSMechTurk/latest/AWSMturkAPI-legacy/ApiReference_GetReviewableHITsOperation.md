---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GetReviewableHITsOperation.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GetReviewableHITs
<a name="ApiReference_GetReviewableHITsOperation"></a>

## Description
<a name="ApiReference_GetReviewableHITsOperation-description"></a>

 The `GetReviewableHITs` operation retrieves the HITs with `Status` equal to **Reviewable** or `Status` equal to **Reviewing** that belong to the Requester calling the operation.

 You can limit the query to HITs with a specified HIT type.

 The operation sorts the results, divides them into numbered pages, and returns a single page of results. You can control sorting and pagination can be controlled with parameters to the operation.

 When (`PageNumber` x `PageSize`) is less than 100, you can get reliable results when you use any of the sort properties. If this number is greater than 100, use the **Enumeration** sort property for best results. The **Enumeration** sort property guarantees that the operation returns all reviewable HITs with no duplicates, but not in any specific order.

## Request Parameters
<a name="ApiReference_GetReviewableHITsOperation-request-parameters"></a>

 The `GetReviewableHITs` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `GetReviewableHITs` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: GetReviewableHITs<br />Default: None | Yes |
|  `HITTypeId`  |  The ID of the HIT type of the HITs to consider for the query. <br />Type: String<br />Default: None. If not specified, all of the Requester's HITs are considered for the query. | No |
|  `Status`  | The status of the HITs to return<br />Type: String<br />Valid Values: Reviewable \| Reviewing<br />Default: Reviewable<br /> To query both **Reviewable** and **Reviewing** HITs, specify multiple `Status` parameters.  | No |
|  `SortProperty`  | The field on which to sort the results.<br />Type: String<br />Valid Values: Title \| Reward \| Expiration \| CreationTime \| Enumeration<br />Default: Expiration | No |
|  `SortDirection`  |  The direction of the sort used with the field specified by the `SortProperty` property. <br />Type: String<br />Valid Values: Ascending \| Descending<br />Default: Descending | No |
|  `PageSize`  |  The number of HITs to include in a page of results. The operation divides the complete sorted result set is divided into pages of this many HITs. <br />Type: positive integer<br />Valid Values: any number between 1 and 100<br />Default: 10 | No |
|  `PageNumber`  |  The page of results to return. After the operation filters, sorts, and divides the HITs into pages of size `PageSize`, it returns the page corresponding to `PageNumber` as the results of the operation. <br />Type: positive integer<br />Default: 1 | No |

## Response Elements
<a name="ApiReference_GetReviewableHITsOperation-response-elements"></a>

 A successful request for the `GetReviewableHITs` operation has a `GetReviewableHITsResult` element in the response.

 The `GetReviewableHITsResult` element contains the following elements:

| Name | Description |
| --- | --- |
|  `NumResults`  |  The number of HITs on this page in the filtered results list, equivalent to the number of HITs this call returns. <br />Type: non-negative integer |
|  `PageNumber`  | The number of this page in the filtered results list.<br />Type: positive integer |
|  `TotalNumResults`  | The total number of HITs in the filtered results list based on this call.<br />Type: non-negative integer |
|  `HIT`  |  The HIT. The response includes one `HIT` element for each HIT returned by the query. <br />Type: a [HIT](ApiReference_HITDataStructureArticle.md) data structure |

## Examples
<a name="ApiReference_GetReviewableHITsOperation-examples"></a>

The following example shows how to use the `GetReviewableHITs` operation.

### Sample Request
<a name="ApiReference_GetReviewableHITsOperation-examples-sample-request"></a>

 The following example retrieves five of the Requester's reviewable HITs, using the default values for the `SortProperty` and `SortOrder` parameters (ExpirationDate, Ascending).

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2017-01-17
&Operation=GetReviewableHITs
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&PageSize=5
&PageNumber=1
```

### Sample Response
<a name="ApiReference_GetReviewableHITsOperation-examples-sample-response"></a>

The following is an example response.

```
<GetReviewableHITsResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <NumResults>1</NumResults>
  <TotalNumResults>1</TotalNumResults>
  <PageNumber>1</PageNumber>
  <HIT>
    <HITId>GBHZVQX3EHXZ2AYDY2T0</HITId>
  </HIT>
</GetReviewableHITsResult>
```
