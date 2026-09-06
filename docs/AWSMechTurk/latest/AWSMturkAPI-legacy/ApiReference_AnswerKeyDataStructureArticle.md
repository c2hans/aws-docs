---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_AnswerKeyDataStructureArticle.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# AnswerKey
<a name="ApiReference_AnswerKeyDataStructureArticle"></a>

**Topics**
+ [Description](#ApiReference_AnswerKeyDataStructureArticle-description)
+ [The Structure of an Answer Key](#ApiReference_AnswerKeyDataStructureArticle-the-structure-of-an-answer-key)
+ [Example](#ApiReference_AnswerKeyDataStructureArticle-example)

## Description
<a name="ApiReference_AnswerKeyDataStructureArticle-description"></a>

 The AnswerKey data structure specifies answers for a Qualification test, and a mechanism to use to calculate a score from the key and a Worker's answers.

 An AnswerKey data structure is a string value that consists of XML data. The XML data must conform to the AnswerKey schema. See [WSDL and Schema Locations](ApiReference_WsdlLocationArticle.md) for the location of this schema. For more information about using XML data as parameter or return value, see [Using XML Parameter Values](ApiReference_XMLParameterValuesArticle.md).

 The AnswerKey data structure is used as a parameter for the following operations:
+  `CreateQualificationType`

 The AnswerKey data structure is used as a return value for the following operations:
+  `GetQualificationType`

 The AnswerKey data structure is a value in a [Qualification type data structure](ApiReference_QualificationTypeDataStructureArticle.md).

 All elements in a `AnswerKey` belong to a namespace whose name is identical to the URL of the `AnswerKey` schema document for the version of the API you are using.

## The Structure of an Answer Key
<a name="ApiReference_AnswerKeyDataStructureArticle-the-structure-of-an-answer-key"></a>

 An answer key is contained in a `AnswerKey` element. This element contains a `Question` element for each question in the Qualification test, and an optional `QualificationValueMapping` element that describes how to calculate the Qualification value from the answer key and the Worker's answers.

### Question
<a name="ApiReference_AnswerKeyDataStructureArticle-the-structure-of-an-answer-key-question"></a>

 A `Question` element contains a `QuestionIdentifier` element, which identifies the question for this answer. This value corresponds to a `QuestionIdentifier` in the QuestionForm.

 A `Question` element has one or more `AnswerOption` elements, one for each combination of selections in the multiple-choice question that affects the Worker's test score.

 Each `AnswerOption` contains one or more `SelectionIdentifier` elements that correspond to identifiers for the selections in the QuestionForm. It also contains an `AnswerScore` element, a number that is added to the Worker's test score if the Worker's answer matches this option. The Worker must select all of the selections specified by the `SelectionIdentifier` elements, and no others, to earn the score.

**Tip**
 An `AnswerScore` for an `AnswerOption` may be negative.

 The `Question` may have an optional `DefaultScore`, a number that is added to the Worker's test score if none of the answer options exactly match the Worker's answer for the question. `DefaultScore` is optional, and defaults to 0.

```
<AnswerOption>
  <SelectionIdentifier>apples</SelectionIdentifier>
  <AnswerScore>10</AnswerScore>
</AnswerOption>
```

### QualificationValueMapping
<a name="ApiReference_AnswerKeyDataStructureArticle-the-structure-of-an-answer-key-qualificationvaluemapping"></a>

 The `Question` may have an optional `QualificationValueMapping` element that describes how to calculate the Worker's overall score from the scores of the Worker's answers. It contains either a `PercentageMapping` element, a `ScaleMapping` element, or a `RangeMapping` element.

 If no `QualificationValueMapping` is specified, the sum of the scores of the answers is used as the Qualification value.

```
<QualificationValueMapping>
  ...
</QualificationValueMapping>
```

 A `PercentageMapping` specifies a maximum score for the test, as a `MaximumSummedScore` element. The Qualification value is calculated as the sum of the scores of the selected answers, divided by the maximum, multiplied by 100 and rounded to the nearest integer to produce a percentage.

```
  ...
  <PercentageMapping>
    <MaximumSummedScore>15</MaximumSummedScore>
  </PercentageMapping>
```

 A `ScaleMapping` specifies a multiplier, as a decimal value in a `SummedScoreMultiplier` element. The Qualification value is calculated as the sum of the scores of the selected answers, multiplied by the multiplier.

```
  ...
  <ScaleMapping>
    <SummedScoreMultiplier>3</SummedScoreMultiplier>
  </ScaleMapping>
```

 A `RangeMapping` assigns specific Qualification values to ranges of total test scores. It contains one or more `SummedScoreRange` elements, each of which specify an `InclusiveLowerBound` element, an `InclusiveUpperBound` element, and a `QualificationValue` that becomes the Qualification value if the sum of the scores of the selected answers falls within the specified range. Finally, the `RangeMapping` includes a single `OutOfRangeQualificationValue`, which specifies the Qualification value if the sum of the scores of the selected answers do not fall within a specified range.

**Note**
 Ranges cannot overlap. If ranges overlap, the behavior is undefined.

```
  ...
  <RangeMapping>
    <SummedScoreRange>
      <InclusiveLowerBound>5</InclusiveLowerBound>
      <InclusiveUpperBound>7</InclusiveUpperBound>
      <QualificationValue>5</QualificationValue>
    </SummedScoreRange>
    <SummedScoreRange>
      <InclusiveLowerBound>8</InclusiveLowerBound>
      <InclusiveUpperBound>10</InclusiveUpperBound>
      <QualificationValue>10</QualificationValue>
    </SummedScoreRange>
    <OutOfRangeQualificationValue>0</OutOfRangeQualificationValue>
  </RangeMapping>
```

## Example
<a name="ApiReference_AnswerKeyDataStructureArticle-example"></a>

The following is an example of a complete `AnswerKey` data structure. Remember that to pass this structure in as a parameter to an operation, XML characters must be escaped as character entities. For more information, see [Using XML Parameter Values](ApiReference_XMLParameterValuesArticle.md).

```
<AnswerKey xmlns="{{[the AnswerKey schema URL]}}">
  <Question>
    <QuestionIdentifier>nextmove</QuestionIdentifier>
    <AnswerOption>
      <SelectionIdentifier>D</SelectionIdentifier>
      <AnswerScore>5</AnswerScore>
    </AnswerOption>
  </Question>
  <Question>
    <QuestionIdentifier>favoritefruit</QuestionIdentifier>
    <AnswerOption>
      <SelectionIdentifier>apples</SelectionIdentifier>
      <AnswerScore>10</AnswerScore>
    </AnswerOption>
  </Question>
  <QualificationValueMapping>
    <PercentageMapping>
      <MaximumSummedScore>15</MaximumSummedScore>
    </PercentageMapping>
  </QualificationValueMapping>
</AnswerKey>
```
