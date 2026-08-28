---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_XMLParameterValuesArticle.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# Using XML Parameter Values
<a name="ApiReference_XMLParameterValuesArticle"></a>

 The [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md), [QuestionFormAnswers](ApiReference_QuestionFormAnswersDataStructureArticle.md), and [AnswerKey](ApiReference_AnswerKeyDataStructureArticle.md) data structures are used as parameter values in service requests, and as return values in service responses. Unlike other data structures described in this API reference, these XML structures are not part of the service API directly, but rather are used as string values going in and out of the service. This article describes the encoding methods needed to use XML data as parameter and return values.

## XML Data as a Parameter
<a name="ApiReference_XMLParameterValuesArticle-xml-data-as-a-parameter"></a>

 For SOAP requests, XML data in a parameter value must appear in the request *XML escaped*. Characters that are part of XML syntax, such as ampersands (**&**) and angle brackets (**<>**), must be replaced with the corresponding XML character entities in the parameter value. Most SOAP toolkits will automatically escape data set as the string value of the parameter.

 The following is a fragment of a `QuestionForm` data structure, escaped with XML character entities:

```
&lt;QuestionForm xmlns="..."&gt;
  &lt;Overview&gt;
    &lt;Text&gt;
      Musicals by Rodgers &amp;amp; Hart...
    &lt;/Text&gt;
  &lt;Overview&gt;
  ...
&lt;/QuestionForm&gt;
```

 For REST requests, the data must be *URL encoded* to appear as a single parameter value in the request. (This is true for all REST parameter values.) Characters that are part of URL syntax, such as question marks (**?**) and ampersands (**&**), must be replaced with the corresponding URL character codes.

**Note**
 XML data in REST requests should only be URL encoded, *not* XML escaped.

 In service responses, this data will be XML escaped.

## Namespaces for XML Parameter Values
<a name="ApiReference_XMLParameterValuesArticle-namespaces-for-xml-parameter-values"></a>

 XML data in parameter values must have a namespace specified for all elements. The easiest way to do this is to include an `xmlns` attribute in the root element equal to the appropriate namespace.

 The namespace for a `QuestionForm`, `QuestionFormAnswers`, or `AnswerKey` element is identical to the URL of the corresponding schema document, including the version date. While XML namespaces need not be URLs according to the XML specification, this convention ensures that the consumer of the value knows which version of the schema is being used for the data.

 For the locations of the schema documents, as well as instructions on how to include the version date in the URL, see [WSDL and Schema Locations](ApiReference_WsdlLocationArticle.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
