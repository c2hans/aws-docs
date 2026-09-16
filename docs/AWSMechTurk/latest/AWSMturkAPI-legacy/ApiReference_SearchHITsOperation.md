---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_SearchHITsOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# SearchHITs
<a name="ApiReference_SearchHITsOperation"></a>

## Description
<a name="ApiReference_SearchHITsOperation-description"></a>

 The `SearchHITs` operation returns all of a Requester's HITs, on behalf of the Requester.

 The operation returns HITs of any status, except for HITs that have been disposed of with the [DisposeHIT](ApiReference_DisposeHITOperation.md) operation or that have been auto-disposed.

**Note**
 The `SearchHITs` operation does not accept any search parameters that filter the results.
 HITs are auto-disposed after 120 days and do not appear in `SearchHITs` responses after that time.

 The operation sorts the results and divides them into numbered pages. The operation returns a single page of results. You can control sorting and pagination with parameters to the operation.

 When (`PageNumber` x `PageSize`) is less than 100, you can get reliable results when you use any of the sort properties. If this number is greater than 100, use the **Enumeration** sort property for best results. The **Enumeration** sort property guarantees that all HITs are returned with no duplicates, but not in any specific order.

## Request Parameters
<a name="ApiReference_SearchHITsOperation-request-parameters"></a>

 The `SearchHITs` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `SearchHITs` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: SearchHITs<br />Default: None | Yes |
|  `SortProperty`  | The field on which to sort the returned results<br />Type: String<br />Valid Values: Title \| Reward \| Expiration \| CreationTime \| Enumeration<br />Default: CreationTime | No |
|  `SortDirection`  |  The direction of the sort, used with the field specified by the `SortProperty` parameter. <br />Type: String<br />Valid Values: Ascending \| Descending<br />Default: Ascending | No |
|  `PageSize`  |  The number of HITs to include in a page of results. The complete sorted result set is divided into pages of this many HITs. <br />Type: positive integer<br />Valid Values: any integer between 1 and 100<br />Default: 10 | No |
|  `PageNumber`  |  The page of results to return. After the operation sorts the HITs and divides them into pages of size `PageSize`, the operation returns the page corresponding to `PageNumber`. <br />Type: positive integer<br />Default: 1 | No |

## Response Elements
<a name="ApiReference_SearchHITsOperation-response-elements"></a>

 A successful request for the `SearchHITs` operation will have a `SearchHITsResult` element in the response.

 The `SearchHITsResult` element contains the following elements:

| Name | Description |
| --- | --- |
|  `NumResults`  |  The number of HITs on this page in the filtered results list, equivalent to the number of HITs being returned by this call. <br />Type: non-negative integer |
|  `PageNumber`  | The number of this page in the filtered results list.<br />Type: positive integer |
|  `TotalNumResults`  | The total number of HITs in the filtered results list based on this call.<br />Type: non-negative integer |
|  `HIT`  |  The HIT. The response includes one `HIT` element for each HIT the query returns. <br />Type: a [HIT](ApiReference_HITDataStructureArticle.md) data structure. |

## Examples
<a name="ApiReference_SearchHITsOperation-examples"></a>

The following example shows how to use the `GetHITsForQualificationType` operation.

### Sample Request
<a name="ApiReference_SearchHITsOperation-examples-sample-request"></a>

 The following example queries all of the HITs for a Requester. The example uses default values for sorting and pagination.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Operation=SearchHITs
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
```

### Sample Response
<a name="ApiReference_SearchHITsOperation-examples-sample-response"></a>

The following is an example response.

```
<SearchHITsResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <NumResults>2</NumResults>
  <TotalNumResults>2</TotalNumResults>
  <PageNumber>1</PageNumber>

  <HIT>
    <HITId>GBHZVQX3EHXZ2AYDY2T0</HITId>
    <HITTypeId>NYVZTQ1QVKJZXCYZCZVZ</HITTypeId>
    <CreationTime>2009-04-22T00:17:32Z</CreationTime>
    <Title>Location</Title>
    <Description>Select the image that best represents</Description>
    <HITStatus>Reviewable</HITStatus>
    <MaxAssignments>1</MaxAssignments>
    <Reward>
      <Amount>5.00</Amount>
      <CurrencyCode>USD</CurrencyCode>
      <FormattedPrice>$5.00</FormattedPrice>
    </Reward>
    <AutoApprovalDelayInSeconds>2592000</AutoApprovalDelayInSeconds>
    <Expiration>2009-04-29T00:17:32Z</Expiration>
    <AssignmentDurationInSeconds>30</AssignmentDurationInSeconds>
    <NumberOfAssignmentsPending>0</NumberOfAssignmentsPending>
    <NumberOfAssignmentsAvailable>0</NumberOfAssignmentsAvailable>
    <NumberOfAssignmentsCompleted>1</NumberOfAssignmentsCompleted>
  </HIT>

  <HIT>
    <HITId>ZZRZPTY4ERDZWJ868JCZ</HITId>
    <HITTypeId>NYVZTQ1QVKJZXCYZCZVZ</HITTypeId>
    <CreationTime>2009-07-07T00:56:40Z</CreationTime>
    <Title>Location</Title>
    <Description>Select the image that best represents</Description>
    <HITStatus>Assignable</HITStatus>
    <MaxAssignments>1</MaxAssignments>
    <Reward>
      <Amount>5.00</Amount>
      <CurrencyCode>USD</CurrencyCode>
      <FormattedPrice>$5.00</FormattedPrice>
    </Reward>
    <AutoApprovalDelayInSeconds>2592000</AutoApprovalDelayInSeconds>
    <Expiration>2009-07-14T00:56:40Z</Expiration>
    <AssignmentDurationInSeconds>30</AssignmentDurationInSeconds>
    <NumberOfAssignmentsPending>0</NumberOfAssignmentsPending>
    <NumberOfAssignmentsAvailable>1</NumberOfAssignmentsAvailable>
    <NumberOfAssignmentsCompleted>0</NumberOfAssignmentsCompleted>
  </HIT>
</SearchHITsResult>
```

## Related Operations
<a name="ApiReference_SearchHITsOperation-related-operations"></a>
+ [GetAssignmentsForHIT](ApiReference_GetAssignmentsForHITOperation.md)
