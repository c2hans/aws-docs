---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_SearchQualificationTypesOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# SearchQualificationTypes
<a name="ApiReference_SearchQualificationTypesOperation"></a>

## Description
<a name="ApiReference_SearchQualificationTypesOperation-description"></a>

 The `SearchQualificationTypes` operation searches for Qualification types using the specified search query, and returns a list of Qualification types.

 The operation sorts the results, divides them into numbered pages, and returns a single page of results. You can control sorting and pagination with parameters to the operation.

## Request Parameters
<a name="ApiReference_SearchQualificationTypesOperation-request-parameters"></a>

 `SearchQualificationTypes` accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `SearchQualificationTypes` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: SearchQualificationTypes<br />Default: None | Yes |
|  `Query`  |  A text query against all of the searchable attributes of Qualification types. <br />Type: String<br /> Default: None. If not specified, the complete set of all Qualification types is considered for the results.  | No |
|  `SortProperty`  | The field on which to sort the results returned by the operation.<br />Type: String<br />Valid Values: Name<br />Default: Name | No |
|  `SortDirection`  |  The direction of the sort used with the field specified by `SortProperty`. <br />Type: String<br />Valid Values: Ascending \| Descending<br />Default: Descending | No |
|  `PageSize`  |  The number of Qualification types to include in a page of results. The operation divides the complete sorted result set into pages of this many Qualification types. <br />Type: positive integer<br />Valid Values: any integer between 1 and 100.<br />Default: 10 | No |
|  `PageNumber`  |  The page of results to return. After the operation filters, sorts, and divides the Qualification types into pages of size `PageSize`, it returns page corresponding to `PageNumber` as the results of the operation. <br />Type: positive integer<br />Default: 1 | No |
|  `MustBeRequestable`  |  Specifies that only Qualification types that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test, are returned as results of the search. Some Qualification types, such as those assigned automatically by the system, cannot be requested directly by users. If `false`, all Qualification types, including those managed by the system, are considered for the search. <br />Type: Boolean<br />Valid Values: true \| false<br />Default: None | Yes |
|  `MustBeOwnedByCaller`  |  Specifies that only Qualification types that the Requester created are returned. If `false`, the operation returns all Qualification types.  | No |

## Response Elements
<a name="ApiReference_SearchQualificationTypesOperation-response-elements"></a>

 A successful request for the `SearchQualificationTypes` operation has a `SearchQualificationTypesResult` element in the response.

 The `SearchQualificationTypesResult` element contains the elements described in the following table:

| Name | Description |
| --- | --- |
|  `NumResults`  |  The number of Qualification types on this page in the filtered results list, equivalent to the number of types this operation returns. <br />Type: non-negative integer |
|  `PageNumber`  | The number of this page in the filtered results list.<br />Type: positive integer |
|  `TotalNumResults`  |  The total number of Qualification types in the filtered results list based on this call. <br />Type: non-negative integer |
|  `QualificationType`  |  The Qualification type. The response includes one `QualificationType` element for each Qualification type the query returns. <br /> Type: a [QualificationType](ApiReference_QualificationTypeDataStructureArticle.md) data structure.  |

## Examples
<a name="ApiReference_SearchQualificationTypesOperation-examples"></a>

The following example shows how to use the `SearchQualificationTypes` operation.

### Sample Request
<a name="ApiReference_SearchQualificationTypesOperation-examples-sample-request"></a>

 The following example performs a simple text query for Qualification types.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2017-01-17
&Operation=SearchQualificationTypes
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&Query=English
```

### Sample Response
<a name="ApiReference_SearchQualificationTypesOperation-examples-sample-response"></a>

The following is an example response.

```
<SearchQualificationTypesResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <NumResults>10</NumResults>
  <TotalNumResults>5813</TotalNumResults>
  <QualificationType>
    <QualificationTypeId>WKAZMYZDCYCZP412TZEZ</QualificationTypeId>
    <CreationTime>2009-05-17T10:05:15Z</CreationTime>
    <Name> WebReviews Qualification Master Test</Name>
    <Description>
    This qualification will allow you to earn more on the WebReviews HITs.
    </Description>
    <Keywords>WebReviews, webreviews, web reviews</Keywords>
    <QualificationTypeStatus>Active</QualificationTypeStatus>
      <Test>
        <QuestionForm xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionForm.xsd">
          <Overview>
          <Title>WebReviews Survey</Title>
          <Text>
          After you have filled out this survey you will be assigned one or more qualifications...
          </Text>
        </Overview>
        <Question>
          <QuestionIdentifier>age</QuestionIdentifier>
          <DisplayName>What is your age?</DisplayName>
          <IsRequired>true</IsRequired>
          <QuestionContent>
            <Text>
            Please choose the age group you belong to.
            </Text>
          </QuestionContent>
          <AnswerSpecification>
    		<SelectionAnswer>
    		  <StyleSuggestion>radiobutton</StyleSuggestion>
    		  <Selections>
    		    <Selection>
    		      <SelectionIdentifier>0018</SelectionIdentifier>
    		      <Text>-18</Text>
    		    </Selection>
  		    <Selection>
  		      <SelectionIdentifier>5160</SelectionIdentifier>
  		      <Text>51-60</Text>
  		    </Selection>
  		    <Selection>
  		      <SelectionIdentifier>6000</SelectionIdentifier>
  		      <Text>60+</Text>
  		    </Selection>
  		  </Selections>
  	    </SelectionAnswer>
         </AnswerSpecification>
      </Question>
    </QuestionForm>
    </Test>
    <TestDurationInSeconds>1200</TestDurationInSeconds>
  </QualificationType>
</SearchQualificationTypesResult>
```
